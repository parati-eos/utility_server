from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from PIL import Image
import requests
import io
from collections import Counter

app = Flask(__name__)
CORS(app)

def replace_most_frequent_color(image, replacement_color):
    # Convert the image to RGB mode (if it's not already in RGB)
    img = image.convert('RGBA')
    
    # Get the image data as a list of pixels
    pixels = list(img.getdata())
    
    # Dictionary to store color counts
    color_counts = {}
    
    # Count the occurrences of each color (excluding black)
    for pixel in pixels:
            color_counts[pixel[:3]] = color_counts.get(pixel[:3], 0) + 1
    
    # Check if there are any colors other than black
    print(color_counts)
    if color_counts:
        # Get the most frequent color
        most_frequent_color = max(color_counts, key=color_counts.get)
        print("Most frequent color:", most_frequent_color)
        print("Replacement color:", replacement_color)
    else:
        # If there are no colors other than black, return the original image
        return img
    
    # Replace the most frequent color with the specified replacement color
    modified_pixels = [replacement_color + (pixel[3],) if pixel[:3] == most_frequent_color else pixel for pixel in pixels]
    
    # Create a new image with the modified pixel data
    modified_img = Image.new('RGBA', img.size)
    modified_img.putdata(modified_pixels)
    
    return modified_img


@app.route('/test', methods=['GET'])
def test():
    return "test successful"

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the image URL and replacement color from the request
        image_url = request.json['image_url']
        replacement_color_hex = request.json['replacement_color']
        
        # Download the image from the URL
        response = requests.get(image_url)
        image_data = response.content

        # Convert the hex color code to RGB tuple
        replacement_color = tuple(int(replacement_color_hex[i:i+2], 16) for i in (0, 2, 4))

        # Convert the image data to a Pillow Image object
        image = Image.open(io.BytesIO(image_data))
        
        # Check if the image is in PNG format
        if image.format != 'PNG':
            return jsonify({'error': 'Only PNG images are supported'}), 400
        
        # Replace the most frequent color (excluding black) with the specified replacement color
        modified_image = replace_most_frequent_color(image, replacement_color)
        
        # Save the modified image to a BytesIO object in PNG format
        output_buffer = io.BytesIO()
        modified_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)
        
        # Return the modified image directly in the response
        return send_file(output_buffer, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

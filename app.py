from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from PIL import Image
import requests
import io
import time
from collections import Counter
import json
import gspread
from google.oauth2 import service_account
from util import json_to_array
from ResponseUtility import Response_json_to_array
from datetime import datetime

app = Flask(__name__)
CORS(app)
from PIL import Image
import io

def get_google_sheet(SheetName,SheetId):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=scope)
    client = gspread.authorize(credentials)
    sheet = client.open_by_key(SheetId)
    print(sheet)
    space_name_sheet = sheet.worksheet(SheetName) 
    print(space_name_sheet)
    return space_name_sheet

def crop_image_bottom(image_data, width_ratio, height_ratio):
    try:
        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        crop_width = min(width, height * width_ratio / height_ratio)
        crop_height = min(height, width * height_ratio / width_ratio)
        left = (width - crop_width) / 2
        top = 0
        right = (width + crop_width) / 2
        bottom = crop_height
        cropped_image = image.crop((left, top, right, bottom))
        
        return cropped_image
    except Exception as e:
        print("Error:", e)
        return None

    
def crop_image(image_data, width_ratio, height_ratio):
    try:

        image = Image.open(io.BytesIO(image_data))
        width, height = image.size
        crop_width = min(width, height * width_ratio / height_ratio)
        crop_height = min(height, width * height_ratio / width_ratio)
        left = (width - crop_width) / 2
        top = (height - crop_height) / 2
        right = (width + crop_width) / 2
        bottom = (height + crop_height) / 2
        cropped_image = image.crop((left, top, right, bottom))
        
        return cropped_image
    except Exception as e:
        print("Error:", e)
        return None


def replace_most_frequent_color(image, replacement_color):
    
    img = image.convert('RGBA')
    pixels = list(img.getdata())
    color_counts = Counter()
    for pixel in pixels:
        if pixel[3] != 0:  
            color_counts[pixel[:3]] += 1
    if color_counts:
        most_frequent_color = max(color_counts, key=color_counts.get)
        print("Most frequent color:", most_frequent_color)
        print("Replacement color:", replacement_color)
    else:
        return img

    modified_pixels = [replacement_color + (pixel[3],) if pixel[:3] == most_frequent_color else pixel for pixel in pixels]
    
    modified_img = Image.new('RGBA', img.size)
    modified_img.putdata(modified_pixels)
    
    return modified_img



@app.route('/test', methods=['GET'])
def test():
    return "test successful"

@app.route('/time')
def get_current_date():
    current_date = datetime.now()
    return f'Current date: {current_date}'

@app.route('/mongodb', methods=['POST'])
def mongodb():
    data = request.data
    start_time = time.time()  # Record the start time
    try:
        json_data = json.loads(data)
        submissionId = json_data.get('user', {}).get('submissionId')
        sheet = get_google_sheet('Native Form Responses','1huVEcxx5ACTgRv7X-OcikIZfSb5KCaKAQ63IQhm2ZLY')
        cell = sheet.find(submissionId) if submissionId else None
        if cell:
            row = cell.row
            arr = json_to_array(json_data)
            cell_list = sheet.range('A' + str(row) + ':MZ'+ str(row))
            for i in range(len(arr)):
                cell_list[i].value = arr[i]
            sheet.update_cells(cell_list, value_input_option='USER_ENTERED')  # Update the fields accordingly
        else:
            sheet.append_row(json_to_array(json_data))  # Update the fields accordingly

        # Log success and execution time
        execution_time = time.time() - start_time
        print(f"Data processed successfully. Time taken: {execution_time:.2f} seconds")
        return jsonify({'message': 'Data received and processed successfully'}), 200
    except Exception as e:
        # Log the error and execution time
        execution_time = time.time() - start_time
        app.logger.error(f"Error: {str(e)}. Time taken: {execution_time:.2f} seconds")
        return jsonify({'error hai': str(e)}), 400
    
    
@app.route('/mongodb_short', methods=['POST'])
def mongodb_short():
    data = request.data
    start_time = time.time()  
    try:
        json_data = json.loads(data)
        submissionId = json_data.get('user', {}).get('submissionId')
        sheet = get_google_sheet('Native Form Responses','1khwJvLdnVLJe5OF96zmOAor7ouBNyMBbxnMJ4LDUeUg')
        cell = sheet.find(submissionId) if submissionId else None
        if cell:
            row = cell.row
            arr = json_to_array(json_data)
            cell_list1 = sheet.range('A' + str(row) + ':MZ'+ str(row))

            for i in range(len(arr)):
                cell_list1[i].value = arr[i]
            sheet.update_cells(cell_list1, value_input_option='USER_ENTERED')  # Update the fields accordingl
        else:
            sheet.append_row(json_to_array(json_data))  # Update the fields accordingly

        # Log success and execution time
        execution_time = time.time() - start_time
        print(f"Data processed successfully. Time taken: {execution_time:.2f} seconds")
        return jsonify({'message': 'Data received and processed successfully'}), 200
    except Exception as e:
        # Log the error and execution time
        execution_time = time.time() - start_time
        app.logger.error(f"Error: {str(e)}. Time taken: {execution_time:.2f} seconds")
        return jsonify({'error hai': str(e)}), 400
    
@app.route('/Response', methods=['POST'])
def Response():
    data = request.data
    start_time = time.time()  
    try:
        json_data = json.loads(data)
        submissionId = json_data.get('user', {}).get('submissionId')
        sheet = get_google_sheet('DB - GPT','1DLb_m5RtRZGdabOzMRJ5K3rbKeBhfKW3s-k-6BKc0h0')
        cell = sheet.find(submissionId) if submissionId else None
        print(cell)
        if cell:
            row = cell.row
            
            arr = Response_json_to_array(json_data)
            cell_list = sheet.range('A' + str(row) + ':QE'+ str(row))
            
            for i in range(len(arr)):
                cell_list[i].value = arr[i]
        
            sheet.update_cells(cell_list, value_input_option='USER_ENTERED')  # Update the fields accordingly
        else:
            print(Response_json_to_array(json_data))
            sheet.append_row(Response_json_to_array(json_data))  # Update the fields accordingly

        # Log success and execution time
        execution_time = time.time() - start_time
        print(f"Data processed successfully. Time taken: {execution_time:.2f} seconds")
        return jsonify(Response_json_to_array(json_data) ), 200
    except Exception as e:
       
        execution_time = time.time() - start_time
        app.logger.error(f"Error: {str(e)}. Time taken: {execution_time:.2f} seconds")
        return jsonify({'error hai': str(e)}), 400

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        
        image_url = request.json['image_url']
        replacement_color_hex = request.json['replacement_color']
        response = requests.get(image_url)
        image_data = response.content
        replacement_color = tuple(int(replacement_color_hex[i:i+2], 16) for i in (0, 2, 4))
        image = Image.open(io.BytesIO(image_data))

        if image.format != 'PNG':
            return jsonify({'error': 'Only PNG images are supported'}), 400
        modified_image = replace_most_frequent_color(image, replacement_color)
        output_buffer = io.BytesIO()
        modified_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)
        return send_file(output_buffer, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/crop_image', methods=['POST'])
def handle_crop_image():
    try:
        image_url = request.json['image_url']
        width_ratio = float(request.json['width'])
        height_ratio = float(request.json['height'])
        response = requests.get(image_url)
        image_data = response.content
        cropped_image = crop_image(image_data,width_ratio,height_ratio)
        
        if cropped_image:
            cropped_image_io = io.BytesIO()
            cropped_image.save(cropped_image_io, format='PNG')
            cropped_image_io.seek(0)
            return send_file(cropped_image_io, mimetype='image/png')
        else:
            return jsonify({'error': 'Failed to crop image'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/crop_image_bottom', methods=['POST'])
def handle_crop_image_bottom():
    try:
        image_url = request.json['image_url']
        width_ratio = float(request.json['width'])
        height_ratio = float(request.json['height'])
        response = requests.get(image_url)
        image_data = response.content
        cropped_image = crop_image_bottom(image_data, width_ratio, height_ratio)
        
        if cropped_image:
            cropped_image_io = io.BytesIO()
            cropped_image.save(cropped_image_io, format='PNG')
            cropped_image_io.seek(0)
            return send_file(cropped_image_io, mimetype='image/png')
        else:
            return jsonify({'error': 'Failed to crop image'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

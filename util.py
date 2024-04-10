from datetime import datetime
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def json_to_array(data_dict):
    user_id = data_dict["user"]["userId"]
    submission_id = data_dict['user']['submissionId']
    submission_date = current_date
    company_name = data_dict['about']['companyName']
    tagline = data_dict['about']['tagline']
    logo_path = data_dict['about']['logo']
    primary_color = data_dict['about']['primaryColor']
    secondary_color = data_dict['about']['secondaryColor']
    establishment_year = data_dict['companyDetails']['establishmentYear']
    company_overview = data_dict['companyDetails']['companyOverview']
    problem_description = data_dict['problemDescription']['problemDescription']
    solution_description = data_dict['solutionDescription']['solutionsDescription']
    sector = data_dict['market']['sector']
    other_sector = data_dict['market']['otherSector']
    market_description = data_dict['market']['marketDescription']
    TAM = data_dict['market']['TAM']
    TAM_growth_rate = data_dict['market']['TAMGrowthRate']
    SAM= data_dict['market']['SAM']
    SAM_growth_rate= data_dict['market']['SAMGrowthRate']
    product_overview = data_dict['product']['productOverview']
    product_roadmap = data_dict['product']['productRoadmap']
    product_roadmap_description = data_dict['product']['productRoadmapDescription']
    technical_architecture = data_dict['product']['technicalArchitecture']
    app_type = data_dict['productScreen']['appType']
    mobile_screenshots = data_dict['productScreen']['mobileScreenshots']
    web_screenshots = data_dict['productScreen']['webScreenshots']
    business_model = data_dict['businessModel']['businessModel']
    key_stakeholders = data_dict['goToMarket']['keyStakeholders']
    customer_persona = data_dict['goToMarket']['customerPersona']
    go_to_market_strategy = data_dict['goToMarket']['goToMarketStrategy']
    track_record = data_dict['trackRecord']['trackRecord']
    case_studies = data_dict['caseStudies']['caseStudies']
    testimonials = data_dict['testimonials']['testimonials']
    competitors = data_dict['competitors']['competitors']
    competitive_diff = data_dict['competitiveDiff']['competitiveDiff']
    team_members = data_dict['teamMembers']['teamMembers']
    website_link = data_dict['contactInfo']['websiteLink']
    linkedin_link = data_dict['contactInfo']['linkedinLink']
    contact_email = data_dict['contactInfo']['contactEmail']
    contact_phone = data_dict['contactInfo']['contactPhone']
    financial_snapshot = data_dict['financialInfo']['financialSnapshot']
    revenue_cost = data_dict['financialInfo']['revenueCost']
    planned_raise = data_dict['financialInfo']['plannedRaise']
    use_of_funds = data_dict['financialInfo']['useOfFunds']
    percentage = data_dict['financialInfo']['percentage']

    revenues = [""] * 10
    costs = [""] * 10 
    for entry in revenue_cost:
        year = int(entry["year"])
        index = year - 2019
        if 0 <= index < len(revenues):
            revenues[index] = entry["revenue"]
            costs[index] = entry["cost"]
    productAndDevelopment = []
    marketingAndSales = []
    capex = []
    businessOperation = []
    teamSalaries = []

    for item in use_of_funds:
        if item["use"] == "Product and Development":
            productAndDevelopment.append(item["percentage"])
        elif item["use"] == "Marketing and Sales":
            marketingAndSales.append(item["percentage"])
        elif item["use"] == "Capex":
            capex.append(item["percentage"])
        elif item["use"] == "Business Operation":
            businessOperation.append(item["percentage"])
        elif item["use"] == "Team Salaries":
            teamSalaries.append(item["percentage"])

    arr = [
    user_id, #
    submission_id,#
    submission_date, #
    company_name,#
    tagline ,#
    logo_path,#
    primary_color,#
    secondary_color,#
    establishment_year,#
    company_overview ,#
    problem_description,#
    solution_description,#
    sector,#
    other_sector,#
    market_description ,#
    TAM,#
    TAM_growth_rate ,#
    SAM,#
    SAM_growth_rate,#
    product_overview,#
    product_roadmap_description,#
    technical_architecture,#
    app_type ,#
    mobile_screenshots[0] if len(mobile_screenshots) > 0 else '',#
    mobile_screenshots[1] if len(mobile_screenshots) > 1 else '',#
    mobile_screenshots[2] if len(mobile_screenshots) > 2 else '',#
    web_screenshots[0] if len(web_screenshots) > 0 else '',#
    web_screenshots[1] if len(web_screenshots) > 1 else '',#
    web_screenshots[2] if len(web_screenshots) > 2 else '',#
    business_model ,#
    key_stakeholders ,#
    customer_persona,#
    go_to_market_strategy ,
    track_record[0]["year1"] if len(track_record) > 0 and track_record[0] != '' else '',
    track_record[0]["year2"] if len(track_record) > 0 and track_record[0] != '' else '',
    track_record[0]["TR"] if len(track_record) > 0 and track_record[0] != '' else '',
    track_record[1]["year1"] if len(track_record) > 1 and track_record[1] != '' else '',
    track_record[1]["year2"] if len(track_record) > 1 and track_record[1] != '' else '',
    track_record[1]["TR"] if len(track_record) > 1 and track_record[1] != '' else '',
    track_record[2]["year1"] if len(track_record) > 2 and track_record[2] != '' else '',
    track_record[2]["year2"] if len(track_record) > 2 and track_record[2] != '' else '',
    track_record[2]["TR"] if len(track_record) > 2 and track_record[2] != '' else '',
    case_studies ,
    testimonials[0]["testimonial"] if len(testimonials) > 0 and testimonials[0] != '' else '',
    testimonials[0]["name"] if len(testimonials) > 0 and testimonials[0] != '' else '',
    testimonials[0]["designation"] if len(testimonials) > 0 and testimonials[0] != '' else '',
    testimonials[0]["company"] if len(testimonials) > 0 and testimonials[0] != '' else '',
    testimonials[1]["testimonial"] if len(testimonials) > 1 and testimonials[0] != '' else '',
    testimonials[1]["name"] if len(testimonials) > 1 and testimonials[0] != '' else '',
    testimonials[1]["designation"] if len(testimonials) > 1 and testimonials[0] != '' else '',
    testimonials[1]["company"] if len(testimonials) > 1 and testimonials[0] != '' else '',
    testimonials[2]["testimonial"] if len(testimonials) > 2 and testimonials[0] != '' else '',
    testimonials[2]["name"] if len(testimonials) > 2 and testimonials[0] != '' else '',
    testimonials[2]["designation"] if len(testimonials) > 2 and testimonials[0] != '' else '',
    testimonials[2]["company"] if len(testimonials) > 2 and testimonials[0] != '' else '',
    testimonials[3]["testimonial"] if len(testimonials) > 3 and testimonials[0] != '' else '',
    testimonials[3]["name"] if len(testimonials) > 3 and testimonials[0] != '' else '',
    testimonials[3]["designation"] if len(testimonials) > 3 and testimonials[0] != '' else '',
    testimonials[3]["company"] if len(testimonials) > 3 and testimonials[0] != '' else '',
    competitors[0] if len(competitors) > 0 else '',
    competitors[1] if len(competitors) > 1 else '',
    competitors[2] if len(competitors) > 2 else '',
    competitors[3] if len(competitors) > 3 else '',
    competitors[4] if len(competitors) > 4 else '',
    competitors[5] if len(competitors) > 5 else '',
    competitive_diff,
    team_members[0]['name'] if len(team_members) > 0 else '',
    team_members[0]['title'] if len(team_members) > 0 else '',
    team_members[0]['experience'] if len(team_members) > 0 else '',
    team_members[0]['linkedin'] if len(team_members) > 0 else '',
    team_members[0]['photoUrl'] if len(team_members) > 0 else '',
    team_members[1]['name'] if len(team_members) > 1 else '',
    team_members[1]['title'] if len(team_members) > 1 else '',
    team_members[1]['experience'] if len(team_members) > 1 else '',
    team_members[1]['linkedin'] if len(team_members) > 1 else '',
    team_members[1]['photoUrl'] if len(team_members) > 1 else '',
    team_members[2]['name'] if len(team_members) > 2 else '',
    team_members[2]['title'] if len(team_members) > 2 else '',
    team_members[2]['experience'] if len(team_members) > 2 else '',
    team_members[2]['linkedin'] if len(team_members) > 2 else '',
    team_members[2]['photoUrl'] if len(team_members) > 2 else '',
    team_members[3]['name'] if len(team_members) > 3 else '',
    team_members[3]['title'] if len(team_members) > 3 else '',
    team_members[3]['experience'] if len(team_members) > 3 else '',
    team_members[3]['linkedin'] if len(team_members) > 3 else '',
    team_members[3]['photoUrl'] if len(team_members) > 3 else '',
    team_members[4]['name'] if len(team_members) > 4 else '',
    team_members[4]['title'] if len(team_members) > 4 else '',
    team_members[4]['experience'] if len(team_members) > 4 else '',
    team_members[4]['linkedin'] if len(team_members) > 4 else '',
    team_members[4]['photoUrl'] if len(team_members) > 4 else '',
    team_members[5]['name'] if len(team_members) > 5 else '',
    team_members[5]['title'] if len(team_members) > 5 else '',
    team_members[5]['experience'] if len(team_members) > 5 else '',
    team_members[5]['linkedin'] if len(team_members) > 5 else '',
    team_members[5]['photoUrl'] if len(team_members) > 5 else '',
    financial_snapshot,
    revenues[0],
    revenues[1],
    revenues[2],
    revenues[3],
    revenues[4],
    revenues[5],
    revenues[6],
    revenues[7],
    revenues[8],
    revenues[9],
    costs[0],
    costs[1],
    costs[2],
    costs[3],
    costs[4],
    costs[5],
    costs[6],
    costs[7],
    costs[8],
    costs[9],
    planned_raise ,
    productAndDevelopment[0] if len( productAndDevelopment) > 0 else '',
    marketingAndSales[0] if len(marketingAndSales) > 0 else '',
    capex[0] if len(capex) > 0 else '',
    businessOperation[0] if len(businessOperation) > 0 else '',
    teamSalaries[0] if len(teamSalaries) > 0 else '',
    website_link ,
    linkedin_link ,
    contact_email,
    contact_phone 
    ]
    return arr






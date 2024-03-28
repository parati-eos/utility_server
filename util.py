
def json_to_array(data_dict):
    user_id = data_dict["user"]["userId"]
    submission_id = data_dict['user']['submissionId']
    submission_date = 'test'
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
    planned_raise = data_dict['financialInfo']['plannedRaise']
    use_of_funds = data_dict['financialInfo']['useOfFunds']
    percentage = data_dict['financialInfo']['percentage']
    print((testimonials))
    arr = [
    user_id,
    submission_id,
    submission_date,
    company_name,
    tagline ,
    logo_path,
    primary_color,
    secondary_color,
    establishment_year,
    company_overview ,
    problem_description,
    solution_description,
    sector,
    other_sector,
    market_description ,
    TAM,
    TAM_growth_rate ,
    SAM,
    SAM_growth_rate,
    product_overview,
    product_roadmap,
    product_roadmap_description,
    technical_architecture,
    app_type ,
    mobile_screenshots[0] if len(mobile_screenshots) > 0 else '',
    mobile_screenshots[1] if len(mobile_screenshots) > 1 else '',
    mobile_screenshots[2] if len(mobile_screenshots) > 2 else '',
    web_screenshots[0] if len(web_screenshots) > 0 else '',
    web_screenshots[1] if len(web_screenshots) > 1 else '',
    web_screenshots[2] if len(web_screenshots) > 2 else '',
    business_model ,
    key_stakeholders ,
    customer_persona,
    go_to_market_strategy ,
    track_record , # ther is some confusion in track record
    'timeline 1',
    'timeline 1',
    'timeline 3',
    'timeline 4',
    'timeline 5',
    'timeline 6',
    'timeline 7',
    'timeline 8',
    case_studies ,
    testimonials[0][0]["name"] if len(testimonials) > 0 and testimonials[0] != '' else '',
    'testimonials Name 0',
    'testimonials Desc 0',
    testimonials[1][0]["name"] if len(testimonials) > 1 else '',
    'testimonials Name 1',
    'testimonials Desc 1',
    testimonials[2][0]["name"] if len(testimonials) > 2 else '',
    'testimonials Name 2',
    'testimonials Desc 2',
    testimonials[3][0]["name"] if len(testimonials) > 3 else '',
    'testimonials Name 3',
    'testimonials Desc 3',
    competitors[0] if len(competitors) > 0 else '',
    competitors[1] if len(competitors) > 1 else '',
    competitors[2] if len(competitors) > 2 else '',
    competitors[3] if len(competitors) > 3 else '',
    competitors[4] if len(competitors) > 4 else '',
    competitors[5] if len(competitors) > 5 else '',
    competitive_diff,
    team_members[0] if len(team_members) > 0 else '',
    'title 0',
    'Experience 0',
    'linkden 0',
    'image 0',
    team_members[1] if len(team_members) > 1 else '',
    'title 1',
    'Experience 1',
    'linkden 1',
    'image 1',
    team_members[2] if len(team_members) > 2 else '',
    'title 2',
    'Experience 2',
    'linkden 2',
    'image 2',
    team_members[3] if len(team_members) > 3 else '',
    'title 3',
    'Experience 3',
    'linkden 3',
    'image 3',
    team_members[4] if len(team_members) > 4 else '',
    'title 4',
    'Experience 4',
    'linkden 4',
    'image 4',
    team_members[5] if len(team_members) > 5 else '',
    'title 5',
    'Experience 5',
    'linkden 5',
    'image 5',
    financial_snapshot,
    website_link ,
    linkedin_link ,
    contact_email,
    contact_phone ,
    planned_raise ,
    use_of_funds ,
    percentage 
    ]
    return arr






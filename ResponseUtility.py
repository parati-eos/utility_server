def Response_json_to_array(data):

    user_id = data.get('user', {}).get('userId', '')
    form_id = data.get('user', {}).get('submissionId', '')

    company_name = data.get('about', {}).get('companyName', '')
    company_logo = data.get('about', {}).get('companyLogo', '')
    primary_r = data.get('about', {}).get('primaryColorR','')
    primary_g = data.get('about', {}).get('primaryColorG', '')
    primary_b = data.get('about', {}).get('primaryColorB', '')
    primary_color_check = data.get('about', {}).get('primaryColorCheck', 0)
    secondary_r = data.get('about', {}).get('secondaryColorR', '')
    secondary_g = data.get('about', {}).get('secondaryColorG', '')
    secondary_b = data.get('about', {}).get('secondaryColorB', '')
    secondary_color_check = data.get('about', {}).get('secondaryColorCheck', 0)
    p100 = data.get('about', {}).get('colorP100', '')
    p75_s25 = data.get('about', {}).get('colorP75_S25', '')
    p50_s50 = data.get('about', {}).get('colorP50_S50', '')
    p25_s75 = data.get('about', {}).get('colorP25_S75', '')
    s100 = data.get('about', {}).get('colorS100', '')
    f_s100 = data.get('about', {}).get('colorF_S100', '')
    f_p100 = data.get('about', {}).get('colorF_P100', '')
    f_p75s25 = data.get('about', {}).get('colorF_P75S25', '')
    f_p50s50 = data.get('about', {}).get('colorF_P50S50', '')
    f_p25s75 = data.get('about', {}).get('colorF_P25S75', '')
    scl = data.get('about', {}).get('SCL', '')
    scd = data.get('about', {}).get('SCD', '')
    tag_line = data.get('about', {}).get('tagLine', '')
    cover_image = data.get('about', {}).get('coverImage', '')
    about_title = data.get('about', {}).get('aboutTitle', '')
    vision = data.get('about', {}).get('aboutVision', '')
    about_gpt = data.get('about', {}).get('aboutGPT', '')
    about_gpt_cleaned = data.get('about', {}).get('aboutGPTCleaned', '')
    about_gpt_1 = data.get('about', {}).get('aboutGPT1', '')
    about_gpt_2 = data.get('about', {}).get('aboutGPT2', '')
    about_gpt_3 = data.get('about', {}).get('aboutGPT3', '')
    about_gpt_4 = data.get('about', {}).get('aboutGPT4', '')
    about_gpt_5 = data.get('about', {}).get('aboutGPT5', '')
    about_1_header = data.get('about', {}).get('aboutHeader1', '')
    about_2_header = data.get('about', {}).get('aboutHeader2', '')
    about_3_header = data.get('about', {}).get('aboutHeader3', '')
    about_4_header = data.get('about', {}).get('aboutHeader4', '')
    about_5_header = data.get('about', {}).get('aboutHeader5', '')
    about_1 = data.get('about', {}).get('about1', '')
    about_2 = data.get('about', {}).get('about2', '')
    about_3 = data.get('about', {}).get('about3', '')
    about_4 = data.get('about', {}).get('about4', '')
    about_5 = data.get('about', {}).get('about5', '')
    about_image_url = data.get('about', {}).get('aboutImageURL', '')

    #problem
    problem_title = data.get('problemDescription', {}).get('problemTitle', '')
    problem_statement = data.get('problemDescription', {}).get('problemStatement', '')
    problem_gpt = data.get('problemDescription', {}).get('problemGPT', '')
    problem_gpt_cleaned = data.get('problemDescription', {}).get('problemGPTCleaned', '')
    problem_gpt_1 = data.get('problemDescription', {}).get('problemGPT1', '')
    problem_gpt_2 = data.get('problemDescription', {}).get('problemGPT2', '')
    problem_gpt_3 = data.get('problemDescription', {}).get('problemGPT3', '')
    problem_gpt_4 = data.get('problemDescription', {}).get('problemGPT4', '')
    problem_gpt_5 = data.get('problemDescription', {}).get('problemGPT5', '')
    problem_gpt_6 = data.get('problemDescription', {}).get('problemGPT6', '')
    problem_header_1 = data.get('problemDescription', {}).get('problemHeader1', '')
    problem_header_2 = data.get('problemDescription', {}).get('problemHeader2', '')
    problem_header_3 = data.get('problemDescription', {}).get('problemHeader3', '')
    problem_header_4 = data.get('problemDescription', {}).get('problemHeader4', '')
    problem_header_5 = data.get('problemDescription', {}).get('problemHeader5', '')
    problem_header_6 = data.get('problemDescription', {}).get('problemHeader6', '')
    problem_description_1 = data.get('problemDescription', {}).get('problemDescription1', '')
    problem_description_2 = data.get('problemDescription', {}).get('problemDescription2', '')
    problem_description_3 = data.get('problemDescription', {}).get('problemDescription3', '')
    problem_description_4 = data.get('problemDescription', {}).get('problemDescription4', '')
    problem_description_5 = data.get('problemDescription', {}).get('problemDescription5', '')
    problem_description_6 = data.get('problemDescription', {}).get('problemDescription6', '')
    problem_icon_1 = data.get('problemDescription', {}).get('problemIcon1', '')
    problem_icon_2 = data.get('problemDescription', {}).get('problemIcon2', '')
    problem_icon_3 = data.get('problemDescription', {}).get('problemIcon3', '')
    problem_icon_4 = data.get('problemDescription', {}).get('problemIcon4', '')
    problem_icon_5 = data.get('problemDescription', {}).get('problemIcon5', '')
    problem_icon_6 = data.get('problemDescription', {}).get('problemIcon6', '')

    #solution
    iterative_solution = data.get('solutionDescription', {}).get('iterativeSolution', '')
    solution_title = data.get('solutionDescription', {}).get('solutionTitle', '')
    solution_statement = data.get('solutionDescription', {}).get('solutionStatement', '')
    solution_gpt = data.get('solutionDescription', {}).get('solutionGPT', '')
    solution_gpt_cleaned = data.get('solutionDescription', {}).get('solutionGPTCleaned', '')
    solution_gpt_1 = data.get('solutionDescription', {}).get('solutionGPT1', '')
    solution_gpt_2 = data.get('solutionDescription', {}).get('solutionGPT2', '')
    solution_gpt_3 = data.get('solutionDescription', {}).get('solutionGPT3', '')
    solution_gpt_4 = data.get('solutionDescription', {}).get('solutionGPT4', '')
    solution_gpt_5 = data.get('solutionDescription', {}).get('solutionGPT5', '')
    solution_gpt_6 = data.get('solutionDescription', {}).get('solutionGPT6', '')
    solution_header_1 = data.get('solutionDescription', {}).get('solutionHeader1', '')
    solution_header_2 = data.get('solutionDescription', {}).get('solutionHeader2', '')
    solution_header_3 = data.get('solutionDescription', {}).get('solutionHeader3', '')
    solution_header_4 = data.get('solutionDescription', {}).get('solutionHeader4', '')
    solution_header_5 = data.get('solutionDescription', {}).get('solutionHeader5', '')
    solution_header_6 = data.get('solutionDescription', {}).get('solutionHeader6', '')
    solution_description_1 = data.get('solutionDescription', {}).get('solutionDescription1', '')
    solution_description_2 = data.get('solutionDescription', {}).get('solutionDescription2', '')
    solution_description_3 = data.get('solutionDescription', {}).get('solutionDescription3', '')
    solution_description_4 = data.get('solutionDescription', {}).get('solutionDescription4', '')
    solution_description_5 = data.get('solutionDescription', {}).get('solutionDescription5', '')
    solution_description_6 = data.get('solutionDescription', {}).get('solutionDescription6', '')
    solution_icon_1 = data.get('solutionDescription', {}).get('solutionIcon1', '')
    solution_icon_2 = data.get('solutionDescription', {}).get('solutionIcon2', '')
    solution_icon_3 = data.get('solutionDescription', {}).get('solutionIcon3', '')
    solution_icon_4 = data.get('solutionDescription', {}).get('solutionIcon4', '')
    solution_icon_5 = data.get('solutionDescription', {}).get('solutionIcon5', '')
    solution_icon_6 = data.get('solutionDescription', {}).get('solutionIcon6', '')
    # Market Information
    industry = data.get('market', {}).get('industry', '')
    market_title_gpt = data.get('market', {}).get('marketTitleGPT', '')
    market_title = data.get('market', {}).get('marketTitle', '')
    market_description = data.get('market', {}).get('marketDescription', '')
    industry_competitiveness = data.get('market', {}).get('industryCompetitiveness', '')
    tam = data.get('market', {}).get('TAM', '')
    tam_description = data.get('market', {}).get('TAMDescription', '')
    sam = data.get('market', {}).get('SAM', '')
    sam_description = data.get('market', {}).get('SAMDescription', '')
    som = data.get('market', {}).get('SOM', '')
    som_description = data.get('market', {}).get('SOMDescription', '')
    growth_driver_gpt = data.get('market', {}).get('growthDriverGPT', '')
    growth_driver_gpt_cleaned = data.get('market', {}).get('growthDriverGPTCleaned', '')
    growth_driver_gpt_1 = data.get('market', {}).get('growthDriverGPT1', '')
    growth_driver_gpt_2 = data.get('market', {}).get('growthDriverGPT2', '')
    growth_driver_gpt_3 = data.get('market', {}).get('growthDriverGPT3', '')
    growth_driver_gpt_4 = data.get('market', {}).get('growthDriverGPT4', '')
    growth_driver_gpt_5 = data.get('market', {}).get('growthDriverGPT5', '')
    growth_driver_1 = data.get('market', {}).get('growthDriver1', '')
    growth_driver_2 = data.get('market', {}).get('growthDriver2', '')
    growth_driver_3 = data.get('market', {}).get('growthDriver3', '')
    growth_driver_4 = data.get('market', {}).get('growthDriver4', '')
    growth_driver_5 = data.get('market', {}).get('growthDriver5', '')
    year_1 = data.get('market', {}).get('year1', '')
    year_2 = data.get('market', {}).get('year2', '')
    tam_growth_rate = data.get('market', {}).get('TAMGrowthRate', '')
    tam_future = data.get('market', {}).get('TAMFuture', '')
    sam_growth_rate = data.get('market', {}).get('SAMGrowthRate', '')
    sam_future = data.get('market', {}).get('SAMFuture', '')

    # Product Information
    product_title = data.get('product', {}).get('productTitle', '')
    product_overview = data.get('product', {}).get('productOverview', '')
    feature_gpt = data.get('product', {}).get('featureGPT', '')
    feature_gpt_cleaned = data.get('product', {}).get('featureGPTCleaned', '')
    feature_gpt_1 = data.get('product', {}).get('featureGPT1', '')
    feature_gpt_2 = data.get('product', {}).get('featureGPT2', '')
    feature_gpt_3 = data.get('product', {}).get('featureGPT3', '')
    feature_gpt_4 = data.get('product', {}).get('featureGPT4', '')
    feature_gpt_5 = data.get('product', {}).get('featureGPT5', '')
    feature_gpt_6 = data.get('product', {}).get('featureGPT6', '')
    feature_1 = data.get('product', {}).get('feature1', '')
    feature_2 = data.get('product', {}).get('feature2', '')
    feature_3 = data.get('product', {}).get('feature3', '')
    feature_4 = data.get('product', {}).get('feature4', '')
    feature_5 = data.get('product', {}).get('feature5', '')
    feature_6 = data.get('product', {}).get('feature6', '')
    feature_description_1 = data.get('product', {}).get('featureDescription1', '')
    feature_description_2 = data.get('product', {}).get('featureDescription2', '')
    feature_description_3 = data.get('product', {}).get('featureDescription3', '')
    feature_description_4 = data.get('product', {}).get('featureDescription4', '')
    feature_description_5 = data.get('product', {}).get('featureDescription5', '')
    feature_description_6 = data.get('product', {}).get('featureDescription6', '')
    feature_icon_1 = data.get('product', {}).get('featureIcon1', '')
    feature_icon_2 = data.get('product', {}).get('featureIcon2', '')
    feature_icon_3 = data.get('product', {}).get('featureIcon3', '')
    feature_icon_4 = data.get('product', {}).get('featureIcon4', '')
    feature_icon_5 = data.get('product', {}).get('featureIcon5', '')
    feature_icon_6 = data.get('product', {}).get('featureIcon6', '')
    product_roadmap_title = data.get('product', {}).get('productRoadmapTitle', '')
    phase_gpt = data.get('product', {}).get('phaseGPT', '')
    phase_gpt_cleaned = data.get('product', {}).get('phaseGPTCleaned', '')
    phase_gpt_1 = data.get('product', {}).get('phaseGPT1', '')
    phase_gpt_2 = data.get('product', {}).get('phaseGPT2', '')
    phase_gpt_3 = data.get('product', {}).get('phaseGPT3', '')
    phase_header_1_name = data.get('product', {}).get('phaseHeader1Name', '')
    phase_header_2_name = data.get('product', {}).get('phaseHeader2Name', '')
    phase_header_3_name = data.get('product', {}).get('phaseHeader3Name', '')
    phase_description_1 = data.get('product', {}).get('phaseDescription1', '')
    phase_description_2 = data.get('product', {}).get('phaseDescription2', '')
    phase_description_3 = data.get('product', {}).get('phaseDescription3', '')
    phase_features_1 = data.get('product', {}).get('phaseFeatures1', '')
    phase_features_2 = data.get('product', {}).get('phaseFeatures2', '')
    phase_features_3 = data.get('product', {}).get('phaseFeatures3', '')
    inputs = data.get('product', {}).get('inputs', '')
    technology_platform = data.get('product', {}).get('technologyPlatform', '')
    value_based_output = data.get('product', {}).get('valueBasedOutput', '')
    mobile_screenshots_description = data.get('productScreen', {}).get('mobileScreenshotsDescription', '')
    mobile_screenshot_1 = data.get('productScreen', {}).get('mobileScreenshot1', '')
    mobile_screenshot_2 = data.get('productScreen', {}).get('mobileScreenshot2', '')
    mobile_screenshot_3 = data.get('productScreen', {}).get('mobileScreenshot3', '')
    web_screenshots_description = data.get('productScreen', {}).get('webScreenshotsDescription', '')
    web_screenshot_1 = data.get('productScreen', {}).get('webScreenshot1', '')
    web_screenshot_2 = data.get('productScreen', {}).get('webScreenshot2', '')
    web_screenshot_3 = data.get('productScreen', {}).get('webScreenshot3', '')

    # Business Model Information
    revenue_model = data.get('businessModel', {}).get('revenueModel', '')
    revenue_model_image = data.get('businessModel', {}).get('revenueModelImage', '')
    revenue_stream_gpt = data.get('businessModel', {}).get('revenueStreamGPT', '')
    revenue_stream_gpt_cleaned = data.get('businessModel', {}).get('revenueStreamGPTCleaned', '')
    revenue_stream_gpt_1 = data.get('businessModel', {}).get('revenueStreamGPT1', '')
    revenue_stream_gpt_2 = data.get('businessModel', {}).get('revenueStreamGPT2', '')
    revenue_stream_gpt_3 = data.get('businessModel', {}).get('revenueStreamGPT3', '')
    revenue_stream_gpt_4 = data.get('businessModel', {}).get('revenueStreamGPT4', '')
    stream_1 = data.get('businessModel', {}).get('stream1', '')
    stream_2 = data.get('businessModel', {}).get('stream2', '')
    stream_3 = data.get('businessModel', {}).get('stream3', '')
    stream_4 = data.get('businessModel', {}).get('stream4', '')
    stream_description_1 = data.get('businessModel', {}).get('streamDescription1', '')
    stream_description_2 = data.get('businessModel', {}).get('streamDescription2', '')
    stream_description_3 = data.get('businessModel', {}).get('streamDescription3', '')
    stream_description_4 = data.get('businessModel', {}).get('streamDescription4', '')
    stream_icon_1 = data.get('businessModel', {}).get('streamIcon1', '')
    stream_icon_2 = data.get('businessModel', {}).get('streamIcon2', '')
    stream_icon_3 = data.get('businessModel', {}).get('streamIcon3', '')
    stream_icon_4 = data.get('businessModel', {}).get('streamIcon4', '')

    # Go To Market (GTM) Information
    stakeholders_title = data.get('goToMarket', {}).get('stakeholdersTitle', '')
    stakeholder_gpt = data.get('goToMarket', {}).get('stakeholderGPT', '')
    stakeholder_gpt_cleaned = data.get('goToMarket', {}).get('stakeholderGPTCleaned', '')
    stakeholder_gpt_1 = data.get('goToMarket', {}).get('stakeholderGPT1', '')
    stakeholder_gpt_2 = data.get('goToMarket', {}).get('stakeholderGPT2', '')
    stakeholder_gpt_3 = data.get('goToMarket', {}).get('stakeholderGPT3', '')
    stakeholder_gpt_4 = data.get('goToMarket', {}).get('stakeholderGPT4', '')
    stakeholder_1 = data.get('goToMarket', {}).get('stakeholder1', '')
    stakeholder_2 = data.get('goToMarket', {}).get('stakeholder2', '')
    stakeholder_3 = data.get('goToMarket', {}).get('stakeholder3', '')
    stakeholder_4 = data.get('goToMarket', {}).get('stakeholder4', '')
    benefits_1 = data.get('goToMarket', {}).get('benefits1', '')
    benefits_2 = data.get('goToMarket', {}).get('benefits2', '')
    benefits_3 = data.get('goToMarket', {}).get('benefits3', '')
    benefits_4 = data.get('goToMarket', {}).get('benefits4', '')
    customer_profile_icon_1 = data.get('goToMarket', {}).get('customerProfileIcon1', '')
    customer_profile_icon_2 = data.get('goToMarket', {}).get('customerProfileIcon2', '')
    customer_profile_icon_3 = data.get('goToMarket', {}).get('customerProfileIcon3', '')
    customer_profile_icon_4 = data.get('goToMarket', {}).get('customerProfileIcon4', '')
    customer_profile_cover_image = data.get('goToMarket', {}).get('customerProfileCoverImage', '')
    persona = data.get('goToMarket', {}).get('persona', '')
    persona_category_gpt = data.get('goToMarket', {}).get('personaCategoryGPT', '')
    persona_category_gpt_cleaned = data.get('goToMarket', {}).get('personaCategoryGPTCleaned', '')
    persona_category_gpt_1 = data.get('goToMarket', {}).get('personaCategoryGPT1', '')
    persona_category_gpt_2 = data.get('goToMarket', {}).get('personaCategoryGPT2', '')
    persona_category_gpt_3 = data.get('goToMarket', {}).get('personaCategoryGPT3', '')
    persona_header_1 = data.get('goToMarket', {}).get('personaHeader1', '')
    persona_header_2 = data.get('goToMarket', {}).get('personaHeader2', '')
    persona_header_3 = data.get('goToMarket', {}).get('personaHeader3', '')
    persona_description_1 = data.get('goToMarket', {}).get('personaDescription1', '')
    persona_description_2 = data.get('goToMarket', {}).get('personaDescription2', '')
    persona_description_3 = data.get('goToMarket', {}).get('personaDescription3', '')
    persona_icon_1 = data.get('goToMarket', {}).get('personaIcon1', '')
    persona_icon_2 = data.get('goToMarket', {}).get('personaIcon2', '')
    persona_icon_3 = data.get('goToMarket', {}).get('personaIcon3', '')
    gtm_title = data.get('goToMarket', {}).get('gtmTitle', '')
    gtm_overview = data.get('goToMarket', {}).get('gtmOverview', '')
    gtm_cover_image_landscape = data.get('goToMarket', {}).get('gtmCoverImageLandscape', '')
    gtm_gpt = data.get('goToMarket', {}).get('gtmGPT', '')
    gtm_gpt_cleaned = data.get('goToMarket', {}).get('gtmGPTCleaned', '')
    gtm_gpt_1 = data.get('goToMarket', {}).get('gtmGPT1', '')
    gtm_gpt_2 = data.get('goToMarket', {}).get('gtmGPT2', '')
    gtm_gpt_3 = data.get('goToMarket', {}).get('gtmGPT3', '')
    gtm_gpt_4 = data.get('goToMarket', {}).get('gtmGPT4', '')
    gtm_gpt_5 = data.get('goToMarket', {}).get('gtmGPT5', '')
    gtm_header_1 = data.get('goToMarket', {}).get('gtmHeader1', '')
    gtm_header_2 = data.get('goToMarket', {}).get('gtmHeader2', '')
    gtm_header_3 = data.get('goToMarket', {}).get('gtmHeader3', '')
    gtm_header_4 = data.get('goToMarket', {}).get('gtmHeader4', '')
    gtm_header_5 = data.get('goToMarket', {}).get('gtmHeader5', '')
    gtm_description_1 = data.get('goToMarket', {}).get('gtmDescription1', '')
    gtm_description_2 = data.get('goToMarket', {}).get('gtmDescription2', '')
    gtm_description_3 = data.get('goToMarket', {}).get('gtmDescription3', '')
    gtm_description_4 = data.get('goToMarket', {}).get('gtmDescription4', '')
    gtm_description_5 = data.get('goToMarket', {}).get('gtmDescription5', '')
    gtm_icon_1 = data.get('goToMarket', {}).get('gtmIcon1', '')
    gtm_icon_2 = data.get('goToMarket', {}).get('gtmIcon2', '')
    gtm_icon_3 = data.get('goToMarket', {}).get('gtmIcon3', '')
    gtm_icon_4 = data.get('goToMarket', {}).get('gtmIcon4', '')
    gtm_icon_5 = data.get('goToMarket', {}).get('gtmIcon5', '')

    track_record_title = data.get('trackRecord', {}).get('trackRecordTitle', '')
    phase_timeline_1 = data.get('trackRecord', {}).get('phaseTimeline1', '')
    phase_timeline_2 = data.get('trackRecord', {}).get('phaseTimeline2', '')
    phase_timeline_3 = data.get('trackRecord', {}).get('phaseTimeline3', '')
    traction_phase_header_1 = data.get('trackRecord', {}).get('tractionPhaseHeader1', '')
    traction_phase_header_2 = data.get('trackRecord', {}).get('tractionPhaseHeader2', '')
    traction_phase_header_3 = data.get('trackRecord', {}).get('tractionPhaseHeader3', '')
    traction_phase_description_1 = data.get('trackRecord', {}).get('tractionPhaseDescription1', '')
    traction_phase_description_2 = data.get('trackRecord', {}).get('tractionPhaseDescription2', '')
    traction_phase_description_3 = data.get('trackRecord', {}).get('tractionPhaseDescription3', '')

    case_study_title = data.get('caseStudies', {}).get('caseStudyTitle', '')
    case_study = data.get('caseStudies', {}).get('caseStudy', '')
    challenges = data.get('caseStudies', {}).get('challenges', '')
    solution = data.get('caseStudies', {}).get('solution', '')
    outcome = data.get('caseStudies', {}).get('outcome', '')
    case_study_cover_image = data.get('caseStudies', {}).get('caseStudyCoverImage', '')

    testimonial_1 = data.get('testimonials', {}).get('testimonial1', '')
    testimonial_name_1 = data.get('testimonials', {}).get('testimonialName1', '')
    designation_1 = data.get('testimonials', {}).get('designation1', '')
    testimonial_2 = data.get('testimonials', {}).get('testimonial2', '')
    testimonial_name_2 = data.get('testimonials', {}).get('testimonialName2', '')
    designation_2 = data.get('testimonials', {}).get('designation2', '')
    testimonial_3 = data.get('testimonials', {}).get('testimonial3', '')
    testimonial_name_3 = data.get('testimonials', {}).get('testimonialName3', '')
    designation_3 = data.get('testimonials', {}).get('designation3', '')
    testimonial_4 = data.get('testimonials', {}).get('testimonial4', '')
    testimonial_name_4 = data.get('testimonials', {}).get('testimonialName4', '')
    designation_4 = data.get('testimonials', {}).get('designation4', '')

    company_1 = data.get('competitors', {}).get('company1', '')
    company_2 = data.get('competitors', {}).get('company2', '')
    company_3 = data.get('competitors', {}).get('company3', '')
    company_4 = data.get('competitors', {}).get('company4', '')
    company_5 = data.get('competitors', {}).get('company5', '')
    company_6 = data.get('competitors', {}).get('company6', '')
    company_7 = data.get('competitors', {}).get('company7', '')
    attribute_gpt = data.get('competitors', {}).get('attributeGPT', '')
    attribute_gpt_cleaned = data.get('competitors', {}).get('attributeGPTCleaned', '')
    attribute_gpt_1 = data.get('competitors', {}).get('attributeGPT1', '')
    attribute_gpt_2 = data.get('competitors', {}).get('attributeGPT2', '')
    attribute_gpt_3 = data.get('competitors', {}).get('attributeGPT3', '')
    attribute_gpt_4 = data.get('competitors', {}).get('attributeGPT4', '')
    attribute_gpt_5 = data.get('competitors', {}).get('attributeGPT5', '')
    attribute_1 = data.get('competitors', {}).get('attribute1', '')
    attribute_2 = data.get('competitors', {}).get('attribute2', '')
    attribute_3 = data.get('competitors', {}).get('attribute3', '')
    attribute_4 = data.get('competitors', {}).get('attribute4', '')
    attribute_5 = data.get('competitors', {}).get('attribute5', '')
    attribute_1_ratings =1 #data.get('competitors', {}).get('attribute1Ratings', '')
    attribute_2_ratings =2 #data.get('competitors', {}).get('attribute2Ratings', '')
    attribute_3_ratings =3 #data.get('competitors', {}).get('attribute3Ratings', '')
    attribute_4_ratings =4 #data.get('competitors', {}).get('attribute4Ratings', '')
    attribute_5_ratings =5 #data.get('competitors', {}).get('attribute5Ratings', '')
    company_1_attribute_1 = data.get('competitors', {}).get('company1Attribute1', '')
    company_1_attribute_2 = data.get('competitors', {}).get('company1Attribute2', '')
    company_1_attribute_3 = data.get('competitors', {}).get('company1Attribute3', '')
    company_1_attribute_4 = data.get('competitors', {}).get('company1Attribute4', '')
    company_1_attribute_5 = data.get('competitors', {}).get('company1Attribute5', '')
    company_2_attribute_1 = data.get('competitors', {}).get('company2Attribute1', '')
    company_2_attribute_2 = data.get('competitors', {}).get('company2Attribute2', '')
    company_2_attribute_3 = data.get('competitors', {}).get('company2Attribute3', '')
    company_2_attribute_4 = data.get('competitors', {}).get('company2Attribute4', '')
    company_2_attribute_5 = data.get('competitors', {}).get('company2Attribute5', '')
    company_3_attribute_1 = data.get('competitors', {}).get('company3Attribute1', '')
    company_3_attribute_2 = data.get('competitors', {}).get('company3Attribute2', '')
    company_3_attribute_3 = data.get('competitors', {}).get('company3Attribute3', '')
    company_3_attribute_4 = data.get('competitors', {}).get('company3Attribute4', '')
    company_3_attribute_5 = data.get('competitors', {}).get('company3Attribute5', '')
    company_4_attribute_1 = data.get('competitors', {}).get('company4Attribute1', '')
    company_4_attribute_2 = data.get('competitors', {}).get('company4Attribute2', '')
    company_4_attribute_3 = data.get('competitors', {}).get('company4Attribute3', '')
    company_4_attribute_4 = data.get('competitors', {}).get('company4Attribute4', '')
    company_4_attribute_5 = data.get('competitors', {}).get('company4Attribute5', '')
    company_5_attribute_1 = data.get('competitors', {}).get('company5Attribute1', '')
    company_5_attribute_2 = data.get('competitors', {}).get('company5Attribute2', '')
    company_5_attribute_3 = data.get('competitors', {}).get('company5Attribute3', '')
    company_5_attribute_4 = data.get('competitors', {}).get('company5Attribute4', '')
    company_5_attribute_5 = data.get('competitors', {}).get('company5Attribute5', '')
    company_6_attribute_1 = data.get('competitors', {}).get('company6Attribute1', '')
    company_6_attribute_2 = data.get('competitors', {}).get('company6Attribute2', '')
    company_6_attribute_3 = data.get('competitors', {}).get('company6Attribute3', '')
    company_6_attribute_4 = data.get('competitors', {}).get('company6Attribute4', '')
    company_6_attribute_5 = data.get('competitors', {}).get('company6Attribute5', '')
    company_7_attribute_1 = data.get('competitors', {}).get('company7Attribute1', '')
    company_7_attribute_2 = data.get('competitors', {}).get('company7Attribute2', '')
    company_7_attribute_3 = data.get('competitors', {}).get('company7Attribute3', '')
    company_7_attribute_4 = data.get('competitors', {}).get('company7Attribute4', '')
    company_7_attribute_5 = data.get('competitors', {}).get('company7Attribute5', '')

    differentiation_title = data.get('competitiveDiff', {}).get('differentiationTitle', '')
    differentiation_gpt = data.get('competitiveDiff', {}).get('differentiationGPT', '')
    differentiation_gpt_cleaned = data.get('competitiveDiff', {}).get('differentiationGPTCleaned', '')
    differentiation_gpt_1 = data.get('competitiveDiff', {}).get('differentiationGPT1', '')
    differentiation_gpt_2 = data.get('competitiveDiff', {}).get('differentiationGPT2', '')
    differentiation_gpt_3 = data.get('competitiveDiff', {}).get('differentiationGPT3', '')
    differentiation_gpt_4 = data.get('competitiveDiff', {}).get('differentiationGPT4', '')
    differentiation_gpt_5 = data.get('competitiveDiff', {}).get('differentiationGPT5', '')
    differentiation_gpt_6 = data.get('competitiveDiff', {}).get('differentiationGPT6', '')
    differentiation_header_1 = data.get('competitiveDiff', {}).get('differentiationHeader1', '')
    differentiation_header_2 = data.get('competitiveDiff', {}).get('differentiationHeader2', '')
    differentiation_header_3 = data.get('competitiveDiff', {}).get('differentiationHeader3', '')
    differentiation_header_4 = data.get('competitiveDiff', {}).get('differentiationHeader4', '')
    differentiation_header_5 = data.get('competitiveDiff', {}).get('differentiationHeader5', '')
    differentiation_header_6 = data.get('competitiveDiff', {}).get('differentiationHeader6', '')
    differentiation_1 = data.get('competitiveDiff', {}).get('differentiation1', '')
    differentiation_2 = data.get('competitiveDiff', {}).get('differentiation2', '')
    differentiation_3 = data.get('competitiveDiff', {}).get('differentiation3', '')
    differentiation_4 = data.get('competitiveDiff', {}).get('differentiation4', '')
    differentiation_5 = data.get('competitiveDiff', {}).get('differentiation5', '')
    differentiation_6 = data.get('competitiveDiff', {}).get('differentiation6', '')
    competition_icon_1 = data.get('competitiveDiff', {}).get('competitionIcon1', '')
    competition_icon_2 = data.get('competitiveDiff', {}).get('competitionIcon2', '')
    competition_icon_3 = data.get('competitiveDiff', {}).get('competitionIcon3', '')
    competition_icon_4 = data.get('competitiveDiff', {}).get('competitionIcon4', '')
    competition_icon_5 = data.get('competitiveDiff', {}).get('competitionIcon5', '')
    competition_icon_6 = data.get('competitiveDiff', {}).get('competitionIcon6', 'competition_icon_6')
    team_title = data.get('teamMembers', {}).get('teamTitle', 'team_title')
    name_1 = data.get('teamMembers', {}).get('name1', '')
    designation_title_1 = data.get('teamMembers', {}).get('designationTitle1', '')
    experience_1 = data.get('teamMembers', {}).get('experience1', '')
    linkedin_1 = data.get('teamMembers', {}).get('linkedin1', '')
    image_1 = data.get('teamMembers', {}).get('image1', '')
    name_2 = data.get('teamMembers', {}).get('name2', '')
    designation_title_2 = data.get('teamMembers', {}).get('designationTitle2', '')
    experience_2 = data.get('teamMembers', {}).get('experience2', '')
    linkedin_2 = data.get('teamMembers', {}).get('linkedin2', '')
    image_2 = data.get('teamMembers', {}).get('image2', '')
    name_3 = data.get('teamMembers', {}).get('name3', '')
    designation_title_3 = data.get('teamMembers', {}).get('designationTitle3', '')
    experience_3 = data.get('teamMembers', {}).get('experience3', '')
    linkedin_3 = data.get('teamMembers', {}).get('linkedin3', '')
    image_3 = data.get('teamMembers', {}).get('image3', '')
    name_4 = data.get('teamMembers', {}).get('name4', '')
    designation_title_4 = data.get('teamMembers', {}).get('designationTitle4', '')
    experience_4 = data.get('teamMembers', {}).get('experience4', '')
    linkedin_4 = data.get('teamMembers', {}).get('linkedin4', '')
    image_4 = data.get('teamMembers', {}).get('image4', '')
    name_5 = data.get('teamMembers', {}).get('name5', '')
    designation_title_5 = data.get('teamMembers', {}).get('designationTitle5', '')
    experience_5 = data.get('teamMembers', {}).get('experience5', '')
    linkedin_5 = data.get('teamMembers', {}).get('linkedin5', '')
    image_5 = data.get('teamMembers', {}).get('image5', '')
    name_6 = data.get('teamMembers', {}).get('name6', '')
    designation_title_6 = data.get('teamMembers', {}).get('designationTitle6', '')
    experience_6 = data.get('teamMembers', {}).get('experience6', '')
    linkedin_6 = data.get('teamMembers', {}).get('linkedin6', 'linkedin_6')
    image_6 = data.get('teamMembers', {}).get('image6', '')

    financials_title = data.get('financialInfo', {}).get('financialTitle', '')
    financial_snapshot = data.get('financialInfo', {}).get('financialSnapshot', '')
    funding_ask = data.get('financialInfo', {}).get('fundingAsk', '')
    revenue_chart = data.get('financialInfo', {}).get('revenueChart', '')
    cost_chart_value = data.get('financialInfo', {}).get('costChartValue', '')
    use_of_funds = data.get('financialInfo', {}).get('useOfFunds', '')
    revenue_2019 = data.get('financialInfo', {}).get('revenue2019', '')
    revenue_2020 = data.get('financialInfo', {}).get('revenue2020', '')
    revenue_2021 = data.get('financialInfo', {}).get('revenue2021', '')
    revenue_2022 = data.get('financialInfo', {}).get('revenue2022', '')
    revenue_2023 = data.get('financialInfo', {}).get('revenue2023', '')
    revenue_2024 = data.get('financialInfo', {}).get('revenue2024', '')
    revenue_2025 = data.get('financialInfo', {}).get('revenue2025', '')
    revenue_2026 = data.get('financialInfo', {}).get('revenue2026', '')
    revenue_2027 = data.get('financialInfo', {}).get('revenue2027', '')
    revenue_2028 = data.get('financialInfo', {}).get('revenue2028', '')
    cost_2019 = data.get('financialInfo', {}).get('cost2019', '')
    cost_2020 = data.get('financialInfo', {}).get('cost2020', '')
    cost_2021 = data.get('financialInfo', {}).get('cost2021', '')
    cost_2022 = data.get('financialInfo', {}).get('cost2022', '')
    cost_2023 = data.get('financialInfo', {}).get('cost2023', '')
    cost_2024 = data.get('financialInfo', {}).get('cost2024', '')
    cost_2025 = data.get('financialInfo', {}).get('cost2025', '')
    cost_2026 = data.get('financialInfo', {}).get('cost2026', '')
    cost_2027 = data.get('financialInfo', {}).get('cost2027', '')
    cost_2028 = data.get('financialInfo', {}).get('cost2028', '')
    product_and_development = data.get('financialInfo', {}).get('productDevelopment', '')
    marketing_and_sales = data.get('financialInfo', {}).get('marketingSales', '')
    capex = data.get('financialInfo', {}).get('capex', '')
    business_operations = data.get('financialInfo', {}).get('businessOperations', '')
    team_salaries = data.get('financialInfo', {}).get('teamSalaries', '')

    contact_email = data.get('contactInfo', {}).get('contactEmail', '')
    contact_phone = data.get('contactInfo', {}).get('contactPhone', '')
    contact_website = data.get('contactInfo', {}).get('contactWebsite', '')
    company_linkedin = data.get('contactInfo', {}).get('companyLinkedin', '')
    contact_us_cover_image = data.get('contactInfo', {}).get('contactUsCoverImage', '')
    status = ''
    error_fields = ''


    res = [
    user_id,
    form_id,
    company_name,
    company_logo,
    primary_r,
    primary_g,
    primary_b,
    secondary_r,
    secondary_g,
    secondary_b,
    primary_color_check,
    secondary_color_check,
    p100,
    p75_s25,
    p50_s50,
    p25_s75,
    s100,
    f_p100,
    f_p75s25,
    f_p50s50,
    f_p25s75,
    f_s100,
    scl,
    scd,
    tag_line,
    cover_image,
    about_title,
    vision,
    about_gpt,
    about_gpt_cleaned,
    about_gpt_1,
    about_gpt_2,
    about_1_header,
    about_2_header,
    about_3_header,
    about_4_header,
    about_5_header,
    about_1,
    about_2,
    about_3,
    about_4,
    about_5,
    about_image_url,
    problem_title,
    problem_statement,
    problem_gpt,
    problem_gpt_cleaned,
    problem_gpt_1,
    problem_gpt_2,
    problem_gpt_3,
    problem_gpt_4,
    problem_gpt_5,
    problem_gpt_6,
    problem_header_1,
    problem_header_2,
    problem_header_3,
    problem_header_4,
    problem_header_5,
    problem_header_6,
    problem_description_1,
    problem_description_2,
    problem_description_3,
    problem_description_4,
    problem_description_5,
    problem_description_6,
    problem_icon_1,
    problem_icon_2,
    problem_icon_3,
    problem_icon_4,
    problem_icon_5,
    problem_icon_6,
    iterative_solution,
    solution_title,
    solution_statement,
    solution_gpt,
    solution_gpt_cleaned,
    solution_gpt_1,
    solution_gpt_2,
    solution_gpt_3,
    solution_gpt_4,
    solution_gpt_5,
    solution_gpt_6,
    solution_header_1,
    solution_header_2,
    solution_header_3,
    solution_header_4,
    solution_header_5,
    solution_header_6,
    solution_description_1,
    solution_description_2,
    solution_description_3,
    solution_description_4,
    solution_description_5,
    solution_description_6,
    solution_icon_1,
    solution_icon_2,
    solution_icon_3,
    solution_icon_4,
    solution_icon_5,
    solution_icon_6,
    industry,
    market_title_gpt,
    market_title,
    market_description,
    industry_competitiveness,
    tam,
    tam_description,
    sam,
    sam_description,
    som,
    som_description,
    growth_driver_gpt,
    growth_driver_gpt_cleaned,
    growth_driver_gpt_1,
    growth_driver_gpt_2,
    growth_driver_gpt_3,
    growth_driver_gpt_4,
    growth_driver_gpt_5,
    growth_driver_1,
    growth_driver_2,
    growth_driver_3,
    growth_driver_4,
    growth_driver_5,
    year_1,
    year_2,
    tam_growth_rate,
    tam_future,
    sam_growth_rate,
    sam_future,
    product_title,
    product_overview,
    feature_gpt,
    feature_gpt_cleaned,
    feature_gpt_1,
    feature_gpt_2,
    feature_gpt_3,
    feature_gpt_4,
    feature_gpt_5,
    feature_gpt_6,
    feature_1,
    feature_2,
    feature_3,
    feature_4,
    feature_5,
    feature_6,
    feature_description_1,
    feature_description_2,
    feature_description_3,
    feature_description_4,
    feature_description_5,
    feature_description_6,
    feature_icon_1,
    feature_icon_2,
    feature_icon_3,
    feature_icon_4,
    feature_icon_5,
    feature_icon_6,
    product_roadmap_title,
    phase_gpt,
    phase_gpt_cleaned,
    phase_gpt_1,
    phase_gpt_2,
    phase_gpt_3,
    phase_header_1_name,
    phase_header_2_name,
    phase_header_3_name,
    phase_description_1,
    phase_description_2,
    phase_description_3,
    phase_features_1,
    phase_features_2,
    phase_features_3,
    inputs,
    technology_platform,
    value_based_output,
    mobile_screenshots_description,
    mobile_screenshot_1,
    mobile_screenshot_2,
    mobile_screenshot_3,
    web_screenshots_description,
    web_screenshot_1,
    web_screenshot_2,
    web_screenshot_3,
    revenue_model,
    revenue_model_image,
    revenue_stream_gpt,
    revenue_stream_gpt_cleaned,
    revenue_stream_gpt_1,
    revenue_stream_gpt_2,
    revenue_stream_gpt_3,
    revenue_stream_gpt_4,
    stream_1,
    stream_2,
    stream_3,
    stream_4,
    stream_description_1,
    stream_description_2,
    stream_description_3,
    stream_description_4,
    stream_icon_1,
    stream_icon_2,
    stream_icon_3,
    stream_icon_4,
    stakeholders_title,
    stakeholder_gpt,
    stakeholder_gpt_cleaned,
    stakeholder_gpt_1,
    stakeholder_gpt_2,
    stakeholder_gpt_3,
    stakeholder_gpt_4,
    stakeholder_1,
    stakeholder_2,
    stakeholder_3,
    stakeholder_4,
    benefits_1,
    benefits_2,
    benefits_3,
    benefits_4,
    customer_profile_icon_1,
    customer_profile_icon_2,
    customer_profile_icon_3,
    customer_profile_icon_4,
    customer_profile_cover_image,
    persona,
    persona_category_gpt,
    persona_category_gpt_cleaned,
    persona_category_gpt_1,
    persona_category_gpt_2,
    persona_category_gpt_3,
    persona_header_1,
    persona_header_2,
    persona_header_3,
    persona_description_1,
    persona_description_2,
    persona_description_3,
    persona_icon_1,
    persona_icon_2,
    persona_icon_3,
    gtm_title,
    gtm_overview,
    gtm_cover_image_landscape,
    gtm_gpt,
    gtm_gpt_cleaned,
    gtm_gpt_1,
    gtm_gpt_2,
    gtm_gpt_3,
    gtm_gpt_4,
    gtm_gpt_5,
    gtm_header_1,
    gtm_header_2,
    gtm_header_3,
    gtm_header_4,
    gtm_header_5,
    gtm_description_1,
    gtm_description_2,
    gtm_description_3,
    gtm_description_4,
    gtm_description_5,
    gtm_icon_1,
    gtm_icon_2,
    gtm_icon_3,
    gtm_icon_4,
    gtm_icon_5,
    track_record_title,
    phase_timeline_1,
    phase_timeline_2,
    phase_timeline_3,
    traction_phase_header_1,
    traction_phase_header_2,
    traction_phase_header_3,
    traction_phase_description_1,
    traction_phase_description_2,
    traction_phase_description_3,
    case_study_title,
    case_study,
    challenges,
    solution,
    outcome,
    case_study_cover_image,
    testimonial_1,
    testimonial_name_1,
    designation_1,
    testimonial_2,
    testimonial_name_2,
    designation_2,
    testimonial_3,
    testimonial_name_3,
    designation_3,
    testimonial_4,
    testimonial_name_4,
    designation_4,
    company_1,
    company_2,
    company_3,
    company_4,
    company_5,
    company_6,
    company_7,
    attribute_gpt,
    attribute_gpt_cleaned,
    attribute_gpt_1,
    attribute_gpt_2,
    attribute_gpt_3,
    attribute_gpt_4,
    attribute_gpt_5,
    attribute_1,
    attribute_2,
    attribute_3,
    attribute_4,
    attribute_5,
    attribute_1_ratings,
    attribute_2_ratings,
    attribute_3_ratings,
    attribute_4_ratings,
    attribute_5_ratings,
    company_1_attribute_1,
    company_1_attribute_2,
    company_1_attribute_3,
    company_1_attribute_4,
    company_1_attribute_5,
    company_2_attribute_1,
    company_2_attribute_2,
    company_2_attribute_3,
    company_2_attribute_4,
    company_2_attribute_5,
    company_3_attribute_1,
    company_3_attribute_2,
    company_3_attribute_3,
    company_3_attribute_4,
    company_3_attribute_5,
    company_4_attribute_1,
    company_4_attribute_2,
    company_4_attribute_3,
    company_4_attribute_4,
    company_4_attribute_5,
    company_5_attribute_1,
    company_5_attribute_2,
    company_5_attribute_3,
    company_5_attribute_4,
    company_5_attribute_5,
    company_6_attribute_1,
    company_6_attribute_2,
    company_6_attribute_3,
    company_6_attribute_4,
    company_6_attribute_5,
    company_7_attribute_1,
    company_7_attribute_2,
    company_7_attribute_3,
    company_7_attribute_4,
    company_7_attribute_5,
    differentiation_title,
    differentiation_gpt,
    differentiation_gpt_cleaned,
    differentiation_gpt_1,
    differentiation_gpt_2,
    differentiation_gpt_3,
    differentiation_gpt_4,
    differentiation_gpt_5,
    differentiation_gpt_6,
    differentiation_header_1,
    differentiation_header_2,
    differentiation_header_3,
    differentiation_header_4,
    differentiation_header_5,
    differentiation_header_6,
    differentiation_1,
    differentiation_2,
    differentiation_3,
    differentiation_4,
    differentiation_5,
    differentiation_6,
    competition_icon_1,
    competition_icon_2,
    competition_icon_3,
    competition_icon_4,
    competition_icon_5,
    competition_icon_6,
    team_title,
    name_1,
    designation_title_1,
    experience_1,
    linkedin_1,
    image_1,
    name_2,
    designation_title_2,
    experience_2,
    linkedin_2,
    image_2,
    name_3,
    designation_title_3,
    experience_3,
    linkedin_3,
    image_3,
    name_4,
    designation_title_4,
    experience_4,
    linkedin_4,
    image_4,
    name_5,
    designation_title_5,
    experience_5,
    linkedin_5,
    image_5,
    name_6,
    designation_title_6,
    experience_6,
    linkedin_6,
    image_6,
    financials_title,
    financial_snapshot,
    funding_ask,
    revenue_chart,
    cost_chart_value,
    use_of_funds,
    revenue_2019,
    revenue_2020,
    revenue_2021,
    revenue_2022,
    revenue_2023,
    revenue_2024,
    revenue_2025,
    revenue_2026,
    revenue_2027,
    revenue_2028,
    cost_2019,
    cost_2020,
    cost_2021,
    cost_2022,
    cost_2023,
    cost_2024,
    cost_2025,
    cost_2026,
    cost_2027,
    cost_2028,
    product_and_development,
    marketing_and_sales,
    capex,
    business_operations,
    team_salaries,
    contact_email,
    contact_phone,
    contact_website,
    company_linkedin,
    contact_us_cover_image,
    status,
    error_fields
    ]
    return res


# API_InnoTalent_Engine

**AI-Powered Talent Dashboard**

API_InnoTalent_Engine is a sophisticated API designed to streamline the hiring process for companies. By integrating five AI models, including one from **OpenAI** and **four custom AI models**, this API evaluates candidate resumes in PDF format. 

![Features](https://github.com/LeeChongKeat/API_InnoTalent_Engine/blob/main/ReadMeImg/features.png)

__Which are:__
1. OpenAI ChatGPT 
2. Resignation Intention AI - https://github.com/LeeChongKeat/Resignation_Intention_Prediction
3. Salary AI - https://github.com/LeeChongKeat/Salary_Prediction
4. Employee Rating AI - https://github.com/LeeChongKeat/Employee_Personal_Rating_Prediction
5. Work Performance (Return on Work) - https://github.com/LeeChongKeat/Work_Performance_Prediction

Based on these evaluations, it provides an overall score to determine if a candidate is the right fit for the company.

AI-Powered Talent Dashboard Report, evaluate the candidate resume based on five aspects to determine if they are the right fit for the company, and then decide whether to proceed with the interview.


![Flow](https://github.com/LeeChongKeat/API_InnoTalent_Engine/blob/main/ReadMeImg/api-flow.png)

## Features
- **AI Integration**: Incorporates one OpenAI model and four custom AI models for comprehensive resume analysis.
- **PDF Resume Analysis**: Allows candidates to upload their resumes in PDF format, saving time and effort for both candidates and employers.
- **Predictive Insights**: Predicts future resignation intention, return on work, working performance, and expected salary based on the candidate's resume.
- **Efficient Screening**: Helps companies filter resumes effectively, enabling them to focus on candidates who are more likely to succeed in the organization.
- **Time-Saving**: By automating the initial evaluation process, it saves valuable time for HR professionals, allowing them to focus on interviewing potential candidates.


## How it Works
1. **Upload Resume**
2. **AI Analysis**
3. **Evaluation**
4. **Overall Score**
5. **Provide Next Action Insight**


## Benefits
- **Smart Decision-Making**: Make data-driven decisions by leveraging AI insights for candidate evaluation.
- **Cost-Efficiency**: Reduce costs associated with manual resume screening and optimize the hiring process.
- **Enhanced Hiring**: Identify and hire candidates who align with the organization's requirements and values.
- **Improved Productivity**: Focus on interviewing candidates who are more likely to contribute positively to the company.


## Get Started
1. Install the environment.yml
2. Change the Config.json file (OpenAI Key and Database)
3. Python command start the API python main.py


## API
1. [POST] api/InnoTalent/SubmitApplication : Upload the Resume PDF File
2. [GET] api/InnoTalent/Get/{Talent_Id} : Get the Talent's Overall Score


## GET api/InnoTalent/Get/{Talent_Id} : Return
talent_results = {
        "talent_id": talent_id,
        "pre_rating": Return on talent matching rate: decimal,
        "pre_performance": Return working performance (Work ROW value) %: decimal,
        "pre_salary": Return talent satisfaction salary: decimal ,
        "pre_salary_next_three_year": Return next 3 years talent satisfaction salary: decimal list,
        "pre_return_next_three_year": Return next 3 years talent ROW: decimal list,
        "next_interview_percentage": Return rate performance: decimal,
        "pre_resign_intention_next_three_year": Return next 3 years resign intention percentage: decimal lis
    }

## Contact
Name: Ts. Lee Chong Keat - jerry_keat@hotmail.com

Project Link: [https://github.com/LeeChongKeat/API_InnoTalent_Engine](https://github.com/LeeChongKeat/API_InnoTalent_Engine)



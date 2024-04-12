from flask import Flask,render_template,redirect,request,jsonify

app = Flask(__name__)

import json
import requests

def cv_extractor(file_name):
    
    
    # path = f'/uploads/samle.png'
    # pth = r"InterviewFrontend\uploads\samle.png"
    path = f'interviewFrontend\\uploads\\{file_name}'
    
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjdlMWMzMzAtNmI1MS00OTUwLWFmMTktNDk1NGQ0NzY1NWViIiwidHlwZSI6ImFwaV90b2tlbiJ9.wJyXklbqYunrNUxQLtE2G6jd-qIkrDcD-bcFW2bdi5c"}

    url = "https://api.edenai.run/v2/ocr/resume_parser"
    data = {
    "providers": "affinda",
    "fallback_providers": ""
    }
    files = {'file': open(path, 'rb')}

    response = requests.post(url, data=data, files=files, headers=headers)

    result = json.loads(response.text)
    result = result['affinda']['extracted_data']
    
    raw_name=result['personal_infos']['name']['raw_name']

    self_summary=result['personal_infos']['self_summary']

    education=result['education']['entries']

    if len(education) > 0 and 'establishment' in education[0]:
        college = education[0]['establishment']
    else:
        college = ""

    if len(education) > 0 and 'gpa' in education[0]:
        gpa = education[0]['gpa']
        if gpa is None:
            gpa = "Good"
    else:
        gpa = "Good" 

    # Handle education
    degree_name = ""
    if len(education) > 0 and 'accreditation' in education[0]:
        degree_name = education[0]['accreditation']

    # Handle skills
    skill_1 = []
    if 'skills' in result:
        skills = result['skills']
        for skill in skills:
            if 'name' in skill and skill['name'] is not None:
                skill_1.append(skill['name'])

    # certificates=result['certifications']
    # certificates_1=[]
    # for certif in certificates:
    #     certificates_1.append(certif['name'])

    # Interviwee_info=f'''My name is {raw_name} and had done {degree_name} from {college} college with a {gpa} 
    #             gpa.I have following {skill_1} and I have also done courses like {certificates_1}.
    #                 I'm here to give Interview '''
    answer.clear()
    answer.append([raw_name,self_summary,skill_1,education,college,degree_name,gpa])
    print(answer)
    return answer



answer =[]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv_parser.html',methods=['GET','POST'])
def cv_parser():
    if len(answer)!=0:  
        # answer = answer[len(answer)-1]
        return render_template('cv_parser.html',answer = json.dumps(answer))
    return render_template('cv_parser.html',answer= {})

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'interviewFrontend\\uploads\\{file.filename}')
    # answer = []
    # answer.clear()
    answer = cv_extractor(file.filename)
    # print(answer)
    # return redirect('/cv_receiver.html')
    return redirect('cv_parser.html')


@app.route('/third.html')
def third():
    return render_template('third.html')
if __name__=='__main__':
    app.run(debug=True)

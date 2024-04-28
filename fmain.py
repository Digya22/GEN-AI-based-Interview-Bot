from flask import Flask,render_template,redirect,request,jsonify,url_for
import requests,json,os
import os,speech_recognition
from stars import Summary
from pyht import Client, TTSOptions, Format
import pyaudio
# from functions import chatgpt,text_to_speech,speech_to_text
# from functions import *
import os

headers = {"Authorization": "Bearer API key"}
answer=[]
history=[]

#Interview Bot Functions
def cv_extracter(file_path):
    # path = os.path.join("/Interview_bot/uploads/",filename)
    url = "https://api.edenai.run/v2/ocr/resume_parser"
    data = {
        "providers": "affinda",
        "fallback_providers": ""
    }
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, data=data, files=files, headers=headers)
    result = json.loads(response.text)
    result=result['affinda']['extracted_data']
    
    Interviwee_info=''
    #extracting Useful data from result
    try:
        raw_name=result['personal_infos']['name']['raw_name']
        self_summary=result['personal_infos']['self_summary']
        education=result['education']['entries']
        if len(education)>0 and 'establishment' in education[0]:
            college=education[0]['establishment']
        else:
             college="No data available"
        if len(education)>0 and 'gpa' in education[0]:
            gpa=education[0]['gpa']
            if gpa==None:
                gpa="Good"
        else:
             gpa="no data available"
        if len(education)>0 and 'accreditation' in education[0]:
            degree_name=education[0]['accreditation']
        else:
             degree_name="No data available"
        skill_1=[]
        if 'skills' in result:
            skills=result['skills']
            for skill in skills:
                if 'name' in skill and skill["name"] is not None:
                     skill_1.append(skill["name"])
                else:
                     continue
        if 'certifications' in result and result['certifications'] is not None:
            certificates=result['certifications']
            certificates_1=[]
            for certif in certificates:
                certificates_1.append(certif['name'])

        Interviwee_info=f'''My name is {raw_name} and had done {degree_name} from {college} college with a {gpa} 
                    gpa.I have following {skill_1} and I have also done courses like {certificates_1}.
                        I'm here to give Interview and this is my self summary {self_summary}'''

    except IndexError:
        Interviwee_info=f'''{result}'''

    answer.clear()
    answer.append([raw_name,self_summary,skill_1,education,college,degree_name,gpa])
   
    
    return Interviwee_info


payload = {
    "providers": "openai",
    "openai":"gpt-4",
    "text": " ",
    "chatbot_global_action": '''
                        Task: Conduct a technical interview to evaluate candidate's expertise, 
                              incorporating aspects from their CV and broader technical knowledge
                        Topic: Assess candidate's proficiency in areas highlighted in their CV, 
                               problem-solving skills, and technical knowledge, supplemented by 
                               general technical questions
                        Style: Professional and inquisitive
                        Tone: Respectful and analytical
                        Audience: Hiring managers and technical team members
                        Word Count: 50 words
                        Format: Text

                        Prompt:
                        As the interviewer, aim to strike a balance between questions directly related to the 
                        candidate's CV and broader technical topics. Craft questions that explore their listed 
                        experiences and skills while also challenging their problem-solving abilities in 
                        diverse scenarios. Use the CV as a starting point but encourage exploration beyond its 
                        scope to gauge the candidate's overall technical prowess.

                            ''',
    # "previous_history": [{'role':'user','message':Interviwee_info}],
     "previous_history": [],
    "temperature": 0.9,
    "max_tokens": 1000,
    "fallback_providers": ""
}

# Interviwee_info=[]
file_path1=[]
app=Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/cv_parser.html',methods=['GET','POST'])
def cv_parser():
    if len(answer)!=0:  
        # answer = answer[len(answer)-1]
        return render_template('cv_parser.html',answer = json.dumps(answer))
    return render_template('cv_parser.html',answer= {})
# file1=None
@app.route('/upload',methods=['GET','POST'])
def upload():
    path="/Interview_bot/uploads/"
    file = request.files['file']
    file_path = os.path.join(path,f"{file.filename}")
    # file_path1.append(file_path)
    print(file_path)
    file.save(file_path)
    # global interview
    Interviewee_info=cv_extracter(file_path)
    payload["previous_history"] = [{"role": "user", "message": Interviewee_info}]
    history.append({"role": "user", "message": Interviewee_info})
    print(history)
    
    return redirect('cv_parser.html')



Interviwee_info = None
@app.route('/third.html',methods=["GET", "POST"])
def third():
    
    if request.method == "POST":
        if request.form["action"] == "start":
            
            speech_text=speech_to_text()
            gpt=chatgpt(speech_text)
            text_to_speech(gpt)
            
        elif request.form["action"]=="exit":
               return redirect(url_for('summary_route'))
    return render_template('third.html')


@app.route('/summary_route',methods=["GET", "POST"])
def summary_route():
    if request.method == "POST":
    
        if request.form["action"] == "report":
            Summary()
    # This is the route you want to redirect to
    return render_template('form2.html')


     


def speech_to_text():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    #convert listened file to wav format
    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

    filename="microphone-results.wav"
    current_directory = os.getcwd()
    absolute_path = os.path.join(current_directory, filename)

    url = "https://api.edenai.run/v2/audio/speech_to_text_async"
    data1 = {
        "providers": "openai",
        "language": "en-US",
    }

    files = {'file': open(absolute_path, 'rb')}

    response = requests.post(url, data=data1, files=files, headers=headers)
    result = json.loads(response.text)
    
    print(result['results']['openai']['text'])
    return result['results']['openai']['text']



# Interviwee_info=Interviwee_info[0]
# Interviwee_info=cv_extracter(file_path1[0])
# Interviwee_info=cv_extracter()
# payload = {
#     "providers": "openai",
#     "openai":"gpt-4",
#     "text": " ",
#     "chatbot_global_action": '''
#                         Task: Act as a smart and intelligent interviewer
#                         Topic: Technical Questions and general questions based on CV
#                         Style: Formal
#                         Tone: Professional
#                         Audience: 25-30 year old
#                         Word Count: 20 words
#                         Format: Text
#                             ''',
#     # "previous_history": [{'role':'user','message':Interviwee_info}],
#      "previous_history": [],
#     "temperature": 0.9,
#     "max_tokens": 1000,
#     "fallback_providers": ""
# }
# global history
# history=[{'role':'user','message':Interviwee_info}]

    


def chatgpt(speech_text):
    # print(Interviwee_info)
    # print(interview)
    url = "https://api.edenai.run/v2/text/chat"
    payload["text"]=speech_text
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    text=result['openai']['generated_text']

    for i in result['openai']['message']:
            #payload["previous_history"].append(i)
            history.append(i)

    save_data()
    return text


def text_to_speech(gpt):
    
    text=gpt

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
            channels=1,
            rate=44000,
            output=True)
   
    client = Client("4UHQvSzaL9dFFBT1nufXJYXTMUp2", "7c8426cce782417d8670aa5481f36a3a")
    options = TTSOptions(

        voice="s3://voice-cloning-zero-shot/9f1ee23a-9108-4538-90be-8e62efc195b6/charlessaad/manifest.json",
        # you can pass any value between 8000 and 48000, 24000 is default
        sample_rate=44000,
        # the generated audio encoding, supports 'raw' | 'mp3' | 'wav' | 'ogg' | 'flac' | 'mulaw'
        format=Format.FORMAT_WAV,
        # playback rate of generated speech
        speed=0.8,
                        )
    #audio_bytes=b""
    try:
    # must use turbo voice engine for the best latency
        for chunk in client.tts(text=text, voice_engine="PlayHT2.0-turbo", options=options):
            #audio_bytes= chunk
            stream.write(chunk)
    except IOError:
            stream.write(chunk)
    
    print("stop")
    stream.stop_stream()
    stream.close()
    p.terminate()


   

def save_data():
        history_copy = history[:]
        payload["previous_history"].extend(history_copy[-4:])
   
        with open("database1.json",'w') as f:
                    json.dump(history_copy,f,indent=2)






if __name__ == '__main__':
   app.run(debug = True)
   

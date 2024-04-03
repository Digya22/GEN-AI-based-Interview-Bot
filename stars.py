import json,requests,time
from fpdf import FPDF


title="Interview Bot"
class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("gen ai logo.jpeg", 10, 8, 25)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        width = self.get_string_width(title) + 6
        doc_w=self.w
        self.set_x((doc_w - width) / 2)
        # Printing title:
        self.cell(width, 10, title, border=1, align="C")
        # Performing a line break:
        self.ln(40)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}", align="C")



pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)
# global i
# i=0
# def pdf_question():
#     pdf.set_font("Times",'B',12)
    
    
def pdf_style():
        # i=i+1
        
        pdf.multi_cell(0, 10, f"QUESTION]:\n{key}", new_x="LMARGIN", new_y="NEXT",align="L")

        pdf.ln(0.5)
        pdf.multi_cell(0, 10, f"ANSWER:\n{dict[key]}", new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.ln(0.5)
        pdf.multi_cell(0, 10, f"MODEL ANSWER:\n{text}", new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.ln(0.5)

    



with open("database.json",'r') as f:
    data=json.load(f)

s=len(data)
print(s)

X=2
dict={}
while X<s:
    try :
        Question=data[X]["message"]
        Answer=data[X+1]["message"]
        dict.__setitem__(Question,Answer)
        X=X+2
    except IndexError:
        break
    

#print(dict)


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzFmNmVkNTQtYTEyOS00OGQ3LWE5M2QtYjY4ZjJhZjE0ODAxIiwidHlwZSI6ImFwaV90b2tlbiJ9.0mqunmwbidTbT4af6mZhGe2Gja76XkYNAZiVKas_4B8"}

url = "https://api.edenai.run/v2/text/chat"


for key in dict.keys():
    payload = {
        "providers": "openai",
        "openai":"gpt-4",
        # "text": '''Question :Great! Let's begin the technical questions. Can you elaborate on your experience with Python and how you have used it in your software development projects? 
        #             Answer : I have good experience in Python.I have been working with python for last 3 years and i have gained many experience in it
        #                     .I had used python in many of my ML projects as python supports many ML libraries.Also i have used python for creating 
        #                        web appliction s using its web framework like Flask.   ''',
        "text": f'''Question:{key}
                    Answer: {dict[key]}
                    ''',
        "chatbot_global_action": '''
                                    you have a task to give rating to pair of question answer on the scale of 1 to 10 based on 
                                    relevance,quality,accuracy of answer depending upon the question.If the question's answer is based on past experience or
                                    dependent on each person view's the you cna give it a rating of 5 and if the answer is totally wrong then give it a 0 rating.
                                    Also provide a model asnwer to that question assuming yourslef
                                    in that position.
                                ''',
        # "chatbot_global_action":''' Task :Give rating to the pair of Question and Answer on the scale of 1 to 10.
        #                                     Also provide a better answer to the asked question based on his/her skills and intellect level and assume yourself while giving the answer.
        #                             Style: Formal
        #                             Tone: Professional
        #                             word count : less than 50
        #                                                         ''',
        "previous_history": [],
        "temperature": 0.5,
        "max_tokens": 500,
        "fallback_providers": "replicate"
    }
    #result="text"
    key1=key
    
    #pdf.set_font("Times", size=12)
    #pdf.content(key1)
    #pdf.get_string_width(key1)
    #pdf.multi_cell(0, 5, f"Printing line number{key}", new_x="LMARGIN", new_y="NEXT",align="L")
    #pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT",align="L")
    # pdf.multi_cell(0, 10, f"Question:{key}", new_x="LMARGIN", new_y="NEXT",align="L")
    # pdf.multi_cell(0, 10, f"Answer:{dict[key]}", new_x="LMARGIN", new_y="NEXT",align="L")
    #pdf.multi_cell(0, 10, f"Model Answer and rating:{text}", new_x="LMARGIN", new_y="NEXT",align="L")
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)
        text=result['openai']['generated_text']
        
        pdf_style()
        print("om")
        # with open("summary.json",'w') as f:
        #             json.dump(key,f,indent=2)
        #             json.dump(dict[key],f,indent=2)
        #             json.dump(text,f,indent=2)
        
    except KeyError:
        continue
    #print(result)
    # print(f"Q]{key}")
    # print(result)
 



        





    #time.sleep(5)
    # except KeyError:
    #     print(KeyError)
    #     #print(result)
    #     continue
    # #i=i+1
print("stopped")
pdf.output("new-tuto2.pdf")







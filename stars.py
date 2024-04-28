import json,requests
from fpdf import FPDF
# from fmain import answer

#global text,key

title="GenAI"
subtitle="AI Interview Platform"
class PDF(FPDF):
    def header(self):
        self.add_font('Jura','B',r'Jura\static\Jura-Bold.ttf',uni=True)
        #self.add_font('Jura','',r'Jura\static\Jura-Bold.ttf',uni=True)
        # Rendering logo:
        self.image("l2-removebg-preview.png", 6, 2, 40,40)
        self.set_font("Jura", "B", 25)
        
        self.cell(80)
        #widt of text
        width = self.get_string_width(title) + 6
        #width of page
        doc_w=self.w
        self.set_x((doc_w - width) / 2)
        self.cell(width, 15, title, border=0, align="C")
        self.ln(2)


        self.set_font("Jura", "B", 15)
        self.cell(80)
        self.cell(30,25,subtitle,border=0,align='C')
        # Performing a line break:
        self.ln(40)
        self.line(x1=4,y1=40,x2=206,y2=40)
        self.line(x1=4,y1=41,x2=206,y2=41)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # pdf.line(x1=4,y1=-15,x2=206,y2=-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}", align="C")



pdf = PDF()
pdf.add_page()


pdf.add_font('Dosis','B',r'Dosis\static\Dosis-Bold.ttf',uni=True)

pdf.add_font('Dosis','',r'Dosis\static\Dosis-Regular.ttf',uni=True)



#pdf.add_font('Dosis','',r'Dosis\Dosis-VariableFont_wght.ttf',uni=True)
#pdf.set_font("Times", size=12)

    
    
def pdf_style(i,key,text):
  
        # pdf.rect(4,4,202,290)
        pdf.set_font("Dosis",style='B',size=13)
        pdf.multi_cell(0, 10, f"Question {i}:", new_x="LMARGIN", new_y="NEXT",align="L")

        pdf.set_font("Dosis",style='B')
        pdf.multi_cell(0, 10, f"{key}", new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.ln(0.5)

        pdf.set_font("Dosis",style='B',size=13)
        pdf.multi_cell(0, 10, f"Answer:", new_x="LMARGIN", new_y="NEXT",align="L")

        pdf.set_font("Dosis",style='')
        pdf.multi_cell(0, 10, f"{dict1[key]}", new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.ln(0.5)

        pdf.set_font("Dosis",style='B',size=13)
        pdf.multi_cell(0, 10, f"Model Answer and Rating:", new_x="LMARGIN", new_y="NEXT",align="L")

        pdf.set_font("Dosis",style='')
        pdf.multi_cell(0, 10, f"{text}", new_x="LMARGIN", new_y="NEXT",align="L")
        pdf.ln(0.5)
        pdf.rect(4,4,202,290)
        # pdf.ln(1)
        x=pdf.get_x()
        y=pdf.get_y()
        
        # pdf.dashed_line(x1=x,y1=y,x2=x+190,y2=y,dash_length=2,space_length=4)
        pdf.set_dash_pattern(dash=4,gap=2,phase=3)
        pdf.line(x1=x,y1=y,x2=x+190,y2=y)
        pdf.set_dash_pattern()
        
    

dict1={}
def Summary():
    with open("database.json",'r') as f:
        data=json.load(f)

    s=len(data)

       

    print(s)

    X=2
   
    while X<s:
        try :
            Question=data[X]["message"]
            Answer=data[X+1]["message"]
            dict1.__setitem__(Question,Answer)
            X=X+2
        except IndexError:
            break

        except UnicodeEncodeError:
            break
        




    headers = {"Authorization": "Bearer API key"}

    url = "https://api.edenai.run/v2/text/chat"

    i=0
    for key in dict1.keys():
        payload = {
            "providers": "openai",
            "openai":"gpt-4",
            "text": f'''Question:{key}
                        Answer: {dict1[key]}
                        ''',
            # "chatbot_global_action": '''
            #                             you have a task to give rating to pair of question answer on the scale of 1 to 10 based on 
            #                             relevance,quality,accuracy of answer depending upon the question.If the question's answer is based on past experience or
            #                             dependent on each person view's the you cna give it a rating of 5 and if the answer is totally wrong then give it a 0 rating.
            #                             Also provide a model asnwer to that question assuming yourslef
            #                             in that position.
            #                         ''',
            "chatbot_global_action":''' Task: Evaluate a set of interview questions and answers, providing the rating first, followed by an analysis of the given answer and a model answer.
                                        Objective: Your objective is to critically assess each answer, considering its relevance, clarity, depth, and professionalism. 
                                        Style: Formal
                                        Tone: Professional and impartial
                                        Word Count: Less than 50
                                        Format: Text

                                        Point of this Prompt:
                                        The purpose of this task is to ensure thorough evaluation of interview responses, including their quality, relevance, and professionalism. By providing ratings and model answers, the aim is to encourage improvement and refinement in communication skills, fostering clearer and more effective interview interactions.

                                                                    '''

                                        ,
            "previous_history": [],
            "temperature": 0.9,
            "max_tokens": 1000,
            "fallback_providers": "replicate"
        }

        #key1=key
        
        
        
        i=i+1
        try:
            response = requests.post(url, json=payload, headers=headers)
            result = json.loads(response.text)
            text=result['openai']['generated_text']
            

            
            pdf_style(i,key,text)
            
        
            # print("om")
            
        except KeyError:
            continue


Summary()

    # name=answer[0]
print("stopped")
pdf.output("interview report.pdf")







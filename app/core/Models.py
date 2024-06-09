import os
import google.generativeai as genai


key = os.getenv("GEMINI_KEY")

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_response(promt):
    promt = f'generate an hbs script for : {promt},use bootstrap,just provide code of the body part only,no explanation needed'
    response = model.generate_content(promt)
    #print(response.text)
    output = response.text.split("\n")
    #print(output[1:-1])
    return output[1:-1]

def check_if_ok():
    if key==None:
        return False
    return True

def generate_route_response(promt,path,code):
    promt = f'consider this code,{code},generate an express route code for :{promt} ,use async/await and use res.render and render path is {path},no explanation needed'
    response = model.generate_content(promt)
    #print(response.text)
    output = response.text.split("\n")
    return output[1:-1]
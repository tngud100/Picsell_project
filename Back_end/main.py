from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import os

app = FastAPI()

main_dir = os.path.dirname(__file__)

templates = Jinja2Templates(directory=f"{main_dir}../")


@app.get('/')
def get_login_form(request: Request):
    return templates.TemplateResponse('index.html', context={'request':request})
# /login을 입력하면 ex.html과 연결하는 것

# @app.post('/login')
# def login(username:str=Form(...), password:str=Form(...)):
#     return {"username":username, "password":password}

# if __name__=='__main__':
#     uvicorn.run(app, host='0.0.0.0', port = 8000)
import time
from fastapi import FastAPI, Request
import jwt

app = FastAPI()

@app.get("/jwt")
async def get_jwt():
    temp = {
        "id":"아이디",
        "exp": time.time() + 30
    }
    
    return jwt.encode(temp, "비밀소금", algorithm="HS256")

@app.get("/")
async def root(request: Request):
    if (request.headers.get("Authoriazation") == None):
        return "토큰없음"
    
    token = request.headers.get("Authoriazation").replace("Bearer ","")
    
    print(token)
    
    try:
        decoded = jwt.decpode(token, "비밀소금", algorithms=["HS256"])
    except Exception as e:
        print(e)
        return "문제있음"
        
    return decoded
from fastapi import FastAPI, Depends, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.security import OAuth2PasswordBearer
from redis import StrictRedis
from dingding import *
from unoserver.client import UnoClient
from loguru import logger

app = FastAPI()
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:8010",
    "http://harbor.maituai.com:40090",
    "http://harbor.maituai.com:41080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

redis_host = '192.168.110.14'
redis_port = 6379
redis_db = 15
redis = StrictRedis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

@app.post("/commit/model")
def model_commit(data: dict):
    run_id = data['run_id']
    model_path_key = 'model_path_' + run_id
    model_code_key = 'model_code_' + run_id
    model_confirm_key = 'model_confirm_' + run_id

    redis.set(model_path_key,data['model_path'])
    redis.set(model_code_key,data['model_code'])
    redis.set(model_confirm_key,'1')
    return {'code':200,'msg':'success'}

@app.get("/commit/resource")
def resource_commit(data: dict):
    run_id = data['run_id']
    resource_path_key = 'resource_path_' + run_id
    cover_path_key = 'cover_path_' + run_id
    resource_confirm_key = 'resource_confirm_' + run_id

    redis.set(resource_path_key,data['resource_path'])
    redis.set(cover_path_key,data['cover_path'])
    redis.set(resource_confirm_key,'1')
    return {'code':200,'msg':'success'}


@app.get("/ppt/images")
def time_test():
    uno_client = UnoClient("192.168.110.14", port="2003")
    out_file_bytes = uno_client.convert(inpath="/mnt/c/Users/12770/Desktop/ppt/素雅黑灰图文排版PPT模板.pptx", convert_to='pdf')


if __name__ == "__main__":
    time_test()
    # uvicorn.run("main:app", port=8002)
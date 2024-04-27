import os

import uvicorn
from fastapi import FastAPI, Request, File
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
import data_manager
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()
data_manager = data_manager.data_manager()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/guest/{page_name}", response_class=HTMLResponse)
async def guest(page_name: str):
    # 通过路径参数指定页面名称，读取对应的 HTML 文件内容并返回
    if "." not in page_name:
        page_name += ".html"
    file_path = f"website/guest/{page_name}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        # 如果文件不存在，跳转至欢迎页面
        return RedirectResponse(url="/")


@app.get("/manager/{page_name}", response_class=HTMLResponse)
async def manager(page_name: str):
    # 通过路径参数指定页面名称，读取对应的 HTML 文件内容并返回
    if "." not in page_name:
        page_name += ".html"
    file_path = f"website/manager/{page_name}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        # 如果文件不存在，返回一个简单的错误页面
        return FileResponse("website/Error.html")


@app.get("/api/manager_page")
async def manager_page():
    return [{"Name": "参赛", "Address": "./join"},
            {"Name": "检录", "Address": "./check"},
            {"Name": "记录", "Address": "./record"},
            {"Name": "修改", "Address": "./edit"},
            ]


@app.get("/api/all_class")
async def all_class():
    return data_manager.basics.all_class()


@app.get("/api/all_event")
async def all_event():
    return data_manager.basics.all_event()


@app.get("/api/join/{class_name}/{name}/{event}")
async def join(class_name: str, name: str, event: str):
    return data_manager.join(class_name, name, event)

@app.post("/api/quickly_join")
async def quickly_join(file: bytes = File(...)):
    path="Temp/up.xlsx"
    with open(path, "wb") as f:
        f.write(file)
    # 读取 Excel 文件
    df = pd.read_excel(path)
    # 将 DataFrame 转换为列表
    data_list = df.values
    print(data_list)
    for student in data_list:
        data_manager.join(str(student[0]), str(student[1]), str(student[2]))
    return "File uploaded successfully."

@app.get("/api/find_event/{event}")
async def find_event(event:str):
    return data_manager.basics.find_event(event)

@app.get("/api/check/{class_name}/{name}/{event}")
async def check(class_name:str,name:str,event:str):
    data_manager.check_in(class_name,name,event)

# @app.get("/api/{class_name}/{name}/{event}")
# async def check(class_name:str,name:str,event:str):
#     data_manager.check_in(class_name,name,event)


@app.get("/{page_name}", response_class=HTMLResponse)
async def main(page_name: str):
    # 通过路径参数指定页面名称，读取对应的 HTML 文件内容并返回
    if "." not in page_name:
        page_name += ".html"
    file_path = f"website/{page_name}"
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        # 如果文件不存在，返回一个简单的错误页面
        return FileResponse("website/Error.html")


@app.get("/", response_class=HTMLResponse)
async def welcome():
    return FileResponse("website/index.html")


if __name__ == "__main__":
    uvicorn.run(app="server:app", host="127.0.0.1", port=80, reload=True)
    # 参数	        作用

    # app	        运行的 py 文件:FastAPI 实例对象
    # host	        访问url，默认 127.0.0.1
    # port	        访问端口，默认 8080
    # reload	        热更新，有内容修改自动重启服务器
    # debug	        同 reload
    # reload_dirs	设置需要 reload 的目录，List[str] 类型
    # log_level	    设置日志级别，默认 info

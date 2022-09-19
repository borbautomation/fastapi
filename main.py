import json
from pathlib import Path

import fastapi
import uvicorn

from services import kva2cable_service
from starlette.staticfiles import StaticFiles
from api import cable_api
from views import home

api = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_api_keys()

def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} no encontrado , porfavor revise settings.json")
        raise Exception(f"Archivo {file} no encontrado , porfavor habla con administrador")

    with open("settings.json") as fin:
        settings = json.load(fin)
        
        kva2cable_service.api_key = settings["kva2cable"].get("api_key")
        


            

def configure_routing():
    api.mount('/static',StaticFiles(directory = 'static') , name = 'static')
    api.include_router(home.router)
    api.include_router(cable_api.router)

if __name__ == '__main__':
    configure()
    uvicorn.run(api,port = 8000 , host = "127.0.0.1")
else:
    configure()


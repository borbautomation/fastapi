import fastapi
from fastapi import Depends
from pydantic import BaseModel
from models.parametros import Parametros
from services import kva2cable_service
from typing import Optional

router = fastapi.APIRouter()
api_key : Optional[str] = None



@router.get('/api/kva2cable')
def kva2cable(par:Parametros = Depends()):
	cable = kva2cable_service.get_kva2amp(par.kva,par.voltaje,par.longitud,par.hilos)
	return cable
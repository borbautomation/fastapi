from pydantic import BaseModel
from typing import Optional

class Parametros(BaseModel):
	kva:float = 11
	voltaje:int = 220
	longitud:Optional[float] = 1
	hilos:Optional[int] = 1
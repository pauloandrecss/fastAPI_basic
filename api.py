from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()
    

class Carro(BaseModel):
    id: int | None = Field(default=None, primary_key=True)
    marca : str
    modelo : str
    preco : float

@app.post('/carros')
def adicionar_carro(carro : Carro) -> object:
    return carro

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
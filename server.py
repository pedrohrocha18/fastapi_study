from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
app = FastAPI()

cars = []

class Carro(BaseModel):
    id: Optional[str] = None
    fabricante: str
    modelo: str
    valor: float
    ano_lancamento: int

@app.get('/cars')
def show_all_cars():
  if len(cars) == 0:
      return {"A garagem está vazia!"}
  else:
    return {"Carros Disponíveis" : cars}

@app.post('/cars')
def add_car(car: Carro):
    car.id = str(uuid4())
    cars.append(car)
    
    return {'Carro adicionado!'}

@app.get('/cars/{car_id}')
def show_by_id(car_id: str):
    for car in cars:
        if car_id == car_id:
            return car
    return {'Carro não encontrado.'}

@app.delete('/cars/{car_id}')
def delete_by_id(car_id: str):
    posicao = -1
    
    for index, car in enumerate(cars):
        if car_id == car_id:
            posicao = index
            break
    if posicao != -1:
        cars.pop(posicao)
        return {"Deletado com sucesso!"}
    else:
        return{"Carro não encontrado!"}
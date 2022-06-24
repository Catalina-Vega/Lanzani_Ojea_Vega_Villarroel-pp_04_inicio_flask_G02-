from flask import Flask
import random
from datetime import date
import numpy as np


app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello from Flask!'


@app.route('/dado')
def numeroDado():
  numero=random.randint(1,6)
  return str(numero)

@app.route('/fecha')
def fecha():
  inicio = date(1970, 1, 1)
  final =  date(2100, 12, 31)
  random_date = str(inicio + (final - inicio) * random.random())
  return random_date

@app.route('/color')
def color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return f'<p style="color:rgb({r}, {g}, {b});">Color random</p>'

@app.route('/dado/<n>')
def numero(n):
  if int(n) >= 10 or int(n) <= 0:
    return("Error")
  else:
    lista = []
    for i in range (1,int(n)+1): 
      lista.append(random.randint(1,6)) 
    return str(lista) 

@app.route('/fecha/<y>')
def fechaAño(y):
  año=int(y)
  inicio = date(año, 1, 1)
  final =  date(año, 12, 31)
  random_date = str(inicio + (final - inicio) * random.random())
  return random_date
  
@app.route('/fecha/<y>/<m>')
def fechaAñoyMes(y,m):
  año=int(y)
  mes=int(m)
  inicio = date(año, mes, 1)
  final =  date(año, mes, 31)
  random_date = str(inicio + (final - inicio) * random.random())
  return random_date
  
app.run(host='0.0.0.0', port=81)

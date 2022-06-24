from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/listado')
def topDiezPerCapita():
  conn = sqlite3.connect("co_emissions.db")
  q = f"""SELECT Country, Value FROM emissions WHERE Series = 'pcap' ORDER BY Value desc"""
  resu = conn.execute(q)
  topDiezPerCapita = []
  for fila in resu:
    topDiezPerCapita.append(fila)
  conn.close()
  return render_template("listado.html", topDiezPerCapita = topDiezPerCapita)

@app.route('/listado/top')
def topDiezTotal():
  conn = sqlite3.connect("co_emissions.db")
  q = f"""SELECT Country, Value FROM emissions WHERE Series = 'total' ORDER BY Value desc"""
  resu = conn.execute(q)
  topDiezTotal = []
  for fila in resu:
    topDiezTotal.append(fila)
  conn.close()
  return render_template("listadoTop.html", topDiezTotal = topDiezTotal)

@app.route('/listado/<pais>')
def totalYPerCapitaPorPais(pais):
  conn = sqlite3.connect("co_emissions.db")
  q = f"""SELECT Country, Series, Value FROM emissions WHERE Country = '{pais}' ORDER BY Value desc"""
  resu = conn.execute(q)
  totalYPerCapitaPorPais = []
  for fila in resu:
    totalYPerCapitaPorPais.append(fila)
  conn.close()
  return render_template("listadoPais.html", totalYPerCapitaPorPais = totalYPerCapitaPorPais)

@app.route('/ayuda')
def acercaDe():
  return render_template("acercaDe.html")

app.run(host='0.0.0.0', port=81)
#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from flask import request
import urllib2
import json
import io
import app_twitter 

"""Programa principal encargado de usar las extensiones FLASk junto
con la API twitter"""
lista_lugares = []

def ObtenerUbicacion(hastag):

    twitter_api = app_twitter.oauth_login()
    datos = twitter_api.search.tweets(q = hastag,count = 100)
    

   
    lugaractual = []
    for lugar in datos["statuses"]:
        if lugar["coordinates"] != None:
            lugaractual = lugar["coordinates"]
            coordenadas = [lugaractual.values()[1][1], lugaractual.values()[1][0]]
            lista_lugares.append(coordenadas)


app = Flask(__name__)
GoogleMaps(app)

@app.route("/buscar", methods=['POST'])
def buscar():
    termino = request.form['text'] 
    coordenadas = ObtenerUbicacion(termino)

    mymap = Map(
        identifier="view-side",
        lat=40.3450396,
        lng=-3.6517684,
        markers= lista_lugares,
	zoom = 3,
        style="height:800px;width:800px;margin:0;"
    ) 
    return render_template('Maps.html', mymap=mymap)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



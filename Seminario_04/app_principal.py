#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import io
import app_twitter
import urllib2
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map


"""Programa principal encargado de usar las extensiones FLASk junto
con la API twitter"""


twitter_api = app_twitter.oauth_login()
hastags = raw_input("Hastags con tuits a buscar: ")
hastags_trends = twitter_api.search.tweets(q = hastags)# result_type = 'index')
#guardamos el fichero json

app_twitter.save_json('Maps_hastags', hastags_trends)

recover_data = app_twitter.load_json('Maps_hastags')


#obtenemos los datos del JSON:
datos = json.loads(open('Maps_hastags.json').read())

lista_lugares = []
cont = False 

for lugar in datos["statuses"]:
	if lugar["coordinates"] != None:
		lugar_actual =  lugar["coordinates"]
		x = lugar_actual.values()[1][0]
		y = lugar_actual.values()[1][1]
		lista_lugares.append([x,y])
		cont = True

if cont == False:
	print "No se han encontrado lugares marcados con este hastags"
	print "Se tu el primero en poner tu ubicacion con el hastags, ", hastags




app = Flask(__name__)
GoogleMaps(app)

@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=40.3450396,
        lng=-3.6517684,
        markers= lista_lugares,
        style="height:800px;width:800px;margin:0;"
    ) 
    return render_template('Maps.html', mymap=mymap)


if __name__ == "__main__":
    app.run(debug=False)



#print json.dumps(ciudades, indent = 1)

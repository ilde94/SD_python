#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import io
#import app_principal

#obtenemos los datos del JSON:
datos = json.loads(open('Maps_hastags.json').read())
lista_ciudades = []

for ciudad in datos["query"]:
	if ciudad["full_name"] != None:
		ciudad_actual = ciudad["full_name"]
		lista_ciudades.append(ciudad_actual)

print lista

#print json.dumps(ciudades, indent = 1)


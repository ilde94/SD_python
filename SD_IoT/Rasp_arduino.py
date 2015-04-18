#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importamos la libreira de PySerial para comunicarnos con arduino
import serial
#librerias para la comunicacion de peticiones http
import httplib, urllib

import time

#Abrimos el puerto del arduino a 9600 baudios, correspondientes a la misma 
#frecuencia para arduino
PuertoSerie = serial.Serial('/dev/ttyACM0', 9600)

#hacemos un reset, asi los datos empezarán desde el principio
PuertoSerie.setDTR(False)
time.sleep(1)
#limpiamos el buffer de arduino y volvemos empezar la captura de datos
PuertoSerie.flushInput()
PuertoSerie.setDTR(True)

# Creamos un buble sin fin
while True:
  # leemos hasta que encontramos el final de linea
  # Mostramos el valor leido y eliminamos el salto de linea del final
    campo1 = PuertoSerie.readline()
    campo1 = campo1.rstrip('\n')
    campo1 = campo1.rstrip('\r')
    print "mensaje 1 enviado: " , campo1

    campo2 = PuertoSerie.readline()
    campo2 = campo2.rstrip('\n')
    campo2 = campo2.rstrip('\r')
    print "Mensaje 2 enviado: ", campo2

    campo3 = PuertoSerie.readline()
    campo3 = campo3.rstrip('\n')
    campo3 = campo3.rstrip('\r')
    print "Mensaje 3 enviado: ", campo3
    #se dispone a realizar una peticion a thigspeak del tipo PUT para actualizar el va$
    conexion = httplib.HTTPConnection("api.thingspeak.com:80")

    #paso de parametros para el envio del formulario POST
    params = urllib.urlencode({'key': "ZCEQVYGHN3J1CDHM",'field1': campo1, 'field2': campo2, 'field3': campo3})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #se hace la peticion
    try:
      conexion.request("POST", "/update", params, headers)
      #como respuesta solo se espera que se haga una actualizacion del canal
      respuesta = conexion.getresponse()
      data = respuesta.read()
      #Es de ayuda mostrar el estado de la conexion:
      print respuesta.status, respuesta.reason
      #time.sleep(3)
    except:
      print "conexion fallida, lo siento :("
conexion.close()

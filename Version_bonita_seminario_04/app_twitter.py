#!/usr/bin/python
# -*- coding: utf-8 -*-

#Modulo que contiene la inicializacion de las claves 
#y autentificacion para la app de twitter

import twitter
import json
import io

"""Rellenamos los parametros de las claves de twitter para usar la API"""
def oauth_login():

    CONSUMER_KEY = 'U5TdZAiwapwACG7TkCVV5MAhD'
    CONSUMER_SECRET = 'rr3nNSE0ICIKeShLzswWTmSPAYbnLoVEoOwZ81r0ZXdAFLjhkA'
    OAUTH_TOKEN = '800577547-nlbgBw4i9Vjd1repQzvLqN3FsH6BhpdozX9MoIEQ'
    OAUTH_TOKEN_SECRET = '8rHFpKgEFrODU6BB6NclupUX5ue4C9As1oYfyhglsqxHJ'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(domain='api.twitter.com', 
                              api_version='1.1',
                              auth=auth
                             )
    #twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Función para grabar la información en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Función para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()







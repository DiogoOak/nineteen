#!/usr/bin/python
# -*- coding: latin-1 -*-

''' 
Modulo API
==========

Este modulo vai ligar-se à base de dados e fazer a interface com a aplicacao.

created by Marco Simões
'''

import psycopg2


conn = None

# dados da connecção
host = 'localhost'
database = 'dropmusic'
user = 'postgres'
password = 'postgres'


def connect():
    # estabelece a conneccao com a bd
    global conn

    if conn == None:
        try:
            conn = psycopg2.connect(host=host,database=database, user=user, password=password)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
 


def login(username, password):
    # verifica se existe um user com este username e password

    sql = '''SELECT username, password, nome, tipo 
             FROM utilizadores
             WHERE username = %s and password = %s'''

    
    if conn == None:
        connect()

    try:
        cur = conn.cursor()
        cur.execute(sql, (username, password, ))

        # nenhum user com esse username e password
        if cur.rowcount < 1:
            cur.close()
            return None
        
        # ir buscar a linha resultado do SQL
        data = cur.fetchone()
        user = {'nome': data[2], 'tipo': data[3]}

        cur.close()
        return user

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def terminate():
    if conn is not None:
        conn.close()

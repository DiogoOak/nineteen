#!/usr/bin/python
# -*- coding: latin-1 -*-


''' 
Modulo da Applicacao
=============

Este modulo faz de interface com o utilizador, apresenta os menus, pede dados, 
executa os comandos e apresenta os resultados.

create by Marco Simões
'''


import menus, api


def validate_option(op, max_op, min_op = 0):
    # valida se a op é um valor inteiro, e se se encontra entre min e max, inclusive
    
    try:
        op = int(op)
        if op >= min_op and op <= max_op:
            return op
    except:
        pass

    print('Valor incorreto, introduza um numero entre %d e %d' % (min_op, max_op))
    return -1



def apresentar_menu(menu_txt, max_op, min_op = 0):
    # mostra o menu até a opção introduzida ser válida

    print(menu_txt)

    op = -1
    while op < 0:
        
        op = validate_option( raw_input("Introduza a sua opcao: "), max_op )

    return op




def menu_user():
    # menu do utilizador normal

    menu_txt = menus.user

    while True:
        op = apresentar_menu(menu_txt, 2)

        if op == 1:
            print('TODO: implementar')
            raw_input('Pressione enter para continuar...')
        elif op == 2:
            print('TODO: implementar')
            raw_input('Pressione enter para continuar...')
        else:
            break


def menu_editor():
    # menu do editor

    menu_txt = menus.editor

    while True:
        op = apresentar_menu(menu_txt, 2)

        if op == 1:
            print('TODO: implementar')
            raw_input('Pressione enter para continuar...')
        elif op == 2:
            print('TODO: implementar')
            raw_input('Pressione enter para continuar...')
        else:
            break


def menu_login():
    # menu de login

    # pedir username e password ao utilizador
    username = raw_input('username: ')
    password = raw_input('password: ')

    # chamar a api para ir validar o username e password à base de dados
    user = api.login(username, password)
    if not user == None:
        print('login efectuado com sucesso!')
        raw_input('Pressione enter para continuar...')

        # apresentamos um menu diferente em funcao do tipo de utilizador
        if user['tipo'] == 'normal':
            menu_user()
        elif user['tipo'] == 'editor':
            menu_editor()
        
    else:
        print('username ou password invalidos, tente novamente')


def menu_registo():
    # menu de registo

    print('TODO: implementar')
    raw_input('Pressione enter para continuar...')


def menu_inicial():
    # menu inicial

    menu_txt = menus.inicial

    while True:
        op = apresentar_menu(menu_txt, 2)

        if op == 1:
            menu_login()
        elif op == 2:
            menu_registo()
        else:
            print('Obrigado por usar o DropMusic. Adeus!')
            api.terminate()
            break



if __name__ == '__main__':
    menu_inicial()



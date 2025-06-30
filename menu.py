from utel import *

def menu_principal():
    limpar_tela()
    print('=' * 40)
    print('       SISTEMA DE EVENTOS')
    print('=' * 40)

    print('[1] Cadastro')
    print('[2] Consultar Eventos')
    print('[3] Consultar participantes')
    print('[4] Estatísticas')
    print('[0] Sair')

    print('-' * 40)

    return ler_opcao(4)

def menu_cadastro():
    limpar_tela()
    print('=' * 40)
    print('           CADASTRO')
    print('=' * 40)

    print('[1] Cadastrar Evento')
    print('[2] Cadastrar Participante')
    print('[0] Voltar')
    print('-' * 40)

    return ler_opcao(2)

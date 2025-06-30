from utel import *


def cadastrar_evento(lista_eventos):
    limpar_tela()
    print('=' * 40)
    print('           CADASTRAR EVENTO')
    print('=' * 40)
    
    
    nome_evento = input('Nome do evento: ')
    
    for evento in lista_eventos:
        if evento['nome'].lower() == nome_evento.lower():
            print('Evento com nome já existente.')
            print('-' * 40)
            input('Precione Enter para continuar.')
            return
    
    data = input('Data do evento (dd/mm/aaaa): ')

    
    tema = input('Tema do evento: ')

    
    evento = {'nome': nome_evento, 'data': data, 'tema': tema, 'participantes': []}
    
    lista_eventos.append(evento)
    print('Evento cadastrado!')
    
    print('-' * 40)
    input('Precione Enter para continuar.')
    return

def consultar_eventos(lista_eventos): # mostra eventos cadastrados, disponiveis para seleção
    limpar_tela()
    print('=' * 40)
    print('           CONSULTAR EVENTOS')
    print('=' * 40)

    if not lista_eventos:
        print('Nenhum evento cadastrado.')
        
        print('-' * 40)
        input('Precione Enter para continuar.')
        return
    else:
        for i, evento in enumerate(lista_eventos, 1):
            print(f'[{i}] {evento['nome']}')
    
    print('[0] Voltar')
    print('-' * 40)
    
    return ler_opcao(len(lista_eventos))

def opcoes_eventos(evento): # opções disponiveis referente ao evento selecionado
    limpar_tela()
    print('=' * 40)
    print(f'           OPÇÕES DO EVENTO')
    print('=' * 40)
    
    print(evento['nome'])
    
    print('[1] Ver detalhes')
    print('[2] Adicionar participante')
    print('[0] Voltar')
    
    print('-' * 40)
    
    return ler_opcao(2)


def detalhes_evento(evento): 
    limpar_tela()
    print('=' * 40)
    print('           DETALHES DO EVENTOS')
    print('=' * 40)

    print(f'NOME: {evento['nome']}')
    print(f'DATA: {evento['data']}')
    print(f'TEMA: {evento['tema']}')
    input(f'Precione Enter para voltar.')
    
    return
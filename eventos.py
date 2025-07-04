from utel import *


def cadastrar_evento(lista_eventos):
    limpar_tela()
    print('=' * 40)
    print('           CADASTRAR EVENTO')
    print('=' * 40)
    
    
    nome_evento = input('Nome do evento: ').strip()
    
    #validação de nome do evento 
    for evento in lista_eventos:
        if evento['nome'].lower() == nome_evento.lower():
            print('Evento com nome já existente.')
            print('-' * 40)
            input('Precione Enter para continuar.')
            return
    
    #validação de data do evento
    data = obter_data_valida()
    
    tema = input('Tema do evento: ')

    
    evento = {'nome': nome_evento, 'data': data.date(), 'tema': tema, 'participantes': []}
    
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
        return 0
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
    print('[3] Excluir evento')
    print('[0] Voltar')
    
    print('-' * 40)
    
    return ler_opcao(3)


def detalhes_evento(evento): 
    limpar_tela()
    print('=' * 40)
    print('           DETALHES DO EVENTOS')
    print('=' * 40)

    print(f'NOME: {evento["nome"]}')
    print(f'DATA: {evento["data"]}')
    print(f'TEMA: {evento["tema"]}')
    
    if evento['participantes']:
        print('PARTICIPANTES: ')
        for p in evento['participantes']:
            print(f'- {p["nome"]} (CPF: {p["cpf"]})')
    else:
        print('Nenhum participante cadastrado.')
    
    input(f'Precione Enter para voltar.')
    
    return

def adicionar_part_evento(evento, lista_participantes):
    limpar_tela()
    print('=' * 40)
    print('       ADICIONAR PARTICIPANTE AO EVENTO')
    print('=' * 40)
    
    if not lista_participantes:
        print('Nenhum participante cadastrado ao sistema.')
        input('Precione Enter para continuar.')
        return
    
    print('Participantes disponíveis para vinculação: ')
    for i, p in enumerate(lista_participantes, 1):
        print(f'[{i}] {p["nome"]} - CPF: {p["cpf"]}')
    
    print('[0] Cancelar')
    print('-' * 40)
    
    op = ler_opcao(len(lista_participantes))
    if op == 0:
        print('Inclusão de participante cancelada.')
        input('Precione Enter para continuar.')
        return
    
    participante = lista_participantes[op - 1]
    
    if participante['cpf'] in [p['cpf'] for p in evento['participantes']]:  
        print('Participante já vinculado ao evento.')
    else:
        evento['participantes'].append(participante)
        print('Participante vinculado com sucesso!')
        
    input('Precione Enter para continuar.')
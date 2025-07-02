from utel import *


def cadastrar_part(lista_participantes, lista_eventos):
    limpar_tela()
    print('=' * 40)
    print('           CADASTRAR PARTICIPANTE')
    print('=' * 40)
    
    nome = input('Digite nome do participante: ').strip()

    cpf = input('Digite CPF do participante: ').strip()
    for p in lista_participantes:
        if p['cpf'] == cpf:
            print('CPF já cadastrado.')
            input('Precione Enter para continuar.')
            return

    email = input('Digite email do participante: ').strip()
    
    temas = list({evento['tema'] for evento in lista_eventos})
    if not temas:
        print('Não há temas cadastrados. Cadastre eventos primeiro.')
        input('Precione Enter para continuar.')
        return
    
    print('Escolha preferência temática: ')
    for i, tema in enumerate(temas, 1):
        print(f'[{i}] {tema}')
    print('[0] Cancelar')
    print('-' * 40)
    
    op = ler_opcao(len(temas))
    if op == 0:
        print('Cadastro cancelado.')
        input('Precione Enter para continuar.')
        return
    
    preferencia = temas[op - 1]
    
    participante = {'nome': nome, 'cpf': cpf, 'email': email, 'preferencia': preferencia}
    
    lista_participantes.append(participante)
    
    
    print('Participante cadastrado com sucesso!')
    input('Precione Enter para continuar.')
    
    return
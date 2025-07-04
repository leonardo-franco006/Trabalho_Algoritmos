from utel import *


def cadastrar_part(lista_participantes, lista_eventos): #cadastra participantes ao sistema 
    limpar_tela()
    print('=' * 40)
    print('           CADASTRAR PARTICIPANTE')
    print('=' * 40)
    
    nome = input('Digite nome do participante: ').strip()

    cpf = input('Digite CPF do participante: ').strip() #verifica se cpf já está cadastrado
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
    
    print('Escolha preferência temática: ') #apresenta temas disponíveis para seleção 
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

def alterar_participante(participante, lista_eventos): #altera dados do participante
    limpar_tela()
    print('=' * 40)
    print('           ALTERAR PARTICIPANTE')
    print('=' * 40)
    
    nome = input(f'Digite novo nome (atual: {participante["nome"]}): ').strip()
    if nome:
        participante['nome'] = nome
    
    email = input(f'Digite novo email (atual: {participante["email"]}): ').strip()
    if email:
        participante['email'] = email

    temas = list({evento['tema'] for evento in lista_eventos})
    print(f'Preferência atual: {participante["preferencia"]}')
    if temas:
        print('Temas disponíveis:')
        for i, tema in enumerate(temas, 1):
            print(f'[{i}] {tema}')
        print('[0] Manter preferência atual')

        op = ler_opcao(len(temas))
        if op != 0:
            participante['preferencia'] = temas[op - 1]
            print('Preferência atualizada com sucesso!')
        else:
            print('Preferência mantida.')
    else:
        print('Nenhum tema disponível para alterar a preferência.')
    
    print('-' * 40)
    input('Pressione Enter para continuar.')



def consultar_participantes(lista_participantes, lista_eventos): #consulta participantes cadastrados
    limpar_tela()
    print('=' * 40)
    print('       BUSCAR PARTICIPANTE CADASTRADO')
    print('=' * 40)
    
    if not lista_participantes:
        print('Nenhum participante cadastrado.')
        input('Precione Enter para continuar.')
        return
    
    cpf_busca = input('Digite o CPF do participante: ').strip()
    
    participante = None
    for p in lista_participantes:
        if p['cpf'] == cpf_busca:
            participante = p
            break
    
    if participante:
        print(f'Nome: {participante["nome"]}')
        print(f'CPF: {participante["cpf"]}')
        print(f'Email: {participante["email"]}')
        print(f'Preferência temática: {participante["preferencia"]}')
        print('-' * 40)
        
        print('[1] Alterar dados')
        print('[2] Excluir participante')
        print('[0] Voltar')
        
        op = ler_opcao(2)
        if op == 1:
            alterar_participante(participante, lista_eventos) 
        elif op == 2:
            confirmar = input('Tem certeza que deseja excluir este participante? (s/n): ').strip().lower()
            if confirmar == 's':
                lista_participantes.remove(participante)
                print('Participante excluído com sucesso!')
                input('Precione Enter para continuar.')
            else:
                print('Exclusão cancelada.')
                return
    else:
        print('Participante não encontrado.')
        print('Precione Enter para continuar.')
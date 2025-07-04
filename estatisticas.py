from util import *

def gerar_estatisticas(eventos, participantes, **kwargs):
    limpar_tela()
    print('=' * 40)
    print('           ESTATÍSTICAS')
    print('=' * 40)
    
    if not eventos or not participantes:
        print('Não há dados suficientes para gerar estatísticas.')
        print('-' * 40)
        input('Pressione Enter para continuar.')
        return
    
    # participantes mais ativos
    if kwargs.get('participantes_ativos', True):
        contador = {}
        
        cpf_para_nome = {p['cpf']: p['nome'] for p in participantes}  # cria um dicionário para mapear CPF a nome
        
        for evento in eventos:
            for p in evento.get('participantes', []):
                cpf = p['cpf']
                contador[cpf] = contador.get(cpf, 0) + 1
        print('Participantes mais ativos: ')
        for cpf, qtd in sorted(contador.items(), key=lambda x: x[1], reverse=True)[:5]: # cria uma lista dos 5 participantes mais ativos, tuplas com (tema, quantidade). ordena do maior para o menor e pega os 5 primeiros
            nome = cpf_para_nome[cpf]
            print(f'- {nome} (CPF: {cpf}) - Eventos Vinculados: {qtd}')
        print('-' * 40)
    
    if kwargs.get('temas_frequentes', True):
        temas = {}  # Dicionário para contar eventos por tema
        
        for evento in eventos:
            tema = evento['tema']
            temas[tema] = temas.get(tema, 0) + 1
        
        print('Temas mais frequentes:')
        for tema, qtd in sorted(temas.items(), key=lambda x: x[1], reverse=True): # cria uma lista de temas e quantidade de eventos vinculados a cada tema. ordena do maior para o menor
            print(f'- {tema}: {qtd} evento(s)')
        print('-' * 40)
    
    # eventos com menos de dois participantes
    if kwargs.get('eventos_com_poucos', True):
        print('Eventos com menos de 2 participantes:')
        
        for evento in eventos:
            num_participantes = len(evento.get('participantes', []))
            if num_participantes < 2:
                data_formatada = evento["data"]
                print(f'- {evento["nome"]} ({data_formatada})')
        print('-' * 40)
    
    # Estatística 4: Taxa média de participação por tema
    if kwargs.get('media_por_tema', True):
        tema_participacoes = {}  # Soma de participantes por tema
        tema_eventos = {}        # Contagem de eventos por tema
        
        for evento in eventos:
            tema = evento['tema']
            qtd = len(evento.get('participantes', [])) # quantidade de participantes no evento
            tema_participacoes[tema] = tema_participacoes.get(tema, 0) + qtd
            tema_eventos[tema] = tema_eventos.get(tema, 0) + 1
        
        print('Taxa média de participação por tema:')
        for tema in tema_eventos:
            media = tema_participacoes[tema] / tema_eventos[tema]
            print(f'- {tema}: {media:.2f} participante(s) por evento') # mostra a média de participantes por evento de cada tema, .2f formata o numero para duas casas deciamais
        print('-' * 40)
    
    input('Pressione Enter para continuar.')
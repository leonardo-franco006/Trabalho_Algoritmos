from menu import *
from eventos import *
from participantes import *

eventos = []
participantes = []


while True:
    op = menu_principal()
    
    if op == 0:
        print('Encerrando...')
        break
    
    elif op == 1: # cadastrar participante ou evento 
        op_cad = menu_cadastro()
        if op_cad == 1: # cadastrar evento ao programa
            cadastrar_evento(eventos)
        elif op_cad == 2: # cadastrar participante ao programa
            cadastrar_part(participantes, eventos)

    
    elif op == 2: # acessar eventos 
        op_evento = consultar_eventos(eventos)
        if op_evento != 0:
            evento_escolhido = eventos[op_evento - 1]
            
            while True:
                op_acao = opcoes_eventos(evento_escolhido) # opções a respeito do evento selecionado
                if op_acao == 1:
                    detalhes_evento(evento_escolhido) # detalhes do evento selecionado
                elif op_acao == 2:
                    adicionar_part_evento(evento_escolhido, participantes) # adicionar participante ao evento selecionado
                elif op_acao == 3:
                    confirmar = input('Tem certeza que deseja excluir este evento? (s/n): ').strip().lower()
                    if confirmar == 's':
                        eventos.remove(evento_escolhido)
                        print('Evento excluído com sucesso!')
                        input('Pressione Enter para continuar.')
                        break
                    else:
                        print('Exclusão cancelada.')
                        input('Pressione Enter para continuar.') 
                elif op_acao == 0: # voltar para o menu principal
                    break  
    
    elif op == 3: # acessar participantes
        consultar_participantes(participantes, eventos) # consultar participantes cadastrados

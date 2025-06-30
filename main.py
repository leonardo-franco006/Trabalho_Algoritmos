from menu import *
from eventos import *
from participantes import *

eventos = []

while True:
    op = menu_principal()
    
    if op == 0:
        print('Encerrando...')
        break
    
    elif op == 1: # cadastrar participante ou evento 
        op_cad = menu_cadastro()
        if op_cad == 1: #cadastrar evento ao programa
            cadastrar_evento(eventos)
        elif op_cad == 2: # cadastrar participante ao programa
            cadastrar_part()

    
    elif op == 2:
        op_evento = consultar_eventos(eventos)
        if op_evento != 0:
            evento_escolhido = eventos[op_evento - 1]
            op_acao = opcoes_eventos(evento_escolhido)
            if op_acao == 1:
                detalhes_evento(evento_escolhido)
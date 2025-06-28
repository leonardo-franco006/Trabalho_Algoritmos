from menu import *

while True:

    op = menu_principal()
    
    if op == 0:
        print('Encerrando...')
        break
    
    elif op == 1:
        op_cad = menu_cadastro()
        if op_cad == 1:
            pass
        elif op_cad == 2:
            pass
    
    elif op == 2:
        op_ev = menu_eventos()
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_opcao(limp_sup):
    while True:
        op = input('Selecione uma opção: ')

        if op.isdigit():
            op = int(op)
            if 0 <= op <= limp_sup:
                return op
            else:
                print(f'Digite uma opção entre 0 e {limp_sup}')
        else:
            print('Opção inválida! Digite somente números.')
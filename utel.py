import os
from datetime import datetime

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

def obter_data_valida():
    while True:
        data_str = input('Data do evento (dd/mm/aaaa): ')
        if len(data_str) == 10 and data_str[2] == '/' and data_str[5] == '/':
            dia, mes, ano = data_str.split('/')
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                try:
                    data_evento = datetime(int(ano), int(mes), int(dia))
                    if data_evento < datetime.now():
                        print('Data inválida, o evento não pode estar no passado.')
                    else:
                        return data_evento
                except ValueError:
                    print('Data inválida, essa data não existe no calendário.')
            else:
                print('Data inválida, use apenas números no formato dd/mm/aaaa.')
        else:
            print('Formato inválido, use apenas o formato dd/mm/aaaa.')
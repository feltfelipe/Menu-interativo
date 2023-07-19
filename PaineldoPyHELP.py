from time import sleep
cores = ['\033[m', #lista de cores que serão usadas para 'dinamizar' o programa (não ficar morto com tudo cinza e com aparente falta de interação, só letras e mais letras)
         '\033[0;30;41m',
         '\033[0;30;42m',
         '\033[0;30;43m',
         '\033[0;30;44m',
         '\033[0;30;45m',
         '\033[7;30m'
         ]

def ajuda(com):
    título(f'Acessando o manual do comando {com}')
    print(cores[5])
    help(com) #função help que será a base do programa
    print(cores[0])
    sleep(2)


def título(msg, cor=0): #função para padronizar os títulos e organizar o programa (com aquele charminho, rs)
      tam = len(msg) + 4
      print(cores[cor])
      print('~' * tam)
      print(f'  {msg}')
      print('~' * tam)
      print(cores[0])
      sleep(1)


comando = ''
while True: #laço infinito para pergunta qual função do python deseja consultar. (As respostas são, obviamente, em inglês)
      título('SISTEMA DE AJUDA PyHELP', 2)
      comando = str(input('Função ou Biblioteca (FIM encerra) > '))
      if comando.upper() == 'FIM':
            break
      else:
            ajuda(comando)
título('ATÉ LOGO', 1)

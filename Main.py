#Projeto o Zero Cancela2

#tela de inicio
print('------------------------------------------------------------------')
print('\t\t<<< Jogo "O Zero Cancela" >>>')
print('------------------------------------------------------------------')
print('Escolha as opções a Seguir:\n'
'\033[32m''[1] Quero Jogar\n''\033[0m'
'\033[33m''[2] Ler as regras.\n''\033[0m'
'\033[31m''[3] Sair do Programa.\n''\033[0m')

num_tela = int ( input ('Opção Desejada: '))

while num_tela != 3:
    #Tela de Erro
    if num_tela != 1 and num_tela != 2:
        num_tela =int ( input (            
'''----------------------------------------------------------------
    Desculpe, o Número Inserido é Inválido.
    Lembre-se:
    \033[32m[1] Para Jogar.\033[0m
    \033[33m[2] Ler as Regras.\033[0m
    \033[31m[3] Finalizar o Jogo.\033[0m

    Opção Desejada: '''))
    #Tela para iniciar o Jogo
    
    if num_tela == 1:
        print('-----------------------------------------------------------------')
        print('\t\t\tJogo Iniciado... ')
        print('-----------------------------------------------------------------')
        num = int ( input ('Informe o Número: '))
    #Tela para ler as regras
    
    elif num_tela == 2:
        print('------------------------------------------------------------------')
        print('\t\t\tRegras')
        print('------------------------------------------------------------------')
        print(
'''O Jogo consiste em somar os Números Digitados pelo usuário. Ca-
so inserido um número indesejado e queira mudar, deverá se atentar
as seguintes Regras:

1. Ao digitar o número 0, O último algarismo inserido séra descon-
    siderado.
2. O usuário tem o Limite Máximo de Três 0 (Zeros) consecutivos, 
    podendo invalidar APENAS os últimos três numeros digitados.
3. Para Finalizar o Jogo Digite um Número Negativo.\n''')
        
        print(
            '\tEscolha as Opções a Seguir: \n'
            '\t\033[32m''[1] Vamos Jogar !:''\033[0m''\n'
            '\t\033[91m''[3] Sair do Programa:''\033[0m')
        
        num_tela = int (input('\tOpção Desejada: '))

    #Inicio do Jogo 
    #O jogo somente irá começar quando num_tela for igual a 1 e
    #o número inserido for maior ou igual a 0

    while num_tela  == 1 and num >= 0: 

        #Variáveis do Jogo  
        #cont = contador
        #num = numeros        

        cont_num_considerados = 0
        cont_num_desconsiderados = 0 
        soma_total = 0

        #Variáveis necessárias para armazenar os 3 últimos números
        ultimo_numero = 0 
        penultimo_numero = 0
        antpenultimo_numero = 0

        contador_zero = 0

        #Condição para manter o Jogo em Loop
        #Após a condição ser quebrada o jogo irá parar e voltar para o loop anterior

        while num >= 0:

            if num > 0:
                soma_total += num   
                cont_num_considerados += 1
                contador_zero = 0 

                #Armazena o último numéro inserido na váriavel{ultimo_numero}
                #Dados os números, serão subsituidos
                #ultimo_numero -> penultimo_numero -> antepenultimo_numero
                #      1       ->       0          ->         0
                #      2       ->       1          ->         0
                #      3       ->       2          ->         1

                antpenultimo_numero = penultimo_numero 
                penultimo_numero = ultimo_numero 
                ultimo_numero=  num 
                
                
            # número igual a 0 
            else:  
                contador_zero +=1
                
                if ultimo_numero > 0 :
                    cont_num_considerados -= 1 
                    cont_num_desconsiderados += 1 
                
                elif ultimo_numero == 0:
                    print('Não Existe Mais Números Para Desconsiderar.')

                soma_total -= ultimo_numero #Remove o último numero digitado da soma total

                ultimo_numero = penultimo_numero #Subsitui o ultimo número pelo penultimo número, pois foi desconsiderada
                penultimo_numero = antpenultimo_numero #Substitui o antepenúltimo como o penultumo número] 
                antpenultimo_numero = 0 #Subistitui o último numero por 0

                # Digitando úm numero > 0, a varíavel{contador_zero} é zerada
                # ao inserir zeros seguidos o contador nao irá zerar, assim, 
                # cria a condição para dar o aviso de limites de zero

                if contador_zero > 3:
                    print('Limite de 3 zeros consecutivos!!')
                
            
            num = int ( input ('Informe o Número: ')) 

        #Tela Após o Encerramento do Jogo
        print('----------------------------------------------------------------')
        print('\tFim do Jogo!! Muito Obrigado por Jogar.')
        print('----------------------------------------------------------------')
        print('\t\tRESULTADOS')
        print('----------------------------------------------------------------')
        print(f'A Soma Total é: {soma_total}')
        print(f'Numeros Considerados: {cont_num_considerados}')
        print(f'Numeros Desconsiderados: {cont_num_desconsiderados}')
        print('----------------------------------------------------------------')
        print('\t\t\t Opções:')
        print('----------------------------------------------------------------')
        print(
        '\033[32m''   [1] Reiniciar.\n''\033[0m'
        '\033[33m''   [2] Ler as Regras Novamentes.\n''\033[0m'
        '\033[31m''   [3] Finalizar o Jogo.''\033[0m' )
        
        num_tela = int ( input ('Opção Desejada: '))

print('----------------------------------------------------------------')

print('\t\t\t FIM DO PROGRAMA')
print('----------------------------------------------------------------')
from verify_passwords import verificar_senha
from requisits import requisitos
from painel_functions import criar_senha, editar_senha, validar_senha, listar_senhas, sair_programa, deletar_senha

print('--- Painel Verificador de Senhas ---')

while True:

    print('\n1 - Criar uma Senha')
    print('2 - Editar sua Senha')
    print('3 - Deletar Senha')
    print('4 - Validar Senha')
    print('5 - Listar Senha')
    print('6 - Sair do Programa')

    opcao = input('\nDigite uma opção: ')
    

    if opcao == '1':
        criar_senha()

    elif opcao == '2':
        editar_senha()

    elif opcao == '3': 
        deletar_senha() 

    elif opcao == '4': 
        validar_senha()     

    elif opcao == '5':
        listar_senhas()

    elif opcao == '6':
        sair_programa()
        break
    else:
        print('Opção Inválida!')

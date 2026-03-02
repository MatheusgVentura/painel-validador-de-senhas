from requisits import requisitos
from verify_passwords import verificar_senha

lista_senhas = []

def criar_senha():
    requisitos()
    nova_senha = input('\nDigite sua senha por favor: ')

    if nova_senha.strip() == '':
        print('Senha inválida, não pode ser vazia!')
    else:
        lista_senhas.append(nova_senha)
        print('Senha criada com sucesso!')

def editar_senha():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
    else:
        print('\nSenhas salvas:')
        for i, s in enumerate(lista_senhas, start=1):
            print(f'{i} - {"*" * len(s)}')

        try:
            escolha_editar = int(input('\nDigite o número da senha que deseja editar: '))

            if escolha_editar < 1 or escolha_editar > len(lista_senhas):
                print('Opção inválida!')
            else:
                alterar_senha = input('Digite a nova senha: ')

                if alterar_senha.strip() == '':
                    print('Senha inválida, não pode ser vazia!')
                else:
                    lista_senhas[escolha_editar - 1] = alterar_senha
                    print('Senha alterada com sucesso!')
        except ValueError:
            print('Opção inválida!')

def deletar_senha():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
    else:
        print('\nSenhas salvas:')
        for i, s in enumerate(lista_senhas, start=1):
            print(f'{i} - {"*" * len(s)}')

        try:
            escolha_deletar = int(input('\nDigite o número da senha que deseja deletar: '))

            if escolha_deletar < 1 or escolha_deletar > len(lista_senhas):
                print('Opção inválida!')
            else:
                senha_removida = lista_senhas.pop(escolha_deletar - 1)
                print(f'Senha "{"*" * len(senha_removida)}" deletada com sucesso!')
        except ValueError:
            print('Opção inválida!')

def qualificar_senha(senha):
    resultado = verificar_senha(senha)

    if isinstance(resultado, list):
        return 'Senha fraca'

    pontos = 0
    caracteres_especiais = '@#$%¨&*!?_-+='

    if len(senha) >= 8:
        pontos += 1

    if len(senha) >= 12:
        pontos += 1

    if any(c.islower() for c in senha):
        pontos += 1

    if any(c.isupper() for c in senha):
        pontos += 1

    if any(c.isdigit() for c in senha):
        pontos += 1

    if any(c in caracteres_especiais for c in senha):
        pontos += 1

    if pontos <= 4:
        return 'Senha média'
    else:
        return 'Senha forte'

def validar_senha():
    try:
        if not lista_senhas:
            print('Nenhuma senha foi criada ainda!')
        else:
            print('\nSenhas salvas:')
            for i, s in enumerate(lista_senhas, start=1):
                print(f'{i} - {"*" * len(s)}')

            escolha_validar = int(input('\nDigite o número da senha que deseja validar: '))

            if escolha_validar < 1 or escolha_validar > len(lista_senhas):
                print('Opção inválida!')
            else:
                senha_escolhida = lista_senhas[escolha_validar - 1]
                resultado = verificar_senha(senha_escolhida)
                classificacao = qualificar_senha(senha_escolhida)

                if isinstance(resultado, list):
                    print('\nErros encontrados:')
                    for i, erro in enumerate(resultado, start=1):
                        print(f'{i}. {erro}')
                    print(f'Classificação: {classificacao}')
                else:
                    print(resultado)
                    print(f'Classificação: {classificacao}')
    except ValueError:
        print('Opção inválida!')

def listar_senhas():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
    else:
        print('\nSenhas salvas:')
        for i, senha in enumerate(lista_senhas, start=1):
            print(f'{i} - {"*" * len(senha)}')

def sair_programa():
    print('Saindo do programa!')
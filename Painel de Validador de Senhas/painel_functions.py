from requisits import requisitos
from verify_passwords import verificar_senha

lista_senhas = []
CARACTERES_ESPECIAIS = '@#$%¨&*!?_-+='

def mostrar_senhas():
    print('\nSenhas salvas:')
    for i, senha in enumerate(lista_senhas, start=1):
        print(f'{i} - {"*" * len(senha)}')

def escolher_indice(mensagem):
    try:
        indice = int(input(mensagem)) - 1

        if indice < 0 or indice >= len(lista_senhas):
            print('Opção inválida!')
            return None

        return indice
    except ValueError:
        print('Opção inválida!')
        return None

def criar_senha():
    requisitos()
    nova_senha = input('\nDigite sua senha por favor: ').strip()

    if nova_senha == '':
        print('Senha inválida, não pode ser vazia!')
        return

    lista_senhas.append(nova_senha)
    print('Senha criada com sucesso!')

def editar_senha():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
        return

    mostrar_senhas()
    indice = escolher_indice('\nDigite o número da senha que deseja editar: ')

    if indice is None:
        return

    nova_senha = input('Digite a nova senha: ').strip()

    if nova_senha == '':
        print('Senha inválida, não pode ser vazia!')
        return

    lista_senhas[indice] = nova_senha
    print('Senha alterada com sucesso!')

def deletar_senha():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
        return

    mostrar_senhas()
    indice = escolher_indice('\nDigite o número da senha que deseja deletar: ')

    if indice is None:
        return

    senha_removida = lista_senhas.pop(indice)
    print(f'Senha "{"*" * len(senha_removida)}" deletada com sucesso!')

def qualificar_senha(senha):
    pontos = 0

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

    if any(c in CARACTERES_ESPECIAIS for c in senha):
        pontos += 1

    if pontos <= 2:
        return 'Senha fraca'
    elif pontos <= 4:
        return 'Senha média'
    else:
        return 'Senha forte'

def validar_senha():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
        return

    mostrar_senhas()
    indice = escolher_indice('\nDigite o número da senha que deseja validar: ')

    if indice is None:
        return

    senha_escolhida = lista_senhas[indice]
    resultado = verificar_senha(senha_escolhida)
    classificacao = qualificar_senha(senha_escolhida)

    if isinstance(resultado, list):
        print('\nErros encontrados:')
        for i, erro in enumerate(resultado, start=1):
            print(f'{i}. {erro}')
    else:
        print(resultado)

    print(f'Classificação: {classificacao}')

def listar_senhas():
    if not lista_senhas:
        print('Nenhuma senha foi criada ainda!')
        return

    mostrar_senhas()

def sair_programa():
    print('Saindo do programa!')
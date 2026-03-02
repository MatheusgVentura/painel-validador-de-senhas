def verificar_senha(senha):
    caracteres_especiais = '@#$%¨&*'
    erros = []

    if len(senha) < 8:
        erros.append('Sua senha contém menos de 8 caracteres!')

    if not any(c in caracteres_especiais for c in senha):
        erros.append('Sua senha precisa ter pelo menos 1 caractere especial!')

    if not any(c.isupper() for c in senha) or not any(c.islower() for c in senha):
        erros.append('Sua senha precisa conter letras maiúsculas e minúsculas!') 

    if not any(c.isdigit() for c in senha):
        erros.append('Sua senha deve conter algum número!')

    if not erros:
        return 'Senha válida com sucesso!'
    else:
        return erros
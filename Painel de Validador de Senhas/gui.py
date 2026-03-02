import tkinter as tk
from tkinter import messagebox

from painel_functions import lista_senhas, qualificar_senha
from verify_passwords import verificar_senha


def ocultar_senha(senha):
    return '*' * len(senha)


def atualizar_lista():
    listbox_senhas.delete(0, tk.END)

    if not lista_senhas:
        listbox_senhas.insert(tk.END, 'Nenhuma senha cadastrada.')
        return

    for i, senha in enumerate(lista_senhas, start=1):
        listbox_senhas.insert(tk.END, f'{i} - {ocultar_senha(senha)}')


def limpar_campos():
    entrada_senha.delete(0, tk.END)
    entrada_senha.focus()


def obter_indice_selecionado():
    selecao = listbox_senhas.curselection()

    if not selecao:
        messagebox.showwarning('Aviso', 'Selecione uma senha na lista.')
        return None

    if not lista_senhas:
        messagebox.showwarning('Aviso', 'Nenhuma senha foi criada ainda!')
        return None

    return selecao[0]


def criar_senha_gui():
    nova_senha = entrada_senha.get()

    if nova_senha.strip() == '':
        messagebox.showerror('Erro', 'Senha inválida, não pode ser vazia!')
        return

    lista_senhas.append(nova_senha)
    atualizar_lista()
    limpar_campos()
    label_resultado.config(text='Senha criada com sucesso!')


def editar_senha_gui():
    indice = obter_indice_selecionado()
    if indice is None:
        return

    nova_senha = entrada_senha.get()

    if nova_senha.strip() == '':
        messagebox.showerror('Erro', 'Digite a nova senha para editar.')
        return

    lista_senhas[indice] = nova_senha
    atualizar_lista()
    limpar_campos()
    label_resultado.config(text='Senha alterada com sucesso!')


def deletar_senha_gui():
    indice = obter_indice_selecionado()
    if indice is None:
        return

    senha_removida = lista_senhas.pop(indice)
    atualizar_lista()
    limpar_campos()
    label_resultado.config(text=f'Senha "{ocultar_senha(senha_removida)}" deletada com sucesso!')


def validar_senha_gui():
    indice = obter_indice_selecionado()
    if indice is None:
        return

    senha_escolhida = lista_senhas[indice]
    resultado = verificar_senha(senha_escolhida)
    classificacao = qualificar_senha(senha_escolhida)

    if isinstance(resultado, list):
        erros = '\n'.join(f'{i}. {erro}' for i, erro in enumerate(resultado, start=1))
        texto = f'Erros encontrados:\n{erros}\n\nClassificação: {classificacao}'
    else:
        texto = f'{resultado}\nClassificação: {classificacao}'

    label_resultado.config(text=texto)


def mostrar_selecionada(event=None):
    indice = obter_indice_selecionado_silencioso()
    if indice is None:
        return

    entrada_senha.delete(0, tk.END)
    entrada_senha.insert(0, lista_senhas[indice])


def obter_indice_selecionado_silencioso():
    selecao = listbox_senhas.curselection()
    if not selecao or not lista_senhas:
        return None
    return selecao[0]


janela = tk.Tk()
janela.title('Validador de Senhas')
janela.geometry('700x650')
janela.resizable(False, False)

label_titulo = tk.Label(
    janela,
    text='Painel de Validação de Senhas',
    font=('Arial', 16, 'bold')
)
label_titulo.pack(pady=10)

label_requisitos = tk.Label(
    janela,
    text=(
        'Requisitos: mínimo 8 caracteres, '
        '1 caracteres especial, '
        'letra maiúscula, '
        'minúscula e número.'
    ),
    wraplength=620,
    justify='center'
)
label_requisitos.pack(pady=5)

frame_entrada = tk.Frame(janela)
frame_entrada.pack(pady=10)

label_senha = tk.Label(frame_entrada, text='Digite a senha:')
label_senha.grid(row=0, column=0, padx=5)

entrada_senha = tk.Entry(frame_entrada, width=35, show='*')
entrada_senha.grid(row=0, column=1, padx=5)
entrada_senha.focus()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_criar = tk.Button(frame_botoes, text='Criar senha', width=15, command=criar_senha_gui)
botao_criar.grid(row=0, column=0, padx=5, pady=5)

botao_editar = tk.Button(frame_botoes, text='Editar senha', width=15, command=editar_senha_gui)
botao_editar.grid(row=0, column=1, padx=5, pady=5)

botao_deletar = tk.Button(frame_botoes, text='Deletar senha', width=15, command=deletar_senha_gui)
botao_deletar.grid(row=0, column=2, padx=5, pady=5)

botao_validar = tk.Button(frame_botoes, text='Validar senha', width=15, command=validar_senha_gui)
botao_validar.grid(row=0, column=3, padx=5, pady=5)

frame_lista = tk.Frame(janela)
frame_lista.pack(pady=10)

label_lista = tk.Label(frame_lista, text='Senhas salvas (mascaradas):')
label_lista.pack(anchor='w')

listbox_senhas = tk.Listbox(frame_lista, width=50, height=10)
listbox_senhas.pack()
listbox_senhas.bind('<<ListboxSelect>>', mostrar_selecionada)

label_dica = tk.Label(
    janela,
    text='Dica: selecione uma senha da lista para editar, deletar ou validar.',
)
label_dica.pack(pady=5)

label_resultado = tk.Label(
    janela,
    text='Resultado aparecerá aqui.',
    justify='left',
    wraplength=620,
    anchor='w'
)
label_resultado.pack(pady=15)

botao_sair = tk.Button(janela, text='Sair', width=15, command=janela.destroy)
botao_sair.pack(pady=10)

atualizar_lista()
janela.mainloop()

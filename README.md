# 🔐 Painel Validador de Senhas

Um gerenciador e validador de senhas desenvolvido em Python, disponível em duas interfaces: **terminal (CLI)** e **interface gráfica (GUI)** com Tkinter.

---

## 💡 Motivação

Este projeto faz parte da minha jornada de transição e aprofundamento na área de **cibersegurança**, com foco em **Blue Team**.

Após participar de um processo seletivo para estágio na área, recebi um feedback valioso do entrevistador: meu currículo era voltado majoritariamente para Red Team, e ele me recomendou começar pelo Blue Team — caminho mais indicado para quem está iniciando na área. Além disso, ele apontou que Python é uma linguagem essencial para cibersegurança, especialmente em automação, sendo mais estratégico do que o foco que eu tinha em C e C++.

A partir disso, comecei a estudar Python de forma direcionada e a desenvolver projetos práticos ligados à segurança, começando pelos mais simples — como este validador de senhas — com o objetivo de evoluir gradualmente para projetos mais complexos.

> Este projeto é parte de um portfólio em construção, documentando minha evolução prática em Python aplicado à segurança da informação.

---

## 📋 Funcionalidades

- **Criar senha** — Adiciona uma nova senha à lista
- **Editar senha** — Altera uma senha existente
- **Deletar senha** — Remove uma senha da lista
- **Validar senha** — Verifica se a senha atende aos requisitos de segurança
- **Listar senhas** — Exibe todas as senhas salvas (mascaradas com `*`)
- **Classificação de força** — Classifica a senha como *fraca*, *média* ou *forte*

---

## ✅ Requisitos de Senha

Para que uma senha seja considerada válida, ela deve atender a todos os critérios abaixo:

| Critério | Descrição |
|---|---|
| Comprimento | Mínimo de 8 caracteres |
| Caractere especial | Pelo menos um de: `@#$%¨&*` |
| Letras maiúsculas e minúsculas | Obrigatório conter ambas |
| Número | Pelo menos um dígito numérico |

### Classificação de Força

| Classificação | Condição |
|---|---|
| 🔴 Senha fraca | Não passou na validação |
| 🟡 Senha média | Passou na validação com até 4 pontos |
| 🟢 Senha forte | Passou na validação com 5 ou mais pontos |

> Pontos são acumulados por comprimento (8+ e 12+ caracteres), uso de maiúsculas, minúsculas, números e caracteres especiais.

---

## 🗂️ Estrutura do Projeto

```
Painel de Validador de Senhas/
├── main_painel.py        # Ponto de entrada da versão CLI
├── gui.py                # Interface gráfica com Tkinter
├── painel_functions.py   # Lógica principal (criar, editar, deletar, validar, listar)
├── verify_passwords.py   # Função de verificação dos requisitos da senha
└── requisits.py          # Exibe os requisitos de senha no terminal
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado
- Tkinter (já incluso na instalação padrão do Python)

### Versão Terminal (CLI)

```bash
python main_painel.py
```

O menu interativo será exibido com as opções numeradas de 1 a 6.

### Versão Gráfica (GUI)

```bash
python gui.py
```

A janela do aplicativo será aberta com todos os controles visuais disponíveis.

---

## 🖥️ Interface Gráfica

A GUI conta com:

- Campo de entrada de senha (mascarado com `*`)
- Botões para **Criar**, **Editar**, **Deletar** e **Validar** senhas
- Lista de senhas salvas com visualização mascarada
- Área de resultado exibindo erros de validação e classificação de força
- Ao clicar em uma senha da lista, ela é carregada automaticamente no campo de edição

---

## 🔒 Observação de Segurança

> As senhas são armazenadas **apenas em memória** durante a execução do programa. Ao encerrar, todos os dados são perdidos. Este projeto tem fins educacionais e de estudo.

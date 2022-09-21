import PySimpleGUI as sg

#janelaLogin
def janelaLogin():
    layout = [
        [sg.Text("LOCADORA DE LIVROS", font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Funcionário já cadastrado? Faça o login:")],
        [sg.Text("Login:")], [sg.Input(key="login")],
        [sg.Text("Senha:")], [sg.InputText(key="senha",password_char="*")],
        [sg.Push()],
        [sg.Button("ENTRAR")],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Ainda não cadastrado? Cadastre-se abaixo!")],
        [sg.Button('CADASTRO DE FUNCIONÁRIO')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VISUALIZAR FUNCIONÁRIOS CADASTRADOS')]
    ]
    return sg.Window("Login/Cadastro", layout, element_justification='center',finalize=True)

#janelaCadastroFuncionario
def janelaCadastroFuncionario():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Nome: "), sg.Push(),sg.Input(key='nomeFuncionario')],
        [sg.Text("Sobrenome: "),sg.Push(),sg.Input(key='sobrenomeFuncionario')],
        [sg.Text("Crie um login: "),sg.Push(),sg.Input(key='loginFuncionario')],
        [sg.Text("Criar senha: "),sg.Push(),sg.Input(key='senha1', password_char="*")],
        [sg.Text("Repetir senha criada: "),sg.Push(),sg.Input(key='senha2', password_char='*')],
        [sg.Push()],
        [sg.Button('CADASTRAR')],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window("Cadastro de Funcionário",layout,element_justification='center',finalize=True)
    
#janelaSistema
def janelaSistema():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('LOCAÇÃO')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('CADASTRAR CLIENTE'), sg.Button('CADASTRAR LIVRO')],
        [sg.Button('VISUALIZAR CLIENTES'), sg.Button('VISUALIZAR LIVROS')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window("Sistema", layout,element_justification='center',finalize=True)

#janelaCadastroCliente
def janelaCadastroCliente():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text('Nome:'),sg.Push(),sg.Input(key='nomeCliente')],
        [sg.Text('CPF:'),sg.Push(),sg.Input(key='cpfCliente')],
        [sg.Push()],
        [sg.Button('CADASTRAR')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastro Cliente', layout, element_justification='center',finalize=True)

#janelaCadastroLivro
def janelaCadastroLivro():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Autor:"),sg.Push(),sg.Input(key='autor')],
        [sg.Text("Título:"),sg.Push(),sg.Input(key='titulo')],
        [sg.Push()],
        [sg.Button('CADASTRAR')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('Cadastro Livro',layout,element_justification='center',finalize=True)

#janelaLocacaoLogin
def janelaLocacaoLogin():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Nome do Cliente:"),sg.Push(),sg.Input(key='nome')],
        [sg.Text("CPF do Cliente:"),sg.Push(),sg.Input(key='cpf', password_char="*")],
        [sg.Push()],
        [sg.Button("ENTRAR")],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window("Login Cliente",layout,element_justification='center',finalize=True)

#janelaLocacao
def janelaLocacao():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text('Seu CPF:'),sg.Push(),sg.Input(key='cpf')],
        [sg.Text("Qual o livro que você procura?")],
        [sg.Text("Título:"),sg.Push(),sg.Input(key='escolha')],
        [sg.Text("Locar por quantos dias?"),sg.Push(),sg.Input(key='dias')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Quer locar outro livro?")],
        [sg.Button('LOCAR')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VISUALIZAR')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window("Locar",layout,element_justification='center',finalize=True)

#janelaCarrinho
def janelaCarrinho():
    layout = [
        [sg.Text('LOCADORA DE LIVROS', font=50)],
        [sg.Image('imagens/biblioteca.png')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Seu CPF:"),sg.Push(),sg.Input(key='cpf')],
        [sg.Push()],
        [sg.HSeparator()],
        [sg.Push()],
        [sg.Text("Valor da locação: R$4,00 x dias")],
        [sg.Button("FINALIZAR")],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window("Carrinho",layout,element_justification='center',finalize=True)

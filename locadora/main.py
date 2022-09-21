'''
UFRPE - LICENCIATURA EM COMPUTAÇÃO
TURMA: LC1
DISCIPLINA: LABORATÓRIO DE PROGRAMAÇÃO 1 2021.2
PROFESSOR: RINALDO LIMA
ALUNO: TÚLIO FALCÃO
'''
import PySimpleGUI as sg
from clientes import Cliente
import janelas
import clientes
import livros
import funcionario
import pickle

#tema
sg.theme('DarkBlue17')

#documentos pickle ==============================

#=== confere se há documento pickle para carregar
try:
    with open('funcionarios.pkl', 'rb') as p:
        funcionario.funcionarios = pickle.load(p)
    with open('clientes.pkl', 'rb') as p:
        clientes.clientes = pickle.load(p)
    with open('livros.pkl','rb') as p:
        livros.livros = pickle.load(p)
except:
    pass

#gerenciamento de janelas
janelaLogin,janelaCadastroFuncionario,janelaSistema,janelaCadastroCliente,janelaCadastroLivro,janelaLocacaoLogin,janelaLocacao,janelaCarrinho = janelas.janelaLogin(),None,None,None,None,None,None,None

#loop do programa
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        #==== cria documentos pickle ao fechar o programa ==========
        with open('funcionarios.pkl', 'wb') as p:
            arqFuncionarios = pickle.dump(funcionario.funcionarios, p)
        with open('clientes.pkl', 'wb') as p:
            arqClientes = pickle.dump(clientes.clientes, p)
        with open('livros.pkl','wb') as p:
            arqLivros = pickle.dump(livros.livros, p)
        break
    
    #========= janelaLogin ===================
    if window == janelaLogin and event == 'CADASTRO DE FUNCIONÁRIO':
        janelaLogin.hide()
        janelaCadastroFuncionario = janelas.janelaCadastroFuncionario()
    
    if window == janelaLogin and event == 'VISUALIZAR FUNCIONÁRIOS CADASTRADOS':
        listaFuncionarios = '\n'.join([str(x.nomeFuncionario) + " " + str(x.sobrenomeFuncionario) for x in funcionario.funcionarios])
        sg.popup(listaFuncionarios)
        
    if window == janelaLogin and event == 'ENTRAR':
        loginF = values['login']
        senhaF = values['senha']
        i = [funcionario.funcionarios.index(x) for x in funcionario.funcionarios if x.loginFuncionario == loginF]
        i = int(i[0])
        if funcionario.funcionarios[i].loginFuncionario == loginF and funcionario.funcionarios[i].senhaFuncionario == senhaF:
            janelaLogin.hide()
            janelaSistema = janelas.janelaSistema()
        else:
            sg.popup("Login e/ou senha não conferem!")
            janelaLogin.hide()
            janelaLogin = janelas.janelaLogin()
    
    #========= janelaCadastroFuncionario =====
    if window == janelaCadastroFuncionario and event == 'CADASTRAR':
        nomeFuncionario = values['nomeFuncionario']
        sobrenomeFuncionario = values['sobrenomeFuncionario']
        loginFuncionario = values['loginFuncionario']
        senha1Funcionario = values['senha1']
        senha2Funcionario = values['senha2']
        tem = [True for x in funcionario.funcionarios if x.nomeFuncionario == nomeFuncionario and x.loginFuncionario == loginFuncionario]
        if True in tem:
            sg.popup("Funcionário já cadastrado!")
            janelaCadastroFuncionario.hide()
            janelaLogin = janelas.janelaLogin()
        else:
            if senha1Funcionario == senha2Funcionario:
                funcionario.funcionarios.append(funcionario.Funcionario(nomeFuncionario,sobrenomeFuncionario,loginFuncionario,senha1Funcionario))
                sg.popup('Funcionário Cadastrado com Sucesso')
                janelaCadastroFuncionario.hide()
                janelaLogin = janelas.janelaLogin()
            else:
                sg.popup('Senhas não conferem!')
                janelaCadastroFuncionario.hide()
                janelaCadastroFuncionario = janelas.janelaCadastroFuncionario()
    
    if window == janelaCadastroFuncionario and event == 'VOLTAR':
        janelaCadastroFuncionario.hide()
        janelaLogin = janelas.janelaLogin()
    
    #========== janelaSistema ==================
    if window == janelaSistema and event == 'VOLTAR':
        janelaSistema.hide()
        janelaLogin = janelas.janelaLogin()
    
    if window == janelaSistema and event == 'CADASTRAR CLIENTE':
        janelaSistema.hide()
        janelaCadastroCliente = janelas.janelaCadastroCliente()
        
    if window == janelaSistema and event == 'VISUALIZAR CLIENTES':
        listaClientes = '\n'.join([str(x.cpfCliente) + " - " + str(x.nomeCliente) for x in clientes.clientes])
        sg.popup(listaClientes)
    
    if window == janelaSistema and event == 'CADASTRAR LIVRO':
        janelaSistema.hide()
        janelaCadastroLivro = janelas.janelaCadastroLivro()
    
    if window == janelaSistema and event == 'VISUALIZAR LIVROS':
        listaLivros = '\n'.join([str(x.autor) + " - " + str(x.titulo) for x in livros.livros])
        sg.popup_scrolled(listaLivros)
    
    if window == janelaSistema and event == 'LOCAÇÃO':
        janelaSistema.hide()
        janelaLocacaoLogin = janelas.janelaLocacaoLogin()
            
    #========== janelaCadastrarCliente ==========
    if window == janelaCadastroCliente and event == 'VOLTAR':
        janelaCadastroCliente.hide()
        janelaSistema = janelas.janelaSistema()
    
    if window == janelaCadastroCliente and event == 'CADASTRAR':
        nome = values['nomeCliente']
        cpf = values['cpfCliente']
        tem = [True for x in clientes.clientes if x.cpfCliente == cpf]
        if len(tem) > 0:
            sg.popup("Cliente Já Cadastrado!")
            janelaCadastroCliente.hide()
            janelaCadastroCliente = janelas.janelaCadastroCliente()
        elif len(tem) == 0:
            clientes.clientes.append(clientes.Cliente(nome,cpf))
            sg.popup("Cliente Cadastrado com Sucesso!")
            janelaCadastroCliente.hide()
            janelaSistema = janelas.janelaSistema()
        
    #========== janelaCadastroLivro ==============
    if window == janelaCadastroLivro and event == 'VOLTAR':
        janelaCadastroLivro.hide()
        janelaSistema = janelas.janelaSistema()
    
    if window == janelaCadastroLivro and event == 'CADASTRAR':
        autor = values['autor']
        titulo = values['titulo']
        tem = [True for x in livros.livros if x.titulo == titulo]
        if len(tem) > 0:
            sg.popup("Livro já Cadastrado!")
            janelaCadastroLivro.hide()
            janelaCadastroLivro = janelas.janelaCadastroLivro()
        elif len(tem) == 0:
            livros.livros.append(livros.Livro(autor,titulo))
            sg.popup("Livro Cadastrado com Sucesso!")
            janelaCadastroLivro.hide()
            janelaSistema = janelas.janelaSistema()
            
    #=========== janelaLocacaoLogin ================
    if window == janelaLocacaoLogin and event == 'VOLTAR':
        janelaLocacaoLogin.hide()
        janelaSistema = janelas.janelaSistema()
    
    if window == janelaLocacaoLogin and event == 'ENTRAR':
        nome = values['nome']
        cpf = values['cpf']
        tem = [True for x in clientes.clientes if x.cpfCliente == cpf]
        if len(tem) > 0:
            janelaLocacaoLogin.hide()
            janelaLocacao = janelas.janelaLocacao()
        elif len(tem) == 0:
            sg.popup("Cliente Não Cadastrado!")
            janelaLocacaoLogin.hide()
            janelaSistema = janelas.janelaSistema()
            

    #=========== janelaLocacao ======================
    if window == janelaLocacao and event == 'VOLTAR':
        janelaLocacao.hide()
        janelaLocacaoLogin = janelas.janelaLocacaoLogin()
    
    if window == janelaLocacao and event == 'LOCAR':
        cpf = values['cpf']
        escolha = values['escolha']
        dias = values['dias']
        tem = [int(livros.livros.index(x)) for x in livros.livros if escolha == x.titulo]
        ind = tem[0]
        if len(tem) > 0:
            clientes.locados.append((livros.livros[ind].autor,livros.livros[ind].titulo,dias))
            clientes.locacao[cpf] = clientes.locados
            sg.popup("No carrinho!")
            janelaLocacao.hide()
            janelaLocacao = janelas.janelaLocacao()
        elif len(tem) == 0:
            sg.popup("Livro Não Encontrado!")
            janelaLocacao.hide()
            janelaLocacao = janelas.janelaLocacao()
            
    if window == janelaLocacao and event == 'VISUALIZAR':
        janelaLocacao.hide()
        janelaCarrinho = janelas.janelaCarrinho()
        
    #=========== janelaCarrinho =====================================
    if window == janelaCarrinho and event == 'VOLTAR':
        janelaCarrinho.hide()
        janelaLocacao = janelas.janelaLocacao()
    
    if window == janelaCarrinho and event == 'FINALIZAR':
        cpf = values['cpf']
        if cpf in clientes.locacao:
            quantidadeArquivos = len(clientes.locacao[cpf])
            for x in range(quantidadeArquivos):
                clientes.carro.append('-'.join(clientes.locacao[cpf][x]))
                clientes.total += clientes.valor * int(clientes.locacao[cpf][x][2])
        carro = '\n'.join([x for x in clientes.carro])
        sg.popup_scrolled(f"EMPRÉSTIMO\nAutor - Título - Dias\n{carro}\nValor da Locação: R${clientes.total},00")

        
window.close()


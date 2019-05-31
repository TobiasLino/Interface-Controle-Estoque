# -*- coding: utf-8 -*-
# OBRA SOCIAL N. S. de FÁTIMA
# CONTROLE DE BENS IMOBILÁRIOS
# 
# GRUPO: ADM Enterpreneur
# Dev: Tobias da Silva Lino
#
# Biblioteca utilizada para a interface
import tkinter as tk
# Classe onde está o Canvas para janelas em scroll
import Scroll as scroll
# banco de dados
import Banco as db


# Paleta de cores
# Variações de verde, branco, e azul escuro
btn_color = '#719C95'
fundo_color = '#2C2B35'
titulo_color = '#3A897C'
lbl_fundo_color = '#3A897C'
branco = '#FFFFFF'
cinza = '#707070'
fundo_escuro = '#2C2B35'
ciano_claro = '#719C95'
ciano_escuro = '#3B544F'
ciano = '#3A897C'

class Program():
    # O programa se inicia com a página de login (somente para administradores). Por motivos de eficiência, existe a opção 'cadastrar'
    # que serve para fazer o cadastro de uma pessoa que vai fazer algum empréstimo, essa opção também pode ser acessada da página principal(Home)
    def __init__(self, master=None):
        self.Login.__call__()
    
    
    # Essa é a autenticação, mais rústica, o nome e a senha são pegos das caixas de texto, inseridas em duas variáveis e então comparadas com os 
    # dados padronizados.
    # Se forem autenticadas, a função destroi os packs da página de login e chama a página principal com um __call__
    # senão, abre uma janela de aviso, com o valor 'Usuário inválido' e apaga os dados inseridos nos campos.
    def Home(self):
        get_nome = str(self.txt_entrar.get())
        get_senha = str(self.txt_senha.get())
        enter = db.decode(db.binario())
        if get_nome == 'admin' and get_senha == enter:
            # Destroy 
            self.frame_principal.destroy()
            self.frame_login.destroy()
            self.frame_entrar.destroy()
            self.frame_senha.destroy()
            self.frame_botoes.destroy()
            self.lbl_login.destroy()
            self.lbl_nome.destroy()
            self.lbl_senha.destroy()
            self.btn_entrar.destroy()
            self.btn_cadastrar.destroy()
            self.txt_entrar.destroy()
            self.txt_senha.destroy()
            # Biblioteca para contagem de tempo da janela 
            import time
            time.sleep(0.05)
            self.Home_interface.__call__()  # Chama a Home
        else:
            class aviso():
                def __init__(self, master=None, t=3):
                    self.frame = tk.Frame(master, bg=ciano)
                    self.lbl_msg = tk.Button(self.frame, text='Usuário/Senha inválidos',command=self.quit_, font=('AirbnbCereal-Book', '21'), bg=ciano, fg='#FFFFFF', border=0)
                    self.frame.pack(fill='both')
                    self.lbl_msg.pack(padx=20, pady=20)
                def quit_(self):
                    root.destroy()
            root = tk.Tk()
            aviso(root)
            self.NOME_VAR.set('')
            self.SENHA_VAR.set('')
            
        
        
    # ****** INTERFACE DA PÁGINA DE LOGIN ******
    # A interface se baseia em uma frame de fundo(escuro) e outro no centro(branco)
    # dentro do frame central, estão as caixas de texto, labels e botões dentro de determinados frames para organização
    # Foi usado um único tipo de fonte(AirbnbCereal), com dois tamanhos: 21, para títulos, e 14, para textos.
    # Cores retiradas da paleta de cores
    def Login(self):
        self.fonte_titulo = ('Roboto-Regular', '21')
        self.fonte_texto = ('Roboto-Regular', '14')
        
        # All frames
        self.frame_principal = tk.Frame(janela, bg=fundo_color)
        self.frame_login = tk.Frame(self.frame_principal, bg='#FFFFFF', height=600, width=500)
        self.frame_login_box = tk.Frame(self.frame_login, bg=ciano_escuro)
        self.frame_entrar = tk.Frame(self.frame_login, bg='#FFFFFF', height=150, width=450)
        self.frame_senha = tk.Frame(self.frame_login, bg='#FFFFFF', height=150, width=450)
        self.frame_botoes = tk.Frame(self.frame_login, bg='#FFFFFF', height=150, width=450)
        
        # Variações no no texto de login
        self.NOME_VAR = tk.StringVar()
        self.SENHA_VAR = tk.StringVar()
        # All Entrys
        self.txt_entrar = tk.Entry(self.frame_entrar, font=self.fonte_texto,  textvariable=self.NOME_VAR, bg='#FFFFFF', fg='#707070', width=40)
        self.txt_senha = tk.Entry(self.frame_senha, font=self.fonte_texto, textvariable=self.SENHA_VAR, show='*', bg='#FFFFFF', fg='#707070', width=40)
        
        # All Labels
        self.lbl_login = tk.Label(self.frame_login_box, text='Login', bg=ciano_escuro, fg=branco, font=self.fonte_titulo)
        self.lbl_nome = tk.Label(self.frame_entrar, text='Nome', bg='#FFFFFF', fg='#000000', font=self.fonte_texto)
        self.lbl_senha = tk.Label(self.frame_senha, text='Senha', bg='#FFFFFF', fg='#000000', font=self.fonte_texto)
        
        # All buttons
        self.btn_entrar = tk.Button(self.frame_botoes, command=self.Home, highlightbackground='#FFFFFF', activeforeground='#707070', bg=ciano_escuro, text='Entrar', font=self.fonte_texto, fg='#FFFFFF', height=8, width=20, border=0)
        self.btn_cadastrar = tk.Button(self.frame_botoes, command=self.Cadastrar, activeforeground='#707070', bg =ciano_escuro, text='Cadastrar', font=self.fonte_texto, fg='#FFFFFF',height=8, width=20, border=0)
                                       
        # ****** ALL LOGIN PACKS ******
        # Frame packs
        self.frame_principal.pack(fil='both', expand=1) 
        
        self.frame_login.pack(padx=(200,200), pady=(200,200), expand=1)
        self.frame_login_box.pack(fill='x')
        self.frame_entrar.pack(padx=(25,25), pady=(20,0), expand=0)
        self.frame_senha.pack(padx=(25,25), pady=(10,10), expand=0)
        self.frame_botoes.pack(padx=(25,25), pady=(0,20), expand=0)
        # Label packs
        self.lbl_login.pack(pady = (25,20))
        self.lbl_nome.pack(side=tk.LEFT, pady = (10,10))
        self.lbl_senha.pack(side=tk.LEFT, pady=(10,10))
        
        # Buton packs
        self.btn_entrar.pack(side=tk.LEFT, padx=(10,10),pady=(20,20))
        self.btn_cadastrar.pack(side=tk.RIGHT, padx=(10,10),pady=(20,20))
        # Entry packs
        self.txt_entrar.pack(pady=(15,10), padx=(25,25))
        self.txt_entrar.bind("<KeyPress>", lambda e: self.txt_entrar.focus() if e.char == '\r' else None)   # Coloca o foco na textbox
        self.txt_senha.pack(pady=(15,10), padx=(25,25))
        self.txt_senha.bind("<KeyPress>", lambda e: self.Home.__call__() if e.char == '\r' else None)       # chama a Home ao apertar o enter
     
        
    # ****** INTERFACE DA PÁGINA DE CADASTRO ******
    # Ao chamar a página de Cadastro é introduzida a nova janela
    # A interface é composta de um frame de fundo(escuro) e um frame central(branco), na qual estão os demais frames, botões, labels 
    # e caixas de texto, onde são pegos os dados e inseridos no Banco de Dados.
    # O botão 'cancelar', destroi todas as operações da página e retorna à página de origem.
    def Cadastrar(self, master=None):
        class Cadastra():
            def __init__(self, master=None):
            # Paleta de Cores
                btn_color = '#719C95'
                branco = '#FFFFFF'
                cinza = '#707070'
                fundo_escuro = '#2C2B35'
                ciano_escuro = '#3B544F'
            # Fontes
                self.fonte_titulo = ('Roboto-Regular', '21')
                self.fonte_texto = ('Roboto-Regular', '14')
            # INTERFACE
            # FRAMES
                self.frame_fundo = scroll.JanelaRolavel(root, bg=fundo_escuro, height=1500)
                self.frame_cadastro = tk.Frame(self.frame_fundo, bg='#FFFFFF', height=1200, width=900)
                self.frame_cadastro_titulo = tk.Frame(self.frame_cadastro, bg=ciano_escuro)
                self.frame_informacoes = tk.Frame(self.frame_cadastro, bg='#FFFFFF', height=300, width=800)
                self.frame_informacoes_nome_sexo = tk.Frame(self.frame_informacoes, bg='#FFFFFF')
                self.frame_informacoes_CPF_nascimento_telefone = tk.Frame(self.frame_informacoes, bg='#FFFFFF')
                self.frame_informacoes_email = tk.Frame(self.frame_informacoes, bg='#FFFFFF')
                self.frame_endereco = tk.Frame(self.frame_cadastro, bg='#FFFFFF', height=300, width=800)
                self.frame_endereco_rua_numero = tk.Frame(self.frame_endereco, bg='#FFFFFF')
                self.frame_endereco_bairro_cidade_UF = tk.Frame(self.frame_endereco, bg='#FFFFFF')
                self.frame_botoes = tk.Frame(self.frame_cadastro, bg='#FFFFFF')
                                          
            # LABELS
                self.lbl_titulo_cadastrar = tk.Label(self.frame_cadastro_titulo, text='Cadastrar', font=self.fonte_titulo, bg=ciano_escuro, fg=branco)
                self.lbl_titulo_dados = tk.Label(self.frame_cadastro, text='Insira os dados', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_titulo_endereco = tk.Label(self.frame_cadastro, text='Endereço', font=self.fonte_texto, bg=branco, fg='#000000')
            # Primeiras informações
                self.lbl_textos_nome = tk.Label(self.frame_informacoes_nome_sexo, text='Nome', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_sexo = tk.Label(self.frame_informacoes_nome_sexo, text='Sexo (M ou F)', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_CPF = tk.Label(self.frame_informacoes_CPF_nascimento_telefone, text='CPF', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_nascimento = tk.Label(self.frame_informacoes_CPF_nascimento_telefone, text='Nascimento', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_telefone = tk.Label(self.frame_informacoes_CPF_nascimento_telefone, text='Telefone', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_email = tk.Label(self.frame_informacoes_email, text='Email', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
            # Endereço
                self.lbl_textos_rua = tk.Label(self.frame_endereco_rua_numero, text='Rua', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_numero = tk.Label(self.frame_endereco_rua_numero, text='Nº', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_bairro = tk.Label(self.frame_endereco_bairro_cidade_UF, text='Bairro', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_cidade = tk.Label(self.frame_endereco_bairro_cidade_UF, text='Cidade', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                self.lbl_textos_UF = tk.Label(self.frame_endereco_bairro_cidade_UF, text='UF', font=self.fonte_texto, bg=ciano_escuro, fg=branco)
                
            # ENTRYS
            # Primeiras informações
                self.txt_nome = tk.Entry(self.frame_informacoes_nome_sexo, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=70)
                self.txt_sexo = tk.Entry(self.frame_informacoes_nome_sexo, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=10)
                self.txt_CPF = tk.Entry(self.frame_informacoes_CPF_nascimento_telefone, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=20)
                self.txt_nascimento = tk.Entry(self.frame_informacoes_CPF_nascimento_telefone, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=15)
                self.txt_telefone = tk.Entry(self.frame_informacoes_CPF_nascimento_telefone, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=20)
                self.txt_email = tk.Entry(self.frame_informacoes_email, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=60)
            # Endereço
                self.txt_rua = tk.Entry(self.frame_endereco_rua_numero, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=60)
                self.txt_numero = tk.Entry(self.frame_endereco_rua_numero, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=5)
                self.txt_bairro = tk.Entry(self.frame_endereco_bairro_cidade_UF, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=40)
                self.txt_cidade = tk.Entry(self.frame_endereco_bairro_cidade_UF, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=30)
                self.txt_UF = tk.Entry(self.frame_endereco_bairro_cidade_UF, font=self.fonte_texto, bg='#E9F2F0', fg=cinza, width=5)
                
            # BUTTONS
                self.teste_btn = tk.Button(self.frame_cadastro, text='Cancela', command=self.Cancelar)
                self.teste_btn.pack()
                self.btn_enviar = tk.Button(self.frame_botoes, activeforeground='#707070', bg=btn_color, text='Enviar', font=self.fonte_texto, fg='#FFFFFF', height=10, width=20)
                self.btn_cancelar = tk.Button(self.frame_botoes, command=self.Cancelar, activeforeground='#707070', bg=ciano_escuro, text='Cancelar', font=self.fonte_texto, fg='#FFFFFF', height=10, width=20)
                
                
            # ALL CADASTRO PACKS
            # ** Frame packs **
                self.frame_fundo.pack(fill='both', expand=1)
                self.frame_cadastro.pack(side=tk.LEFT, padx=(100,100), pady=(100,0), expand=1)
                self.frame_cadastro_titulo.pack(fill='x')
                self.frame_informacoes.pack(padx=(50,50), pady=(30,0))
                self.frame_informacoes_nome_sexo.pack(fill='x')
                self.frame_informacoes_CPF_nascimento_telefone.pack(fill='x')
                self.frame_informacoes_email.pack(fill='x')
                self.frame_endereco.pack(side=tk.LEFT, padx=(50,50), pady=(0,20))
                self.frame_endereco_rua_numero.pack(fill='x')
                self.frame_endereco_bairro_cidade_UF.pack(fill='x')
            # ** Label Packs **
            # primeiras informações
                self.lbl_titulo_cadastrar.pack(pady=(20,10), padx=(20,20))
                self.lbl_titulo_dados.pack(after=self.lbl_titulo_cadastrar, pady=(5,5), padx=(0,0))
                self.lbl_titulo_endereco.pack(after=self.frame_informacoes, pady=(5,5), padx=(20,20))
                self.lbl_textos_nome.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_sexo.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_CPF.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_nascimento.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_telefone.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_email.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
            # Endereço
                self.lbl_textos_rua.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_numero.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_bairro.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_cidade.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
                self.lbl_textos_UF.pack(side=tk.LEFT, pady=(20,20), padx=(20,0))
            # ** Entry Packs **
                self.txt_nome.pack(after=self.lbl_textos_nome, side=tk.LEFT)
                self.txt_sexo.pack(after=self.lbl_textos_sexo, side=tk.LEFT)
                self.txt_CPF.pack(after=self.lbl_textos_CPF, side=tk.LEFT)
                self.txt_nascimento.pack(after=self.lbl_textos_nascimento, side=tk.LEFT)
                self.txt_telefone.pack(after=self.lbl_textos_telefone, side=tk.LEFT)
                self.txt_email.pack(after=self.lbl_textos_email, side=tk.LEFT)
                self.txt_rua.pack(after=self.lbl_textos_rua, side=tk.LEFT)
                self.txt_numero.pack(after=self.lbl_textos_numero, side=tk.LEFT)
                self.txt_bairro.pack(after=self.lbl_textos_bairro, side=tk.LEFT)
                self.txt_cidade.pack(after=self.lbl_textos_cidade, side=tk.LEFT)
                self.txt_UF.pack(after=self.lbl_textos_UF, side=tk.LEFT)
            # ** Button Packs **
                self.btn_enviar.pack(side=tk.LEFT)
                self.btn_cancelar.pack(side=tk.RIGHT)
            # Função do botão 'cancelar', destroi a janela de cadastro e retorna à página de origem
            def Cancelar(self):
                root.destroy()
                
        # Cria a janela
        root = tk.Tk()
        Cadastra(root)
        root.state('zoomed')
        root.title('Cadastrar')
        root.mainloop()
    
    
    
    # Interface da página principal, onde estão as opções de cadastro de itens e de pessoas, o acesso à tela de About com informações do
    # desenvolvedor, a seção de buscas de itens, notificações dos itens emprestados em atraso e a opção para registar um empréstimo.
    # Composta de: um frame de fundo(escuro); um frame na esquerda, com os botões de cadastro de pessoa, cadastro de itens e 'sobre';
    # três frames, um de aviso para atrasos, outro para buscar um item e um maior para inserir dados do empréstimo.
    # Usa a fonte 'AirbnbCereal' com tamanhos: 16 para títulos e 12 para textos.
    # Cores retiradas da paleta de cores
    def Home_interface(self):
        # Fonts
        self.fonte_titulo = ('Roboto-Regular', '16')
        self.fonte_texto = ('Roboto-Regular', '12')
        
        # Frames
        self.frame_fundo = tk.Frame(janela, bg=fundo_escuro)
        self.frame_menu = tk.Frame(self.frame_fundo, bg=ciano, width=350)
        self.frame_menu_titulo = tk.Frame(self.frame_menu, bg=ciano_escuro, height=80, width=350)
        self.frame_menu_botoes = tk.Frame(self.frame_menu, bg=ciano, height=500, width=350)
        self.frame_menu_about = tk.Frame(self.frame_menu, bg=ciano, height=80, width=350)
        self.frame_blocos_menores = tk.Frame(self.frame_fundo, bg=fundo_escuro, height=250, width=1150)
        self.frame_bloco_1 = tk.Frame(self.frame_blocos_menores, bg=branco, height=270, width=400)
        self.frame_bloco_1_interno = tk.Frame(self.frame_bloco_1, bg=ciano_escuro, height=300, width=400)
        self.frame_bloco_1_interno_notificações = tk.Frame(self.frame_bloco_1, bg=branco, height=290, width=400)
        self.frame_bloco_2 = tk.Frame(self.frame_blocos_menores, bg=branco, height=200, width=325)
        self.frame_bloco_2_interno = tk.Frame(self.frame_bloco_2, bg=ciano_escuro, height=250, width=325)
        self.frame_bloco_2_interno_busca = scroll.JanelaRolavel(self.frame_bloco_2, bg=branco, height=100, width=305)
        self.frame_principal = tk.Frame(self.frame_fundo, bg=branco, height=500, width=990)
        self.frame_principal_interno = tk.Frame(self.frame_principal, bg=ciano, height=460, width=950)
        self.frame_principal_interno_entrys = tk.Frame(self.frame_principal_interno, height=260, width=750)
        
        # Labels
        self.lbl_titulo_nome = tk.Label(self.frame_menu_titulo, text='Administrador', font=self.fonte_titulo, bg=ciano_escuro, fg=branco, width=15)
        self.lbl_about_line = tk.Label(self.frame_menu_about, text='___________________________________', font=('AirbnbCereal-Book', '12'), bg=ciano, fg='#8FAAA5')
        self.lbl_bloco_1_atraso = tk.Label(self.frame_bloco_1_interno, text='Atrasos', font=self.fonte_titulo, bg=ciano_escuro, fg=branco)
        self.lbl_bloco_2_busca = tk.Label(self.frame_bloco_2_interno, text='Buscar', font=self.fonte_titulo, bg=ciano_escuro, fg=branco)
        self.resultados = tk.StringVar()
        self.lbl_bloco_2_busca_result = tk.Label(self.frame_bloco_2_interno_busca, wraplength=330, textvariable=self.resultados, font=self.fonte_texto, bg=branco, fg=cinza)
        self.lbl_principal_nome = tk.Label(self.frame_principal_interno_entrys, text='Nome', font=self.fonte_texto, bg=branco, fg=cinza)
        self.lbl_principal_descricao = tk.Label(self.frame_principal_interno_entrys, text='Descrição do Bem', font=self.fonte_texto, bg=branco, fg=cinza)
        self.lbl_principal_No_patrimonio = tk.Label(self.frame_principal_interno_entrys, text='Nº do Patrimônio', font=self.fonte_texto, bg=branco, fg=cinza)
        self.lbl_principal_data_saida = tk.Label(self.frame_principal_interno_entrys, text='Data de Saída', font=self.fonte_texto, bg=branco, fg=cinza)
        self.lbl_principal_data_devolucao = tk.Label(self.frame_principal_interno_entrys, text='Devolução', font=self.fonte_texto, bg=branco, fg=cinza)
        
        # Buttons
        self.btn_cadastrar = tk.Button(self.frame_menu_botoes, text='Cadastrar', command=self.Cadastrar, font=self.fonte_texto, bg=ciano, fg=branco, border=0)
        self.btn_inserir_item = tk.Button(self.frame_menu_botoes, text='Inserir um novo item', command=self.novo_item, font=self.fonte_texto, bg=ciano, fg=branco, border=0)
        self.btn_about = tk.Button(self.frame_menu_about, text='Sobre', font=self.fonte_texto, command=self.about, bg=ciano, fg=branco, border=0)
        self.btn_buscar = tk.Button(self.frame_bloco_2_interno, text='Buscar', font=self.fonte_texto, command=self.Busca, bg=ciano_escuro, fg=branco, border=0)
        
        # Entrys
        self.txt_busca = tk.Entry(self.frame_bloco_2_interno, font=self.fonte_texto, bg=branco, fg=cinza, width=30, border=1)
        self.txt_emprestimo_nome = tk.Entry()
        self.txt_emprestimo_descricao = tk.Entry()
        self.txt_emprestimo_No_patrimonio = tk.Entry()
        self.txt_emprestimo_data_saida = tk.Entry()
        self.txt_emprestimo_data_devolucao = tk.Entry()
        
        #  **** Packs ****
        self.frame_fundo.pack(fil='both')
        self.frame_menu.pack(side=tk.LEFT,fill='y')
        self.frame_menu_titulo.grid(row=0, column=0)
        self.frame_menu_botoes.grid(row=1, column=0, padx=(10), pady=(10,400), sticky='w')
        self.frame_menu_about.grid(row=2, column=0, sticky='s')
        self.frame_blocos_menores.pack()
        self.frame_bloco_1.grid(row=0, column=0, padx=(0), pady=15)
        self.frame_bloco_1_interno.grid(row=0, column=0, padx=10)
        self.frame_bloco_1_interno_notificações.grid(row=1, column=0, pady=(0,10))
        self.frame_bloco_2.grid(row=0, column=1, padx=(5,5), pady=5)
        self.frame_bloco_2_interno.grid(row=0, column=0)
        self.frame_bloco_2_interno_busca.grid(row=1, column=0)
        self.frame_principal.pack(padx=(10,10), pady=(10,15))
        self.frame_principal_interno.pack(padx=20, pady=20)
        self.frame_principal_interno_entrys.pack(padx=50, pady=50)
        
        # Label
        self.lbl_titulo_nome.pack(side=tk.LEFT, padx=(10,195), pady=(20,20))
        self.lbl_about_line.grid(row=0, column=0, pady=(0,10), sticky='w')
        self.lbl_bloco_1_atraso.grid(row=0, column=0, padx=(125,125),pady=10, sticky='n')
        self.lbl_bloco_2_busca.grid(row=0, column=0,padx=(20,0), pady=10, sticky='n')
        self.lbl_bloco_2_busca_result.pack()
        
        # Button
        self.btn_cadastrar.grid(row=0, column=0, padx=0, pady=8, sticky='w')
        self.btn_inserir_item.grid(row=1, column=0, padx=(1,0), pady=8, sticky='w')
        self.btn_about.grid(row=1, column=0, padx=(0,5), sticky='w')
        self.btn_buscar.grid(row=1, column=1, padx=(0,10), pady=(0,5), sticky='w')
        # Entry
        self.txt_busca.grid(row=1, column=0, padx=(10,0), pady=(0,5), sticky='w')
        
    
    # Janela About com informações do Desenvolvedor
    def about(self):
        class About():
            branco = '#FFFFFF'
            cinza = '#707070'
            fundo_escuro = '#2C2B35'
            ciano_escuro = '#3B544F'
            def __init__(self, master=None):
                
                self.frame_fundo = tk.Frame(master, bg=fundo_escuro, height=75, width=150)
                self.frame_about = tk.Frame(self.frame_fundo, bg=fundo_escuro, height=25, width=125)
                self.lbl_title = tk.Label(self.frame_about, text='Controle de Estoque\nObra Social Nossa Senhora de Fátima\n\n\nEnterpreneur\n\n', font=('Roboto-Italic','14'), bg=fundo_escuro, fg=branco)
                self.img = tk.PhotoImage(file = 'Logo.png')
                self.logo = tk.Label(self.frame_about, image=self.img)
                self.lbl_name = tk.Label(self.frame_about, text='\n\nTobias Lino\nJoão Pedro\nElieser Costa\nIgor Sene\nJoão VItor Simão\n\n2019', font=('Roboto-Italic','14'), bg=fundo_escuro, fg=branco)
                self.frame_fundo.pack()
                self.frame_about.pack(padx=20, pady=10)
                self.lbl_title.pack(padx=100, pady=(75,0))
                self.logo.pack()
                self.lbl_name.pack(padx=100, pady=(10,75))
                
        root = tk.Tk()
        About(root)
        root.title('Sobre')
        root.mainloop()
                
    # A opção de Adicionar um novo item abre uma janela com as informações necessárias para inserir um item
    # A função Insere_item é o que faz o item ser adicionado à lista
    def novo_item(self):   
        class New_item():
    # Interface da janela de adição de itens
            def __init__(self, master=None):
                # Paleta de cores
                branco = '#FFFFFF'
                cinza = '#707070'
                fundo_escuro = '#2C2B35'
                ciano_escuro = '#3B544F'
                # Fontes
                self.fonte_titulo = ('Roboto-Regular', '21')
                self.fonte_texto = ('Roboto-Regular', '14')
                
                self.frame_fundo = tk.Frame(master, bg=fundo_escuro)
                self.frame_insercao = tk.Frame(self.frame_fundo, bg=branco, height=400, width=800)
                self.frame_titulo = tk.Frame(self.frame_insercao, bg=ciano_escuro, height=40, width=800)
                # Labels
                self.lbl_titulo = tk.Label(self.frame_titulo, text='Inserir Item', font=self.fonte_titulo, bg=ciano_escuro, fg=branco)
                self.lbl_No_patrimonio = tk.Label(self.frame_insercao, text = 'Nº do Patrimônio', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_descricao = tk.Label(self.frame_insercao, text='Descrição do Bem', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_quantidade = tk.Label(self.frame_insercao, text='Quantidade', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_localizacao = tk.Label(self.frame_insercao, text='Localização', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_No_nota_fiscal = tk.Label(self.frame_insercao, text='Nº da Nota Fiscal', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_data_aquisicao = tk.Label(self.frame_insercao, text='Data de Aquisição', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_data_saida = tk.Label(self.frame_insercao, text='Data de Saída', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_fornecedor = tk.Label(self.frame_insercao, text='Fornecedor', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_valor = tk.Label(self.frame_insercao, text='Valor', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_grau_depreciacao = tk.Label(self.frame_insercao, text='Grau de Depreciação', font=self.fonte_texto, bg=branco, fg=cinza)
                self.lbl_niveis = tk.Label(self.frame_insercao, text=' A-Ótimo\nB-Bom\n  C-Razoável', font=self.fonte_texto, bg=branco, fg=cinza)
                # Entrys
                self.txt_No_patrimonio = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Descricao = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Quantidade = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Localizacao = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_No_nota_fiscal = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Data_aquisicao = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Data_saida = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Fornecedor = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Valor = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                self.txt_Grau_depreciacao = tk.Entry(self.frame_insercao, font=self.fonte_texto, bg=branco, fg=cinza)
                # Buttons
                self.btn_go = tk.Button(self.frame_insercao, command=self.Insere_item, text='Inserir', font=self.fonte_texto, bg=ciano_escuro, fg=branco, border=0, width=10)
                self.btn_cancel = tk.Button(self.frame_insercao, command=self.Cancelar, text='Cancelar',font=('Roboto-Regular','10') , bg=branco, fg=ciano_escuro, border=0, width=10)
                
                # Packs
                self.frame_fundo.pack(fill='both')
                self.frame_insercao.grid(padx=40, pady=40)
                self.frame_titulo.grid(row=0, column=0, columnspan=1, sticky='n')
                
                self.lbl_titulo.pack(pady=10)
                self.lbl_No_patrimonio.grid(row=1, column=0, padx=(10,0), pady=10)
                self.lbl_descricao.grid(row=1, column=2, padx=(10,0), pady=10)
                self.lbl_quantidade.grid(row=1, column=4, padx=(10,0), pady=10)
                self.lbl_localizacao.grid(row=2, column=0, padx=(10,0), pady=10)
                self.lbl_No_nota_fiscal.grid(row=2, column=2, padx=(10,0), pady=10)
                self.lbl_data_aquisicao.grid(row=2, column=4, padx=(10,0), pady=10)
                self.lbl_data_saida.grid(row=3, column=0, padx=(10,0), pady=10)
                self.lbl_fornecedor.grid(row=3, column=2, padx=(10,0), pady=10)
                self.lbl_valor.grid(row=3, column=4, padx=(10,0), pady=10)
                self.lbl_grau_depreciacao.grid(row=4, column=0, padx=(10,0), pady=10)
                self.lbl_niveis.grid(row=4, column=2, padx=(10,0), pady=10)
                
                self.txt_No_patrimonio.grid(row=1, column=1, padx=(0,10),pady=10)
                self.txt_Descricao.grid(row=1, column=3, padx=(0,10),pady=10)
                self.txt_Quantidade.grid(row=1, column=5, padx=(0,10),pady=10)
                self.txt_Localizacao.grid(row=2, column=1, padx=(0,10),pady=10)
                self.txt_No_nota_fiscal.grid(row=2, column=3, padx=(0,10),pady=10)
                self.txt_Data_aquisicao.grid(row=2, column=5, padx=(0,10),pady=10)
                self.txt_Data_saida.grid(row=3, column=1, padx=(0,10),pady=10)
                self.txt_Fornecedor.grid(row=3, column=3, padx=(0,10),pady=10)
                self.txt_Valor.grid(row=3, column=5, padx=(0,10),pady=10)
                self.txt_Grau_depreciacao.grid(row=4, column=1, padx=(0,10),pady=10)
                
                self.btn_go.grid(row=5, column=5, padx=5, pady=10, sticky='w')
                self.btn_cancel.grid(row=5, column=4, padx=5, pady=10, sticky='e')
                
                
            def Insere_item(self):
                import json
                _file = open(r'Planilhas_de_Dados\Planilha_estoque.json').read()
                df = json.loads(_file)
                No_patrimonio = self.txt_No_patrimonio.get()
                Descricao = self.txt_Descricao.get()
                Quantidade = self.txt_Quantidade.get()
                Localizacao = self.txt_Localizacao.get()
                No_nota_fiscal = self.txt_No_nota_fiscal.get()
                Data_aquisicao = self.txt_Data_aquisicao.get()
                Data_saida = self.txt_Data_saida.get()
                Fornecedor = self.txt_Fornecedor.get()
                Valor = self.txt_Valor.get()
                Grau_depreciacao = self.txt_Grau_depreciacao.get()
                
                df.append({'N do Patrimonio': No_patrimonio,'Descricao do Bem': Descricao, 'Quantidade': Quantidade,'Localizacao': Localizacao, 'N Nota Fiscal': No_nota_fiscal,'Data de Aquisicao': Data_aquisicao, 'Data  de  Saida': Data_saida,'Fornecedor': Fornecedor, 'Valor R$':Valor, 'Grau de Depreciacao': Grau_depreciacao})
                print(df[-1])
                
            # Botão Cancelar
            def Cancelar(self):
                root.destroy()
                    
        root = tk.Tk()
        New_item(root)
        root.state('normal')
        root.title('Novo item')
        root.iconbitmap(r'C:\Users\tobli\OneDrive\Área de Trabalho\Obra_Social_Estoque\Programa_Oficial\img\Plus_itens.ico')
        root.mainloop()
    
    # Função de busca por nome
    def json_find(self, data, pattern, path=()):
        import re
        if isinstance(data, (str, float, int, bool, type(None))):
            if re.findall(pattern, str(data)):
                yield data, path
        elif isinstance(data, list):
            for i, item in enumerate(data):
                yield from self.json_find(item, pattern, path=path+(i,))
    
        elif isinstance(data, dict): 
            for i, (key, value) in enumerate(data.items()):
                yield from self.json_find(value, pattern, path=path+(key,))
        else:
            raise TypeError("Can't search patterns in instances of {}".format(type(data)))
    # Função de busca por chave
    def get_json_item_at(self, data, path):
        if not path:
            return data
        return self.get_json_item_at(data[path[0]], path[1:])
    
    def Busca(self):
    # Fazendo a busca do item na lista em json
        import json
        _file = open(r'Planilhas_de_Dados\Planilha_estoque.json').read()
        file = json.loads(_file)
        busca =str(self.txt_busca.get())   # fator de pesquisa
        def Value():
            lista = list(self.json_find(file, f'{busca}'))
            return self.resultados.set(str(lista))
        s = str(Value())
        aux = 0
        for i in range(len(s)):
            if s[i].isdigit():              
                aux = aux * 10 + int(s[i])
            else:
                if aux > 0:
                    return self.resultados.set(f'\nNº do Patrimônio: {(aux+1)}')
                aux = 0
        if (aux > 0):
                return self.resultados.set(f'\nNº do Patrimônio: {(aux+1)}')
    
    
    
janela = tk.Tk()
Program(janela)
janela.state('zoomed')
janela.iconbitmap(r'C:\Users\tobli\OneDrive\Área de Trabalho\Obra_Social_Estoque\Programa_Oficial\img\LOGO.ico')
janela.title('Estoque')
janela.mainloop()
# -*- coding: utf-8 -*-
# Banco de Dados de cadastros para empréstimos de itens

import sqlite3
class DB():
    def __init__(self):
        self.conexao = sqlite3.connect('Banco_de_Usuarios.db')
        self.createTable()
    
    # Cadastro de Usuários simples
    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''create table if not exists usuarios (
                    ID integer primary key autoincrement,
                    nome text,
                    sexo text,
                    CPF text(11),
                    nascimento date,
                    telefone text,
                    email text,
                    rua text,
                    numero number,
                    bairro text,
                    cidade text,
                    UF text(2))''')
        self.conexao.commit()
        c.close()

# Codificador para a senha
def binario():
    return '1101111 1100010 1110010 1100001 1110011 1101111 1100011 1101001 1100001 1101100 '

def decode(binario):
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  # 0x101100110
        k += 1
    return string

def encode(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario
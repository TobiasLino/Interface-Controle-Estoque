# -*- coding: utf-8 -*-
# Cadastro dos usuários que poderão fazer empréstimos

from Banco import DB
class Cadastro(object):
    def __init__(self, ID=0, nome='', sexo='', CPF='', nascimento='', telefone='',email='', rua='', numero='',bairro='', cidade='', UF=''):
        # As informações são tratadas como objeto self; as mesmas são pegas da página de cadastro
        self.info = {}
        self.ID = ID
        self.nome = nome
        self.sexo = sexo
        self.CPF = CPF
        self.nascimento = nascimento
        self.telefone = telefone
        self.email = email
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.UF = UF
        
    def Inserir_usuario(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('insert into Cadastro (nome, sexo, CPF, nascimento, telefone, email, rua, numero, bairro, cidade, UF) values("'+self.nome+"', "+self.sexo+"', "+self.CPF+"', "+self.nascimento+"', "+self.telefone+"', "+self.email+"', "+self.rua+"', "+self.numero+"', "+self.bairro+"', "+self.cidade+"', "+self.UF+'")')
            banco.conexao.commit()
            c.close()
            return 'Cadastro realizado!'
        except:
            return 'Ocorreu um erro no cadastro'
        
        def Atualizar_Usuario(self):
            banco = DB()
            try:
                c = banco.conexao.cursor()
                c.execute("update Cadstro set nome = '"+self.nome+"', sexo = '"+self.sexo+"',CPF = '"+self.CPF+"', nascimento = '"+self.nascimento+"', telefone = '"+self.telefone+"', email = '"+self.email+"', rua = '"+self.rua+"', bairro = '"+self.bairro+"', cidade = '"+self.cidade+"', UF = '"+self.UF+"'where Id  = "+self.ID+"")
                banco.conexao.commit()
                c.close()
                return 'Usuário atualizado!'
            except:
                return 'Ocorreu um erro ao atualizar o Usuário'
            
            def Deletar_Usuario(self):
                banco = DB()
                try:
                    c = banco.conexao.cursor()
                    c.execute('delete from Cadastro where'+self.ID+'')
                    banco.conexao.commit()
                    c.close()
                    return 'Usuário excluído!'
                except:
                    return 'Houve um erro ao excluir o usuário'
                
            def Buscar_Usuario(self):
                banco = DB()
                try:
                    c = banco.conexao.cursor()
                    c.execute('select * from Cadastro where ID = '+self.ID+'')
                    banco.conexao.commit()
                    c.close()
                    for linha in c:
                        self.ID = linha[0]
                        self.nome = linha[1]
                        self.telefone = linha[2]
                        self.email = linha[3]
                    c.close()
                    return 'Id:'+self.ID+'Nome:'+self.nome+'Telefone'+self.telefone
                except:
                    return 'Ocorreu um erro na busca'
            
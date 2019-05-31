# -*- coding: utf-8 -*-
# teste de rolagem 


import tkinter as tk

class JanelaRolavel(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)            

        # cria um canvas e uma barra de rolagem para rolá-lo:
        rolagem = tk.Scrollbar(self, orient=tk.VERTICAL)
        rolagem.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=rolagem.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        rolagem.config(command=self.canvas.yview)

        # reseta a visão:
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # cria um frame dentro do canvas
        # para que seja rolado junto com ele:
        self.conteudo =  tk.Frame(self.canvas)
        self.id_conteudo = self.canvas.create_window(
            0, 0, window=self.conteudo, anchor=tk.NW)

        # cria eventos para detectar mudanças no canvas
        # e sincronizar com a barra de rolagem:
        self.conteudo.bind('<Configure>', self._configurar_conteudo)
        self.canvas.bind('<Configure>', self._configurar_canvas)

    def _configurar_conteudo(self, evento):
            # atualiza a barra de rolagem para o tamanho do frame de conteudo:
            tamanho = (
                self.conteudo.winfo_reqwidth(),
                self.conteudo.winfo_reqheight()
            )
            self.canvas.config(scrollregion="0 0 %s %s" % tamanho)
            if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
                # atualizar tambem a largura do canvas para caber o conteudo:
                self.canvas.config(width=self.conteudo.winfo_reqwidth())

    def _configurar_canvas(self, evento):
        if self.conteudo.winfo_reqwidth() != self.canvas.winfo_width():
            # atualizar tambem a largura do conteudo para preencher o canvas:
            self.canvas.itemconfigure(
                self.id_conteudo, width=self.canvas.winfo_width())
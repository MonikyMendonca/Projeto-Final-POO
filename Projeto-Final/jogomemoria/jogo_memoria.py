import tkinter as tk
from tkinter import messagebox
import random
from jogo_base import JogoBase

class JogoMemoria(JogoBase):
    NUM_LINHAS = 4
    NUM_COLUNAS = 4
    CARTAO_SIZE_W = 10
    CARTAO_SIZE_H = 5
    CORES_CARTAO = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink']
    FONTE_STYLE = ('Arial', 12, 'bold')
    MAX_TENTATIVAS = 25

    def __init__(self, root):
        super().__init__(root, "Jogo da Memória")
        self._grid = self._criar_grade()
        self._cartoes = []
        self._cartoes_revelados = []
        self._cartoes_correspondentes = []
        self._numero_tentativas = 0
        self._criar_interface()

    def _criar_grade(self):
        cores = self.CORES_CARTAO * 2
        random.shuffle(cores)
        return [[cores.pop() for _ in range(self.NUM_COLUNAS)] for _ in range(self.NUM_LINHAS)]

    def _criar_interface(self):
        for linha in range(self.NUM_LINHAS):
            linha_cartoes = []
            for coluna in range(self.NUM_COLUNAS):
                cartao = tk.Button(
                    self._root, 
                    command=lambda r=linha, c=coluna: self._cartao_clicado(r, c),
                    width=self.CARTAO_SIZE_W, 
                    height=self.CARTAO_SIZE_H, 
                    bg='black',
                    relief=tk.RAISED, 
                    bd=3
                )
                cartao.grid(row=linha, column=coluna, padx=5, pady=5)
                linha_cartoes.append(cartao)
            self._cartoes.append(linha_cartoes)

        self._label_tentativas = tk.Label(
            self._root, 
            text=f'Tentativas: {self._numero_tentativas}/{self.MAX_TENTATIVAS}', 
            fg='white', 
            bg="#343a40", 
            font=self.FONTE_STYLE
        )
        self._label_tentativas.grid(row=self.NUM_LINHAS, columnspan=self.NUM_COLUNAS, padx=10, pady=10)

    def _cartao_clicado(self, linha, coluna):
        cartao = self._cartoes[linha][coluna]
        if cartao['bg'] == 'black':
            cartao['bg'] = self._grid[linha][coluna]
            self._cartoes_revelados.append(cartao)

            if len(self._cartoes_revelados) == 2:
                self._verificar_par()

    def _verificar_par(self):
        cartao1, cartao2 = self._cartoes_revelados
        if cartao1['bg'] == cartao2['bg']:
            cartao1.after(1000, cartao1.destroy)
            cartao2.after(1000, cartao2.destroy)
            self._cartoes_correspondentes.extend([cartao1, cartao2])
            self._verificar_vitoria()
        else:
            cartao1.after(1000, lambda: cartao1.config(bg='black'))
            cartao2.after(1000, lambda: cartao2.config(bg='black'))

        self._cartoes_revelados.clear()
        self._atualizar_tentativas()

    def _verificar_vitoria(self):
        if len(self._cartoes_correspondentes) == self.NUM_LINHAS * self.NUM_COLUNAS:
            messagebox.showinfo('Parabéns!', 'Você ganhou o jogo!')
            self._root.quit()

    def _atualizar_tentativas(self):
        self._numero_tentativas += 1
        self._label_tentativas.config(text=f'Tentativas: {self._numero_tentativas}/{self.MAX_TENTATIVAS}')

        if self._numero_tentativas >= self.MAX_TENTATIVAS:
            messagebox.showinfo('Fim de jogo', 'Você perdeu o jogo!')
            self._root.quit()

    def iniciar(self):
        self._root.mainloop()

import tkinter as tk
from jogo_memoria import JogoMemoria

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoMemoria(root)
    jogo.iniciar()

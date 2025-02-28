import tkinter as tk

class JogoBase:
    def __init__(self, root, titulo):
        self._root = root
        self._root.title(titulo)
        self._root.configure(bg="#343a40")

    def iniciar(self):
        """Método genérico para iniciar um jogo (será sobrescrito)"""
        raise NotImplementedError("O método iniciar() deve ser implementado na classe filha")
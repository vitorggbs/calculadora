# Calculadora básica com as quatro operações.
import tkinter as tk


def calcular():
    try:
        primeiro = float(campo1.get())
        segundo = float(campo2.get())
        operacao = escolha.get()

        if operacao == "+":
            valor = primeiro + segundo
        elif operacao == "-":
            valor = primeiro - segundo
        elif operacao == "×":
            valor = primeiro * segundo
        elif operacao == "÷":
            if segundo == 0:
                resultado.config(text="Não dá para dividir por zero.")
                return
            valor = primeiro / segundo
        resultado.config(text="Resultado: " + str(valor))
    except ValueError:
        resultado.config(text="Preencha os dois campos com números.")


janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("320x300")
janela.resizable(False, False)
janela.configure(padx=20, pady=16)
tk.Label(janela, text="Calculadora", font=("Arial", 16, "bold")).pack(pady=(0, 12))
tk.Label(janela, text="Primeiro número").pack()
campo1 = tk.Entry(janela, justify="center")
campo1.pack(pady=4)
tk.Label(janela, text="Operação").pack()
escolha = tk.StringVar(value="+")
tk.OptionMenu(janela, escolha, "+", "-", "×", "÷").pack(pady=3)
tk.Label(janela, text="Segundo número").pack()
campo2 = tk.Entry(janela, justify="center")
campo2.pack(pady=4)
tk.Button(janela, text="Calcular", command=calcular).pack(pady=8)
resultado = tk.Label(janela, text="")
resultado.pack()
janela.mainloop()

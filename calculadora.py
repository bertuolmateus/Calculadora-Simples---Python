import tkinter as tk

def printar_display(valor):
    texto_atual = label["text"]
    label.config(text=texto_atual + valor)

def clear():
    label.config(text="")

def calcular():
    try:
        expressao = label["text"]
        resultado = str(eval(expressao))
        label.config(text=resultado)
    except Exception as e:
        label.config(text="Erro")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("185x300")

label = tk.Label(janela, text="")
label.grid(row=0, columnspan=7, pady=10, padx=10)

#calcular e apagar
bot_equal = tk.Button(janela, text="=", command=lambda: calcular(), width=5, height=3)
bot_equal.grid(row=8, column=2, pady=0)

bot_clear = tk.Button(janela, text="C", command=lambda: clear(), width=5, height=3)
bot_clear.grid(row=8, column=0, pady=0)

#números
bot0 = tk.Button(janela, text="0", command=lambda: printar_display("0"), width=5, height=3)
bot0.grid(row=8, column=1, pady=0)

bot7 = tk.Button(janela, text="7", command=lambda: printar_display("7"), width=5, height=3)
bot7.grid(row=5, column=0, pady=0)

bot8 = tk.Button(janela, text="8", command=lambda: printar_display("8"), width=5, height=3)
bot8.grid(row=5, column=1, pady=0)

bot9 = tk.Button(janela, text="9", command=lambda: printar_display("9"), width=5, height=3)
bot9.grid(row=5, column=2, pady=0)

bot4 = tk.Button(janela, text="4", command=lambda: printar_display("4"), width=5, height=3)
bot4.grid(row=6, column=0, pady=0)

bot5 = tk.Button(janela, text="5", command=lambda: printar_display("5"), width=5, height=3)
bot5.grid(row=6, column=1, pady=0)

bot6 = tk.Button(janela, text="6", command=lambda: printar_display("5"), width=5, height=3)
bot6.grid(row=6, column=2, pady=0)

bot1 = tk.Button(janela, text="1", command=lambda: printar_display("1"), width=5, height=3)
bot1.grid(row=7, column=0, pady=0)

bot2 = tk.Button(janela, text="2", command=lambda: printar_display("2"), width=5, height=3)
bot2.grid(row=7, column=1, pady=0)

bot3 = tk.Button(janela, text="3", command=lambda: printar_display("3"), width=5, height=3)
bot3.grid(row=7, column=2, pady=0)

#operadores
bot_mais = tk.Button(janela, text="+", command=lambda: printar_display("+"), width=5, height=3)
bot_mais.grid(row=8, column=3, pady=0)

bot_menos = tk.Button(janela, text="-", command=lambda: printar_display("-"), width=5, height=3)
bot_menos.grid(row=7, column=3, pady=0)

bot_vezes = tk.Button(janela, text="*", command=lambda: printar_display("*"), width=5, height=3)
bot_vezes.grid(row=6, column=3, pady=0)

bot_dividir = tk.Button(janela, text="/", command=lambda: printar_display("/"), width=5, height=3)
bot_dividir.grid(row=5, column=3, pady=0)

# Iniciar janela
janela.mainloop()
import tkinter as tk

def adicionar_caractere(event):
    caractere = event.char
    if caractere.isdigit() or caractere in "+-*/.":
        entrada_texto.insert(tk.END, caractere)
    elif event.keysym == "Return":
        calcular()
    return "break"

def calcular():
    try:
        expressao = entrada_texto.get()
        resultado = eval(expressao)
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, str(resultado))
    except Exception as e:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Erro")

def limpar():
    entrada_texto.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="#333333")  # Define a cor de fundo da janela principal

entrada_texto = tk.Entry(root, width=30, borderwidth=5, bg="#444444", fg="white")  # Cores para a entrada de texto
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entrada_texto.bind("<KeyPress>", adicionar_caractere)

botoes = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 2, 0),
    ("5", 2, 1), ("6", 2, 2), ("7", 3, 0), ("8", 3, 1),
    ("9", 3, 2), ("0", 4, 1), (".", 4, 0), ("+", 1, 3),
    ("-", 2, 3), ("*", 3, 3), ("/", 4, 3), ("=", 4, 2),
    ("%", 0, 3), ("Limpar", 0, 2)
]

for texto, linha, coluna in botoes:
    if texto == "=":
        tk.Button(root, text=texto, padx=40, pady=20, bg="#007acc", fg="white", command=calcular).grid(row=linha, column=coluna)  # Cores para o botão "="
    elif texto == "Limpar":
        tk.Button(root, text=texto, padx=40, pady=20, bg="#cc3300", fg="white", command=limpar).grid(row=linha, column=coluna)  # Cores para o botão "Limpar"
    else:
        tk.Button(root, text=texto, padx=40, pady=20, bg="#666666", fg="white", command=lambda texto=texto: entrada_texto.insert(tk.END, texto)).grid(row=linha, column=coluna)  # Cores para os outros botões

root.mainloop()

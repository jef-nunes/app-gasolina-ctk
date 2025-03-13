# Módulos para construção da interface gráfica
import customtkinter as ctk
from tkinter import messagebox

# Definir tema escuro para toda a aplicação
ctk.set_appearance_mode("dark")

# Personalizar janela da aplicação e barra de titulo
janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False,False)
janela.title("App Gasolina 2025")
janela.iconbitmap("./images/fuelpump.ico")

# Criar elementos do corpo da janela

# Título
titulo = ctk.CTkLabel(janela,
                      text="App Gasolina 2025",
                      text_color="springgreen",
                      font=("verdana",30,"bold"))

# Subtítulo
subtitulo = ctk.CTkLabel(janela,
                         text="Calcule os seus custos com gasolina",
                         text_color="seagreen",
                         font=("verdana",18,"bold"))

# Input distância percorrida em quilômetros
distancia = ctk.CTkEntry(janela, placeholder_text="Distância(Km)")

# Input consumo em litros
consumo = ctk.CTkEntry(janela, placeholder_text="Consumo(L)")

# Input preço da gasolina em reais
preco = ctk.CTkEntry(janela, placeholder_text="Preço(R$)")

# Botão para calcular o resultado
botao = ctk.CTkButton(janela, text="Calcular")

# Posicionar elementos
titulo.place(x=20,y=10)
subtitulo.place(x=20,y=50)
distancia.place(x=20,y=110)
consumo.place(x=20,y=150)
preco.place(x=20,y=190)
botao.place(x=20,y=230)

# Iniciar o loop principal da janela
janela.mainloop()

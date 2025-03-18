import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path

#---------------------------------------------------------------------------------------------------
# Personalizar janela da aplicação e barra de titulo

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False,False)
janela.title("App Gasolina 2025")

if Path("./images/fuelpump.ico").exists():
    janela.iconbitmap("./images/fuelpump.ico")
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
# Função para calcular o resultado de consumo de gasolina
def calcular_resultado():
    # Consumo (L)
    c = int(consumo_entry.get())
    # Distancia (Km)
    d = int(distancia_entry.get())
    # Preço(R$)
    p = float(preco_entry.get())
    # Fórmula
    formula = (d/c)*p
    # Exibir o resultado
    messagebox.showinfo("App Gasolina",f"O valor gasto para essa viagem será de R${round(formula, 2)}")
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
# Criar elementos do corpo da janela

# Título
titulo_label = ctk.CTkLabel(janela,
                      text="App Gasolina 2025",
                      text_color="springgreen",
                      font=("verdana",30,"bold"))

# Subtítulo
subtitulo_label = ctk.CTkLabel(janela,
                         text="Calcule os seus custos com gasolina",
                         text_color="seagreen",
                         font=("verdana",18,"bold"))

# Input distância percorrida em quilômetros
distancia_entry = ctk.CTkEntry(janela, placeholder_text="Distância(Km)")

# Input consumo em litros
consumo_entry = ctk.CTkEntry(janela, placeholder_text="Consumo(L)")

# Input preço da gasolina em reais
preco_entry = ctk.CTkEntry(janela, placeholder_text="Preço(R$)")

# Botão para calcular o resultado
calculo_button = ctk.CTkButton(janela, text="Calcular", fg_color="dimgrey", text_color="springgreen", hover_color="dimgrey", command=calcular_resultado)

#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
# Posicionar elementos
titulo_label.place(x=20,y=10)
subtitulo_label.place(x=20,y=50)
distancia_entry.place(x=20,y=110)
consumo_entry.place(x=20,y=150)
preco_entry.place(x=20,y=190)
calculo_button.place(x=20,y=230)
#---------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------
# Iniciar o loop principal da janela
janela.mainloop()
#---------------------------------------------------------------------------------------------------

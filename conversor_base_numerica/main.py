# Importando tkinter
import tkinter
from tkinter import *
from tkinter import ttk

# Cores -----------------------
cor0 = "white" # White
cor1 = "black" # Black
cor2 = "#048291" # Esverdeado claro
cor3 = '#036773' # Esverdeado medio
cor4 = '#017d77' # Esverd. medio e.
cor5 = "#02454d" # Esverd. escuro


# Configuração da janela -----------------------

janela = Tk()
janela.title('Conversor de Base Numerica')
janela.geometry('400x310')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

# Estilo ---------------------------------------
estilo = ttk.Style(janela)
estilo.theme_use('clam')
# linha separatória
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=200)

# Dividindo a janela em 2 frames ----------------

# frame cima
frame_cima = Frame(janela, width=400, height=60, pady=0, padx=0, bg=cor5)
frame_cima.grid(row=1, column=0)

# frame baixo
frame_baixo = Frame(janela, width=400, height=300, pady=12, padx=20, bg=cor4)
frame_baixo.grid(row=2, column=0, sticky=NW)

# Configuração frame cima -----------------------
app_nome = Label(frame_cima, text='Conversor de Base Numerica', relief=FLAT, anchor='center', font=('System 20'), bg=cor0, fg=cor5)
app_nome.place(x=6, y=10)


# Função converter -----------------------------------------
def converter():
    # Função para converter qualquer número em uma base,
    # para o seu correspondente em Decimal
    def numero_para_decimal(numero, base):
        # o numero decimal correspondente
        decimal = int(numero, base)

        binario = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        l_binario['text'] = str(binario[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:].upper())

    numero = e_valor.get()  
    base = combo.get()

    # Definindo o valor da base
    if base == 'BINARIO':
        base= 2
    elif base == 'OCTAL':
        base= 8
    elif base == 'DECIMAL':
        base= 10
    else:
        base= 16

    # Chamando a função
    numero_para_decimal(numero, base)

# numero a ser convertido e sua base
numero = '010111' # o zero a esquerda é ignorado
base = 2

# Configuração frame baixo -----------------------

# lista
bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
# COMBOBOX
combo = ttk.Combobox(frame_baixo, width=14, justify=CENTER, font=('Ivy 12 bold'))
# para mostrar valores
combo['values'] = (bases)
# para posicionar dentro do frame
combo.place(x=10, y=10)

# criando Entry ------------------------------------
e_valor = Entry(frame_baixo, width=12, justify='center', font=('',13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)


# Criando botão de conversão -----------------------
b_converter = Button(frame_baixo, command=converter, text='CONVERTER', relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor0, fg=cor5)
b_converter.place(x=280, y=10)


# Configuração da Label BINARIO -----------------------
l_binario = Label(frame_baixo, text='BINARIO', width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor0, fg=cor5)
l_binario.place(x=10, y=60)
# resultado BINARIO 
l_binario = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor5)
l_binario.place(x=160, y=60)

# Configuração da Label OCTAL -----------------------
l_octal = Label(frame_baixo, text='OCTAL', width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor0, fg=cor5)
l_octal.place(x=10, y=90)
# resultado OCTAL 
l_octal = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor5)
l_octal.place(x=160, y=90)

# Configuração da Label DECIMAL -----------------------
l_decimal = Label(frame_baixo, text='DECIMAL', width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor0, fg=cor5)
l_decimal.place(x=10, y=120)
# resultado DECIMAL
l_decimal = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor5)
l_decimal.place(x=160, y=120)

# Configuração da Label HEXADECIMAL -----------------------
l_hexadecimal = Label(frame_baixo, text='HEXADECIMAL', width=12, relief=FLAT, anchor='nw', font=('Verdana 13'), bg=cor0, fg=cor5)
l_hexadecimal.place(x=10, y=150)
# resultado HEXADECIMAL -----------------------
l_hexadecimal = Label(frame_baixo, text='', width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=cor5)
l_hexadecimal.place(x=160, y=150)

janela.mainloop()
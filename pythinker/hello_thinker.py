import tkinter as tk

# Instanciar a janela
janela = tk.Tk()

janela.title("Primeiro App")

janela.geometry("300x100+20+20")


# Criar e posicionar um label com a mensagem 
lblMsg = tk.Label(janela,text="hello world!")
# Gerenciador de geometria
lblMsg.pack()

# Exibir a janela
janela.mainloop()
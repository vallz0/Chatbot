import tkinter as tk
from Levenshtein import distance as levenshtein_distance
import re

respostas:dict = {
    'teste1': '[Chatbot] teste2'
}
def encontrar_melhor_resposta(mensagem, respostas):

    melhor_resposta = 'desculpe, nao entendi'
    melhor_pontuacao = 0

    for pergunta, resposta in respostas.items():
        palavras_pergunta = set(re.findall(r'\b\w+\b', pergunta.lower()))

        palavras_mensagem = set(re.findall(r'\b\w+\b', mensagem.lower()))

        pontuacao = len(palavras_pergunta.intersection(palavras_mensagem))

        if pontuacao >  melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_resposta = resposta
    return melhor_resposta

def enviar_mensagem():
    mensagem = entrada.get()

    if not mensagem:
        return

    canvas.create_text(790, canvas.y, text=mensagem, font=('Arial', 20),anchor='e', tags='text', fill='blue')
    canvas.y += 30

    resposta = encontrar_melhor_resposta(mensagem, respostas)

    canvas.create_text(20, canvas.y, text=resposta, font=('Arial', 20), anchor='w', tags='text', fill='green')

    canvas.y += 30
    entrada.delete(0, tk.END)

janela = tk.Tk()

janela.title('Chatbot')

canvas = tk.Canvas(janela,
                   bg='white',
                   width=500,
                   height=400)

canvas.pack(expand=tk.YES, fill=tk.BOTH)
canvas.y = 30

entrada = tk.Entry(janela,font=('Arial 20'), width=50)

entrada.pack(side=tk.LEFT, padx=10, pady=10)

btn_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)

btn_enviar.pack(side=tk.RIGHT, padx=10, pady=10)

janela.mainloop()

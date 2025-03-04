import customtkinter as ctk
from datetime import datetime

class ChatGPTUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ChatGPT - CustomTKinter")
        self.geometry("630x600")
        
        self.chat_frame = ctk.CTkTextbox(self, width=550, height=450, wrap="word")
        self.chat_frame.grid(row=0, column=0, padx=10, pady=20, columnspan=2)
        self.chat_frame.configure(state="disabled")
        
        # Campo de entrada de texto
        self.entry = ctk.CTkEntry(self, width=450, placeholder_text="Digite sua mensagem...")
        self.entry.grid(row=1, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)  # Enviar ao pressionar Enter
        
        # Botão de envio
        self.send_button = ctk.CTkButton(self, text="Enviar", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
    
    def send_message(self, event=None):
        user_message = self.entry.get().strip()
        if user_message:
            self.update_chat("Você", user_message)
            response = self.generate_fake_response(user_message)
            self.update_chat("ChatGPT", response)
            self.entry.delete(0, 'end')
    
    def update_chat(self, sender, message):
        self.chat_frame.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_frame.insert("end", f"{timestamp} {sender}: {message}\n\n")
        self.chat_frame.configure(state="disabled")
        self.chat_frame.yview_moveto(1)
    
    def generate_fake_response(self, message):
        responses = [
            "Isso é muito interessante! Pode me contar mais?",
            "Ótima pergunta! O que você acha disso?",
            "Eu concordo com você. Quer discutir mais sobre isso?",
            "Não tenho certeza, mas podemos descobrir juntos!",
            "Hmm, nunca pensei nisso dessa forma."
        ]
        import random
        return random.choice(responses)


def main():
    ctk.set_appearance_mode("Dark") 
    ctk.set_default_color_theme("blue") 
    
    app = ChatGPTUI()
    app.mainloop()
    
if __name__ == "__main__":
    main()

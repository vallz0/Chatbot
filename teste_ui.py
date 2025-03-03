import customtkinter


app = customtkinter.CTk()
app.geometry("900x700")
app.title("Chatbot")

app.resizable(False,False)

left_frame = customtkinter.CTkFrame(app, width=80,height=700, fg_color="#1E1E1E")
left_frame.pack(side='left', fill='y')

center_frame = customtkinter.CTkFrame(app, width=700,height=500)
center_frame.place(relx=0.543, rely=0.4, anchor="center")

bottom_frame = customtkinter.CTkFrame(app, width=700,height=105, fg_color="#4f4f4f")
bottom_frame.pack(side='bottom', fill='y', pady=30)

text_entry = customtkinter.CTkEntry(bottom_frame, width=550, height=95,
                                    fg_color='transparent', border_width=0)
text_entry.pack(side='left', padx=10, pady=10)

send_button = customtkinter.CTkButton(bottom_frame, text=".",width=50,height=50, corner_radius=100)
send_button.pack(side='right', padx=10, pady=10)

app.mainloop()

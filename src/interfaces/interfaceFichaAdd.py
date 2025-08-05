import datetime
import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox

# Janela principal
root = tk.Tk()
root.title("FICHA ADMISSIONAL   - MUSICOTERAPIA")
root.geometry("800x900")

# Frame com rolagem
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

form_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor="nw")



# Função para criar entradas
def criar_linha(label_text, row):
    tk.Label(form_frame, text=label_text, anchor="w").grid(row=row, column=0, sticky="w", pady=3)
    entry = tk.Entry(form_frame, width=100)
    entry.grid(row=row, column=1, pady=3, padx=5)
    return entry

def criar_texto(label_text, row):
    tk.Label(form_frame, text=label_text, anchor="w").grid(row=row, column=0, sticky="w", pady=3)
    text = tk.Text(form_frame, width=75, height=2)
    text.grid(row=row, column=1, pady=3, padx=5)
    return text




def formatar_data(data):
    valor = data.get()

    numeros = re.sub(r'\D', '', valor)  # Remove tudo que não é dígito

    if len(numeros) == 8:  # Formato DDMMYYYY
        data_formatada = f"{numeros[:2]}/{numeros[2:4]}/{numeros[4:]}"
        data.delete(0, tk.END)
        data.insert(0, data_formatada)

        try:
            dia = int(numeros[:2])
            mes = int(numeros[2:4])
            ano = int(numeros[4:])
            hoje = datetime.date.today()
            nascimento = datetime.date(ano, mes, dia)
            idade_valor = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            idade.delete(0, tk.END)
            idade.insert(0, str(idade_valor))

        except ValueError:
            data.delete(0, tk.END)
            idade.delete(0, tk.END)
            idade.insert(0, "")
            messagebox.showerror("Erro", "Data inválida. Verifique o dia, mês e ano.")
            



    elif valor:
        messagebox.showerror("Erro", "Formato de data inválido. Use DDMMYYYY.")    



# Cabeçalho
tk.Label(form_frame, text="Dados do Paciente", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

nome = criar_linha("Nome do Paciente:", 1)
data_admissao = criar_linha("Data de Admissão:", 2)
data_nasc = criar_linha("Data de Nascimento:", 3)  
data_nasc.bind("<FocusOut>", lambda e: formatar_data(data_nasc))  # Formata data dd/mm/yyyy ao perder o foco
idade = criar_linha("Idade Cronológica:", 4)
escola = criar_linha("Escola:", 5)
endereco = criar_linha("Endereço:", 6)
responsavel = criar_linha("Responsável:", 7)
contato = criar_linha("Contato:", 8)


# Referências Musicais
tk.Label(form_frame, text="REFERÊNCIAS MUSICAIS", font=("Arial", 12, "bold"), bg="lightblue").grid(row=9, column=0, columnspan=2, pady=10, sticky="we")

q1 = criar_texto("1 - Quais as preferências/recusas musicais/sonoras dos responsáveis?", 10)
q2 = criar_texto("2 - Quais/Como foram as vivências musicais/sonoras durante a gestação?", 11)
q3 = criar_texto("3 - Quais/Como foram as primeiras vivências musicais/sonoras pós nascimento?", 12)
q4 = criar_texto("4 - Quais as preferências/recusas musicais/sonoras da criança?", 13)
q5 = criar_texto("5 - Possui experiência musical? (em musicalização ou musicoterapia)", 14)
q6 = criar_texto("6 - Possui familiares musicistas?", 15)
q7 = criar_texto("7 - Possui instrumentos musicais em casa?", 16)
q8 = criar_texto("8 - Como “mais” se envolve musicalmente? (cantando, tocando, dançando, ouvindo, improvisando, outros)", 17)

# ----------------------------
# Referências Gerais
tk.Label(form_frame, text="REFERÊNCIAS GERAIS", font=("Arial", 12, "bold"), bg="lightblue").grid(row=18, column=0, columnspan=2, pady=10, sticky="we")

q9 = criar_texto("9 - Possui alguma deficiência ou doença? Alguma hiper ou hipossensibilidade?", 19)
q10 = criar_texto("10 - Faz uso de algum medicamento?", 20)
q11 = criar_texto("11 - Possui algum tipo de alergia?", 21)
q12 = criar_texto("12 - Possui alguma dificuldade motora, social, comunicativa, cognitiva, emocional ou outra?", 22)
q13 = criar_texto("13 - Realiza intervenções/acompanhamentos/terapias?", 23)
q14 = criar_texto("14 - Possui algum hiperfoco?", 24)

# ----------------------------
# Botão de salvar
def salvar():
    print("Dados coletados:")
    print("Nome:", nome.get())
    print("Preferências musicais responsáveis:", q1.get("1.0", tk.END))

tk.Button(form_frame, text="Salvar", command=salvar, bg="lightgreen").grid(row=25, column=0, columnspan=2, pady=20)

root.mainloop()

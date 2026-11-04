import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

# --- Configurações ---
DATA_FILE = "dados_presencas.json"

# --- Funções de dados ---
def carregar_dados():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"alunos": [], "aulas": [], "presencas": {}}

def salvar_dados():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- Funções principais ---
def adicionar_aluno():
    nome = simpledialog.askstring("Adicionar Aluno", "Nome do aluno:")
    if nome:
        if nome not in dados["alunos"]:
            dados["alunos"].append(nome)
            salvar_dados()
            atualizar_listas()
        else:
            messagebox.showwarning("Atenção", "Aluno já existe!")

def remover_aluno():
    selecionado = lista_alunos.curselection()
    if selecionado:
        nome = lista_alunos.get(selecionado)
        if messagebox.askyesno("Confirmar", f"Remover aluno {nome}?"):
            dados["alunos"].remove(nome)
            dados["presencas"].pop(nome, None)
            salvar_dados()
            atualizar_listas()

def adicionar_aula():
    aula = simpledialog.askstring("Adicionar Aula", "Nome da aula (ex: 10/11/2025):")
    if aula:
        if aula not in dados["aulas"]:
            dados["aulas"].append(aula)
            salvar_dados()
            atualizar_listas()
        else:
            messagebox.showwarning("Atenção", "Aula já existe!")

def remover_aula():
    selecionado = lista_aulas.curselection()
    if selecionado:
        aula = lista_aulas.get(selecionado)
        if messagebox.askyesno("Confirmar", f"Remover aula {aula}?"):
            dados["aulas"].remove(aula)
            for aluno in dados["presencas"].values():
                aluno.pop(aula, None)
            salvar_dados()
            atualizar_listas()

def marcar_presenca():
    aluno_sel = lista_alunos.curselection()
    aula_sel = lista_aulas.curselection()
    if aluno_sel and aula_sel:
        aluno = lista_alunos.get(aluno_sel)
        aula = lista_aulas.get(aula_sel)

        if aluno not in dados["presencas"]:
            dados["presencas"][aluno] = {}

        atual = dados["presencas"][aluno].get(aula, False)
        dados["presencas"][aluno][aula] = not atual
        salvar_dados()
        atualizar_tabela_presencas()
    else:
        messagebox.showinfo("Info", "Selecione um aluno e uma aula.")

def atualizar_tabela_presencas(*args):
    for i in tabela.get_children():
        tabela.delete(i)

    aluno_sel = lista_alunos.curselection()
    if not aluno_sel:
        return

    aluno = lista_alunos.get(aluno_sel)
    label_aluno.config(text=f"Aluno: {aluno}")

    for aula in dados["aulas"]:
        presente = dados["presencas"].get(aluno, {}).get(aula, False)
        tabela.insert("", "end", values=(aula, "✅ Presente" if presente else "❌ Ausente"))

def atualizar_listas():
    lista_alunos.delete(0, tk.END)
    for a in dados["alunos"]:
        lista_alunos.insert(tk.END, a)

    lista_aulas.delete(0, tk.END)
    for a in dados["aulas"]:
        lista_aulas.insert(tk.END, a)

    atualizar_tabela_presencas()

# --- Interface gráfica ---
dados = carregar_dados()
root = tk.Tk()
root.title("📋 Controle de Presenças")
root.geometry("900x500")
root.config(bg="#1e1e1e")

style = ttk.Style(root)
style.theme_use("clam")

# --- Estilo Dark ---
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#2d2d2d", foreground="white", font=("Segoe UI", 10), padding=6)
style.map("TButton", background=[("active", "#3a3a3a")])
style.configure("Treeview", background="#2d2d2d", fieldbackground="#2d2d2d", foreground="white", font=("Segoe UI", 10))
style.configure("Treeview.Heading", background="#3a3a3a", foreground="white", font=("Segoe UI", 10, "bold"))

# --- Frames principais ---
frame_alunos = tk.Frame(root, bg="#1e1e1e")
frame_alunos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_aulas = tk.Frame(root, bg="#1e1e1e")
frame_aulas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

frame_presencas = tk.Frame(root, bg="#1e1e1e")
frame_presencas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# --- Alunos ---
ttk.Label(frame_alunos, text="👨‍🎓 Alunos").pack()
lista_alunos = tk.Listbox(frame_alunos, exportselection=False, bg="#2d2d2d", fg="white", selectbackground="#4a4a4a")
lista_alunos.pack(fill=tk.BOTH, expand=True, pady=5)
ttk.Button(frame_alunos, text="Adicionar", command=adicionar_aluno).pack(fill=tk.X)
ttk.Button(frame_alunos, text="Remover", command=remover_aluno).pack(fill=tk.X)

# --- Aulas ---
ttk.Label(frame_aulas, text="📅 Aulas").pack()
lista_aulas = tk.Listbox(frame_aulas, exportselection=False, bg="#2d2d2d", fg="white", selectbackground="#4a4a4a")
lista_aulas.pack(fill=tk.BOTH, expand=True, pady=5)
ttk.Button(frame_aulas, text="Adicionar", command=adicionar_aula).pack(fill=tk.X)
ttk.Button(frame_aulas, text="Remover", command=remover_aula).pack(fill=tk.X)

# --- Presenças ---
ttk.Label(frame_presencas, text="📖 Registro de Presenças").pack()
label_aluno = ttk.Label(frame_presencas, text="Aluno: —")
label_aluno.pack(pady=5)

tabela = ttk.Treeview(frame_presencas, columns=("Aula", "Status"), show="headings", height=12)
tabela.heading("Aula", text="Aula")
tabela.heading("Status", text="Presença")
tabela.column("Aula", width=120)
tabela.column("Status", width=120)
tabela.pack(fill=tk.BOTH, expand=True)

ttk.Button(frame_presencas, text="✅ Marcar / ❌ Desmarcar", command=marcar_presenca).pack(pady=10)

# --- Eventos ---
lista_alunos.bind("<<ListboxSelect>>", atualizar_tabela_presencas)
lista_aulas.bind("<<ListboxSelect>>", atualizar_tabela_presencas)

atualizar_listas()
root.mainloop()







# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 03:12:05 2026

@author: hp
"""

import customtkinter as ctk
from tkinter import messagebox
import time
import random

# إعدادات المظهر (Dark Mode)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

lang_data = {
    "AR": {"title": "حجرة ورقة مقص", "p1": "لاعب 1", "p2": "لاعب 2", "ready": "اختر سلاحك!", "win": "ربح!", "draw": "تعادل!", "final": "الفائز النهائي:", "rock": "حجرة", "paper": "ورقة", "scissors": "مقص"},
    "FR": {"title": "PIERRE-FEUILLE-CISEAUX", "p1": "Joueur 1", "p2": "Joueur 2", "ready": "Choisissez !", "win": "a gagné !", "draw": "Égalité !", "final": "Gagnant final :", "rock": "Pierre", "paper": "Feuille", "scissors": "Ciseaux"},
    "EN": {"title": "ROCK-PAPER-SCISSORS", "p1": "Player 1", "p2": "Player 2", "ready": "Pick weapon!", "win": "wins!", "draw": "Draw!", "final": "Final Winner:", "rock": "Rock", "paper": "Paper", "scissors": "Scissors"}
}

current_lang = "AR"
p1_choice, p2_choice = "", ""
p1_score, p2_score, manches = 0, 0, 0

def change_lang(l):
    global current_lang
    current_lang = l
    refresh_ui()

def refresh_ui():
    d = lang_data[current_lang]
    title_label.configure(text=d["title"])
    p1_label.configure(text=name1_entry.get() if name1_entry.get() != "" else d["p1"])
    p2_label.configure(text=name2_entry.get() if name2_entry.get() != "" else d["p2"])
    result_label.configure(text=d["ready"])
    for i, txt in enumerate([d["rock"], d["paper"], d["scissors"]]):
        btns_p1[i].configure(text=txt)
        btns_p2[i].configure(text=txt)

def select_choice(player, idx):
    global p1_choice, p2_choice
    choices = ["🪨", "📄", "✂️"]
    if player == 1: p1_choice = choices[idx]
    if player == 2: p2_choice = choices[idx]
    if p1_choice != "" and p2_choice != "": calculate_result()

def calculate_result():
    global p1_score, p2_score, manches, p1_choice, p2_choice
    d = lang_data[current_lang]
    for i in ["3...", "2...", "1...", "GO!"]:
        result_label.configure(text=i, text_color="#f1c40f")
        root.update(); time.sleep(0.4)
    
    n1 = name1_entry.get() if name1_entry.get() != "" else d["p1"]
    n2 = name2_entry.get() if name2_entry.get() != "" else d["p2"]

    if p1_choice == p2_choice: res_text = d["draw"]
    elif (p1_choice == "🪨" and p2_choice == "✂️") or (p1_choice == "📄" and p2_choice == "🪨") or (p1_choice == "✂️" and p2_choice == "📄"):
        res_text = f"{n1} {d['win']}"; p1_score += 1
    else: res_text = f"{n2} {d['win']}"; p2_score += 1
    
    manches += 1
    score_label.configure(text=f"{p1_score}  -  {p2_score}")
    result_label.configure(text=f"{p1_choice} VS {p2_choice}\n{res_text}", text_color="#2ecc71")
    p1_choice, p2_choice = "", ""
    if manches == 5:
        fw = n1 if p1_score > p2_score else n2
        messagebox.showinfo(d["title"], f"{d['final']} {fw}")
        reset_game()

def reset_game():
    global p1_score, p2_score, manches
    p1_score, p2_score, manches = 0, 0, 0
    score_label.configure(text="0  -  0")
    refresh_ui()

# الواجهة
root = ctk.CTk()
root.geometry("600x750")
root.title("PRO RPS App")

# إطار اللغات (أزرار دائرية)
lang_frame = ctk.CTkFrame(root, fg_color="transparent")
lang_frame.pack(pady=20)
for l in ["AR", "FR", "EN"]:
    ctk.CTkButton(lang_frame, text=l, width=60, corner_radius=20, command=lambda lang=l: change_lang(lang)).pack(side="left", padx=5)

title_label = ctk.CTkLabel(root, text="", font=("Arial", 28, "bold"), text_color="#e74c3c")
title_label.pack(pady=10)

# الأسماء (خانات جذابة)
names_frame = ctk.CTkFrame(root, fg_color="transparent")
names_frame.pack()
name1_entry = ctk.CTkEntry(names_frame, placeholder_text="Player 1", width=150, corner_radius=10)
name1_entry.pack(side="left", padx=15)
name2_entry = ctk.CTkEntry(names_frame, placeholder_text="Player 2", width=150, corner_radius=10)
name2_entry.pack(side="left", padx=15)

area = ctk.CTkFrame(root, fg_color="transparent")
area.pack(pady=40)

btns_p1, btns_p2 = [], []
# اللاعب 1
f1 = ctk.CTkFrame(area, fg_color="transparent")
f1.pack(side="left", padx=30)
p1_label = ctk.CTkLabel(f1, text="", font=("Arial", 14, "bold"))
p1_label.pack(pady=10)
for i in range(3):
    btn = ctk.CTkButton(f1, text="", width=120, height=45, corner_radius=15, fg_color="#3498db", command=lambda x=i: select_choice(1, x))
    btn.pack(pady=5); btns_p1.append(btn)

# اللاعب 2
f2 = ctk.CTkFrame(area, fg_color="transparent")
f2.pack(side="right", padx=30)
p2_label = ctk.CTkLabel(f2, text="", font=("Arial", 14, "bold"))
p2_label.pack(pady=10)
for i in range(3):
    btn = ctk.CTkButton(f2, text="", width=120, height=45, corner_radius=15, fg_color="#e67e22", command=lambda x=i: select_choice(2, x))
    btn.pack(pady=5); btns_p2.append(btn)

score_label = ctk.CTkLabel(root, text="0  -  0", font=("Arial", 50, "bold"), text_color="#f1c40f")
score_label.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 18, "bold"))
result_label.pack(pady=20)

refresh_ui()
root.mainloop()
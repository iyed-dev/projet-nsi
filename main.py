import customtkinter
import customtkinter as ctk
import json
import time
import random
import os
import datetime
from fpdf import FPDF


def charger_menu():
    with open('bdd.json', 'r', encoding="utf-8") as f: 
        data = json.load(f)
    categories = {}
    for categorie in data["menu"]:
        categories[categorie["category"]] = categorie["items"]
    return categories

panier = {}
liste_order = []

def commands_number():
    if liste_order != []:
        liste_order.append(liste_order[-1]+1)
        return liste_order[-1]+1
    elif liste_order == []:
        print("vide")
        liste_order.append(0)
    print(liste_order)
    return liste_order


def vider_panier(): 
    panier.clear() #clear du panier
    afficher_panier()

def afficher_panier():
    total = 0
    panier_string = "Votre panier: "
    
    for plat_name, info in panier.items():
        panier_string += f"{plat_name} - {info['quantity']} x {info['price']}€\n" # =+ c'est addition
        total += info['quantity'] * info['price']
    panier_label.configure(text=panier_string)
    total_label.configure(text=f"Total: {total}€")

def ajouter_au_panier(plat, entry):
    x = datetime.datetime.now()
    horaire = x.strftime("%c")
    table_number = entry.get()
    if plat['name'] in panier:
        panier[plat['name']]['quantity'] += 1 #ajout d'un truc si il est déjà la genre en x1 x2 x3 etc.
    else:
        panier[plat['name']] = {"price": plat['price'], "quantity": 1, "table_number": table_number, "Date, Heure": horaire, "Statut": state} #l'ajoute si il n'est pas la 
    afficher_panier()
    return panier
    return table_number

app = customtkinter.CTk()
app.geometry("1080x1920")
app.title("Restaurant - Menu")


state = "En cours..."

def toggle_status():
    global state, statut_btn
    state = "Livré" if state == "En cours..." else "En cours..."  #changement des status
    statut_btn.configure(text=state)
    return state



menu_categories = charger_menu()

panier_frame = customtkinter.CTkFrame(app)
panier_frame.pack(side="right", padx=10, pady=10, fill="y")

categories_frame = customtkinter.CTkFrame(app)
categories_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

def valider():
    with open("fichier.json", "w") as f:
        json.dump(panier, f, ensure_ascii=False, indent=4)

edit_button = customtkinter.CTkButton(panier_frame, text="Vider le panier", command=vider_panier)
edit_button.pack(pady=5, fill="x")

total_label = customtkinter.CTkLabel(panier_frame, text="Total: 0€", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

panier_label = customtkinter.CTkLabel(panier_frame, text="Votre panier:\n", font=("Arial", 12))
panier_label.pack(pady=10)

statut_btn = customtkinter.CTkButton(panier_frame, text=state, command=toggle_status)
statut_btn.pack(padx=20, pady=20)

button = customtkinter.CTkButton(panier_frame, text="Valider", command=valider)
button.pack(padx=20, pady=20)

entry = ctk.CTkEntry(panier_frame, placeholder_text="Entrez le numéro de table...")
entry.pack(padx=20, pady=20)

for categorie, plats in menu_categories.items():
    label = customtkinter.CTkLabel(categories_frame, text=categorie, font=("Arial", 16, "bold"))
    label.pack(pady=5, anchor="w")
    
    for plat in plats:
        button = customtkinter.CTkButton(categories_frame, text=f"{plat['name']} - {plat['price']}€", 
        command=lambda p=plat,entry=entry: ajouter_au_panier(p, entry))
        button.pack(pady=5, anchor="w")


def print_bill():
    liste = commands_number()
    
    table_number = entry.get()
    with open("fichier.json", "r") as file:
        data = json.load(file)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=10)

    pdf.cell(200, 10, "TICKET DE CAISSE", ln=True, align="C")
    pdf.cell(200, 10, f"TABLE : {table_number}", ln=True, align="C")
    pdf.cell(200, 10, f"Numéro : {liste}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=8, style='B')
    pdf.cell(200, 10, "----------------------------------------", ln=True, align="C")
    pdf.ln(5)

    def add_json_to_pdf(json_data, pdf_obj):
        total_global = 0
        for item_name, details in json_data.items():
            pdf_obj.set_font("Arial", size=10, style='B')
            pdf_obj.cell(100, 8, item_name, border=0, ln=False)
            
            pdf_obj.set_font("Arial", size=10)
            pdf_obj.cell(30, 8, f"{details['quantity']} x {details['price']}E", border=0, ln=False)

            total_price = details['quantity'] * details['price']
            pdf_obj.cell(40, 8, f"{total_price:.2f}E", border=0, ln=True)
            
            total_global += total_price
        
        pdf_obj.set_font("Arial", size=8, style='B')
        pdf_obj.cell(200, 10, "----------------------------------------", ln=True, align="C")
        pdf.ln(5)

        pdf_obj.set_font("Arial", size=10, style='B')
        pdf_obj.cell(100, 8, "TOTAL", border=0, ln=False)
        pdf_obj.set_font("Arial", size=10)
        pdf_obj.cell(40, 8, f"{total_global:.2f}E", border=0, ln=True)

        pdf_obj.ln(10)
        pdf_obj.set_font("Arial", size=8)
        pdf_obj.cell(200, 8, f"Commandé à : {details['Date, Heure']}", ln=True)

    add_json_to_pdf(data, pdf)

    pdf.output("ticketdecaisse.pdf")

bill = customtkinter.CTkButton(panier_frame, text="Print Bill", command=print_bill)
bill.pack(padx=20, pady=20)

def edit_items():
    print("test")


app.mainloop()
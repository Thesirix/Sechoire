import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import math
import os
import sys
import pygame


COULEUR_FOND = "#e6f7ff" 
COULEUR_BORDURE = "#80bfff"
COULEUR_BOUTON = "#0078D7" 
COULEUR_BOUTON_SURVOL = "#005A9E"

MOIS_FR = ["", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def formater_date_francais(date_obj):
    return f"{date_obj.day} {MOIS_FR[date_obj.month]} {date_obj.year}"

def calculer_semaines(poids_initial, poids_final, pourcentage_perte=0.01):
    return math.ceil(math.log(poids_final / poids_initial) / math.log(1 - pourcentage_perte))

def calculer_date_debut(date_butoir, semaines):
    jours = semaines * 7
    date_debut = date_butoir - timedelta(days=jours)
    return date_debut

def dessiner_rectangle_arrondi(canvas, x1, y1, x2, y2, rayon, tag, couleur_fond, couleur_bordure):
    canvas.create_oval(x1, y1, x1+2*rayon, y1+2*rayon, tags=tag, fill=couleur_fond, outline="")
    canvas.create_oval(x2-2*rayon, y1, x2, y1+2*rayon, tags=tag, fill=couleur_fond, outline="")
    canvas.create_oval(x1, y2-2*rayon, x1+2*rayon, y2, tags=tag, fill=couleur_fond, outline="")
    canvas.create_oval(x2-2*rayon, y2-2*rayon, x2, y2, tags=tag, fill=couleur_fond, outline="")
    canvas.create_rectangle(x1+rayon, y1, x2-rayon, y2, tags=tag, fill=couleur_fond, outline="")
    canvas.create_rectangle(x1, y1+rayon, x2, y2-rayon, tags=tag, fill=couleur_fond, outline="")
    
    epaisseur = 2
    canvas.create_arc(x1, y1, x1+2*rayon, y1+2*rayon, start=90, extent=90, style=tk.ARC, outline=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_arc(x2-2*rayon, y1, x2, y1+2*rayon, start=0, extent=90, style=tk.ARC, outline=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_arc(x2-2*rayon, y2-2*rayon, x2, y2, start=270, extent=90, style=tk.ARC, outline=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_arc(x1, y2-2*rayon, x1+2*rayon, y2, start=180, extent=90, style=tk.ARC, outline=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_line(x1+rayon, y1, x2-rayon, y1, fill=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_line(x1+rayon, y2, x2-rayon, y2, fill=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_line(x1, y1+rayon, x1, y2-rayon, fill=couleur_bordure, width=epaisseur, tags=tag)
    canvas.create_line(x2, y1+rayon, x2, y2-rayon, fill=couleur_bordure, width=epaisseur, tags=tag)

def afficher_resultats():
    try:
        poids_initial = float(entry_poids_actuel.get())
        poids_final = float(entry_poids_cible.get())

        text_resultat.config(state=tk.NORMAL)
        text_resultat.delete(1.0, tk.END)

        if poids_initial <= poids_final:
            text_resultat.insert(tk.END, "Erreur : Le poids actuel doit être\nsupérieur au poids cible pour une sèche.", ("center", "highlight_red"))
        else:
            today = datetime.today()
            semaines = calculer_semaines(poids_initial, poids_final)
            
         
            perte_totale = poids_final - poids_initial
            
      
            date_butoir = datetime(today.year, 6, 21)
            date_debut = calculer_date_debut(date_butoir, semaines)

            # 2. TANT QUE la date de début est dans le passé, on repousse l'objectif d'un an
            while date_debut < today:
                date_butoir = datetime(date_butoir.year + 1, 6, 21)
                date_debut = calculer_date_debut(date_butoir, semaines)

            # Affichage de l'objectif avec la perte entre parenthèses
            text_resultat.insert(tk.END, "Objectif : ", "center")
            text_resultat.insert(tk.END, f"{poids_final:g} kg ({perte_totale:g} kg)\n", ("center", "highlight_blue"))
            
            text_resultat.insert(tk.END, "Temps nécessaire : ", "center")
            text_resultat.insert(tk.END, f"{semaines} semaines\n\n", ("center", "highlight_red"))
            
            text_resultat.insert(tk.END, "Pour une sèche ", "center")
            text_resultat.insert(tk.END, "PARFAITE", ("center", "rouge_gras"))
            text_resultat.insert(tk.END, " commencez le : \n", "center")
            text_resultat.insert(tk.END, f"{formater_date_francais(date_debut)}\n\n", ("center", "highlight_green"))
            
            text_resultat.insert(tk.END, "Objectif atteint le : ", "center")
            text_resultat.insert(tk.END, f"{formater_date_francais(date_butoir)}", ("center", "highlight_blue"))
            
            text_resultat.insert(tk.END, " 💪\n", ("center", "emoji"))

            text_resultat.insert(tk.END, "( Basé sur -1% du poids total par semaine)", ("center", "small"))

        text_resultat.config(state=tk.DISABLED)
        
        text_resultat.place(x=0, y=0) 
        reposition_widgets()
        
    except ValueError:
        text_resultat.config(state=tk.NORMAL)
        text_resultat.delete(1.0, tk.END)
        text_resultat.insert(tk.END, "Erreur : Veuillez entrer des chiffres valides.", ("center", "highlight_red"))
        text_resultat.config(state=tk.DISABLED)
        
        text_resultat.place(x=0, y=0)
        reposition_widgets()

def resize_bg(event):
    new_width = root.winfo_width()
    new_height = root.winfo_height()

    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig(bg_image_id, image=bg_image)
    canvas.image = bg_image  

    reposition_widgets()

def reposition_widgets():
    window_width = root.winfo_width()
    cx = window_width // 2

    canvas.delete("bg_shapes")

    dessiner_rectangle_arrondi(canvas, cx - 220, 90, cx - 10, 130, 15, "bg_shapes", COULEUR_FOND, COULEUR_BORDURE)
    label_poids_actuel.place(x=cx - 210, y=96)
    
    dessiner_rectangle_arrondi(canvas, cx + 10, 90, cx + 120, 130, 15, "bg_shapes", "white", COULEUR_BORDURE)
    entry_poids_actuel.place(x=cx + 20, y=98, width=90, height=26)

    dessiner_rectangle_arrondi(canvas, cx - 220, 140, cx - 10, 180, 15, "bg_shapes", COULEUR_FOND, COULEUR_BORDURE)
    label_poids_cible.place(x=cx - 210, y=146)
    
    dessiner_rectangle_arrondi(canvas, cx + 10, 140, cx + 120, 180, 15, "bg_shapes", "white", COULEUR_BORDURE)
    entry_poids_cible.place(x=cx + 20, y=148, width=90, height=26)

    button_calculer.place(x=cx - 60, y=200, width=120, height=40)

    contenu = text_resultat.get("1.0", "end-1c")
    if len(contenu) > 0:
        if "Erreur" in contenu:
            dessiner_rectangle_arrondi(canvas, cx - 250, 260, cx + 250, 360, 20, "bg_shapes", COULEUR_FOND, COULEUR_BORDURE)
            text_resultat.place(x=cx - 240, y=285, width=480, height=60)
        else:
            dessiner_rectangle_arrondi(canvas, cx - 250, 260, cx + 250, 480, 20, "bg_shapes", COULEUR_FOND, COULEUR_BORDURE)
            text_resultat.place(x=cx - 240, y=270, width=480, height=200)
    else:
        text_resultat.place_forget()

root = tk.Tk()
root.title("Séchoire")

window_width = 800
window_height = 510
root.geometry(f"{window_width}x{window_height}")

image_path = resource_path("summer.webp")
try:
    image = Image.open(image_path)
except FileNotFoundError:
    image = Image.new('RGB', (800, 510), color = (73, 109, 137))

canvas = tk.Canvas(root, highlightthickness=0)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

resized_image = image.resize((window_width, window_height), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(resized_image)
bg_image_id = canvas.create_image(0, 0, anchor="nw", image=bg_image)
canvas.image = bg_image 

font_large = ("Arial", 14, "bold")

label_poids_actuel = tk.Label(root, text="Poids actuel (kg) :", bg=COULEUR_FOND, font=font_large, bd=0)
entry_poids_actuel = tk.Entry(root, font=font_large, width=10, relief="flat", bg="white", bd=0, highlightthickness=0)

label_poids_cible = tk.Label(root, text="Poids cible (kg) :", bg=COULEUR_FOND, font=font_large, bd=0)
entry_poids_cible = tk.Entry(root, font=font_large, width=10, relief="flat", bg="white", bd=0, highlightthickness=0)

button_calculer = tk.Button(root, text="Calculer", command=afficher_resultats, font=font_large, 
                            bg=COULEUR_BOUTON, fg="white", activebackground=COULEUR_BOUTON_SURVOL, 
                            activeforeground="white", relief="flat", bd=0, cursor="hand2")

text_resultat = tk.Text(root, font=font_large, bg=COULEUR_FOND, bd=0, highlightthickness=0, wrap="word")

text_resultat.tag_configure("center", justify='center')
text_resultat.tag_configure("highlight_blue", foreground="#0056b3")
text_resultat.tag_configure("highlight_red", foreground="#d9534f", font=("Arial", 14, "bold"))
text_resultat.tag_configure("highlight_green", foreground="#28a745", font=("Arial", 14, "bold"))
text_resultat.tag_configure("rouge_gras", foreground="red", font=("Arial", 14, "bold"))
text_resultat.tag_configure("emoji", font=("Segoe UI Emoji", 14), justify='center')
text_resultat.tag_configure("small", font=("Arial", 11, "italic"), justify='center')

reposition_widgets()

root.bind("<Configure>", resize_bg)
resize_bg(None)

try:
    pygame.mixer.init()
    pygame.mixer.music.load(resource_path("scarface.wav"))
    pygame.mixer.music.play(-1)  
except:
    pass 

root.mainloop()
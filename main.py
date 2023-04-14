from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import random
from time import strftime
from PIL import ImageTk, Image
import os


class SuperMarche:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Super Marche")
        self.root.geometry("1920x1040+0+0")

     # CREATION DU TITRE ////////////////////////////////////////////////////////////////////////////////////////////////

        title = Label(self.root, text="Auchan", font=(
            "Algerian", 35), bg="red", fg="white")
        title.pack(side=TOP, fill=X)

        # CREATION DU L'heure sur le côté de l'application
        def heure():
            heur = strftime("%H:%M:%S")
            lblheure.config(text=heur)
            lblheure.after(1000, heure)

        lblheure = Label(self.root, text="HH:MM:SS", font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        lblheure.place(x=0, y=10, width=120, height=45)

        heure()
# //////////////////////////////////////// Toutes nos variables ////////////////////////////////////////////////////////

        self.c_nom = StringVar()
        self.c_phon = StringVar()

        self.n_factu = StringVar()
        z = random.randint(1000, 9999)
        self.n_factu.set(z)

        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = IntVar
        self.qte = IntVar()
        self.totalbrute = StringVar()
        self.totalnet = StringVar()

   # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

   # //////////////////////////////////// CREATION DE CATEGORIE //////////////////////////////////////////////////////

    # frame Principale

        Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        Main_Frame.place(x=23, y=70, width=1320, height=920)

    # frame client
        client_frame = LabelFrame(Main_Frame, text="Nos Clients", font=(
            "times new roman", 15), bg="white")
        client_frame.place(x=19, y=5, width=450, height=150)

        self.lbl_conctact = Label(client_frame, text="Téléphone :", font=(
            "times new roman", 15, "bold"), bg="white")
        self.lbl_conctact.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_nomclient = Label(client_frame, text="Nom :", font=(
            "times new roman", 15, "bold"), bg="white")
        self.lbl_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_email = Label(client_frame, text="Mail :", font=(
            "times new roman", 15, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.txt_contact = ttk.Entry(
            client_frame, font=("times new roman", 15))
        self.txt_contact.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.txt_nomclient = ttk.Entry(
            client_frame, font=("times new roman", 15))
        self.txt_nomclient.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.txt_email = ttk.Entry(client_frame, font=("times new roman", 15))
        self.txt_email.grid(row=2, column=1, sticky=W, padx=5, pady=2)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


if __name__ == "__main__":
    root = Tk()
    obj = SuperMarche(root)
    root.mainloop()

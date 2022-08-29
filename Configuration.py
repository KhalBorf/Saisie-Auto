import configparser
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from pynput import keyboard
import pyautogui as sy
import ast

sy.PAUSE = 0
from Coordonnées import CoordonnéesEcran
CE = CoordonnéesEcran
path = 'Q:/SYLOB/10 - Saisie auto/autosais V05/configurations55.ini'
profile = [
    'Khalil']
choix2 = [
    '0']
la_posi = [
    0,
    0]
liste = list(CE.dictio.keys())

def lecture_clique():
    with keyboard.Events() as events:
        event = events.get(6)
        if format(event) == 'Press(key=Key.esc)' or format(event) == 'Release(key=Key.esc)':
            la_posi = sy.position()
            return la_posi[0], la_posi[1]

def fenetre_charger():
    config = read_config()
    profiles_noms = config.sections()
    fenetre(profiles_noms, 'charger')


def fenetre_supprimer():
    config = read_config()
    profiles_noms = config.sections()
    fenetre(profiles_noms, 'supprimer')


fenetre_ajouter = lambda : fenetre(liste, 'ajouter')

def fenetre(langs, le_type):
    root = tk.Tk()
    root.geometry('200x100')
    root.resizable(False, False)
    root.title('Listbox')
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight = 1)
    langs_var = tk.StringVar(value = langs)
    listbox = tk.Listbox(root, listvariable = langs_var, height = 6, selectmode = 'browse')
    listbox.grid(column = 0, row = 0, sticky = 'nwes')
    scrollbar = ttk.Scrollbar(root, orient = 'vertical', command = listbox.yview)
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.grid(column = 1, row = 0, sticky = 'ns')

    def instruction(titre, msg):
        showinfo(title = titre, message = msg)


    def event_handler(event):
        selected_indices = listbox.curselection()
        selected_langs = ",".join([ listbox.get(i) for i in selected_indices])

        def charger_la_config():
            profile[0] = selected_langs
            instruction('Information', f'Vous avez selectioné: {selected_langs}')


        def supprimer_la_config():
            profile[0] = selected_langs
            instruction('Information', f'Vous avez selectioné: {selected_langs}')


        def ajouter_une_config():
            choix2[0] = selected_langs

            def compcx(linstruction = None):
                instruction('Information', linstruction)
                jouter = lecture_clique()
                instruction('Instructions', f'Coordonées: {jouter}')
                return (jouter[0], jouter[1])

            CE.dictio[choix2[0]][0] = compcx(CE.dictio[choix2[0]][1])

        if le_type == 'ajouter':
            ajouter_une_config()
        if le_type == 'charger':
            charger_la_config()
        if le_type == 'supprimer':
            supprimer_la_config()

    listbox.bind('<<ListboxSelect>>', event_handler)
    root.mainloop()


def lire_config():
    config = read_config()
    if config.has_section(profile[0]):
        for clé in liste:
            input = config[profile[0]][clé]
            input = input.strip('[(')
            input = input.strip('[')
            input = input.strip(']]').split('),')
            CE.dictio[clé] = input
            CE.dictio[clé][0] = ast.literal_eval(CE.dictio[clé][0])
    else:
        sy.confirm(text = 'Vous n\'avez selectioné aucune configuration', title = 'Erreur', buttons = ['ok'])


def read_config():
    config = configparser.ConfigParser()
    config.read(path)
    return config


def create_config():
    config = read_config()
    config[profile[0]] = CE.dictio
    save_config(config)


def supprimer_config():
    config = read_config()
    config.remove_section(profile[0])
    save_config(config)


def save_config(config):
    with open(path, "w") as file_object:
        config.write(file_object)


def config_choix(sta, choix1):
    choix1 = '0'
    if choix1 == '0':
        choix1 = sy.confirm(text = 'Veuillez faire un choix', title = 'Demarage', buttons = [
            'Suivant',
            'Charger une config',
            'Ajouter une config',
            'Supprimer une config'])
    if choix1 == 'Charger une config':
        fenetre_charger()
        lire_config()
        choix1 = '0'
    elif choix1 == 'Supprimer une config':
        fenetre_supprimer()
        if sy.confirm(text = 'Etes vous sure de vouloir supprimer la configuration', title = 'Confirmation', buttons = [
            'Oui',
            'Annuler']) == 'Oui':
            supprimer_config()
        choix1 = '0'
    elif choix1 == 'Ajouter une config':
        fenetre_ajouter()
        choix1 = sy.confirm(text = 'Veuillez faire un choix', title = 'Confirmation', buttons = [
            'Enregistrer',
            'Annuler',
            'Modifier'])
        if choix1 == 'Enregistrer':
            profile[0] = sy.prompt(text = 'Veuillez nommer la configuration', title = 'Configuration', defualt = '')
            create_config()
            choix1 = '0'
        elif choix1 == 'Modifier':
            choix1 = 'Ajouter une config'
        else:
            choix1 = '0'
    elif choix1 == 'Suivant':
        return
    config_choix(0, '0')



class Configu:

    def execute(cls):
        config_choix(0, '0')
        return CE.dictio
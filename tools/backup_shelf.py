'''
Authors: 
    Elise Vidal
    email: evidal@artfx.fr
    Angele Sionneau
    email: asionneau@artfx.fr
date: january 2023

[Backup Shelf]
This script create a backup of the choosen shelf in a folder ".old". 
This folder is stored at the same location os the shelf.
_______________________________________
[Backup Shelf]
Ce script crée une sauvegarde du shelf demandé dans un dossier ".old".
Le dossier ".old" est stocké au même endroit que le shelf.
'''

import hou
import os
from datetime import datetime
import shutil

def get_shelf_name():
    index = 0
    infos = []
    name = None
    text = "Wich shelf do you want to backup?"
    while index == 0 :
        infos = hou.ui.readInput(message=text, buttons=("OK", "Close"),close_choice=1, default_choice=1)
        name = infos[1].strip()
        index = infos[0]
        print(f"index = {index}")
        print(f"infos = {infos}")
        if index == 0:
            if len(name) <= 0:
                hou.ui.displayMessage("Please enter a shelf name")
            elif is_shelf_exists(name) == False:
                hou.ui.displayMessage(f"The shelf [{name}] doesn't exist.")
            else:
                index = 1000
    return name

def is_shelf_exists(name):
    shelf = None
    try:
        shelf = hou.shelves.shelves()[name]
        return True
    except KeyError:
        return False

def backup(name):
    '''Copies the current shelf to a backup location on disk.'''
    shelf = hou.shelves.shelves()[name]
    shelf_path = shelf.filePath()
    shelf_file_name = os.path.basename(shelf_path)
    new_shelf_name = datetime.now().strftime('%d-%m-%y_%H-%M')+"_"+shelf_file_name
    shelf_dir = os.path.dirname(shelf_path)
    backup_dir = shelf_dir + '/.old'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    backup = backup_dir+ "/" +new_shelf_name
    shutil.copy(shelf_path, backup)

name = get_shelf_name()
if name is not "":
    backup(name)
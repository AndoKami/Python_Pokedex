import tkinter as tk
from io import BytesIO

import PIL.Image
import PIL.ImageTk
import pypokedex
import urllib3

# create app window
window = tk.Tk()
window.geometry("500x700")
window.configure(bg='#fa6666')
window.title("Python Pokédex")
window.config(padx=10, pady=10)
window.resizable(False, False)  # This disables the user from resizing the window
title_label = tk.Label(window, text="PYkedex")
title_label.config(font=("Ariel", 32))
title_label.config(background="#fa6666")
title_label.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]).title())
    # Divide Height and Weights by 10 for accurate values vis Bulbapedia
    pokemon_height.config(text=f"{pokemon.height / 10}" + " m")
    pokemon_weight.config(text=f"{pokemon.weight / 10}" + " kilograms")


#load pokémon images and other attributes
# Utilisation de la fonction pour créer les étiquettes
def create_label(parent, text="", font=("Arial", 15), background="#fa6666", padx=10, pady=10):
    label = tk.Label(parent)
    label.config(text=text, font=font, background=background)
    label.pack(padx=padx, pady=pady)
    return label


pokemon_image = create_label(window)
pokemon_information = create_label(window)
pokemon_name = create_label(window)
pokemon_types = create_label(window)
pokemon_height = create_label(window)
pokemon_weight = create_label(window)

# Function to load Pokémon
label_id_name = tk.Label(window, text=" Enter ID or Name: ")
label_id_name.config(font=("Arial", 20), background="#fa6666")
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Search...", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop(0)

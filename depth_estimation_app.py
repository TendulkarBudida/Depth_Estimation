from transformers import pipeline
from PIL import Image
import requests
import tkinter as tk
from tkinter import filedialog
import sys
import os

import matplotlib.pyplot as plt

# Create a Tkinter window
window = tk.Tk()
window.geometry("300x300")

# Function to open file dialog and get the image file path
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        process_image(file_path)

# Function to process the selected image
def process_image(file_path):
    # Load the pipeline
    pipe = pipeline(task="depth-estimation", model="LiheYoung/depth-anything-small-hf")

    # Load the image
    image = Image.open(file_path)

    # Inference
    depth = pipe(image)["depth"]

    # Display the depth map
    plt.imshow(depth, cmap=cmap)
    plt.colorbar()
    plt.title("Depth Map")
    plt.axis('off')
    plt.show()

# Create a button to open the file dialog
# Create a drop-down list to select cmap
cmap_label = tk.Label(window, text="Select cmap:")
cmap_label.pack()

cmap_var = tk.StringVar(window)
cmap_var.set("jet")  # Set default cmap

def update_cmap(*args):
    global cmap
    cmap = cmap_var.get()

cmap_var.trace("w", update_cmap)

cmap_dropdown = tk.OptionMenu(window, cmap_var, "jet", "viridis", "plasma", "inferno", "magma", "cividis", "Greys", "Blues", "Greens", "Oranges", "Reds")
cmap_dropdown.pack()

# Call update_cmap initially to set the initial value of cmap
update_cmap()

# Create a button to open the file dialog
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

# Center the button in the window
window.update()
button_width = open_button.winfo_width()
button_height = open_button.winfo_height()
window_width = window.winfo_width()
window_height = window.winfo_height()
x = (window_width - button_width) // 2
y = (window_height - button_height) // 2
open_button.place(x=x, y=y)

# Run the Tkinter event loop
window.mainloop()
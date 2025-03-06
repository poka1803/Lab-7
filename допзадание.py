import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def load_fox_image():
    response = requests.get("https://randomfox.ca/floof/")
    if response.status_code == 200:
        data = response.json()
        image_url = data["image"]
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_data = image_response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((400, 300), Image.Resampling.LANCZOS) 
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo  
        else:
            print("Ошибка загрузки изображения")
    else:
        print("Ошибка запроса к API")

root = tk.Tk()
root.title("Генератор картинок с лисами")
root.geometry("450x400")  

image_label = ttk.Label(root)
image_label.pack(pady=20)

button = ttk.Button(root, text="Другое фото", command=load_fox_image)
button.pack(pady=10)
load_fox_image()
root.mainloop()
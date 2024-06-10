import tkinter as tk
from tkinter import *
import qrcode
from tkinter import PhotoImage
from PIL import Image, ImageTk

# QR Code Configuration
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

def rgb_to_tk_color(rgb):
    # Convert an RGB tuple to a tkinter-compatible color code
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

# Define RGB colors
fg_rgb = (4, 17, 67)
bg_rgb = (153, 217, 234)
qrbg=(237,232,245)
qrfg=(4,17,67)

# Convert RGB colors to Tkinter-compatible colors
fg_color = rgb_to_tk_color(fg_rgb)
bg_color = rgb_to_tk_color(bg_rgb)
qrfg_color=rgb_to_tk_color(qrfg)
qrbg_color=rgb_to_tk_color(qrbg)

# Global variables to hold Entry widgets
input1 = None
input2 = None

def click():
    global input1, input2
    value1 = input1.get()
    value2 = input2.get()
    
    # Generate QR code
    qr.add_data(value1)
    qr.make(fit=True)
    
    # Generate the image
    img = qr.make_image(fill_color=(qrfg_color), back_color=(qrbg_color))
    full_filename = f"{value2}.png"
    img.save(full_filename)
    l3=Label(root,text=f"Your file is saved as {full_filename} in your Directory",fg=fg_color,bg=bg_color)
    l3.place(x=(y1//2)+225, y=(x1//2)+220)
    

def qrcode_fun():
    global input1, input2
    input_q = Label(root, text="Enter any text or valid Link", fg=fg_color,bg=bg_color)
    input_q.place(x=(y1//2)+225, y=(x1//2)+25)
    input1 = Entry(root, width=90, fg=fg_color)
    input1.place(x=(y1//2)+225, y=(x1//2)+50)
    input_q2 = Label(root, text="Enter FileName to be saved", fg=fg_color,bg=bg_color)
    input_q2.place(x=(y1//2)+225, y=(x1//2)+75)
    input2 = Entry(root, width=90, fg=fg_color)
    input2.place(x=(y1//2)+225, y=(x1//2)+100)
    button1 = Button(root, text="Submit", command=click, fg=fg_color)
    button1.place(x=(y1//2)+720, y=(x1//2)+150)

root = tk.Tk()
root.title("QrCode Generator")
# Load the background image
background_image = Image.open("finalbg.png")

# Resize the image as needed
desired_width = root.winfo_screenwidth()  # Set the desired width
desired_height = root.winfo_screenheight()  # Set the desired height
background_image = background_image.resize((desired_width, desired_height), Image.BICUBIC)

# Convert the resized image to PhotoImage
background_photo = ImageTk.PhotoImage(background_image)

# Create a label with the resized background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

l1 = Label(root, text="Welcome to QR Code Generator!!!", fg=fg_color,bg=bg_color, font=("Brush Script MT", 30))
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x1 = screen_width//2
y1 = screen_height//2
l1.place(x=(y1//2)+225, y=(x1//2)-100)
b1 = Button(root, text="Create QR Code", command=qrcode_fun, fg=fg_color, bg=bg_color)
b1.place(x=(y1//2)+425, y=(x1//2)-20)

root.mainloop()

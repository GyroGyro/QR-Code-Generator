import os
import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_folder = "QR Codes"
    if not os.path.exists(qr_folder):
        os.makedirs(qr_folder)
    
    qr_path = os.path.join(qr_folder, file_name)
    img.save(qr_path, 'PNG')

def on_generate_button_click():
    link = link_entry.get()
    file_name = file_name_entry.get()+".png"

    if link and file_name:
        generate_qr_code(link, file_name)
        result_label.config(text=f"QR Code generated and saved as {file_name}")
    else:
        result_label.config(text="Enter link and file name!")

# [✔] 🠗 Create the main window 🠗 
root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg='#122b49')

# [✔] 🠗 Create and place widgets 🠗 
frame = tk.Frame(root, padx=20, pady=20, bg='#122b49', relief=tk.RIDGE, bd=2)  
frame.pack(padx=10, pady=10)

link_label = tk.Label(frame, text="Enter the link:", font=("Arial", 12), bg='#122b49', fg='white')  
link_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

link_entry = tk.Entry(frame, width=40, font=("Arial", 12), relief=tk.GROOVE, bd=4)
link_entry.grid(row=1, column=0, columnspan=2, pady=(0, 10))

file_name_label = tk.Label(frame, text="Enter the file name:", font=("Arial", 12), bg='#122b49', fg='white')
file_name_label.grid(row=2, column=0, sticky="w", pady=(0, 5))

file_name_entry = tk.Entry(frame, width=40, font=("Arial", 12), relief=tk.GROOVE, bd=4)
file_name_entry.grid(row=3, column=0, pady=(0, 10))

generate_button = tk.Button(frame, text="Generate QR Code", command=on_generate_button_click, font=("Arial", 14, "bold"), bg="#459bfa", fg="white")
generate_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

result_label = tk.Label(frame, text="", font=("Arial", 12), fg="#459bfa", bg='#122b49', pady=10)
result_label.grid(row=5, column=0, columnspan=2)

# [✔] 🠗 Credits 🠗 
author_name_label = tk.Label(frame, text="Author: ~Gყɾσ", font=("Arial", 10), bg='#122b49', fg='white')
author_name_label.grid(row=7, column=0, columnspan=2, sticky="se")

# [✔] 🠗 Start the event loop 🠗 
root.mainloop()

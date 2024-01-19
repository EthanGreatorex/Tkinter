import tkinter as tk
import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Variables
WIDTH = 1300
HEIGHT = 800
TEXT_FRAME_COLOUR = '#16181c'
SIDE_BAR_COLOUR = '#26292f'
BUTTON_COLOUR = '#393e49'
BUTTON_HOVER_COLOUR = '#3c414d'

# Functions
def open_file(text_area):
  filepath = askopenfilename(filetypes=[("Text Files","*.txt")])

  if not filepath:
    return
  
  text_area.delete(1.0,ctk.END)
  with open(filepath,'r',encoding="utf-8") as f:
    content = f.read()
    text_area.insert(ctk.END, content)

def save_file(text_area):
  filepath = asksaveasfilename(filetypes=[("Text FIles,","*.txt")])

  if not filepath:
    return
  
  with open(filepath, "w",encoding="utf-8") as f:
    content = text_area.get(1.0, tk.END)
    f.write(content)

def clear_file(text_area):
  text_area.delete(1.0,tk.END)  

def slider_event(event):
  text_area.configure(font=("Helvitica",event))


# Create the app
app = ctk.CTk()
app.title("Text Editor")  

# App configurations
app_width = WIDTH
app_height = HEIGHT
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_position = (screen_width - app_width) // 2
y_position = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
app.configure(fg_color=SIDE_BAR_COLOUR)

app.rowconfigure(0, weight=1)  # Top row
app.rowconfigure(1, weight=1)  # Bottom row
app.columnconfigure(1, weight=1)  # Column 1

# Create the top sidebar
side_barT_frame = ctk.CTkFrame(master=app, fg_color=SIDE_BAR_COLOUR, height=130)
side_barT_frame.grid(row=0, column=1, sticky="nsew")

# Create elements for our top sidebar
font_size_slider = ctk.CTkSlider(master=side_barT_frame,width=500,height=20, from_=8, to=100, command=slider_event)
font_size_slider.set(20)
font_size_slider.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Create the left sidebar
side_barL_frame = ctk.CTkFrame(master=app, fg_color=SIDE_BAR_COLOUR, width=120, height=HEIGHT)  # Adjust the height
side_barL_frame.grid(row=1, column=0, sticky="ns")

# Create elements for our left sidebar
open_file_button = ctk.CTkButton(master=side_barL_frame,text="+",font=("Helvitica",40),fg_color=BUTTON_COLOUR, hover_color=BUTTON_HOVER_COLOUR,width=60,command=lambda: open_file(text_area))
open_file_button.place(rely=0.1,relx=0.5,anchor=ctk.CENTER)

save_file_button = ctk.CTkButton(master=side_barL_frame,text="💾",font=("Helvitica",40),fg_color=BUTTON_COLOUR, hover_color=BUTTON_HOVER_COLOUR,width=60,command=lambda: save_file(text_area))
save_file_button.place(rely=0.3,relx=0.5,anchor=ctk.CENTER)

clear_file_button = ctk.CTkButton(master=side_barL_frame,text="-",font=("Helvitica",40),fg_color=BUTTON_COLOUR, hover_color=BUTTON_HOVER_COLOUR,width=60,command=lambda: clear_file(text_area))
clear_file_button.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Create the text frame
text_frame = ctk.CTkFrame(master=app, fg_color=TEXT_FRAME_COLOUR)
text_frame.grid(row=1, column=1, sticky="nsew")

# Create text area for our text frame
text_area = ctk.CTkTextbox(master=text_frame,fg_color=TEXT_FRAME_COLOUR,width=WIDTH-120, height=HEIGHT-130,font=("Helvitica",20))
text_area.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Keep the app running
app.mainloop()

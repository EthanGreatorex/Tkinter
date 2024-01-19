# Password generator app using tkinter/customtkinter

# Imports
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from numpy import random

# Variables
current_layout = None
TEXT_FRAME_COLOUR = '#16181c'
SIDE_BAR_COLOUR = '#26292f'
BUTTON_COLOUR = '#393e49'
BUTTON_HOVER_COLOUR = '#3c414d'

# Functions
def show_layout(layout):
    global current_layout
    # Hide the current layout
    current_layout.grid_forget()

    # Show the new layout
    layout.grid(row=0, column=1, sticky="nsew")

    # Update the current layout
    current_layout = layout

def generate_password():
  if include_numbers == "Yes" and include_symbols == "Yes":
    type_choice = ["l","n","s"] # Letter | number | symbol
  elif include_numbers == "Yes" and include_symbols == "No":
     type_choice = ["l","n"]
  elif include_numbers == "No" and include_symbols == "Yes":
     type_choice = ["l","s"]
  else:
     type_choice = ["l"]
  letters = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
  numbers = "0123456789"
  symbols = "!@#$%&*?"

  password = ''

  for char in range(int(password_length)):
    type = random.choice(type_choice) # Get a random char type
    if type == "l":
      random_letter_index = random.randint(0,25)
      random_letter = letters[random_letter_index]
      random_case = random.randint(0,10)
      if random_case >= 5:
         random_letter = random_letter.lower()
      password += random_letter
    elif type == "n":
       random_number_index = random.randint(0,8)
       random_number = numbers[random_number_index]
       password += random_number
    elif type == "s":
       random_symbol_index = random.randint(0,7)
       random_symbol = symbols[random_symbol_index]
       password += random_symbol
  
  home_password_output.configure(text=password)
  copy_to_clipboard(password)


def update_password(value):
   global password_length
   password_length = value

def update_do_numbers(value):
   global include_numbers
   include_numbers = value

def update_do_symbols(value):
   global include_symbols
   include_symbols = value
  
def copy_to_clipboard(password):
  home_generate_password_button.configure(text="Copied!")
  home_generate_password_button.update()
  app.after(2000, lambda: home_generate_password_button.configure(text="Create"))

  app.clipboard_clear()
  app.clipboard_append(password)
  app.update()

# Create the basis of the app
app = ctk.CTk()
app.title("Password creator")
app.geometry('1200x900')


# Configure the rows and columns
app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=2)  # Adjust the weight for the side_bar column

# Create a theme for the app
app.configure(fg_color=SIDE_BAR_COLOUR)
ctk.set_appearance_mode("Dark")

# FRAMES

# Settings page frame

# Settings variables
password_length = "8"
include_numbers = "Yes"
include_symbols = "Yes"

settings_page_frame = ctk.CTkFrame(master=app, fg_color=TEXT_FRAME_COLOUR)
settings_page_frame.grid(row=0, column=1, sticky="nsew")
settings_page_frame.grid_forget()  # Hide the frame initially

# Settings page frame widgets
settings_header_label = ctk.CTkLabel(master=settings_page_frame, text="Settings", font=('', 40))
settings_header_label.place(rely=0.05, relx=0.10, anchor=ctk.CENTER)

settings_done_button = ctk.CTkButton(master=settings_page_frame, text="Done", command=lambda: show_layout(home_page_frame))
settings_done_button.place(rely=0.947, relx=0.9, anchor=ctk.CENTER)

settings_password_lengthMsg = ctk.CTkLabel(master=settings_page_frame,text="Password length",font=("",20))
settings_password_lengthMsg.place(rely=0.2,relx=0.15,anchor=ctk.CENTER)

settings_password_lengthOpt = ctk.CTkOptionMenu(master=settings_page_frame, values=["1","2","3","4","5","6","7","8","9","10"],dropdown_fg_color="#171717",command=update_password)
settings_password_lengthOpt.set("8")
settings_password_lengthOpt.place(rely=0.25,relx=0.15,anchor=ctk.CENTER)

settings_password_incNumbersMsg = ctk.CTkLabel(master=settings_page_frame, text="Include numbers in password",font=("",20))
settings_password_incNumbersMsg.place(rely=0.35,relx=0.15,anchor=ctk.CENTER)

settings_password_incNumbersOpt = ctk.CTkOptionMenu(master=settings_page_frame,values=["Yes","No"], dropdown_fg_color='#171717', command=update_do_numbers)
settings_password_incNumbersOpt.set("Yes")
settings_password_incNumbersOpt.place(rely=0.40,relx=0.15,anchor=ctk.CENTER)

settings_password_incSymbolsMsg = ctk.CTkLabel(master=settings_page_frame,text="Include symbols in password",font=("",20))
settings_password_incSymbolsMsg.place(rely=0.50,relx=0.15,anchor=ctk.CENTER)

settings_password_incSymbolsOpt = ctk.CTkOptionMenu(master=settings_page_frame, values=["Yes","No"], dropdown_fg_color='#171717', command=update_do_symbols)
settings_password_incSymbolsOpt.set("Yes")
settings_password_incSymbolsOpt.place(rely=0.55,relx=0.15,anchor=ctk.CENTER)


# Home page frame
home_page_frame = ctk.CTkFrame(master=app,fg_color=TEXT_FRAME_COLOUR)
home_page_frame.grid(row=0, column=1, sticky="nsew")

# Home page frame widgets
home_header = ctk.CTkLabel(master=home_page_frame,text="Password Creator",font=("",45))
home_header.place(rely=0.08,relx=0.5,anchor=ctk.CENTER)

home_password_output = ctk.CTkLabel(master=home_page_frame, text="",font=("",35),fg_color="#0d0d0d", width=500,corner_radius=10)
home_password_output.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

home_generate_password_button = ctk.CTkButton(master=home_page_frame, text="Create",font=("",35),command=generate_password)
home_generate_password_button.place(rely=0.6,relx=0.5,anchor=ctk.CENTER)

# Create a side bar for options
side_bar = ctk.CTkFrame(master=app, fg_color=SIDE_BAR_COLOUR)
side_bar.grid(row=0, column=0, sticky="ns")

# Load an image using PhotoImage
lock_icon_image_path = 'images/lockIcon.png'
lock_icon_image = Image.open(lock_icon_image_path)

# Create a CTkImage instance
lock_icon_ctk_image = ctk.CTkImage(dark_image=lock_icon_image, light_image=lock_icon_image, size=(200,200))
lock_icon_label = ctk.CTkLabel(master=side_bar, image=lock_icon_ctk_image,text=None)
lock_icon_label.place(rely=0.1, relx=0.5, anchor=ctk.CENTER)

# Create settings button to show the settings frame
locate_settings_button = ctk.CTkButton(master=side_bar, text="Settings", command=lambda: show_layout(settings_page_frame))
locate_settings_button.place(rely=0.95, relx=0.5, anchor=ctk.CENTER)

# Set the current layout variable to home
current_layout = home_page_frame

# Keep the app running
app.mainloop()

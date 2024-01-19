import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import subprocess

# Variables
WIDTH = 800
HEIGHT = 800
BACKGROUND_COLOUR = '#16181c'
FRAME_COLOUR = '#26292f'
BUTTON_COLOUR = '#3c414d'

# Functions

def close_app():
    global app
    app.destroy()

def open_app(appChoice):
  if appChoice == "countdown":
    file_path = "HIDDEN"
    subprocess.run(["start","",file_path],shell=True)
    # After we have opened the app close the app hub
    close_app()
  elif appChoice == "textEditor":
    file_path = "HIDDEN"
    subprocess.run(["start","",file_path],shell=True)
    close_app()
  elif appChoice == "aiChat":
    file_path = "HIDDEN"
    subprocess.run(["start","",file_path],shell=True)
    close_app()
  elif appChoice == "password":
    file_path = "HIDDEN"
    subprocess.run(["start","",file_path],shell=True)
    close_app()

# Create the app
app = ctk.CTk()
app.title("App hub")

# App configurations
app_width = WIDTH
app_height = HEIGHT
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_position = (screen_width - app_width) // 2
y_position = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")
app.configure(fg_color=BACKGROUND_COLOUR)
app.overrideredirect(1)

# Create the frame for countdown-app
countdown_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FRAME_COLOUR)
countdown_frame.place(rely=0.30, relx=0.25, anchor=ctk.CENTER)

# Create an image for the countdown-app
countdown_image = Image.open('./images/stopwatch.png')
countdown_image = countdown_image.resize((150, 150), Image.LANCZOS)
countdown_image_tk = ImageTk.PhotoImage(countdown_image)

# Create a button for the countdown-app
countdown_button = ctk.CTkButton(master=countdown_frame, image=countdown_image_tk, text='', fg_color=BUTTON_COLOUR,command=lambda: open_app('countdown'))
countdown_button.place(rely=0.5, relx=0.5, anchor=ctk.CENTER)

# Create the frame for textEditor-app
textEditor_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FRAME_COLOUR)
textEditor_frame.place(rely=0.30, relx=0.75, anchor=ctk.CENTER)

# Create an image for the textEditor-app
textEditor_image = Image.open('./images/text-editor.png')
textEditor_image = textEditor_image.resize((150, 150), Image.LANCZOS)
textEditor_image_tk = ImageTk.PhotoImage(textEditor_image)

# Create a button for textEditor-app
textEditor_button = ctk.CTkButton(master=textEditor_frame, image=textEditor_image_tk, text='', fg_color=BUTTON_COLOUR,command=lambda: open_app('textEditor'))
textEditor_button.place(rely=0.5, relx=0.5, anchor=ctk.CENTER)

# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------
# Create an image for the Ai chat-app
aiChat_image = Image.open('./images/chat-gpt.png')
aiChat_image = aiChat_image.resize((150, 150), Image.LANCZOS)
aiChat_image_tk = ImageTk.PhotoImage(aiChat_image)

# Create the frame for Ai chat-app
aiChat_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FRAME_COLOUR)
aiChat_frame.place(rely=0.70, relx=0.25, anchor=ctk.CENTER)

# Create a button for Ai chat-app
aiChat_button = ctk.CTkButton(master=aiChat_frame,image=aiChat_image_tk,text='', fg_color=BUTTON_COLOUR, width=150, height=150,command=lambda: open_app('aiChat'))
aiChat_button.place(rely=0.5, relx=0.5, anchor=ctk.CENTER)

# Create an image for the  Secure password-app
password_image = Image.open('./images/lock.png')
password_image = password_image.resize((150, 150), Image.LANCZOS)
password_image_tk = ImageTk.PhotoImage(password_image)

# Create the frame for secure password-app
securePassword_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FRAME_COLOUR)
securePassword_frame.place(rely=0.70, relx=0.75, anchor=ctk.CENTER)

# Create a button for secure password-app
securePassword_button = ctk.CTkButton(master=securePassword_frame, text='',image=password_image_tk, fg_color=BUTTON_COLOUR, width=150, height=150, command=lambda: open_app('password'))
securePassword_button.place(rely=0.5, relx=0.5, anchor=ctk.CENTER)
# -----------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------

# Close the app after 20 seconds
app.after(10000, close_app)

# Keep the app running
app.mainloop()

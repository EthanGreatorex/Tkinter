# Imports
import tkinter as tk 
import customtkinter as ctk


# Variables
BG_COLOUR = "#1d2025" # For the app background
FG_COLOUR = "#273037" # Frame colour for our minutes and seconds frames
SECONDARY_COLOUR = "#1f2933" # Frame colour for our plus and minus button
ACCENT_COLOUR = "#efc9a4" # Button colour for our start button
TIME_INCREASE = 5 # Used to increase the timer

# Functions

# Function to update the timer labels
def update_timer():
  current_minutes = int(minutes_label.cget("text"))
  current_seconds = int(seconds_label.cget("text"))

  if current_minutes == 0 and current_seconds == 0:
    # Re-enable the buttons
    start_button.configure(state=ctk.NORMAL)
    minus_button.configure(state=ctk.NORMAL)
    plus_button.configure(state=ctk.NORMAL)
    return

  if current_seconds == 0:
    # Decrement minutes and set seconds to 59
    updated_minutes = current_minutes - 1
    updated_seconds = 59
  else:
    updated_minutes = current_minutes
    updated_seconds = current_seconds - 1

  minutes_label.configure(text=f"{updated_minutes:02d}")
  seconds_label.configure(text=f"{updated_seconds:02d}")
  app.after(1000, update_timer)

def start_countdown():
    # Disable all the buttons during the countdown
    start_button.configure(state=ctk.DISABLED)
    minus_button.configure(state=ctk.DISABLED)
    plus_button.configure(state=ctk.DISABLED)
    
    # Start the countdown
    update_timer()

def add_time():
  current_time = int(minutes_label.cget("text"))

  # Only update the time if the amount of minutes is less than 60
  if current_time < 60:
    updated_time = current_time + TIME_INCREASE
    minutes_label.configure(text=updated_time)
    minutes_label.update()

def decrease_time():
  current_time = int(minutes_label.cget("text"))

  # Only decrease the time if the amount of minutes is greater than 5
  if current_time > 5:
    updated_time = current_time - TIME_INCREASE
    minutes_label.configure(text=updated_time)
    minutes_label.update()




# Create the app window
app = ctk.CTk()
app.title("Countdown")
app.configure(height=600,width=600, fg_color=BG_COLOUR)
app.eval('tk::PlaceWindow . center')

# Create a Frame for the minutes
minutes_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FG_COLOUR)
minutes_frame.place(rely=0.3,relx=0.25,anchor=ctk.CENTER)
minutes_label = ctk.CTkLabel(master=minutes_frame, text="25", font=("Helvitica",100))
minutes_label.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Label for the colon between the minutes and seconds frames
seperator_label = ctk.CTkLabel(master=app, text=":", font=("Helvitica",(120)))
seperator_label.place(rely=0.3,relx=0.5,anchor=ctk.CENTER)

# Create a Frame for the seconds
seconds_frame = ctk.CTkFrame(master=app, width=250, height=250, fg_color=FG_COLOUR)
seconds_frame.place(rely=0.3,relx=0.75,anchor=ctk.CENTER)
seconds_label = ctk.CTkLabel(master=seconds_frame, text="00", font=("Helvitica",100))
seconds_label.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Create a frame for the minus button
minus_frame = ctk.CTkFrame(master=app,width=130,height=130, fg_color=FG_COLOUR)
minus_frame.place(rely=0.7,relx=0.25, anchor=ctk.CENTER)
minus_button = ctk.CTkButton(master=minus_frame, text="-",font=("Helvitica",80), width=100, height=65,fg_color=SECONDARY_COLOUR, text_color="#121212", command=decrease_time)
minus_button.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)

# Create a frame for the plus button
plus_frame = ctk.CTkFrame(master=app,width=130,height=130, fg_color=FG_COLOUR)
plus_frame.place(rely=0.7,relx=0.75, anchor=ctk.CENTER)
plus_button = ctk.CTkButton(master=plus_frame, text="+",font=("Helvitica",80), width=100, height=65, fg_color=SECONDARY_COLOUR, text_color="#121212", command=add_time)
plus_button.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)


# Create a frame for the start button
start_frame = ctk.CTkFrame(master=app,width=120,height=120, fg_color=FG_COLOUR, corner_radius=20)
start_frame.place(rely=0.7,relx=0.5, anchor=ctk.CENTER)
start_button = ctk.CTkButton(master=start_frame, text="▶", width=90, height=65,font=("Helvitica",80), fg_color=SECONDARY_COLOUR, text_color="#121212", corner_radius=10, command=start_countdown)
start_button.place(rely=0.5,relx=0.5,anchor=ctk.CENTER)


# Keep the app running
app.mainloop()

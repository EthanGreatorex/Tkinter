# We first need to import the neccessary tools for scraping
import httpx
from selectolax.parser import HTMLParser
# Import tools for our gui
import tkinter as tk
import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename


# This function is responsible for get the intial html from the webpage
def get_html(url):
  # The header is used for accessing a webpage
  headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
  resp = httpx.get(url, headers=headers,follow_redirects=True)
  # We return the html results
  return resp


# This function takes two parameters. First is the html. The second is our "selector" The selector will be something like div#messages
# or h1. The selector tells the code what html elements to look for and retrieve
def extract_text(html, sel):
  try:
    parsed_html = HTMLParser(html.text)
    # If the selector is <p> then we loop through every <p> instane in the html and return it as an array
    if sel == "p":
      return [element.text() for element in parsed_html.css(sel)]
    # If the selector is <h1> then we just return the text value. This is because we only want one <h1> element for our title.
    elif sel == "h1":
      return parsed_html.css_first(sel).text()
    # If no html under our selector could be found, we return None
  except AttributeError:
    return None

# This will format the inputted text depending on its type E.g. h1 or p
def format_text(text, type):  # E.g. if the text is h1 or p
  # Our inputted text is an array with each <p> an element
  if type == "p": 
    formatted_text = []
    # This will loop through every element inside our text array.
    for element in text:
      # Only if the element has text inside of it do we append it to our formatted text array. This is to remove and blank words there may be
      if element:
        formatted_text.append(element)
    return formatted_text
  # If the type is a header we just return the text.
  elif type == "h1":
    return text


# This function allows us the save the article as a text file
def export_to_txt(text_area):
  filepath = asksaveasfilename(filetypes=[("Text FIles,","*.txt")])

  if not filepath:
    return
  
  with open(filepath, "w", encoding="utf-8") as f:
    content = text_area.get(1.0, tk.END)
    f.write(content)

# This function will take our text and calculate an estimated reading time
def get_reading_time(text):
  total_words = 0
  for paragraph in text:
    # Split each paragraph in our text into an array of words
    words = paragraph.split()
    total_words += len(words)

  return total_words // 200 # Calculates the reading time in MINUTES




# App variables
light_mode = False

def main():
  # url = "https://www.businessinsider.com/guides/tech/what-is-a-graphics-card?r=US&IR=T"
  # url = "https://towardsdatascience.com/why-does-a-graphics-card-help-in-machine-learning-8f365593b22"
  # url = "https://www.digitaltrends.com/computing/what-is-a-cpu/"

  # This function is resonsible for calling our other functions that fetch the website data and format it
  def retrieveWebInfo(url):
    html = get_html(url)
    header = extract_text(html,"h1")
    text = extract_text(html,"p")
    header = format_text(header,"h1")
    text = format_text(text,"p")
    # We return the header and text
    return header,text

  # This function takes our header and text. The function will output the text in the corresponding areas
  def output_results(header,text):
    if len(text) < 3:
      text_area.delete("0.0",ctk.END)
      text_area.insert("0.0","Page not found :(")
    else: 
      reading_time = get_reading_time(text)
      reading_time_text.configure(text="")
      reading_time_message = f"Estimated reading time: {reading_time} minutes"
      reading_time_text.configure(text=reading_time_message)
      header_text.configure(text="")
      header_text.configure(text=header)
      text_area.delete("0.0",ctk.END)
      
      # We loop through our array of paragraphs so we can add correct spacing between them
      for paragraph in text:
        text_area.insert(ctk.END,paragraph)
        text_area.insert(ctk.END,"\n\n")

  # This is called when the "fetch" button is clicked. It will get the url the user inputted and call our retrieveWebInfo function
  def on_submit():
    url = url_input.get("0.0", ctk.END).strip()  # Remove leading/trailing whitespaces

    if url != "Paste url..." and url != "":
      header, text = retrieveWebInfo(url)
      output_results(header,text)
    
  # This function is changes our theme from light to dark mode. It uses a boolean value to check which mode is currently activated.
  def change_theme():
    global light_mode
    if light_mode:
      ctk.set_appearance_mode("Dark")
      theme_button.configure(text="🌙")
      light_mode = False
    else:
      ctk.set_appearance_mode("Light")
      theme_button.configure(text="☀️")
      light_mode = True

  # When the url input is clicked on, this function removed the text inside. E.g. the placeholder
  def clear_placeholder(event):
    url_input.delete("0.0", ctk.END)

  # This will open a dialog for the user to enter a wiki search term
  def open_wiki_search():
    wiki_dialog = ctk.CTkInputDialog(text="Enter wiki search term",title="Wiki searcher")
    wiki_input = wiki_dialog.get_input().strip()
    # We then format a url using the search term
    if wiki_input:
      wiki_url = f"https://en.wikipedia.org/wiki/{wiki_input}"
      # We call our retrieveWebInfo function with the url
      header,text = retrieveWebInfo(wiki_url)
      # This function will update the url_input to show the link for the wiki page
      url_input.delete("0.0",ctk.END)
      url_input.insert("0.0",wiki_url)
      # We call a function to output the results
      output_results(header,text)

  # Create the app
  ctk.set_appearance_mode("Dark")
  app = ctk.CTk()
  app.title("Easy Article")
  screen_width = app.winfo_screenwidth() // 2
  screen_height = app.winfo_screenheight() // 2
  app.configure(fg_color=["#ffffff","#171717"])
  app.geometry(f"{screen_width + 500}x{screen_height + 300}")


  # Create a button to change the app theme
  theme_button = ctk.CTkButton(master=app,text="🌙",command=lambda: change_theme())
  theme_button.place(rely=0.04,relx=0.07,anchor=ctk.CENTER)

  # Create the apps url input 
  url_input = ctk.CTkTextbox(master=app,height=30,width=screen_width)
  url_input.insert("0.0","Paste url...")
  url_input.place(rely=0.04,relx=0.5,anchor=ctk.CENTER)
  url_input.bind("<Button-1>", clear_placeholder)

  # Create a button to submit url
  submit_button = ctk.CTkButton(master=app,text="Fetch",command=on_submit)
  submit_button.place(rely=0.03,relx=0.93,anchor=ctk.CENTER)
  
  # Create a save button
  save_button = ctk.CTkButton(master=app,text="Save",command=lambda: export_to_txt(text_area))
  save_button.place(rely=0.075,relx=0.93,anchor=ctk.CENTER)


  # Create the apps header text area
  header_text = ctk.CTkLabel(master=app,font=('Georgia',24,"bold"),pady=30,text="",height=30)
  header_text.place(rely=0.17,relx=0.5,anchor=ctk.CENTER)

  # Create wiki search button
  wiki_button = ctk.CTkButton(master=app,text="Wiki searcher",command=open_wiki_search)
  wiki_button.place(rely=0.125,relx=0.93,anchor=ctk.CENTER)

  # Create the reading time text area
  reading_time_text = ctk.CTkLabel(master=app,font=('Georgie',18,"bold"),text="")
  reading_time_text.place(rely=0.215,relx=0.5,anchor=ctk.CENTER)

  # Create the apps text area
  text_area = ctk.CTkTextbox(master=app,font=('Georgia',20),width=screen_width + 270,height=screen_height + 150,fg_color=["#ffffff","#171717"],text_color=["#000000","#ffffff"], spacing2=10)
  text_area.place(rely=0.665,relx=0.5,anchor=ctk.CENTER)

  # Keep the app running
  app.mainloop()

# This makes sure the code will only run as a script and not an imported module
if __name__ == "__main__":
  main()
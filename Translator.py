# Libraries Imported
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from textblob import *
import pygame

# Main Configurations
root = Tk()
root.geometry("800x400")
root.title("Kunal Translator")
root.resizable(False, False)
root.configure(bg="grey")
root.iconbitmap("Translate.ico")
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 
'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 
'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

# Functions to Run
# pygame.mixer.init()
pygame.mixer.init()
def sound(event=None):
    try:
        pygame.mixer.music.load("rider.mp3")
        pygame.mixer.music.play()
        word3 = TextBlob(varname1.get())
        lan = word3.detect_language()
        lan_todict = language.get()
        lan_to = lan_dict[lan_todict]
        word3 = word3.translate(from_lang=lan, to=lan_to)
        varname2.set(word3)
    except:
        varname2.set("A Problem Has Been Occured")    
def mainexit():
    rr = messagebox.askyesnocancel('Exit Kunal Translator', 'Are You Want to Exit Kunal Translator Machine', parent= root)
    if (rr==True):
        root.destroy()

    # Binding [Hover] Functions 
def on_entry1click(e):
    entry1['bg'] = "lightblue"
def on_entry1leave(e):
    entry1['bg'] = "lightgreen"

def on_click(e):
    btn1['bg'] =  "green"
    btn1['foreground'] =  "black"
def on_leave(e):
    btn1['bg'] =  "pink"
    btn1['foreground'] =  "red" 
def on_2click(e):
    btn2['bg'] =  "black"  
    btn2['foreground'] =  "blue"  
def on_2leave(e):
    btn2['bg'] =  "red" 
    btn2['foreground'] =  "white"   

# Combo Box

language = StringVar()
font_box = Combobox(root, width=30, textvariable = language, state="readonly")
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=130, y=147)
# Title Of My Program
label1 = Label(root,foreground="aqua", text="Kunal Translator Machine", font=('Arial', 15, 'italic bold'), bg="grey")
label1.place(x=278, y=10)

# Translator Boxes

    #Text Feeder
varname1 = StringVar()
entry1 = Entry(root, width=30, bg="lightgreen", textvariable=varname1, font=('ubuntu', 15, 'bold'))
entry1.place(x=400, y=70)

    #Text Output
varname2 = StringVar()
entry2 = Entry(root, width=30, bg="purple", textvariable=varname2, font=('ubuntu', 15, 'bold'), state="readonly")
entry2.place(x=400, y=220)

# # Labels 

    #Translate To 
label4 = Label(root,foreground="white",  text="Translate To :-", font=('ubuntu', 8, 'bold'), bg="grey")
label4.place(x=34, y=147)    
    #Text Feeder Label
label1 = Label(root,foreground="yellow",  text="Enter The Word to Translate :-", font=('ubuntu', 15, 'bold'), bg="grey")
label1.place(x=38, y=70)
    #Text Output Label
label2 = Label(root,foreground="orange", text="Translated Word Here :-", font=('ubuntu', 15, 'bold'), bg="grey")
label2.place(x=56, y=220)

#Buttons Here

    # Translater Button

btn1 = Button(root, text="Translate",  bg="pink", foreground="red",command= sound, font=('ubuntu', 15, 'bold'),relief=RAISED,\
                         cursor="hand2")
btn1.place(x=350, y=140)
root.bind('<Return>', sound)

    # Exit Button

btn2 = Button(root, text="Exit", bg="red",command= mainexit, foreground="white", padx=18, pady=8, font=('ubuntu', 15, 'bold'),relief=RAISED,\
                         cursor="hand2")
btn2.place(x=350, y=350)

#Binding 

    #Text Feeder Binding
entry1.bind('<Enter>', on_entry1click)
entry1.bind('<Leave>', on_entry1leave)


    #Translate Button Binding
btn1.bind('<Enter>', on_click)
btn1.bind('<Leave>', on_leave)

    #Exit Button Binding
btn2.bind('<Enter>', on_2click)
btn2.bind('<Leave>', on_2leave)



root.mainloop()
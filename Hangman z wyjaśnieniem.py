#==========Zad==========
# a)	Przykładowe projekty aplikacji desktopowych w oparciu o technologie Python:
# 23. Gra w hangmana - użytkownik próbuje odgadnąć ukryte słowo, podając kolejne litery. Aplikacja rysuje wisielca w przypadku nieudanych prób.
#=============kod=============

#=======import=======
import tkinter as tk
import random

#=======window=======
root = tk.Tk()                                              # ┐
root.title("hangman")                                       # | tworzenie okna
root.geometry("1000x640")                                   # 」

root.overrideredirect(False)                                # ] można usunąć ramke (dodatkowe)

window_width = 1000                                         # ┐
window_height = 640                                         # |
screen_width = root.winfo_screenwidth()                     # |
screen_height = root.winfo_screenheight()                   # | ustawianie okna na środku ekranu
x = (screen_width // 2) - (window_width // 2)               # |
y = (screen_height // 2) - (window_height // 2)             # |
root.geometry(f"{window_width}x{window_height}+{x}+{y}")    # 」


bg_label = tk.Label(root, bg="#344b32")                   # ┐
bg_label.place(x=0, y=0, relwidth=1, relheight=1)           # 」 tworzenie zielonego tła

#=======variables=======
words = ["CAT", "DOG", "SUN", "MOON", "BOOK", "HOUSE", "PLANT", "WATER", "TABLE",]

def random_letter():                                                                                    # ┐
    global word, how_many_letters, no_duplicate_letters                                                 # |
    word = list(random.choice(words))                                                                   # |
    how_many_letters = len(word)                                                                        # | ustawienie losowego słowa
    no_duplicate_letters = list(dict.fromkeys(word))                                                    # |
random_letter()                                                                                         # 」

def set_variables():                                                                                    # ┐
    global used_letters, correct_letters, mistakes                                                      # |
    used_letters = []                                                                                   # |
    correct_letters=[]                                                                                  # | reset zmiennych
    mistakes=0                                                                                          # |
set_variables()                                                                                         # 」

#==========game==========
def exit_game():                                                                                        # ┐
    root.destroy()                                                                                      # 」wyłącza gre
    
    
def start_game(event):
    global game_canva, bg_image2, how_many_letters, images, images2
    
    menu_canva.destroy()                                                                                # ] usunięcie menu 
    
    game_canva = tk.Canvas(root, width=1000, height=640, highlightthickness=0)                          # ┐
    game_canva.pack()                                                                                   # |
    bg_image2 = tk.PhotoImage(file="./pngs/bg.png")                                                     # | stworzenie 
    game_bg = game_canva.create_image(0, 0, image=bg_image2, anchor="nw")                               # 」
    
    line_pos_x = 425                                                                                    # ┐
    line_pos_y = 450                                                                                    # |
    spacing = 100                                                                                       # |
    images = []                                                                                         # |
    image_ids = []                                                                                      # |
    for i in range(how_many_letters):                                                                   # | stworzenie miejs na poprawne litery
        img = tk.PhotoImage(file="./pngs/ABC/line 0.png")                                               # |
        images.append(img)                                                                              # |
        img_id = game_canva.create_image(line_pos_x + i * spacing, line_pos_y, image=img, anchor="n")   # 」
        image_ids.append(img_id)
        
    mistake_pos_x = 30                                                                                  # ┐
    mistake_pos_y = 490                                                                                 # |
    spacing2 = 70                                                                                       # |
    images2 = []                                                                                        # |
    mistake_image_ids2 = []                                                                             # |
    for i in range(8):                                                                                  # |
        img = tk.PhotoImage(file="./pngs/mistake ABC/mistake 0.png")                                    # |
        images2.append(img)                                                                             # |
        if i <= 3:                                                                                      # |
            mistake_img_id = game_canva.create_image(mistake_pos_x + i * spacing2,                      # |
                                                  mistake_pos_y, image=img, anchor="n")                 # | stworzenie miejs na niepoprawne litery
            mistake_image_ids2.append(mistake_img_id)                                                   # |
        else:                                                                                           # |
            mistake_img_id = game_canva.create_image((mistake_pos_x-280) + i * spacing2,                # |
                                                  mistake_pos_y+50, image=img, anchor="n")              # |
            mistake_image_ids2.append(mistake_img_id)                                                   # 」
        

    exit_button.lift()                                                                                  # ] przeniesienie guzika na pierwszy plan (by go było widać)
    
    
    def key_pressed(event):                                                                             
        global game_canva, bg_image2, mistakes
        
        if mistakes == 9:                                                                               # ┐
            return None                                                                                 # 」nie przejdzie jeżeli już zużyto wszystkie szanse
        if len(correct_letters) == len(no_duplicate_letters):                                           # ┐
            return None                                                                                 # 」nie przejdzie jażeli rozwiązano odpowiedź
        
        key = str(event.keysym).upper()                                                                 # ┐
        print("Naciśnięto:", key)                                                                       # 」key = kliknięta litera np: key = A
        
        if key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":                                                         # ┐
            if key in used_letters:                                                                     # | sprawdza czy key to litera
                print('already used')                                                                   # 」
            else:
                used_letters.append(key)
                if key in word:                                                                         # ┐
                    correct_letters.append(key)                                                         # |
                    for index, letter in enumerate(word):                                               # |
                        if key == letter:                                                               # | uzupełnia prawidłowo kliknięte litery
                            new_img = tk.PhotoImage(file=f"./pngs/ABC/line {key}.png")                  # |
                            images[index] = new_img                                                     # |
                            game_canva.itemconfig(image_ids[index], image=new_img)                      # 」
                            
                else:
                    mistakes += 1
                    def you_lost():                                                                     # ┐
                        global lost_image, end_canva                                                    # |
                        game_canva.destroy()                                                            # |
                        end_canva = tk.Canvas(root, width=1000, height=640, highlightthickness=0)       # |
                        end_canva.pack()                                                                # | koniec gry (pojawia "You lost.png" i z opóźnieniem wyłącza gre)
                        lost_image = tk.PhotoImage(file="./pngs/You lost.png")                          # |
                        end_canva.create_image(0, 0, image=lost_image, anchor="nw")                     # |
                        root.unbind("<Key>")                                                            # |
                        root.after(2000, reset)                                                         # 」
                        
                        
                    bg_image2 = tk.PhotoImage(file=f"./pngs/gallows/gallows {mistakes}.png")            # ┐
                    game_canva.itemconfig(game_bg, image=bg_image2,)                                    # |
                    mistake_img = tk.PhotoImage(file=f"./pngs/mistake ABC/mistake {key}.png")           # | uzupełnia nieprawidłowo kliknięte litery
                    images2[mistakes-1] = mistake_img                                                   # |
                    game_canva.itemconfig(mistake_image_ids2[mistakes-1], image=mistake_img)            # 」
                    
                    if mistakes >= 8:                                                                   # ┐    
                        root.after(2000, you_lost)                                                      # 」 z opóźnieniem włącza you_lost def
        else:
            print('Tylko ABC')

        if len(correct_letters) == len(no_duplicate_letters):                                           # ┐
            def you_won():                                                                              # |
                global won_image, end_canva                                                             # |
                game_canva.destroy()                                                                    # |
                end_canva = tk.Canvas(root, width=1000, height=640, highlightthickness=0)               # | koniec gry (pojawia "You won.png" i z opóźnieniem wyłącza gre)
                end_canva.pack()                                                                        # |
                won_image = tk.PhotoImage(file="./pngs/You won.png")                                    # |
                end_canva.create_image(0, 0, image=won_image, anchor="nw")                              # |
                root.unbind("<Key>")                                                                    # |
                root.after(2000, reset)                                                                 # 」
                
            root.after(2000, you_won)                                                                   # ] z opóźnieniem włącza you_won def                                                                   
            
    root.bind("<Key>", key_pressed)                                                                     # ┐
    root.focus_set()                                                                                    # 」reaguje na kliknięcie
    
def reset():                                                                                            # ┐
    end_canva.destroy()                                                                                 # |
    random_letter()                                                                                     # | reset gry
    set_variables()                                                                                     # |
    menu()                                                                                              # 」
    
#==========menu==========
def menu():
    global bg_image, exit_image, dsw_index_image, exit_button, menu_canva
    menu_canva = tk.Canvas(root, width=1000, height=640, highlightthickness=0)                # ┐
    menu_canva.pack()                                                                         # |
    bg_image = tk.PhotoImage(file="./pngs/start_main.png")                                    # | ustawienie menu i tła
    menu_canva.create_image(0, 0, image=bg_image, anchor="nw")                                # 」

    Start_button = menu_canva.create_rectangle(370, 380, 670, 500, outline="", fill="")       # ┐
    menu_canva.tag_bind(Start_button, "<Button-1>", start_game)                               # 」 tworzenie (Stats) gusika


    exit_image = tk.PhotoImage(file="./pngs/exit.png")                                        # ┐                                                                   
    exit_button = tk.Button(root,image=exit_image,relief="flat",borderwidth=0,                # |
    highlightthickness=0,activebackground="#344b32",command=exit_game)                      # | tworzenie (Exit) guzika
    exit_button.place(relx=0.885)                                                             # 」

    dsw_index_image = tk.PhotoImage(file= "./pngs/my dsw index.png")                          # ┐
    dsw_index = menu_canva.create_image(710, 575, image=dsw_index_image, anchor="nw")         # 」 tworzenie dsw index w menu
menu()

root.mainloop()


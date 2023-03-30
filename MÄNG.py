import random
import tkinter as tk

window = tk.Tk()
window.title("Камень, ножницы, бумага")

def play_game(user_choice):
    possible_actions = ["камень", "бумага", "ножницы"]
    computer_choice = random.choice(possible_actions)
    result_text.set(f"Вы выбрали {user_choice}, компьютер выбрал {computer_choice}.\n")

    if user_choice == computer_choice:
        result_text.set(result_text.get() + "Ничья!")
    elif user_choice == "камень":
        if computer_choice == "ножницы":
            result_text.set(result_text.get() + "Камень бьет ножницы! Вы выиграли!")
        else:
            result_text.set(result_text.get() + "Бумага побеждает камень! Вы проиграли.")
    elif user_choice == "бумага":
        if computer_choice == "камень":
            result_text.set(result_text.get() + "Бумага побеждает камень! Вы выиграли!")
        else:
            result_text.set(result_text.get() + "Ножницы режут бумагу! Вы проиграли.")
    elif user_choice == "ножницы":
        if computer_choice == "бумага":
            result_text.set(result_text.get() + "Ножницы режут бумагу! Вы выиграли!")
        else:
            result_text.set(result_text.get() + "Камень бьет ножницы! Вы проиграли.")

    play_again_button.grid(row=3, column=1)

def reset_game():
    result_text.set("")
    play_again_button.grid_forget()

choices_frame = tk.Frame(window)
choices_frame.grid(row=1, column=1)

rock_button = tk.Button(choices_frame, text="Камень", command=lambda: play_game("камень"))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(choices_frame, text="Бумага", command=lambda: play_game("бумага"))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(choices_frame, text="Ножницы", command=lambda: play_game("ножницы"))
scissors_button.pack(side=tk.LEFT, padx=5)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 18), wraplength=400)
result_label.grid(row=2, column=1)

play_again_button = tk.Button(window, text="Сыграть ещё раз")


import random 


while True:
    user_action = input("Tee oma valik – kivi, käärid või paber: ")
    possible_actions = ["kivi", "paber", "käärid"]
    computer_action = random.choice(possible_actions)
    print(f"\nSina valisid {user_action}, arvuti valis {computer_action}.\n")
    if user_action == computer_action:
        print(f"Mõlemad kasutajad on valinud {user_action}. Ничья!!")
    elif user_action == "kivi":
        if computer_action == "käärid":
            print("Kivi lööb käärid! Sina võitsid!")
        else:
            print("Paber võidab kivi! Sa kaotasid.")
    elif user_action == "paber":
        if computer_action == "kivi":
            print("Paber võidab kivi! Sina võitsid!")
        else:
            print("Käärid lõikavad paberit! Sa kaotasid.")
    elif user_action == "käärid":
        if computer_action == "paber":
            print("Käärid lõikavad paberit! Sina võitsid!")
        else:
            print("Kivi lööb käärid! sa kaotasid.")

    play_again = input("Mängime uuesti? (+/-): ") 
    if play_again.lower() != "+":
        break


    import random
import tkinter as tk



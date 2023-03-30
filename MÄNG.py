import random
import tkinter as tk

window = tk.Tk()
window.title("Kivi,paber,käärid")

def play_game(user_choice):
    possible_actions = ["kivi", "paber", "käärid"]
    computer_choice = random.choice(possible_actions)
    result_text.set(f"Sina valisid {user_choice}, arvuti valis {computer_choice}.\n")

    if user_choice == computer_choice:
        result_text.set(result_text.get() + "Ничья!")
    elif user_choice == "kivi":
        if computer_choice == "Käärid":
            result_text.set(result_text.get() + "Kivi lööb käärid! Sa oled võitnud!")
        else:
            result_text.set(result_text.get() + "Paber võidab kivi! Sa kaotasid.")
    elif user_choice == "paber":
        if computer_choice == "kivi":
            result_text.set(result_text.get() + "Paber võidab kivi! Sa oled võitnud!")
        else:
            result_text.set(result_text.get() + "Käärid lõikavad paberit! Sa kaotasid.")
    elif user_choice == "Käärid":
        if computer_choice == "paber":
            result_text.set(result_text.get() + "Käärid lõikavad paberit! Sa oled võitnud!")
        else:
            result_text.set(result_text.get() + "Kivi lööb käärid! Sa kaotasid.")

    play_again_button.grid(row=3, column=1)

def reset_game():
    result_text.set("")
    play_again_button.grid_forget()

choices_frame = tk.Frame(window)
choices_frame.grid(row=1, column=1)

rock_button = tk.Button(choices_frame, text="Kivi", command=lambda: play_game("kivi"))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(choices_frame, text="Paber", command=lambda: play_game("paber"))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(choices_frame, text="Käärid", command=lambda: play_game("Käärid"))
scissors_button.pack(side=tk.LEFT, padx=5)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 18), wraplength=400)
result_label.grid(row=2, column=1)

play_again_button = tk.Button(window, text="mängi uuesti")


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

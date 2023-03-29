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

   

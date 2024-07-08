import poke_api_request 
from colorama import init, Fore, Back, Style

def menu():
    print("Enter the Pokémon name or 0 to exit:")
    poke_name = input()
    if poke_name == "0":
        return True
    else:
        #CODE
        print("")
    return

def main():
    while True:
        flag = menu()
        if flag == True:
            break
    return

if __name__ == "__main__":
    main()
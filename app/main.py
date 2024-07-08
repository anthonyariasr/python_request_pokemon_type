from poke_api_request import request
from colors import pick_color

def menu():
    print("\nEnter the Pokémon name or 0 to exit:")
    poke_name = input()
    if poke_name == "0":
        return True
    else:
        try:
            data = request(poke_name)
            types = [type_info['type']['name'] for type_info in data['types']]
            # Print the types
            print(f"\nPokémon '{poke_name.capitalize()}' types:")
            for pokemon_type in types:
                print("")
                pick_color(pokemon_type)
        except: 
            print("\nOps! Pokémon not found")
    return

def main():
    while True:
        flag = menu()
        if flag == True:
            break
    return

if __name__ == "__main__":
    main()
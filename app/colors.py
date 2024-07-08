from colored import fore, back, style

#Use colored.py to set a color depending of the pokemon type
def pick_color(poke_type):
    match poke_type:
        case "normal":
            color: str = f"{style('bold')} {fore('white')} {back('grey_35')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "fighting":
            color: str = f"{style('bold')} {fore('white')} {back('dark_orange_3a')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "flying":
            color: str = f"{style('bold')} {fore('white')} {back('steel_blue')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "poison":
            color: str = f"{style('bold')} {fore('white')} {back('dark_violet_1a')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "ground":
            color: str = f"{style('bold')} {fore('black')} {back('light_yellow')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "rock":
            color: str = f"{style('bold')} {fore('black')} {back('sandy_brown')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "bug":
            color: str = f"{style('bold')} {fore('black')} {back('green_yellow')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "ghost":
            color: str = f"{style('bold')} {fore('white')} {back('blue_violet')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "steel":
            color: str = f"{style('bold')} {fore('black')} {back('light_cyan_3')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "fire":
            color: str = f"{style('bold')} {fore('black')} {back('orange_1')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "water":
            color: str = f"{style('bold')} {fore('white')} {back('dodger_blue_3')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "grass":
            color: str = f"{style('bold')} {fore('white')} {back('spring_green_3a')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "electric":
            color: str = f"{style('bold')} {fore('black')} {back('yellow_1')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "psychic":
            color: str = f"{style('bold')} {fore('white')} {back('pink_3')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "ice":
            color: str = f"{style('bold')} {fore('white')} {back('light_cyan_3')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "dragon":
            color: str = f"{style('bold')} {fore('white')} {back('blue_violet')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "dark":
            color: str = f"{style('bold')} {fore('white')} {back('dark_red_1')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "fairy":
            color: str = f"{style('bold')} {fore('white')} {back('pink_1')}"
            print(f'{color}{poke_type.capitalize()}{style('reset')}')
        case "unknown":
            print(poke_type.capitalize())
    return 
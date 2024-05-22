def ascii_from_cube(cubes):
    ascii_codes = [int(round(cube ** (1/3))) for cube in cubes]
    return ''.join([chr(code) for code in ascii_codes])

def main():
    cubes_input = input("Veuillez saisir les cubes séparés par des ';' : ")
    cubes = [float(cube) for cube in cubes_input.split(';') if cube.strip()]

    text = ascii_from_cube(cubes)
    print("Le mot correspondant aux cubes donnés est :", text)

if __name__ == "__main__":
    main()
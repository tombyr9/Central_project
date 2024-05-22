def cube_function(text):
    ascii_codes = [ord(char) for char in text]
    cubes = [code ** 3 for code in ascii_codes]
    return cubes

def main():
    text = input("Veuillez saisir un texte : ")
    cubes = cube_function(text)
    print("Cube des codes ASCII des lettres du texte saisi :")
    print("; ".join(str(cube) for cube in cubes))

if __name__ == "__main__":
    main()
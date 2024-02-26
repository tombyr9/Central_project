def open_the_shop(shop): #Fonction pour ouvrir le magasin
    print("Bienvenu dans la boutique. Voici les infrastructures disponibles.")
    for key in shop.keys():
        print(key,":",shop[key]," dollars.")

def see_the_wallet(wallet): #Fonction pour ouvrir le portemonnaie
    print("Vous avez", wallet, "dollars dans votre portemonnaie.")

def buy_in_the_shop(shop, bag, wallet): #Fonction pour acheter dans le shop
    T = []
    i = 1
    for value in shop: #J'affiche les infrastructures et les nombres à saisir pour les ajouter au sac.
        print(value,":" ,i, end=" ||| ")
        T.append(value) #Je mets les infrastructures dans une liste mais au premier terme plutôt qu'au ième terme.
        i+=1
    x = int(input("\nSaisir l'objet à acheter :")) #L'utilisateur donne le chiffre associé pour que le programme retrouve l'infrastructure dans la liste.
    if shop[T[x-1]] <= wallet: #Vérifie que la valeur de l'insfrastructure qui lui est associé dans le dico "shop" soit inférieur à la somme dans le portmonnaie.
        bag.append(T[x-1]) #Le terme i = 1 est à la place 0 du tableau, donc pareil pour tous les autres, incrémentation de -1.
    wallet = wallet-shop[T[x-1]]

def print_bag(bag): #Fonction qui affiche ce qu'il y a dans le sac de l'utilisateur.
    print("Vous possédez dans votre sac :", bag)
def open_the_shop(shop): #Fonction pour ouvrir le magasin
    print("Bienvenu dans la boutique. Voici les infrastructures disponibles.")
    for key in shop.keys():
        print(key,":",shop[key]," dollars.")

def see_the_wallet(m): #Fonction pour ouvrir le portemonnaie
    print("Vous avez", m, "dollars dans votre portemonnaie.")

def buy_in_the_shop(shop, bag, m): #Fonction pour acheter dans le shop
    T = []
    i = 1
    for value in shop: #J'affiche les infrastructures et les nombres à saisir pour les ajouter au sac.
        print(value,":" ,i, end=" ||| ")
        T.append(value) #Je mets les infrastructures dans une liste mais au premier terme plutôt qu'au ième terme.
        i+=1
    x = int(input("\nSaisir l'objet à acheter :")) #L'utilisateur donne le chiffre associé pour que le programme retrouve l'infrastructure dans la liste.
    if shop[T[x-1]] <= m: #Vérifie que la valeur de l'insfrastructure qui lui est associé dans le dico "shop" soit inférieur à la somme dans le portmonnaie.
        bag.append(T[x-1]) #Le terme i = 1 est à la place 0 du tableau, donc pareil pour tous les autres, incrémentation de -1.
    m = m-shop[T[x-1]]

def print_bag(bag): #Fonction qui affiche ce qu'il y a dans le sac de l'utilisateur.
    print("Vous possédez dans votre sac :", bag)

def gain(P,M,G,I):
    m+=1*P+5*M+15*G+35*I
    return m

def production(P,M,G,I):
    Z=P*2+M*5+G*12.5+I*50
    return Z

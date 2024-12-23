#Chaque commentaire sur une ligne seule a pour but d'informer la ligne en dessous
#Chaque commentaire au bout d'une ligne informe sur la ligne elle-même

import pandas as pd
import random

# Charger les données Pokémon
pokemon_df = pd.read_csv("pokemon.csv")
pokemon_df['Level'] = 1

#class Pokémon
class Pokemon:
    def __init__(self, name, type1, type2, total, hp, attack, defense, sp_atk, sp_def, speed, generation, legendary,level):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.type1}/{self.type2}) - HP: {self.hp}, ATK: {self.attack}, DEF: {self.defense}, SPEED: {self.speed}: LEVEL: {self.level})"

#class Roster
class Roster:
    def __init__(self, dataframe, num_pokemon):
        self.dataframe = dataframe
        self.num_pokemon = num_pokemon
        self.pokemon_list = self.init_roster()

    def init_roster(self): #return une liste d'objects pokemon
        #on choisit num_pokemon lignes du dataframe aléatoirement (.sample)
        sous_dataframe = self.dataframe.sample(self.num_pokemon)
        roster = []
        #iterrows() retourne le tuple (index, ligne(serie en panda)) donc on utilise pas i
        for i, row in sous_dataframe.iterrows(): #on parcours chaque ligne du sous dataframe crée
            pokemon = Pokemon(
                name=row['Name'],
                type1=row['Type 1'],
                type2=row['Type 2'],
                total=row['Total'],
                hp=row['HP'],
                attack=row['Attack'],
                defense=row['Defense'],
                sp_atk=row['Sp. Atk'],
                sp_def=row['Sp. Def'],
                speed=row['Speed'],
                generation=row['Generation'],
                legendary=row['Legendary'],
                level=row['Level']
            )
            roster.append(pokemon)
        return roster

    def total_power(self): #Calcule la somme des scores de puissance (self.total) de tous les Pokémon d'un roaster
        return sum(pokemon.total for pokemon in self.pokemon_list)

    def print_roster(self): # affiche le roster de manière lisible et jolie
        for index, pokemon in enumerate(self.pokemon_list, start=1):
            print(f"{index}. {pokemon}")

    def verif_power(self,roster_fort,roster_faible):

    # Fonction pour équilibrer les rosters
    # diff = différence maximale de puissance en pourcentage entre les 2 rosters qu'on cherche à avoir
    def balance_rosters(roster1, roster2, diff=3):
        powerR1 = roster1.total_power()
        powerR2 = roster2.total_power()
        diff_power = round(abs((powerR1 - powerR2) / powerR2) * 100, 2) #Calcul de la différence
        print(f"\nPuissances initiales des équipes :\n"
              f"Puissance roster 1: {powerR1}\n"
              f"Puissance roster 2: {powerR2}\n"
              f"Difference de puissance: {diff_power}%\n"
              f"Différence de puissance max: {diff}%")

        max_iterations = 100  # Limite pour éviter une boucle infinie si on met une différence de puissance max trop petite
        cpt = 0 #compteur

        while diff_power > diff and cpt < max_iterations:
            cpt += 1
            # Identifier les Pokémons à échanger
            if powerR1 > powerR2:  # Roster 1 est plus fort
                pokemon_fort = max(roster1.pokemon_list, key=lambda p: p.total)  # Pokémon le plus fort du roster 1
                pokemon_faible = min(roster2.pokemon_list, key=lambda p: p.total)  # Pokémon le plus faible du roster 2

                #echange le pokemon le plus fort de roster 1 contre le pokemon le plus faible de roster 2
                roster1.pokemon_list.remove(pokemon_fort)
                roster1.pokemon_list.append(pokemon_faible)
                roster2.pokemon_list.append(pokemon_fort)
                roster2.pokemon_list.remove(pokemon_faible)

            else:  # Roster 2 est plus fort
                pokemon_fort = max(roster2.pokemon_list, key=lambda p: p.total)
                pokemon_faible = min(roster1.pokemon_list, key=lambda p: p.total)

                # echange le pokemon le plus fort de roster 2 contre le pokemon le plus faible de roster 1
                roster2.pokemon_list.remove(pokemon_fort)
                roster2.pokemon_list.append(pokemon_faible)
                roster1.pokemon_list.append(pokemon_fort)
                roster1.pokemon_list.remove(pokemon_faible)


                # Mettre à jour les puissances
                powerR1 = new_power1
                powerR2 = new_power2
                diff_power = round(abs(powerR1 - powerR2) / max(powerR1, powerR2) * 100, 2)
            else:
                # Si aucun échange bénéfique, arrêter
                print("Échange inefficace, fin de la tentative d'équilibrage.")
                break

            # Affichage après chaque tentative
            print(f"\nRecalcul des puissances après équilibrage:\n"
                  f"Puissance roster 1 :{powerR1}\n"
                  f"Puissance roster 2 :{powerR2}\n"
                  f"Difference de puissance: {diff_power}%\n"
                  f"Difference de puissance max: {diff}%")

        if cpt == max_iterations:
            print("Équilibrage arrêté après avoir atteint la limite d'itérations.")

        print("\nÉquilibrage terminé.")

# Initialisation des rosters
num_pokemon = 3  # Modifiable
roster_player1 = Roster(pokemon_df, num_pokemon)
roster_player2 = Roster(pokemon_df, num_pokemon)

# Équilibrage des équipes (Bonus 1/3)
Roster.balance_rosters(roster_player1, roster_player2)

# Affichage des rosters
print("\nRoster équilibré du joueur 1:")
roster_player1.print_roster()

print("\nRoster équilibré du joueur 2:")
roster_player2.print_roster()
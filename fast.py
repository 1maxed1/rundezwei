import numpy as np
import itertools
import matplotlib.pyplot as plt


def generate_all_connections(n):
    return list(itertools.combinations(range(2 * n), 2))


def generate_solutions(connections, n, corners):
    # Erzeuge jumps_made Dictionary
    jumps_made = {i: [] for i in range(n)}

    for segment in connections:
        if segment[1] == (2 * n) - 1 and segment[0] == 0:
            index = 0
        else:
            diff = abs(segment[1] - segment[0] - 1)
            index = diff if diff <= (n - 1) else diff - 2 * (diff - (n - 1))
        jumps_made[index].append(segment)

    solutions = []
    root = (n - 1, 0)  # Starte am Wurzelknoten (letzte Stufe, erstes Element)

    #Rekursive Funktion
    def explore_path(node, banned, path):
        nonlocal solutions  # Declare solutions as nonlocal to modify the outer variable

        m, index = node
        if m < 0:
            #Keine Lösung gefunden
            return False

        if m == n - 1:
            # Nur für das erste Element des n-ten Index prüfen
            filteredArray = [jumps_made[m][0]]
        else:
            #Rekursion
            filteredArray = list(filter(lambda item: all(num not in item for num in banned), jumps_made[m]))

        for i, segment in enumerate(filteredArray):
            #Gehe eine Ebene tiefer
            next_node = (m - 1, i)
            next_banned = list(banned)
            next_banned.extend(segment)
            new_path = path + [segment]
            if len(new_path) == n:
                #Endzustand
                solutions.append(new_path)
                return True  
            #Searches for a new path
            if explore_path(next_node, next_banned, new_path):
                return True  
    #Startet mit dem Wurzelknoten
    explore_path(root, [], [])
    return solutions



def main():
    n = int(input("Wert für n (>= 2) ein: "))

    if n < 2:
        print("Ungültige Eingabe. n muss größer oder gleich 2 sein.")
        return
    all_connections = generate_all_connections(n)
    gsl = generate_solutions(all_connections, n, corners)
    print(f"Solutions: {gsl}")


if __name__ == "__main__":
    main()

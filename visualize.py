import numpy as np
#Zeichenlibrary
import matplotlib.pyplot as plt
#Regex
import re
import ast


def draw_regular_polygon(n, corners, valid_solution):
    #Seperate xy >Koordinaten
    x, y = corners.T  

    plt.figure(figsize=(10, 10))
    plt.axis('equal')

    #Zeichnet die Seiten
    for i in range(2 * n):
        plt.plot([x[i], x[(i + 1) % (2 * n)]], [y[i], y[(i + 1) % (2 * n)]], color='black', linewidth=2.0)

    #Zeichnet die Diagonalen
    for i in range(2 * n):
        for j in range(i + 2, 2 * n):
            plt.plot([x[i], x[j]], [y[i], y[j]], color='gray', linestyle='--', linewidth=0.5)

    
    for i, corner in enumerate(corners):
        plt.text(corner[0], corner[1], str(i), fontsize=12, ha='center', va='center')

    #Valide Strecken rot überzeichnet
    for (start, end) in valid_solution:
        plt.plot([x[start], x[end]], [y[start], y[end]], color='red', linewidth=2)

    plt.xticks([])
    plt.yticks([])
    
    #Zeigt das Fenster auf dem Bildschirm an
    plt.show()


def main():
    n = int(input("Bitte gib einen Wert für n (>= 2) ein: "))
    solution_str = input("Lösung (Format: [(x1, y1), (x2, y2), ...]): ")

    if n < 2:
        print("Ungültige Eingabe. n muss größer oder gleich 2 sein.")
        return

    if not solution_str:
        print("Lösung muss angegeben werden")
        return

    #eigegebener Array wird auf formgültigkeit überprüft
    try:
        solution_list = ast.literal_eval(solution_str)
        if not all(isinstance(item, tuple) and len(item) == 2 for item in solution_list):
            raise ValueError
    except (ValueError, SyntaxError):
        print("Ungültiges Format für Lösung.")
        return

    solution_pairs = [(int(x), int(y)) for x, y in solution_list]

    corners = np.array([(np.cos(i * np.pi / n), np.sin(i * np.pi / n)) for i in range(2 * n)])
    #Zeichenfunktion
    draw_regular_polygon(n, corners, solution_pairs)

if __name__ == "__main__":
    main()

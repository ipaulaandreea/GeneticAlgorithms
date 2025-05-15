import random
# Metoda HillClimbing reprezinta un algoritm de optimizare locală.
# Acesta porneste de la o solutie initiala, aleatoare, apoi verifica solutiile "vecine".
# Daca gaseste una mai buna, o accepta pentru ca apoi sa verifice noii vecini.
# Algoritmul se oprește cand nu mai exista vecini mai buni - minimum local.

# Este obținută întotdeauna soluția optimă?
# Nu, solutia nu este intotdeauna optima deoarecere rezultatul algoritmului hillclimbing depinde de vecinii solutiei
# initiale si de vecinii acesteia.
# Astfel, in cazul in care se ajunge intr-o zona in care toti vecinii sunt mai slabi, solutia aceea va fi considerata optima,
# cu toate ca pot exista variante mai bune la nivel global.
# In plus, interschimbarea vecinilor se produce intre elemente adiancente, deci nu putem gasi solutii aflate
# departe in spatiul posibilitatilor.
#Pentru a creste sansa de a obtine solutia optima, putem incerca rezolvarea acestei probleme cu ajutorul algoritmilor genetici.



# Funcția pentru calcularea costului total al unui traseu
def calc_cost(path, D):
    cost = 0
    for i in range(len(path)):
        # modulo ne ajuta sa calculam si costul de la ultimul oras la primul (D[8][0])
        cost += D[path[i]][path[(i + 1) % len(path)]]
    return cost


# Functie pentru generarea vecinilor prin interschimbarea a doua orașe din traseu (de pe pozitiile i si j)
def get_neighbors(path):
    neighbors = []
    # pozitia 0 ramane pe loc, fiind punctul de pornire fixat
    for i in range(1, len(path) - 1):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Functia Hill Climbing
def hill_climbing(D):
        # Etapa 1. Initializare
    n = len(D)
    current_path = list(range(n)) # pornim de la un traseu initial [0, 1, 2,...,8]
    random.shuffle(current_path[1:])  # amestecam orasele 1-8 (orasul de start ramane pe loc)

        # Etapa 2. Calcularea costului primului traseu
    current_cost = calc_cost(current_path, D)

    while True:
        # Etapa 3. Determinarea vecinilor
        neighbors = get_neighbors(current_path)
        # Etapa 4. Alegerea drumului cu cost minim
        next_path = min(neighbors, key=lambda x: calc_cost(x, D))
        next_cost = calc_cost(next_path, D)
        # Etapa 5. Daca costul vecinului este mai mic decat costul curent,
        # continuam sa cautam vecinii vecinului (ramanem in bucla while)
        if next_cost < current_cost:
            current_path = next_path
            current_cost = next_cost
        # Altminteri, am gasit un optim local si putem iesi din bucla while
        else:
            break

    return current_path, current_cost

# Matricea de mai jos se citeste astfel:
##D[0][1] = 4     -> costul de la orașul 0 la orașul 1 este 4
##D[2][5] = 9     -> costul de la orașul 2 la orașul 5 este 9
D = [
    [0, 4, 5, 1, 4, 2, 5, 5, 2],
    [4, 0, 4, 3, 1, 6, 4, 8, 4],
    [5, 4, 0, 7, 9, 9, 1, 3, 5],
    [1, 3, 7, 0, 5, 5, 6, 7, 8],
    [4, 1, 9, 5, 0, 7, 8, 2, 5],
    [2, 6, 9, 5, 7, 0, 2, 6, 1],
    [5, 4, 1, 6, 8, 2, 0, 8, 8],
    [5, 8, 3, 7, 2, 6, 8, 0, 4],
    [2, 4, 5, 8, 5, 1, 8, 4, 0]
]

path, cost = hill_climbing(D)
print("Traseu gasit:", path)
print("Cost total:", cost)

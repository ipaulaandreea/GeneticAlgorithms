import random

#1. Functia pentru calcularea scorului fiecarei permutari
# Functia fitness primeste drept parametru o posibila aranjare a reginelor pe tabla
# si verifica conflictele pe diagonala
# scorul maxim este dat de scenariul cu conflicte = 0
def fitness(p):
    n = len(p)
    conflicts = sum(1 for i in range(n) for j in range(i + 1, n) if abs(p[i] - p[j]) == abs(i - j))
    return n * (n - 1) // 2 - conflicts

#2. Functia pentru generarea aleatoare a unei populatii
# functia de generare a populatiei de solutii
# fiecare individ este o configurare a celor n regine pe tabla de sah
# functia returneaza si scorul calculat pentru fiecare configurare a tablei
def generate_population(dim, n):
    population = []
    for _ in range(dim):
        individual = list(range(n))
        random.shuffle(individual)
        score = fitness(individual)
        population.append(individual + [score])
    return population

#3. Functia de mutatie cu inserare - introducem variatie in populatie si evitam blocarea in minime locale
# Alegem inserarea si nu alt tip de mutatie deoarece dorim sa obtinem modificari mici, usor de controlat
# Rezultatul este o interschimbare a doua pozitii aleatoare
def insertion_mutation(individual):
    n = len(individual) - 1
    ind = individual[:n]  # exclude scorul
    i, j = sorted(random.sample(range(n), 2))
    gene = ind.pop(j)
    ind.insert(i, gene)
    score = fitness(ind)
    return ind + [score]

# 4. Functie pentru introducerea unei mutatii in populatie cu un anumit grad de probabilitate (pm);
# pm = 0.0 -> niciun individ nu va fi mutat
# pm = 1.0 -> toti indivizii vor fi mutati
def mutate_population(pop, pm):
    new_pop = []
    #Pentru fiecare individ,
    for individual in pop:
        # generam un numar aleator cu random.random();
        # Daca acel numar este mai mic decat pm, efectuam mutatia
        if random.random() < pm:
            new_individual = insertion_mutation(individual)
        else:
            #Alftel, individul nu va suferi mutatia
            new_individual = individual[:]
        new_pop.append(new_individual)
    return new_pop

# Exemplu de utilizare

# Parametri
n = 10         # dimensiunea unei solutii (pentru 8 regine)
dim = 10       # dimensiunea populatiei
pm = 0.5       # probabilitate de mutatie

# Generare populatie initiala
pop = generate_population(dim, n)
print("Populatia initiala:")
for p in pop:
    print(p)

# Mutatie
popm = mutate_population(pop, pm)
print("\nPopulatia dupa mutatie:")
for p in popm:
    print(p)
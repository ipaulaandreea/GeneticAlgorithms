import random

#1. Functia de initializare a populatiei
#Va returna o populatie de POP_SIZE indivizi, unde fiecare individ este un vector continand m obiecte in diverse proportii
def init_populatie():
    return [[random.uniform(0, 1) for _ in range(m)] for _ in range(POP_SIZE)]


#2. Functia fitness
def fitness(individ):
    #calculam costul total de selectie al individului (fractiunile de obiecte inmnultite cu costurile lor individuale)
    cost_total = sum(individ[i] * costuri[i] for i in range(m))
    if cost_total > Cmax:
        return 0
    #daca acest cost este sub pragul acceptabil, calculam valoarea generata de acest inidivid (fractiunile de obiecte inmnultite cu valorile lor individuale)
    return sum(individ[i] * valori[i] for i in range(m))

#3. Functia de selectie a parintilor
#Alegem indivizii apti de a produce copii
# Vom realiza o selectie tip ruleta: cu cat un individ are un fitness mai mare, cu atat mai multe sanse va avea sa fie selectat
def selectie(pop, fitnessuri):
    total = sum(fitnessuri)
    if total == 0:
        return random.choice(pop)
    r = random.uniform(0, total)
    #setam un acumulator
    acc = 0
    #iteram prin fiecare pereche de individ si fitnessul lui
    for individ, fit in zip(pop, fitnessuri):
        #adunam scorul lui la acumulator
        acc += fit
        #individul la randul caruia acumulatorul a depasit valoarea
        # generata aleator r va fi cel selectat sa devina parinte
        if acc >= r:
            return individ
    return pop[-1]

#4. Functia de crossover (combinarea parintilor)
#Copilul va reprezenta un individ al carui proportii per obiect reprezinta media aritmetica a obiectelor corespunzatoare
# ale parintilor
def crossover(parinte1, parinte2):
    copil = [(parinte1[i] + parinte2[i]) / 2 for i in range(m)]
    return copil

#5. Functia de mutatie (inserare de mici modificari)
# Functia parcurge fiecare gena a individului si va introduce modificari cu o probabilitate dependenta de MUTATIE_PROB
def mutatie(individ):
    for i in range(m):
        if random.random() < MUTATIE_PROB:
            individ[i] = min(max(individ[i] + random.uniform(-0.1, 0.1), 0), 1)
    return individ

#6. Algormitul genetic va folosi tehnica elitismului pentru a pastra cei mai buni indivizi
# dintr-o generatie astfel incat acestia sa nu fie pierduti in procesul de evolutie
#Algoritmul va avea un numar de iteratii egal cu numarul dorit de generatii
def algoritm_genetic():
    populatie = init_populatie()
    for generatie in range(GENERATII):
        fitnessuri = [fitness(ind) for ind in populatie]
        #construim o lista noua pentru noua generatie
        new_pop = []

        # daca folosim elitism, pastram cel mai bun individ din generatia curenta
        # pentru a nu pierde cel mai bun individ gasit pana acum
        if ELITISM:
            best = max(populatie, key=fitness)
            new_pop.append(best)
        # adaugam copii noi in noua populatie
        while len(new_pop) < POP_SIZE:
            p1 = selectie(populatie, fitnessuri)
            p2 = selectie(populatie, fitnessuri)
            copil = crossover(p1, p2)
            copil = mutatie(copil)
            new_pop.append(copil)
        #inlocuim vechea populatie cu cea noua
        populatie = new_pop

    # Rezultatul final - cautam cel mai bun individ din fiecare generatie
    #Pentru ca folosim elitism, cel mai bun individ de pana acum este pastrat de la o generatie la alta
    best = max(populatie, key=fitness)
    return best, fitness(best)

# Exemplu de utilizare

# Datele problemei
m = 10  # număr de obiecte
valori = [random.randint(10, 100) for _ in range(m)]
costuri = [random.randint(5, 50) for _ in range(m)]
Cmax = 150

# Parametrii genetici
POP_SIZE = 100
GENERATII = 200
MUTATIE_PROB = 0.1
ELITISM = True

solutie, valoare_maxima = algoritm_genetic()
print("Proportii obiecte selectate:", solutie) #fiecare se inmulteste cu 100 pentru a afla procentul ales din fiecare obiect
print("Valoare totala maximizata:", valoare_maxima) #dorim sa obtinem o valoare cat mai mare care sa respecte restrictia de cost (Cmax)
print("Cost total:", sum(solutie[i] * costuri[i] for i in range(m)))

import matplotlib.pyplot as plt
import random as rd


dt = 0.01
g = 9.8
height = []


def sim(simv, simh, simm, simml, a, ison):
    resolh = simh + simv * dt
    if ison:
        resolv = simv - (g - a * a / 3 * (simm + simml)) * dt  # 분사할 때
        resolml = simml - a * dt
        return resolv, resolh, resolml
    else:
        resolv = simv - g * dt  # 분사 안할 때
        return resolv, resolh, simml


def generate_population(size=10):
    population = []

    for j in range(size):
        gene = []
        for i in range(9):
            gene.append(rd.randrange(1,30))
        population.append(gene)

    return population


def fitness(gene):
    t, v, h = 0, 0, 0
    m1, m2, m3, ml1, ml2, ml3, a1, a2, a3 = gene

    while v >= 0:
        if ml1 > a1 * dt:
            print(t, sim(v, h, m1 + m2 + m3 + ml2 + ml3, ml1, a1, True))
            v, h, ml1 = sim(v, h, m1, ml1, a1, True)
            height.append(h)
        elif ml2 > a2 * dt:
            print(t, sim(v, h, m2 + m3 + ml3, ml2, a2, True))
            v, h, ml2 = sim(v, h, m1, ml2, a2, True)
            height.append(h)
        elif ml3 > a3 * dt:
            print(t, sim(v, h, m3, ml3, a3, True))
            v, h, ml3 = sim(v, h, m1, ml3, a3, True)
            height.append(h)
        else:
            print(t, sim(v, h, m3, ml3, a3, False))
            v, h, ml3 = sim(v, h, m1, ml3, a3, False)
            height.append(h)
        t = (t + 1)


pop = generate_population()
fitness(pop[0])
print(pop[0])

plt.plot(range(len(height)), height, 'b')
plt.grid()
plt.show()

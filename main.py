import matplotlib.pyplot as plt

t = 0
v = 0
h = 0  # 최고 높이가 가장 높은게 목표

dt = 0.1
g = 9.8
m1 = 10
m2 = 10
m3 = 10
ml1 = 10
ml2 = 10
ml3 = 10
a = -30  # 분사 속도
u = 10  # 상대 속도

height = []


def sim(simv, simh, simm, simml, ison):
    resolh = simh + simv * dt
    if ison:
        resolv = simv - (g + u * a / (simm + simml)) * dt  # 분사할 때
        resolml = simml + a * dt
        return resolv, resolh, resolml
    else:
        resolv = simv - g * dt  # 분사 안할 때
        return resolv, resolh, simml


while v >= 0:
    if ml1 > 0:
        print(t, sim(v, h, m1 + m2 + m3 + ml2 + ml3, ml1, True))
        v, h, ml1 = sim(v, h, m1, ml1, True)
        height.append(h)
    elif ml2 > 0:
        print(t, sim(v, h, m2 + m3 + ml3, ml2, True))
        v, h, ml2 = sim(v, h, m1, ml2, True)
        height.append(h)
    elif ml3 > 0:
        print(t, sim(v, h, m3, ml3, True))
        v, h, ml3 = sim(v, h, m1, ml3, True)
        height.append(h)
    else:
        print(t, sim(v, h, m3, ml3, False))
        v, h, ml3 = sim(v, h, m1, ml3, False)
        height.append(h)
    t = (t + 1)

plt.plot(range(len(height)), height, 'b')
plt.grid()
plt.show()

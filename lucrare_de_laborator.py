from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
import math

pi = math.pi
df = pd.read_csv('data.csv')
print("\033[1mLUCRARE DE LABORATOR: Determinarea experimentala a valorii acceleratiei gravitationale\033[0m")
print("\n1.TEORIA LUCRARII\n"
      "T0 = Δt/N\n"
      "T0 = 2 * π * rad(l/g_experimental) => g_experimental = 4 * π * l/(T0^2)\n"
      "α = r/2m = coeficientul de amortizare\n"
      "η = 2 * α */(3 * π * r)\n\n")
print("2.DISPOZITIVE SI MATERIALE UTILIZATE\n"
      " - pendul gravitational\n"
      " - rigla\n"
      " - cronometru\n\n")
print("3.MODUL DE LUCRU\n"
      "1. Se masoara raza sferei si masa sferei"
      "2. Bila se suspenda de sfoara la o anumita inaltime\n"
      "3. Se masoara lungimea sforii la momentul respectiv\n"
      "4. Se masoara nr. de oscilatii ale bilei si timpul in care acestea se realizeaza\n"
      "5. Se repeta masuratorile de minim 10 ori\n\n")
print("4.PRELUCRAREA DATELOR EXPERIMENTALE\n")
#print(df)
data = []
finaldata = []
for i in range(1, 14):
    data.append([i, df.values[i][0], df.values[i][1], df.values[i][2], 0, 0, 0, 0, 0])

col_names = ["Nr. mas", "l(cm)", "N", "Δt(s)", "t0", "g(m/s^2)", "g mediu", "Δg", "Δg mediu"]
#print(tabulate(data, headers=col_names))
#print("\n")
for i in range(0, 13):
    t0 = data[i][4] = data[i][3] / data[i][2]
    gexp = data[i][5] = (4 * pi * data[i][0])/(t0 * t0)
    data[i][6] += gexp
gmediu = data[12][6] /15

for i in range(0, 13):
    data[i][7] = abs(data[i][5] - gmediu)
    data[i][8] += data[i][7]
dgmediu = data[12][8] / 15

x_values = []
y_values = []

for i in range(0, 13):
    if i == 0:
        finaldata.append([i+1, data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], gmediu, data[i][7], dgmediu])
    else:
        finaldata.append([i + 1, data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], "-", data[i][7], "-"])
    x_values.append(data[i][4]*data[i][4])
    y_values.append(data[i][1])

print(tabulate(finaldata, headers=col_names))
print("4.CONCLUZII\n"
      "g ∈ [g_mediu - Δg; g_mediu + Δg]\n"
      "g ∈ [" , gmediu - dgmediu, ";" ,gmediu + dgmediu,"]\n"
      "Posibile erori: Determinarea gresita a masei/razei sferei, numarului de oscilatii,\n"
      "timpului in care s-a realizat miscarea oscilatorie")
plt.plot(x_values, y_values, label='Values')
plt.xlabel('t0^2(s^2)')
plt.ylabel('l(cm)')
plt.title('Valoarea acceleratiei gravitationale')
plt.show()

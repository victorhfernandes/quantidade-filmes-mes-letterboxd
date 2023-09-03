import pandas as pd

year = input("Digite o ano que deseja ver a quantidade de filmes: ")

MONTHS = [
    "Janeiro", "Fevereiro", "Março", "Abril", 
    "Maio", "Junho", "Julho", "Agosto", 
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

df = pd.read_csv('ratings.csv')
data = df['Date'].tolist()

norepeat = list(set(data))
norepeat.sort()
films = []
total = 0

for date in data:
    if (date[:4] == year):
        films.append(date)

for index in range(12):
    total = 0
    for film in films:
        if (film[5:7] == str(index+1).zfill(2)):
            total += 1
    print(f"{MONTHS[index]}: {total}")
times = ("palmeiras", "flamengo", "fluminense", "são paulo", "athletico-PR", "coritiba", "bahia", "botafogo", "atlético-MG", "internacional", "red bull bragantino", "vasco", "cruzeiro", "vitória", "grêmio", "corinthians", "santos", "mirassol", "remo", "chapecoense")

print(f'''{"=-" * 21}
    Os cinco primeiros colocados são: 
{"=-" * 21}''')

for i in range(0, 5):
    print(f"        {i + 1}° = {times[i].capitalize():.>20}")

print(f'''{"=-" * 21}
    Os quatro últimos colocados são: 
{"=-" * 21}''')

for i in range(1, 5):
    print(f"        {i}°{times[-i].capitalize():.>20}")

print(f'''{"=-" * 21}
      Os times em ordem alfabética: 
{"=-" * 21}''')
print(sorted(times))

print(f'''{"=-" * 21}
O time 'Chapecoense' está na posição: {times.index("chapecoense") + 1}°
{"=-" * 21}''')

import matplotlib.pyplot as plt
#Vetor com os estados e seus vizinhos:
estados = {
    "Acre": ["Amazonas", "Rondônia"],
    "Alagoas": ["Bahia", "Pernambuco", "Sergipe"],
    "Amapá": ["Pará"],
    "Amazonas": ["Acre", "Rondônia", "Mato Grosso", "Roraima", "Pará"],
    "Bahia": ["Alagoas", "Espírito Santo", "Goiás", "Pernambuco", "Sergipe", "Minas Gerais", "Tocantins", "Piauí"],
    "Ceará": ["Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte"],
    "Espírito Santo": ["Bahia", "Minas Gerais", "Rio de Janeiro"],
    "Goiás": ["Bahia", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Distrito Federal", "Tocantins"],
    "Maranhão": ["Pará", "Piauí", "Tocantins"],
    "Mato Grosso": ["Amazonas", "Goiás", "Mato Grosso do Sul", "Tocantins", "Pará", "Rondônia"],
    "Mato Grosso do Sul": ["Goiás", "Mato Grosso", "Paraná", "São Paulo", "Minas Gerais"],
    "Minas Gerais": ["Bahia", "Espírito Santo", "Goiás", "Rio de Janeiro", "São Paulo", "Distrito Federal", "Mato Grosso do Sul"],
    "Pará": ["Amapá", "Amazonas", "Maranhão", "Mato Grosso", "Roraima", "Tocantins"],
    "Paraíba": ["Ceará", "Pernambuco", "Rio Grande do Norte"],
    "Paraná": ["Mato Grosso do Sul", "São Paulo", "Santa Catarina"],
    "Pernambuco": ["Alagoas", "Bahia", "Ceará", "Paraíba", "Piauí"],
    "Piauí": ["Ceará", "Maranhão", "Bahia", "Tocantins", "Pernambuco"],
    "Rio de Janeiro": ["Espírito Santo", "Minas Gerais", "São Paulo"],
    "Rio Grande do Norte": ["Ceará", "Paraíba"],
    "Rio Grande do Sul": ["Santa Catarina"],
    "Rondônia": ["Acre", "Amazonas", "Mato Grosso"],
    "Roraima": ["Amazonas", "Pará"],
    "São Paulo": ["Mato Grosso do Sul", "Minas Gerais", "Paraná", "Rio de Janeiro"],
    "Santa Catarina": ["Paraná", "Rio Grande do Sul"],
    "Sergipe": ["Alagoas", "Bahia"],
    "Tocantins": ["Bahia", "Goiás", "Maranhão", "Mato Grosso", "Pará", "Piauí"],
    "Distrito Federal": ["Goiás", "Minas Gerais"],
}

#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#
#                             a) • lista indexada
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________

# Índices de início dos sucessores
alpha = [0]
# Lista de sucessores
beta = []

for estado, vizinhos in estados.items():
    # Adiciona vizinhos na lista β (extend adiciona n elementos na lista)
    beta.extend(vizinhos)
    # Define onde começa o próximo estado (append adiciona exatamente 1 elementos na lista)
    alpha.append(len(beta))

def get_vizinhos(estado):
    if estado not in estados:
        return []
    index = list(estados.keys()).index(estado)
    return beta[alpha[index]:alpha[index + 1]]

#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#
#                               • Extra
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________

#Prompt para ver se o usuário quer ver um estado específico
ver_estado = input("\n Deseja ver os vizinhos de um estado específico? (Sim/Não)")
if ver_estado == "sim" or ver_estado == "Sim":    
    # Entrada do usuário
    estado_buscado = input("\n Digite o nome do estado para ver seus vizinhos: ")

    # Exibir os vizinhos do estado informado pelo usuário
    if estado_buscado in estados:
        vizinhos = ", ".join(get_vizinhos(estado_buscado))
        print(f"-> {estado_buscado}: {len(estados[estado_buscado])} vizinhos ({vizinhos})")
    else:
        print("Estado não encontrado.")
    

#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#
#  C) • Identificar a unidade da federação com maior e menor quantidade de Vizinhos 
#     • Listar esses Vizinhos para cada situação anterior.
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________

# Cálculo do grau de cada estado
graus = {estado: len(vizinhos) for estado, vizinhos in estados.items()}

# Identificar estados com maior e menor grau
grau_maximo = max(graus.values())
grau_minimo = min(graus.values())

estados_max_grau = [estado for estado, grau in graus.items() if grau == grau_maximo]
estados_min_grau = [estado for estado, grau in graus.items() if grau == grau_minimo]

# Exibir estados com maior número de vizinhos
print("\nEstado(s) com maior número de vizinhos:")
for estado in estados_max_grau:
    vizinhos = ", ".join(get_vizinhos(estado))
    print(f"-> {estado}: {graus[estado]} vizinhos ({vizinhos})")

# Exibir estados com menor número de vizinhos
print("\nEstado(s) com menor número de vizinhos:")
for estado in estados_min_grau:
    vizinhos = ", ".join(get_vizinhos(estado))
    print(f"-> {estado}: {graus[estado]} vizinhos ({vizinhos})")

#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#
#           C) • Calcular a frequência dos graus dos vértices
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________
#____________________________________________________________________________________

# Cálculo da frequência dos graus dos vértices
frequencia_graus = {}
for grau in graus.values():
    if grau in frequencia_graus:
        frequencia_graus[grau] += 1
    else:
        frequencia_graus[grau] = 1

# Exibir a frequência dos graus dos vértices
plt.figure(figsize=(10, 6))
plt.bar(frequencia_graus.keys(), frequencia_graus.values(), color='royalblue')

# Configuração do gráfico
plt.xlabel("Grau (Número de vizinhos)", fontsize=12)
plt.ylabel("Número de estados", fontsize=12)
plt.title("Frequência dos Graus dos Estados", fontsize=14)

# Garante que os graus apareçam ordenados no eixo X
plt.xticks(sorted(frequencia_graus.keys()))

plt.grid(axis="y", linestyle="--", alpha=0.7)

# Exibir valores no topo das barras
for grau, frequencia in frequencia_graus.items():
    plt.text(grau, frequencia + 0.1, str(frequencia), ha='center', fontsize=11)

# Mostrar o gráfico
plt.show()

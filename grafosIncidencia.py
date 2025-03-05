import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, estados):
        self.estados = estados
        self.nomes = list(estados.keys())  # Lista dos estados
        self.num_vertices = len(self.nomes)
        self.num_arestas = sum(len(v) for v in estados.values()) // 2  # Cada aresta é contada duas vezes

        # Criar matriz de incidência
        self.matriz_incidencia = [[0] * self.num_arestas for _ in range(self.num_vertices)]
        self._construir_matriz_incidencia()

    def _construir_matriz_incidencia(self):
        """Constrói a matriz de incidência"""
        aresta_index = 0
        arestas_adicionadas = set()  # Evitar duplicação de arestas

        for i, estado in enumerate(self.nomes):
            for vizinho in self.estados[estado]:
                if (estado, vizinho) not in arestas_adicionadas and (vizinho, estado) not in arestas_adicionadas:
                    j = self.nomes.index(vizinho)
                    self.matriz_incidencia[i][aresta_index] = 1
                    self.matriz_incidencia[j][aresta_index] = 1
                    arestas_adicionadas.add((estado, vizinho))
                    aresta_index += 1


    def exibir_matriz_incidencia(self):
        """Exibe a matriz de incidência formatada e alinhada corretamente"""
        espaco = 1  # Define um espaçamento adequado para alinhamento
        print("\nMatriz de Incidência:\n")

        cabecalho = " " + " ".join(f"E{i:>{espaco-1}}" for i in range(self.num_arestas))
        print(cabecalho)

        for i, linha in enumerate(self.matriz_incidencia):
            linha_formatada = " ".join(f"{valor:>{espaco}}" for valor in linha)
            print(f"{self.nomes[i]:<3} {linha_formatada}")


estados = {
    "AC": ["AM", "RO"],
    "AL": ["BA", "PE", "SE"],
    "AP": ["PA"],
    "AM": ["AC", "RO", "MT", "RR", "PA"],
    "BA": ["AL", "ES", "GO", "PE", "SE", "MG", "TO", "PI"],
    "CE": ["PB", "PE", "PI", "RN"],
    "ES": ["BA", "MG", "RJ"],
    "GO": ["BA", "MT", "MS", "MG", "DF", "TO"],
    "MA": ["PA", "PI", "TO"],
    "MT": ["AM", "GO", "MS", "TO", "PA", "RO"],
    "MS": ["GO", "MT", "PR", "SP", "MG"],
    "MG": ["BA", "ES", "GO", "RJ", "SP", "DF", "MS"],
    "PA": ["AP", "AM", "MA", "MT", "RR", "TO"],
    "PB": ["CE", "PE", "RN"],
    "PR": ["MS", "SP", "SC"],
    "PE": ["AL", "BA", "CE", "PB", "PI"],
    "PI": ["CE", "MA", "BA", "TO", "PE"],
    "RJ": ["ES", "MG", "SP"],
    "RN": ["CE", "PB"],
    "RS": ["SC"],
    "RO": ["AC", "AM", "MT"],
    "RR": ["AM", "PA"],
    "SP": ["MS", "MG", "PR", "RJ"],
    "SC": ["PR", "RS"],
    "SE": ["AL", "BA"],
    "TO": ["BA", "GO", "MA", "MT", "PA", "PI"],
    "DF": ["GO", "MG"],
}

# Criando o grafo
grafo = Grafo(estados)

# Exibir Matrizes

grafo.exibir_matriz_incidencia()

# Função para calcular e exibir o histograma dos graus (número de conexões de cada estado)
def exibir_grafico_frequencia_graus(matriz_incidencia, nomes_estados):
    """Calcula e exibe o gráfico da frequência dos graus dos vértices."""

    # Cálculo do grau de cada estado (soma dos valores na matriz de incidência)
    graus = {estado: sum(matriz_incidencia[i]) for i, estado in enumerate(nomes_estados)}

    # Cálculo da frequência dos graus dos vértices
    frequencia_graus = {}
    for grau in graus.values():
        if grau in frequencia_graus:
            frequencia_graus[grau] += 1
        else:
            frequencia_graus[grau] = 1

    # Criando o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(frequencia_graus.keys(), frequencia_graus.values(), color='purple', alpha=0.75, edgecolor='black')

    # Configuração do gráfico
    plt.xlabel("Grau (Número de vizinhos)", fontsize=12)
    plt.ylabel("Número de estados", fontsize=12)
    plt.title("Frequência dos Graus dos Estados - Matriz de Incidência", fontsize=14)

    # Garante que os graus apareçam ordenados no eixo X
    plt.xticks(sorted(frequencia_graus.keys()))

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Exibir valores no topo das barras
    for grau, frequencia in frequencia_graus.items():
        plt.text(grau, frequencia + 0.1, str(frequencia), ha='center', fontsize=11, color='black')

    # Mostrar o gráfico
    plt.show()


# Exibir gráfico da frequência dos graus da matriz de incidência
exibir_grafico_frequencia_graus(grafo.matriz_incidencia, grafo.nomes)


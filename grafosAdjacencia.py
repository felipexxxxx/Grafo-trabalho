import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, estados):
        self.estados = estados
        self.nomes = list(estados.keys())  # Lista dos estados
        self.num_vertices = len(self.nomes)
        self.num_arestas = sum(len(v) for v in estados.values()) // 2  # Cada aresta é contada duas vezes

        # Criar matriz de adjacência
        self.matriz_adjacencia = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        self._construir_matriz_adjacencia()

    def _construir_matriz_adjacencia(self):
        """Constrói a matriz de adjacência"""
        for i, estado in enumerate(self.nomes):
            for vizinho in self.estados[estado]:
                j = self.nomes.index(vizinho)
                self.matriz_adjacencia[i][j] = 1  # Conexão entre os estados

    def exibir_matriz_adjacencia(self):
        """Exibe a matriz de adjacência formatada e alinhada corretamente"""
        espaco = 3  # Define um espaçamento adequado para alinhamento
        print("\nMatriz de Adjacência:\n")

        # Cabeçalho com os nomes dos estados alinhados corretamente
        cabecalho = "    " + " ".join(f"{nome:>{espaco}}" for nome in self.nomes)
        print(cabecalho)

        # Exibição das linhas da matriz
        for i, linha in enumerate(self.matriz_adjacencia):
            linha_formatada = " ".join(f"{valor:>{espaco}}" for valor in linha)
            print(f"{self.nomes[i]:<3} {linha_formatada}")  # Nome do estado + linha da matriz

    def calcular_graus(self):
        """Calcula o grau de cada estado"""
        return {estado: sum(self.matriz_adjacencia[i]) for i, estado in enumerate(self.nomes)}

    def identificar_grau_max_min(self):
        """Identifica os estados com maior e menor quantidade de vizinhos"""
        graus = self.calcular_graus()
        grau_maximo = max(graus.values())
        grau_minimo = min(graus.values())

        estados_max_grau = [estado for estado, grau in graus.items() if grau == grau_maximo]
        estados_min_grau = [estado for estado, grau in graus.items() if grau == grau_minimo]

        return estados_max_grau, estados_min_grau, grau_maximo, grau_minimo

    def listar_vizinhos(self, estado):
        """Lista os vizinhos de um estado"""
        index = self.nomes.index(estado)
        return [self.nomes[i] for i, valor in enumerate(self.matriz_adjacencia[index]) if valor == 1]

    def calcular_frequencia_graus(self):
        """Calcula a frequência dos graus dos vértices"""
        graus = self.calcular_graus()
        frequencia_graus = {}
        for grau in graus.values():
            if grau in frequencia_graus:
                frequencia_graus[grau] += 1
            else:
                frequencia_graus[grau] = 1
        return frequencia_graus

    def exibir_grafico_frequencia_graus(self):
        """Exibe o gráfico da frequência dos graus dos vértices"""
        frequencia_graus = self.calcular_frequencia_graus()

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


# Definição dos estados e suas conexões (grafo)
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

# Exibir Matriz de Adjacência
grafo.exibir_matriz_adjacencia()

# Identificar estados com maior e menor grau
estados_max_grau, estados_min_grau, grau_maximo, grau_minimo = grafo.identificar_grau_max_min()

# Exibir estados com maior número de vizinhos
print("\nEstado(s) com maior número de vizinhos:")
for estado in estados_max_grau:
    vizinhos = ", ".join(grafo.listar_vizinhos(estado))
    print(f"-> {estado}: {grau_maximo} vizinhos ({vizinhos})")

# Exibir estados com menor número de vizinhos
print("\nEstado(s) com menor número de vizinhos:")
for estado in estados_min_grau:
    vizinhos = ", ".join(grafo.listar_vizinhos(estado))
    print(f"-> {estado}: {grau_minimo} vizinhos ({vizinhos})")

# Exibir gráfico da frequência dos graus
grafo.exibir_grafico_frequencia_graus()

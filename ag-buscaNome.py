import random

class Util:
    letras = "abcdefghijklmnopqrstuvwxyz"
    tamanho = len(letras)

    @staticmethod
    def gerar_palavra(n):
        
        palavra = ''
        
        for i in range(n):
            palavra += Util.letras[random.randrange(Util.tamanho)] 
        return palavra

class Cromossomo:
    
    def __init__(self, valor, estado_final):
        self.valor = valor
        self.aptidao =  self.calcular_aptidao(estado_final)

    @staticmethod
    def calcular_aptidao(self, estado_final):
        nota = 0
        for i in range (len(estado_final)):
            if (estado_final[i] in self.valor):
                nota += 5
            if (self.valor[i] == estado_final[i]):
                nota+= 50    
        return nota

    def __eq__(self,other):
        if isinstance(other, Cromossomo):
            return self.valor == other.valor
        return False    

    def __gt__(self, other):
        return self.aptidao <= other.aptidao

    def __str__(self):
        return f"valor= {self.valor}, aptidao= {self.aptidao}"
        
class AG:
    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for i in range (tamanho_populacao):
            # Coloca na lista palavras geradas aleatorias com base no tamanho do estado_final
            populacao.append(Cromossomo(Util.gerar_palavra(len(estado_final)), estado_final))

    @staticmethod
    def exibir_populacao(populacao):
        for i in populacao:
            #Printa o equals re-escrito do Cromossomo
            print(i)

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        
        torneio = []
        qtd_selecionados = taxa_selecao * len(populacao) / 100
        
        # elitismo
        nova_populacao.append(populacao.get[0])
        
        i = 1
        while(i <= qtd_selecionados):
            c1 = populacao [ random.randrange(len(populacao)) ]

            # vai repitir, mas igual funciona
            while(True):
                c2 = populacao [ random.randrange(len(populacao)) ]
                if c2 != c1:
                 break

            while(True):
                c3 = populacao [ random.randrange(len(populacao)) ]
                if c3 != c2 != c1:
                 break 

            torneio.append(c1)
            torneio.append(c2)
            torneio.append(c3)   
            torneio.sort()

            selecionado = torneio[0]

            if not selecionado in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1

            torneio.clear()      
            #parei aqui (arrumar a main)
            


def main():
    print('AG Gerador nome')

    tamanho_populacao = int(input("Tamanho populacao: "))
    estado_final = input("Palavra desejada: ")
    taxa_selecao = int(input("Taxa selecao (20%-40%): "))
    taxa_reproducao = 100 - taxa_selecao
    taxa_mutacao = int(input("Taxa mutacao (5%-10%): "))
    qtd_geracoes = int(input("Qtd. de geracoes: "))

    populacao = []
    nova_populacao = []

    AG.gerar_populacao(populacao, tamanho_populacao, estado_final)
    populacao.sort()
    
    print("Gen. 1")
    AG.exibir_populacao(populacao)

    for i in range(1, qtdGeracoes):
        selecionar_por_torneio(populacao, novaPopulacao, taxaSelecao)
        
        reproduzir(populacao, novaPopulacao, taxaReproducao, estadoFinal)


        if (i % (populacao.size() / taxaMutacao) == 0) {
            mutar(novaPopulacao, estadoFinal); //estadoFinal é passado, pq indivíduos mutados devem ter suas aptidões recalculadas
        }
        
        populacao.clear()
        populacao.copy(nova_populacao)
        novaPopulacao.clear()
        populacao.sort()

        print("\n\nGeracao "+ (i + 1))
        exibir_populacao(populacao);
main()



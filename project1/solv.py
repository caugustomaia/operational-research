from __future__ import print_function
from ortools.graph import pywrapgraph

# Nome e caminho do arquivo:

fileName = 'instancias/instance1.txt'

def main():

  # 
  # LEITURA DO ARQUIVO
  #

  arq = open(fileName)

  verticesNumber = int(arq.readline())
  arcsNumber     = int(arq.readline())
  sourceNode     = int(arq.readline())
  sinkNode       = int(arq.readline())

  lines = [0]*arcsNumber

  for i in range(arcsNumber):
      lines[i] = arq.readline().split(' ')

  arq.close()
  
  # 
  # FIM DA LEITURA DO ARQUIVO
  #

  #
  # INÍCIO DA MODELAGEM
  #

  # Somando +1 para considerar uma das etapas da modelagem de PFM para PFCM 
  # em que se adiciona um arco da origem ao escoadouro 
  
  totalArcs = arcsNumber + 1
  totalVertices = verticesNumber + 1

  # Declaração dos arrays que o Solver usa como entrada de dados

  start_nodes = [0]*totalArcs
  end_nodes   = [0]*totalArcs
  capacities  = [0]*totalArcs
  unit_costs  = [0]*totalArcs
  supplies    = [0]*totalVertices

  # Declaração de variáveis que vão auxiliar no processo de modelagem
  capacitiesSum = 0

  # Atribuindo os valores lidos do arquivo aos arrays de entrada
  # de dados do Solver

  for i in range(arcsNumber):
      start_nodes[i] = int(lines[i][0])
      end_nodes[i]   = int(lines[i][1])
      capacities[i]  = int(lines[i][2])

      # PRIMEIRA ETAPA DA MODELAGEM ONDE Cij = 0
      unit_costs[i]  = 0
      
      # Somatório utilizado para dar o chute dos valores de capacidade, 
      # custo e suprimento do arco da modelagem
      capacitiesSum += capacities[i]


  # SEGUNDA ETAPA DE MODELAGEM: ATRIBUINDO UM LIMITE SUPERIOR SEGURO COMO OFERTA E DEMANDA DO NÓ
  # DE INÍCIO E NÓ ESCOADOURO
  for i in range(verticesNumber):
      supplies[i] = 0

  supplies[sourceNode] = capacitiesSum 
  supplies[sinkNode]   = -capacitiesSum

  # TERCEIRA ETAPA DA MODELAGEM, ADICIONANDO UM ARCO QUE VAI DO NÓ INICIAL
  # AO NÓ ESCOADOURO
  start_nodes[totalArcs - 1] = sourceNode
  end_nodes[totalArcs - 1]   = sinkNode

  # CONTINUANDO TERCEIRA ETAPA DE MODELAGEM, ATRIBUINDO CAPACIDADE "INFINITA"
  # E CUSTO ALTO AO ARCO ADICIONADO ANTERIORMENTE
  capacities[totalArcs - 1]  = capacitiesSum*3 
  unit_costs[totalArcs - 1]  = capacitiesSum*3 
  
  print('Start Nodes:')
  print(start_nodes)
  print('End Nodes:')
  print(end_nodes)
  print('Capacities:')
  print(capacities)
  print('Unit Costs:')
  print(unit_costs)
  print('Supplies:')
  print(supplies)

  #
  # FIM DA MODELAGEM
  #

  # Instanciando o solver SimpleMinCostFlow.
  min_cost_flow = pywrapgraph.SimpleMinCostFlow()

  # Adicionando os arcos
  for i in range(0, len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                capacities[i], unit_costs[i])

  # Adicionando os nós

  for i in range(0, len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

  # Variável usada para calcular Z
  z = 0

  # Encontrando o fluxo de custo mínimo
  if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('')
    print('  Arc    Flow / Capacity  Cost')
    for i in range(min_cost_flow.NumArcs()):
      cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
      if(not(min_cost_flow.Tail(i) == sourceNode and min_cost_flow.Head(i) == sinkNode) and min_cost_flow.Flow(i) != 0):
        print('%1s -> %1s   %3s  / %3s       %3s' % (
            min_cost_flow.Tail(i),
            min_cost_flow.Head(i),
            min_cost_flow.Flow(i),
            min_cost_flow.Capacity(i),
            cost))
      if(min_cost_flow.Head(i) == sinkNode):
        if(min_cost_flow.Tail(i) != sourceNode):
          z += min_cost_flow.Flow(i) 
  else:
    print('There was an issue with the min cost flow input.')
  
  print('')
  print('Z = ', z)
  print('')

if __name__ == '__main__':
  main()
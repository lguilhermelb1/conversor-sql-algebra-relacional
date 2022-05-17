from conversor import priest
import igraph as ig
from node import Node
import numpy as np
import re

def arvore_inicial(txt):
   alg_rel = priest(txt)

   nodes = []
   nodes.append(Node(0, alg_rel.get('select')))
   nodes.append(Node(1, alg_rel.get('where')))
   nodes[1].setPai(nodes[0])

   joins = joins_from(alg_rel.get('from'))

   #Adiciona as relações entre as tabelas no grafo
   for j in joins:
      pai = nodes[len(nodes)-1]
      node = Node(len(nodes), f"|x| {j.get('join')}")
      node.setPai(pai)
      nodes.append(node)
      
   # Adiciona as tabelas no grafo
   tabelas_adicionadas = []
   joins.reverse()
   for i in range(len(joins)):
      pai_index = (len(nodes)-1)-i-len(tabelas_adicionadas)
      pai = nodes[pai_index]
      tabelas = joins[i].get('tabelas')

      for j in range(len(tabelas)):
         if not tabelas_adicionadas.__contains__(tabelas[j]):
            node = Node(len(nodes), tabelas[j])
            node.setPai(pai)
            nodes.append(node)
            tabelas_adicionadas.append(tabelas[j])
         
   plot_graph(nodes)


# Plota o grafo
def plot_graph(nodes):
   g = ig.Graph(n = len(nodes), directed = True)
   labels = []

   for node in nodes:
      label = f"{node.label}"
      if node.pai == None:
         labels.insert(node.id, label)
         continue
      labels.insert(node.id, label)
      g.add_edge(node.id, node.pai.id)

   
   g.vs["label"] = labels
   ig.plot(g,"grafo_ar.png", layout = g.layout_reingold_tilford(mode="in", root=0), bbox=(800,800), margin = 150)


# Separa as tabelas e a relação entre as duas
def joins_from(txt):
   condicoes = re.findall(r'\w+\.\w+\s*\=\s*\w+\.\w+',txt)
   joins = []
   for c in condicoes:
      join = re.sub(r'\w+\.','',c)
      tabelas = re.split(r'\s*\=\s*', re.sub(r'\.\w+','',c))

      joins.append({"tabelas": tabelas, "join": join})

   return joins
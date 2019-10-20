#!/usr/bin/python

'''
Trabalho de Pesquisa Operacional

Alunos:
Rian
Vinicius
Vitor

'''

from gurobipy import *
from input import *
import utils
import sys


class TeamLocationModel:
	model = None
	allocate = None

	
	def solveTeamLocationModel(self, instance): #languageTeam, languagesUser
		try:
			print('\n------------------- Inicio Solucao modelo ------------------\n')
			
			# Criacao do modelo
			self.model = Model('AllocationTeamMineraGitPo')

			# Cria variaveis
			self.allocate = self.model.addVars(instance.numUsers, instance.numTeams, vtype=GRB.BINARY, name='allocate')
			
			# Define objetivo
			# maximizar o somatório de pesos das pessoas alocadas em equipes
			self.model.setObjective((quicksum(self.allocate[user,team]*instance.beneffits[user][team] for user in range(instance.numUsers) for team in range(instance.numTeams))), GRB.MAXIMIZE)
			
			# Definindo restricoes

			# Restricao 1: cada vertice do tipo pessoa é atribuído apenas a uma equipe ou a nenhuma
			self.model.addConstrs((quicksum(self.allocate[user,team] for team in range(instance.numTeams)) <= 1 for user in range(instance.numUsers)), 'totalidade')
			#*beneffits[user,team]
			# m.setObjective(quicksum(pay[w]*x[w,s] for w,s in availability), GRB.MINIMIZE)
			
			# Restricao 2: quantidade de pessoas alocadas em cada equipe seja maior que a quantidade mínima desejada
			self.model.addConstrs((quicksum(self.allocate[user,team] for user in range(instance.numUsers)) >= instance.minMembersTeam[team] for team in range(instance.numTeams)), 'cardinalidade_min')

			# Restricao 3: quantidade de pessoas alocadas em cada equipe seja menor que a quantidade máxima desejada
			self.model.addConstrs((quicksum(self.allocate[user,team] for user in range(instance.numUsers)) <= instance.maxMembersTeam[team] for team in range(instance.numTeams)), 'cardinalidade_max')
			
			# Restricao 4: # maxXp, minXp, langXp, qtdUserMaxXp, qtdUserMinXp
			self.model.addConstrs((quicksum(self.allocate[user,team]*(instance.langXp[user][team] <= instance.lowerXp[team]) for user in range(instance.numUsers)) >= instance.qtdUsersMinXp[team] for team in range(instance.numTeams)), 'conhecimento_min')

			# Restricao 5:
			self.model.addConstrs((quicksum(self.allocate[user,team]*(instance.langXp[user][team] >= instance.upperXp[team]) for user in range(instance.numUsers)) >= instance.qtdUsersMaxXp[team] for team in range(instance.numTeams)), 'conhecimento_max')
			
			#Abaixo explicação sobre as restrições 4 e 5
			'''
			As restrições (5) e (6) são responsáveis pelo conhecimento de uma linguagem que uma
			pessoa i possui em detrimento ao que uma equipe j necessita, ela determina (em (5)) que cada
			equipe j tenha no mínimo uma quantidade de pessoas Z 1 que possuem pelo menos um nível
			L 1 de conhecimento da linguagem requerida pela equipe e em (5) determina que cada equipe
			j tenha no mínimo uma quantidade de pessoas Z 2 que possuem nível de conhecimento da
			linguagem acima de L 1 . Nestas restrições citadas acima podemos observar que temos os
			conjuntos I 1 e I 2 , dos quais são subconjuntos de pessoas de V 1 que possuem conhecimento
			da linguagem requerida pela equipe j e obedecem a condição de experiência na linguagem
			de programação.
			Pensando no problema, poderíamos considerar L 1 sendo pessoas com níveis de expe-
			riências mais baixo, como é o caso de estagiários e trainees. Pelo contrário, temos L 2 que
			poderia ser representado como sendo as pessoas mais experientes e influentes que poderiam
			conseguir um cargo melhor na empresa, como um gestor, um programador sênior ou gerente
			de equipe.
			'''



			'''
			Salva modelo em arquivo de saida
			Modelo salvo com separacao de arquivos de entrada
			Cada arquivo de entrada tera seu proprio arquivo de modelo
			'''
			self.model.write('model_allocation_' + instance.name + '.lp')

			# Otimiza modelo de programacao linear
			self.model.optimize()



		# Captura e trata erro no gurobi
		except GurobiError as e:
			print('Error code ' + str(e.errno) + ': ' + str(e))

		# Captura e trata erro de atributo
		except AttributeError:
			print('Encountered an attribute error')


def main(args):
	if len(args) > 0:
		instance = Instance(args[0]) # passar por linha de comando o caminho da instancia
	else:
		instance = Instance('instances/exemplo.txt') #1-Instancia 1.txt # passar por linha de comando o caminho da instancia
	#model = solveTeamLocationModel(instance)
	teamLocationSolver = TeamLocationModel()
	teamLocationSolver.solveTeamLocationModel(instance)
	utils.saveSolution(teamLocationSolver.model, instance, teamLocationSolver.allocate)
	utils.printSolution(teamLocationSolver.model, instance, teamLocationSolver.allocate)
	print('------------------ Fim da execucao do algoritmo ------------------')

	
	#utils.scatterPlot(teamLocationSolver.model, instance, teamLocationSolver.allocate)


if __name__ == '__main__':
	main(sys.argv[1:])
	# Ver esse link depois
	# https://cadernodelaboratorio.com.br/2017/06/05/python-3-processando-argumentos-da-linha-de-comando/

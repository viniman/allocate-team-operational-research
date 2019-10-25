#!/usr/bin/python

'''
Trabalho de Pesquisa Operacional

Alunos:
Rian das Dores Alves - 201676040
Vinícius Carlos de Oliveira - 201635025
Vitor Queiroz de Campos - 201565234AC

Para executar o algoritmo, siga a seguinte instrucao:
python3 model.py caminho/para/a/instancia.txt

'''

from gurobipy import *
from input import *
import utils
import sys


class TeamLocationModel:
	'''
	Classe para execucao do modelo 
	'''
	model = None
	allocate = None

	
	def solveTeamLocationModel(self, instance):
		'''
		Funcao de solucao do modelo
		Os dados importantes ficam salvos na estrutura da classe TeamLocationModel
		'''
		try:
			print('\n------------------- Inicio Solucao modelo ------------------\n')
			
			# Criacao do modelo
			self.model = Model('AllocationTeamMineraGitPo')

			# Cria variaveis
			self.allocate = self.model.addVars(instance.numUsers, instance.numTeams, vtype=GRB.BINARY, name='allocate')
			
			# Define objetivo
			# maximizar o somatório de pesos das pessoas alocadas em equipes
			self.model.setObjective(
			(quicksum(self.allocate[user,team]*instance.beneffits[user][team] 
			for user in range(instance.numUsers) 
			for team in range(instance.numTeams))), GRB.MAXIMIZE)
			

			# Definindo restricoes

			# Restricao 1: cada vertice do tipo pessoa é atribuído apenas a uma equipe ou a nenhuma
			self.model.addConstrs(
			(quicksum(self.allocate[user,team] 
			for team in range(instance.numTeams)) <= 1 
			for user in range(instance.numUsers)), 'totalidade')

			
			# Restricao 2: quantidade de pessoas alocadas em cada equipe seja maior que a quantidade mínima desejada
			self.model.addConstrs(
			(quicksum(self.allocate[user,team] 
			for user in range(instance.numUsers)) >= instance.minMembersTeam[team] 
			for team in range(instance.numTeams)), 'cardinalidade_min')


			# Restricao 3: quantidade de pessoas alocadas em cada equipe seja menor que a quantidade máxima desejada
			self.model.addConstrs(
			(quicksum(self.allocate[user,team] 
			for user in range(instance.numUsers)) <= instance.maxMembersTeam[team] 
			for team in range(instance.numTeams)), 'cardinalidade_max')
			
			# Restricao 4: Explicacao sobre as restricoes 4 e 5 mais abaixo no codigo
			self.model.addConstrs(
			(quicksum(self.allocate[user,team]*(instance.langXp[user][team] <= instance.lowerXp[team]) 
			for user in range(instance.numUsers)) >= instance.qtdUsersMinXp[team] 
			for team in range(instance.numTeams)), 'conhecimento_min')

			# Restricao 5: Explicacao sobre as restricoes 4 e 5 mais abaixo no codigo
			self.model.addConstrs(
			(quicksum(self.allocate[user,team]*(instance.langXp[user][team] >= instance.upperXp[team]) 
			for user in range(instance.numUsers)) >= instance.qtdUsersMaxXp[team] 
			for team in range(instance.numTeams)), 'conhecimento_max')
			
			
			'''
			Abaixo explicação sobre as restrições 4 e 5

			As restrições (4) e (5) são responsáveis pelo conhecimento de uma linguagem que uma
			pessoa i possui em detrimento ao que uma equipe j necessita, ela determina que cada
			equipe j tenha no mínimo uma quantidade de pessoas 'lowerXp' que possuem pelo menos um nível
			'qtdUsersMinXp' de conhecimento da linguagem requerida pela equipe e determina que cada equipe
			j tenha no mínimo uma quantidade de pessoas 'upperXp' que possuem nível de conhecimento da
			linguagem acima de 'qtdUsersMaxXp'.
			Pensando no problema, poderíamos considerar 'lowerXp' sendo pessoas com níveis de experiências 
			mais baixo, como é o caso de estagiários e trainees. Pelo contrário, temos 'upperXp'
			que poderia ser representado como sendo as pessoas mais experientes e influentes que poderiam
			conseguir um cargo melhor na empresa, como um gestor, um programador sênior ou gerente de equipe.
			'''



			'''
			Salva modelo em arquivo de saida
			Modelo salvo com separacao de arquivos de entrada
			Cada arquivo de entrada tera seu proprio arquivo de modelo
			'''
			self.model.write('models/model_allocation_' + instance.name + '.lp')

			# Otimiza modelo de programacao linear
			self.model.optimize()

			# Comment: teste em instancias que geramos onde nao tinha solucao viavel
			#if self.model.status == GRB.INFEASIBLE:
				#self.model.feasRelaxS(1, False, False, True)
				#self.model.optimize()


		# Captura e trata erro no gurobi
		except GurobiError as e:
			print('Error code ' + str(e.errno) + ': ' + str(e))

		# Captura e trata erro de atributo
		except AttributeError:
			print('Encountered an attribute error')



def main(args):
	'''
	Funcao main

	'''
	if len(args) > 0:
		instance = Instance(args[0]) # passar por linha de comando o caminho da instancia
	else:
		print('A instancia de exemplo sera executada.')
		print('Caso queira executar outras instancias:')
		print('Passe como parametro o caminho da instancia')
		print('Ex: python3 model.py instances/teamalloc_u250_t10.txt')
		instance = Instance('instances/exemplo.txt')

	# Cria objeto da classe TeamLocationModel
	teamLocationSolver = TeamLocationModel()
	# Soluciona o modelo linear para o problema
	teamLocationSolver.solveTeamLocationModel(instance)
	# Salva solucao em arquivo de saida localizado em: solutions/solution-nomeinstancia.csv
	utils.saveSolution(instance, teamLocationSolver.model, teamLocationSolver.allocate)
	# Imprime solucao na linha de comandos do terminal
	utils.printSolution(instance, teamLocationSolver.model, teamLocationSolver.allocate)
	print('------------------ Fim da execucao do algoritmo ------------------')



if __name__ == '__main__':
	'''
	Associacao da funcao main para execucao
	'''
	main(sys.argv[1:])

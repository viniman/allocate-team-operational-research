#!/usr/bin/python

'''
Trabalho de Pesquisa Operacional

Alunos:
Rian
Vinicius
Vitor

'''

from file_utils import *
from gurobipy import *

def teamLocation(numUsers, numTeams, minMembersTeam, maxMembersTeam, beneffits): #languageTeam, languagesUser
	try:
		print(numUsers)
		print(numTeams)
		print(minMembersTeam)
		print(maxMembersTeam)
		print(beneffits)
		#Create a new model
		model = Model('mineragit_po')
	    
	    # Range of teams-users variables
		alloc_user_team = [[0 for user in range(users)] for team in range(teams)]

		print(alloc_user_team)

		# Cria variaveis
		allocate = model.addVars(numUsers, numTeams, vtype=GRB.BINARY, name="allocate")
		#allocation = model.addVars(alloc_user_team, vtype=GRB.BINARY, name="allocation")
	    
	    # Create variables
	    #allocateam = model.addVars(aloc_user_team, vtype=GRB.BINARY, obj=beneffits, name="allocateam")

		# Define objetivo
		# maximizar o somatório de pesos das pessoas alocadas em equipes
		model.setObjective(allocate.sum(), GRB.MAXIMIZE) # for aloc in allocation * peso
		# for user in range(numUsers) for team in range(numTeams): allocation[user,team]*weight[user,team]

		# Definindo restricoes
		# Restricao: cada vertice do tipo pessoa é atribuído apenas a uma equipe ou a nenhuma
		model.addConstrs((quicksum(allocate[user,team] for user in range(numUsers)) == 1 for team in range(numTeams)), 'totalidade')

		# Restricao: quantidade de pessoas alocadas em cada equipe seja maior que a quantidade mínima desejada
		model.addConstrs((quicksum(allocate[user,team] for user in range(numUsers)) >= minMembersTeam[team] for team in range(numTeams)), "cardinalidade_min")

		# Restricao: quantidade de pessoas alocadas em cada equipe seja menor que a quantidade máxima desejada
		model.addConstrs((quicksum(allocate[user,team] for user in range(numUsers)) <= maxMembersTeam[team] for team in range(numTeams)),"uncardinalidade_max")


		model.optimize()

		
		for v in model.getVars():
			print('%s %g' % (v.varName, v.x))

		print('Obj: %g' % model.objVal)

	except GurobiError as e:
		print('Error code ' + str(e.errno) + ": " + str(e))

	except AttributeError:
		print('Encountered an attribute error')



if __name__ == '__main__':
	teamLocation(users, teams, minMembers, maxMembers, beneffitsWeight)
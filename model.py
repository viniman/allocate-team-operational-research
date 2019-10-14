#!/usr/bin/python

'''
Trabalho de Pesquisa Operacional

Alunos:
Rian
Vinicius
Vitor

'''

from utils import *
from gurobipy import *

def teamLocation(numUsers, numTeams, minMembersTeam, maxMembersTeam, beneffits, upperXp, lowerXp, langXp, qtdUserMaxXp, qtdUserMinXp): #languageTeam, languagesUser
	try:
		print(numUsers)
		print(numTeams)
		print(minMembersTeam)
		print(maxMembersTeam)
		print(beneffits, '\n-------------------------\n')
		#Create a new model
		model = Model('mineragit_po')
	    
	    # Range of teams-users variables
		alloc_user_team = [[0 for user in range(users)] for team in range(teams)]

		print(alloc_user_team)

		# Cria variaveis
		allocate = model.addVars(numUsers, numTeams, vtype=GRB.BINARY, name="allocate")
		
		#allocate = model.addVars(alloc_user_team, vtype=GRB.BINARY, obj=beneffits, name="allocate")
		#allocation = model.addVars(alloc_user_team, vtype=GRB.BINARY, name="allocation")
	    # Create variables
	    #allocateam = model.addVars(aloc_user_team, vtype=GRB.BINARY, obj=beneffits, name="allocateam")

		# Define objetivo
		# maximizar o somatório de pesos das pessoas alocadas em equipes
		model.setObjective((quicksum(allocate[user,team]*beneffits[user][team] for user in range(numUsers) for team in range(numTeams))), GRB.MAXIMIZE) # for aloc in allocation * peso
		# for user in range(numUsers) for team in range(numTeams): allocation[user,team]*weight[user,team]

		# Definindo restricoes

		# Restricao 1: cada vertice do tipo pessoa é atribuído apenas a uma equipe ou a nenhuma
		model.addConstrs((quicksum(allocate[user,team] for team in range(numTeams)) <= 1 for user in range(numUsers)), 'totalidade')
		#*beneffits[user,team]
		# m.setObjective(quicksum(pay[w]*x[w,s] for w,s in availability), GRB.MINIMIZE)

		# Restricao 2: quantidade de pessoas alocadas em cada equipe seja maior que a quantidade mínima desejada
		model.addConstrs((quicksum(allocate[user,team] for user in range(numUsers)) >= minMembersTeam[team] for team in range(numTeams)), 'cardinalidade_min')

		# Restricao 3: quantidade de pessoas alocadas em cada equipe seja menor que a quantidade máxima desejada
		model.addConstrs((quicksum(allocate[user,team] for user in range(numUsers)) <= maxMembersTeam[team] for team in range(numTeams)), 'cardinalidade_max')

		# Restricao 4: # maxXp, minXp, langXp, qtdUserMaxXp, qtdUserMinXp
		model.addConstrs((quicksum(allocate[user,team]*(lowerXp[team] <= langXp[user][team]) for user in range(numUsers)) >= qtdUserMinXp[team] for team in range(numTeams)), 'conhecimento_min')

		# Restricao 5:
		model.addConstrs((quicksum(allocate[user,team]*(upperXp[team] >= langXp[user][team]) for user in range(numUsers)) >= qtdUserMaxXp[team] for team in range(numTeams)), 'conhecimento_max')

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



		# Salva modelo em arquivo de saida
		model.write('model_allocation.lp')

		# Otimiza modelo de programacao linear
		model.optimize()

		


		for v in model.getVars():
			print('%s %g' % (v.varName, abs(v.x)))

		print('Obj: %g' % model.objVal)

		model.printAttr('X')

		status = model.status
		if status == GRB.Status.UNBOUNDED:
			print('The model cannot be solved because it is unbounded')
			exit(0)
		if status == GRB.Status.OPTIMAL:
			print('The optimal objective is %g' % model.objVal)
			exit(0)
		if status != GRB.Status.INF_OR_UNBD and status != GRB.Status.INFEASIBLE:
			print('Optimization was stopped with status %d' % status)
			exit(0)

		'''
		# do IIS
		print('The model is infeasible; computing IIS')
		model.computeIIS()
		if model.IISMinimal:
			print('IIS is minimal\n')
		else:
			print('IIS is not minimal\n')
		print('\nThe following constraint(s) cannot be satisfied:')
		for c in model.getConstrs():
			if c.IISConstr:
				print('%s' % c.constrName)
		'''

	except GurobiError as e:
		print('Error code ' + str(e.errno) + ": " + str(e))

	except AttributeError:
		print('Encountered an attribute error')



if __name__ == '__main__':
	teamLocation(users, teams, minMembers, maxMembers, beneffitsWeight, maxExperienceLangTeam, minExperienceLangTeam, langExperience, qtdUsersForMaxXp, qtdUsersForMinXp)
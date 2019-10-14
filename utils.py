#!/usr/bin/python


# exemplo instantica
users = 10 # quantidade de usuários
teams = 3 # quantidade de equipes
maxMembers = [2, 3, 1] # número máximo de membros em cada equipe
minMembers = [1, 1, 1] # número mínimo de membros em cada equipe
langTeam = [0, 0 , 1] # id da linguagem requerida pela equipe
langUsers = [[0, 1], # id das lingagens de cada usuário
             [0, 1],
             [0, 3],
             [2, 1],
             [0, 2],
             [0, 1],
             [0, 1],
             [5, 2],
             [3, 1],
             [0, 1]]
beneffitsWeight = [[4, 3, 4], # matriz de beneficio (users x teams)
                   [56, 7, 78], # linhas=users, colunas=teams
                   [5, 34, 3],
                   [3, 88, 3],
                   [4, 56, 4], 
                   [9, 5, 6],
                   [5, 9, 4], 
                   [6, 7, 5], 
                   [7, 10, 5],
                   [34, 3, 1]]

#Restrição 4
minExperienceLangTeam = [0.2, 0.3, 0.1]
qtdUsersForMinXp = [0, 0, 0]

# Restrição 5
maxExperienceLangTeam = [0.2, 0.3, 0.1]
qtdUsersForMaxXp = [0, 0, 0]

langExperience = [[0.4, 0.3, 0.4], # matriz de beneficio (users x teams)
                   [0.56, 0.7, 0.78], # linhas=users, colunas=teams
                   [0.5, 0.34, 0.3],
                   [0.3, 0.88, 0.3],
                   [0.4, 0.56, 0.4], 
                   [0.9, 0.5, 0.6],
                   [0.5, 0.9, 0.4], 
                   [0.6, 0.7, 0.5], 
                   [0.7, 0.10, 0.5],
                   [0.34, 0.3, 0.1]]


# class Instance:
#     def __init__(self, path):
#         self.instanceRead(path)


# users, teams, minMembers, maxMembers, beneffitsWeight, maxExperienceLangTeam, minExperienceLangTeam, langExperience, qtdUsersForMaxXp, qtdUsersForMinXp
def instanceRead(path): #def instanceRead(self, path):
    print('Leitura de Instância')
    inputFile = open(path,'r')

    line = inputFile.readline()
    print(line)
    line = line.split()
    print(line)
    
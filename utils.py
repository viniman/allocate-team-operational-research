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
beneffitsWeight = [[4, 3, 4, 56, 7, 78, 5, 34, 3, 3], # matriz de beneficio (users x teams)
                   [88, 3, 4, 56, 4, 9, 5, 6, 5, 9],  # linhas=users, colunas=teams
                   [4, 6, 7, 5, 7, 10, 5, 34, 3, 1]]
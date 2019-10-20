#!/usr/bin/python

import matplotlib.pyplot as plt
from gurobipy import *
import time
import csv
import model

def scatterPlot(model, instance, varAllocation):
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()




def saveSolution(model, instance, varAllocation):
    print('\n------------ Salvando solucao em arquivo de saida ------------')
    #with open('saida.csv', 'a') as outputFile:
        #print('OIIII!!!!!!!')

    try:
        error = False
        with open('solutions/solution-instance-' + instance.name + '.csv', 'a') as outputFile: #csvfile
            csv_writer = csv.writer(outputFile, delimiter='\t')
            csv_writer.writerow(('Nome Instancia: ', instance.name))
            csv_writer.writerow(('Num usuarios: '+str(instance.numUsers), 'Num equipes: '+str(instance.numTeams)))
            csv_writer.writerow(('Valor da solucao objetivo: ', model.ObjVal))
            csv_writer.writerow(('Data', '        Hora', '    Tempo de Execucao (s)'))
            date = time.strftime('%Y-%m-%d')
            hour = time.strftime('    %H:%M:%S')
            runtime = round(model.Runtime, 6)
            csv_writer.writerow((date, hour, runtime))
            csv_writer.writerow(('Team', '    Allocated Users'))
            for j in range(instance.numTeams):
                result = [int(i) for i in range(instance.numUsers) if varAllocation[i, j].x != 0]
                resultStr = ' '.join(str(x) for x in result)
                csv_writer.writerow(('Equipe ' + str(j), resultStr)) 
            csv_writer.writerow('')
            csv_writer.writerow('')
    except (IOError, OSError) as e:
        print('------------------ Algo de errado aconteceu! -----------------')
        print('Python details:\n', e)
        error = True
    finally:
        if error:
            print('----------------- Erro: Solucao nao foi salva ----------------\n')
        else:
            print('------------------ Solucao salva com sucesso -----------------\n')
            


def printSolution(model, instance, varAllocation):
    print('------------- Impressao de solucao do modelo-------------')
    print('Valor da solução objetivo (MAX): %g' % model.objVal)
    print('\n    ------ Alocacao das variaveis ------')
    print('Pessoa i alocada no time j(allocate[i,j]):')
    model.printAttr('X')
    
    print('SOLUTION:')
    for j in range(instance.numTeams):
        print('Users in the team %s: ' % j, end='')
        for i in range(instance.numUsers):
            if varAllocation[i,j].x != 0:
                print(i, end=' ')
        print('')


    status = model.status
    if status == GRB.Status.UNBOUNDED:
        print('The model cannot be solved because it is unbounded')
        #exit(0)
    elif status == GRB.Status.OPTIMAL:
        print('The optimal objective is %g' % model.objVal)
        #exit(0)
    elif status != GRB.Status.INF_OR_UNBD and status != GRB.Status.INFEASIBLE:
        print('Optimization was stopped with status %d' % status)
        #exit(0)

    print('       ---------- Outras informacoes ----------')
    model.printQuality()
    model.printStats()


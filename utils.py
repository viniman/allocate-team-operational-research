#!/usr/bin/python


from gurobipy import *
import matplotlib.pyplot as plt
import time
import csv
import model


def saveSolution(instance, model, varAllocation):
    '''
        Salva solucao em arquivo de saida do tipo csv
        Solucoes ficam na pasta de 'solutions'
    '''

    print('\n------------ Salvando solucao em arquivo de saida ------------')
    print('          CAMINHO DA INSTANCIA:', instance.name)

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
            


def printSolution(instance, model, varAllocation):
    '''
        Impressao da solucao do modelo
        Juntamente com a plotagem da solucao a
        a partir de um gráfico de dispersão
    '''


    print('------------- Impressao de solucao do modelo -------------')
    print('Valor da solução objetivo (MAX): %g' % model.objVal)
    print('\n   ------ Alocacao das variaveis ------')
    print('Pessoa i alocada no time j(allocate[i,j]):')
    model.printAttr('X')
    
    # Neste ponto, é feito loops de range de equipe e usuário
    # A fim de imprimir a solucao por equipes e também
    # criar uma lista que serve para plotagem do gŕafico
    listadeListas=[]
    print('SOLUTION:')
    for j in range(instance.numTeams):
        print('Users in the team %s: ' % j, end='')
        listax=[]
        listay=[]
        
        for i in range(instance.numUsers):
            if varAllocation[i,j].x != 0:
                print(i, end=' ')
                listax.append(j)
                listay.append(instance.beneffits[i][j])
                grupo = (listax,listay)
                #print('Quantidade: %g' % abs(len(lista)))
                
        listadeListas.append(grupo)
        listax.clear
        listay.clear
        print('')
        
       # print('Quantidade de grupos com listas: %g' % abs(len(listadeListas)))
    
             
   
    '''
    Plota grafico para auxiliar na visualizacao das solucoes por meio visual
    No eixo x temos as equipes das quais sao identificadas por numeros
    No eixo y temos o benefício do usuario ser alocado

    Podemos ver nesse gráfico, como é a qualidade da solução quando pensado
    também em níveis de diversidade, pois a empresa pode querer dar oportunidades
    para quem está começando a carreira, como também precisa de pessoas para
    gerenciar tais equipes, além de ter aquelas pessoas que são medianas e 
    se comprometem para o beneficio da empresa.

    Assim podemos ver uma solução bem diversificada, onde não só os melhores foram
    escolhidos, mas que também houve oportunidade para os que tem pouca experiencia
    se aprimorarem como profissionais.
    '''

    cores=("#FFD700","#00FFFF", "red", "green","pink","black", "yellow", "purple","orange","white","brown","#808000","#556B2F","#8A2BE2","#C71585","#FFE4C4","#FF4500","#FF69B4","#2F4F4F","#00FA9A","#FFD700","#00FFFF", "red", "green","pink","black", "yellow", "purple","orange","white", "purple","orange","white","brown","#808000","#556B2F","#8A2BE2","#C71585","#FFE4C4","#FF4500","#FF69B4","#FFD700","#00FFFF", "red", "green","pink","black", "yellow", "purple","orange","white","brown","#808000","#556B2F","#8A2BE2","#C71585","#FFE4C4","#FF4500","#FF69B4","#2F4F4F","#00FA9A","#FFD700","#00FFFF", "red", "green","pink","black","black", "yellow", "purple","orange","white","brown","#808000","#556B2F","#8A2BE2","#C71585","#FFE4C4","#FF4500","#FF69B4","#2F4F4F","#00FA9A","#FFD700","#00FFFF", "red", "green","pink","black", "yellow", "purple","orange","white", "purple","orange","white","brown","#808000","#556B2F","#FFD700","#00FFFF", "red", "green")
    labels=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80")
  
    # Create plot
    fig = plt.figure()
    
    ax = fig.add_subplot(1, 1, 1, facecolor='#E6E6E6')

    for data, color, group in zip(listadeListas,cores, labels):
        x, y = data
        ax.scatter(x, y, alpha=1.0, c=color, edgecolors='none', s=35, label=group)
 
    # titulo do grafico
    plt.title('Usuários X Equipes')

    plt.show()
    
 
    # insere legenda dos estados
    # plt.legend(loc=1)
        
        
        
    # Verifica status do modelo e imprime dado sua caracteristica
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

    print('\n       ---------- Outras informacoes ----------')
    # informacoes sobre qualidade do modelo
    model.printQuality()
    # algumas estatisticas referente ao modelo
    model.printStats()



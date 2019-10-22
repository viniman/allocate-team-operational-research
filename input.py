

class Instance:

    '''
        Classe de leitura de instancias
        Salva todos os atributos necessários
    '''

    name = None
    numUsers = None
    numTeams = None
    minMembersTeam = []
    maxMembersTeam = []
    lowerXp = []
    upperXp = []
    qtdUsersMinXp = []
    qtdUsersMaxXp = []
    beneffits = []
    langXp = []

    def __init__(self, filepath):
        '''
            Construtor da instancia a partir de uma caminho para a instancia
        '''
        self.setNameInstance(filepath)
        print('+'*60)
        print('Leitura de Instância'.rjust(40))
        print('+'*60)
        print('\nInstance Path: ', filepath)
        print('Instance Name: ', self.name)
        self.readInstance(filepath)


    def setNameInstance(self, filepath):
        '''
            Seta nome da instancia
        '''

        self.name = filepath.replace('\\','/').split(sep='/')[-1].split(sep='.')[0]


    def readInstance(self, filepath):
        '''
            Leitura da instancia
            É feito da seguinte forma
            Vai pegando linha por linha e splitando e transformando
            em dados separados para associar a instancia
        '''

        try:
            with open(filepath,'r') as inputFile:
                line = inputFile.readline()
                line = line.split()
                self.numUsers = int(line[0])
                self.numTeams = int(line[1])
                line = inputFile.readline().split()
                self.minMembersTeam.extend(list(map(int, line)))
                line = inputFile.readline().split()
                self.maxMembersTeam.extend(list(map(int, line)))
                line = inputFile.readline().split()
                self.lowerXp.extend(list(map(float, line)))
                line = inputFile.readline().split()
                self.qtdUsersMinXp.extend(list(map(int, line)))
                line = inputFile.readline().split()
                self.upperXp.extend(list(map(float, line)))
                line = inputFile.readline().split()
                self.qtdUsersMaxXp.extend(list(map(int, line)))
                cont = 0
                
                # loop para pegar a experiencia de cada usuario para cada grupo
                for i in range(self.numUsers):
                    cont+=1
                    line = inputFile.readline().split()
                    line = list(map(float, line))
                    self.langXp.append(line)

                # loop para pegar o peso de cada usuario para cada grupo
                for i in range(self.numUsers):
                    line = inputFile.readline().split()
                    line = list(map(float, line))
                    self.beneffits.append(line)
        except (IOError, OSError) as e:
            print('\n-------------- Algo de errado aconteceu! -------------')
            print('Python details:\n', e)
            print('-------------- Encerramento do algoritmo -------------\n')
        else:
            print('\n---------- Leitura de instancia feita com sucesso ----------')
            print('+'*60)
            

class Instance:
    numUsers = None
    numTeams = None
    minMembersTeam = []
    maxMembersTeam = []
    lowerXp = [] # minExperienceLangTeam
    upperXp = [] # maxExperienceLangTeam
    qtdUsersMinXp = [] # qtdUsersForMinXp
    qtdUsersMaxXp = [] # qtdUsersForMaxXp
    beneffits = []
    langXp = [] # langExperience

    def __init__(self, filepath):
        print('Leitura de Instância')
        self.readInstance(filepath)
        print('++++++++++++++++++++++++++++')
        print(self.numTeams)
        print(self.numUsers)
        print(self.minMembersTeam)
        print(self.maxMembersTeam)
        print(self.lowerXp)
        print(self.upperXp)
        print(self.qtdUsersMaxXp)
        print(self.qtdUsersMinXp)
        print(self.beneffits)
        print(self.langXp)
        
        print('++++++++++++++++++++++++++++')

    def readInstance(self, filepath):
        with open(filepath,'r') as inputFile:
            line = inputFile.readline()
            line = line.split()
            self.numUsers = int(line[0])
            self.numTeams = int(line[1])
            print(self.numUsers, self.numTeams)
            line = inputFile.readline().split()
            print(line)
            self.minMembersTeam.extend(list(map(int, line)))
            print(self.minMembersTeam)
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
            print('adasdasdasdasdaada', self.qtdUsersMaxXp)
            cont = 0
            for i in range(self.numUsers):#while cont < users:
                cont+=1
                print(line)
                line = inputFile.readline().split()
                line = list(map(float, line))
                self.langXp.append(line)
                print(line)

            for i in range(self.numUsers):#while line: # line
                print(line)
                line = inputFile.readline().split()
                line = list(map(int, line))
                self.beneffits.append(line)
                print(line)
            
            print(self.langXp)
            print(self.beneffits)

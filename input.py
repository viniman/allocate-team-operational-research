
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
        print('++++++++++++++++++++++++++++')
        print('    Leitura de Instância')
        print('++++++++++++++++++++++++++++')
        self.readInstance(filepath)

    def readInstance(self, filepath):
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
            for i in range(self.numUsers):#while cont < users:
                cont+=1
                line = inputFile.readline().split()
                line = list(map(float, line))
                self.langXp.append(line)

            for i in range(self.numUsers):#while line: # line
                line = inputFile.readline().split()
                line = list(map(float, line))
                self.beneffits.append(line)
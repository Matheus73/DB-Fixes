templatePK = 'CONSTRAINT {}_PK PRIMARY KEY ({})'
templateFK = 'CONSTRAINT {}_{}_FK FOREIGN KEY {}\n   REFERENCES {}{}'

def getData(path):
  file = open(path, "r").read()
  return file[:file.find("ALTER")], file[file.find("ALTER"):] # separando os create dos alter

def formatAlter(alterTables:str):
  splitedTables=[]

  alterTables = alterTables.split(";\n") #quebrando cada comando em uma string

  for line in alterTables:
    splitedTables.append(" ".join(line.split())) # tirando espaços e juntanto tudo numa linha só
  
  for x in range(0, len(splitedTables)):
    splitedTables[x] = splitedTables[x].replace('ALTER TABLE ', '').replace('ADD CONSTRAINT ', '').replace('FOREIGN KEY ', '').replace('REFERENCES ', '') #tira altertable e add constraint
    splitedTables[x] = splitedTables[x].replace(splitedTables[x].split(' ')[1]+' ','') #remove nome tosco de constraint
    splitedTables[x] = splitedTables[x][:splitedTables[x].rfind(")")+1] #tira tudo dps do ultimo ")"
    splitedTables[x] = splitedTables[x].replace(', ', '--').split(' ') #caso tenha 2 foreins 
    splitedTables[x][1] = splitedTables[x][1].replace('--', ', ') #desfazendo
    splitedTables[x][3] = splitedTables[x][3].replace('--', ', ') #desfazendo

    splitedTables[x] = [splitedTables[x][0],templateFK.format(
      splitedTables[x][0],
      splitedTables[x][2],
      splitedTables[x][1],
      splitedTables[x][2],
      splitedTables[x][3]
    )]

    #print(splitedTables[x]+'\n')
  return splitedTables

def formatCreate(createTables):
  pos=''
  tableName=''
  pkName=''
  constraints = []
  createTables = createTables[createTables.rfind('/')+1:].strip()
  createTables = createTables.split(';')
 # print(createTables)
  for x in range(0, len(createTables)):
    createTables[x] = createTables[x].strip().split('\n')
    tableName = createTables[x][0].replace('CREATE TABLE ', '').replace(' (', '')
    for y in range(0, len(createTables[x])):
      pkName = 'NONE'
      pos = createTables[x][y].strip().find('PRIMARY KEY')
      if(pos != -1):
        if(pos==0):
          #createTables[x][y] = '    CONSTRAINT '+tableName+'_PK '+createTables[x][y].strip()+'\n)'
          constraints.append([tableName, 'CONSTRAINT '+tableName+'_PK '+createTables[x][y].strip()])
        else:
          pkName = createTables[x][y].strip()[:createTables[x][y].strip().find(' ')]
          #createTables[x].append(',    '+templatePK.format(tableName, pkName) + ')\n)')
          #createTables[x][y] = createTables[x][y].replace('PRIMARY KEY', '')
          if(not tableName.islower()):
            constraints.append([tableName, templatePK.format(tableName, pkName)])       
    #try:
    #  createTables[x].remove(')')
    #except:
    #  pass
  return constraints
  

  
        




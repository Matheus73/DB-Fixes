def generate_list(file:str):
    my_file = open(file, "r")
    content_list = [line.strip() for line in my_file.readlines()]

    tables = {}
    flag = False
    aux = ''
    primarys = []
    for i in content_list:
        if "CREATE TABLE" in i:
            aux = i.split()[2]
            flag = True
            tables[aux] = [i]
        elif ';' in i:
            if len(primarys) != 0:
                tables[aux][-1] += ','
                tables[aux].append(primarys[0])
            flag = False 
            aux = ''
            primarys = []
        elif flag:
            if 'PRIMARY KEY,' in i:
                atr = i.split()[0]
                final = f"CONSTRAINT {aux}_PK PRIMARY KEY ({atr})"
                primarys.append(final)
                i = i.replace('PRIMARY KEY','')
                tables[aux].append(i)
            elif 'PRIMARY KEY (' in i:
                final = f"CONSTRAINT {aux}_PK {i.replace('_',' ')}"
                tables[aux].append(final)
            else: 
                tables[aux].append(i)


    constraints = {}
    flag = False
    aux = ''
    for i in tables:
        constraints[i] = []


    atributes = ''
    references = ''
    name_ref = ''
    for i in content_list:
        if 'ALTER TABLE' in i:
            aux = i.split()[2]
            flag = True
        elif flag and 'FOREIGN' in i:
            atributes = i
        elif flag and 'REFERENCES' in i:
            references = i
            name_ref = i.split()[1]

            final = f"CONSTRAINT {aux}_{name_ref}_FK {atributes} {references}".translate({ord(';'): None})

            flag = False
            constraints[aux].append(final)

            
    for i in constraints:
        if len(constraints[i]) == 0:
            tables[i].append(')ENGINE=innoDB;')
        else:
            for cons in constraints[i]:
                tables[i][-1] += ','
                tables[i].append(cons)
                if cons == constraints[i][-1]:
                    tables[i].append(')ENGINE=innoDB;')



    for key in tables:
        # print(f"-- {key}")
        for i in tables[key]:
            print(i)
        print('\n')

            
    return  tables

name = input("Digite o nome do arquivo gerado pelo BRMODELO: ")
generate_list(name)



import functions

menu = """
        Opções de atributos:
+---------------+-------------------------------------------------------+
| opcoes        | definicao                                             |
+---------------+-------------------------------------------------------+
| cpf           | Gera um cpf aleatorio                                 |
| nome          | Gera um nome de pessoa aleatorio                      |
| cnpj          | Gera um CNPJ aleatorio                                |
| data          | Gera uma data aleatoria de 1980 a 2015                |
| estado-cidade | Gera dois atributos sendo eles um estado e uma cidade |
| random(n)     | Gera um inteiro com N algarismos                      |
| placa         | Gera uma placa de veiculo aleatoriamente              |
| chassi        | Gera um chassi de um veiculo aleatoriamente           |
| cor           | Gera uma cor                                          |
| telefone      | Gera um numero de telefone com area e DDD             |
| cep           | Gera um CEP aleatorio                                 |
+---------------+-------------------------------------------------------+
"""

if __name__ == '__main__':
    table = input("Qual o nome da tabela? ")

    n = int(input("Quantas tuplas gostaria de adicionar na tabela? "))

    print(menu)

    atributes = input("Quais atributos gostaria de add? (separados por espaco) ").split()

    s = f"INSERT INTO {table}( "
    for i in atributes:
        if i == atributes[-1]:
            s = s + i
        else:
            s = s + i + ', '

    s += ') VALUES'
    print(s)



    lines = []
    for i in range(n):
        tmp = []
        for atr in atributes:
            if atr == 'cpf':
                tmp.append(functions.generate_cpf())
            elif atr == 'nome':
                tmp.append(functions.generate_name())
            elif atr == 'cnpj':
                tmp.append(functions.generate_cnpj())
            elif atr == 'data':
                tmp.append(functions.generate_date())
            elif atr == 'estado-cidade':
                b = functions.generate_city()
                tmp.append(b[0])
                tmp.append(b[1])
            elif 'random' in atr:
                num = int(atr[-3:-1])
                tmp.append(functions.generate_random_value(num))
            elif atr == 'placa':
                tmp.append(functions.generate_car_license())
            elif atr == 'chassi':
                tmp.append(functions.generate_chassi())
            elif atr == 'cor':
                tmp.append(functions.generate_color())
            elif atr == 'telefone':
                tmp.append(functions.generate_phone())
            elif atr == 'cep':
                tmp.append(functions.generate_cep())
        lines.append(tmp)


    for i in lines:
        if i == lines[-1]:
            print(tuple(i),';')
        else:
            print(tuple(i),',')





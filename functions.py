import datetime
import random

list_letters_upper = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'X',
        'Y',
        'Z',
        ]

list_letters_lower = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'x',
        'y',
        'z',
        ]

def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def generate_cnpj():
    def calculate_special_digit(l):
        digit = 0

        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)

        digit = 11 - digit % 11

        return digit if digit < 10 else 0

    cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])


def generate_name():
    list_names = ['Maria','Joao','Raimundo','Henrique','Ana','Eduardo','Pedro']
    list_surnames = ['Pinto','da Cunha','de Lima','Alves','Rodrigues','Melo']

    return random.choice(list_names) + ' ' + random.choice(list_surnames)

def generate_date():
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2015, 1, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return str(random_date)

def generate_city():
    list_cities = [
            ('DF','Gama'),
            ('DF','Guara'),
            ('DF','Samambaia'),
            ('RJ', 'Rio de Janeiro'),
            ('RJ', 'Bangu'),
            ('SP', 'Sao Paulo'),
            ('SP', 'Santos'),
            ('SP', 'Blumenal'),
            ('SP', 'Braganca'),
            ('SP', 'Mirassol'),
            ('MG', 'Buritis'),
            ('MG', 'Belo Horizonte'),
            ('MG', 'Uberlandia'),
            ('BA', 'Salvador'),
            ('BA', 'Juazeiro'),
            ('BA', 'Vitoria'),
            ('TO', 'Araguaina'),
            ('TO', 'Araguatins'),
            ('TO', 'Palmas'),
            ('GO', 'Goiania'),
            ('GO', 'Pedregal'),
            ('GO', 'Luziania'),
            ('GO', 'Anapolis'),
            ]
    tmp = random.choice(list_cities)
    # return f"'{tmp[0]}', '{tmp[1]}'"
    return tmp

def generate_random_value(tam):
    return random.randint(10**(tam-1), 10**(tam))

def generate_car_license():
    return random.choice(list_letters_upper) + random.choice(list_letters_upper) + random.choice(list_letters_upper) + str(random.randint(10**3,10**(4)))

def generate_chassi():
    chassi = ''
    for i in range(3):
        flag = random.randint(0,2)
        if flag == 0:
            chassi += random.choice(list_letters_lower)
        elif flag == 1:
            chassi += random.choice(list_letters_upper)
        else:
            chassi += str(random.randint(0,9))

    chassi += ' '

    for i in range(6):
        flag = random.randint(0,2)
        if flag == 0:
            chassi += random.choice(list_letters_lower)
        elif flag == 1:
            chassi += random.choice(list_letters_upper)
        else:
            chassi += str(random.randint(0,9))

    chassi += ' '


    for i in range(2):
        flag = random.randint(0,2)
        if flag == 0:
            chassi += random.choice(list_letters_lower)
        elif flag == 1:
            chassi += random.choice(list_letters_upper)
        else:
            chassi += str(random.randint(0,9))

    chassi += ' '

    for i in range(6):
        flag = random.randint(0,2)
        if flag == 0:
            chassi += random.choice(list_letters_lower)
        elif flag == 1:
            chassi += random.choice(list_letters_upper)
        else:
            chassi += str(random.randint(0,9))

    return chassi

def generate_color():
    colors = [
            "verde",
            "amarelo",
            "rosa",
            "preto",
            "prata",
            "vermelho",
            "vinho",
            "azul",
            "branco",
            "bege"
            ]
    return random.choice(colors)

def generate_phone():
    phone = f'+55 ({random.randint(10,99)}) 9{random.randint(10**3,10**4 -1)}-{random.randint(10**3,10**4 -1)}'
    return phone

def generate_cep():
    cep = f"{random.randint(10**4,10**5 -1)}-{random.randint(10**2,10**3 -1)}"
    return cep

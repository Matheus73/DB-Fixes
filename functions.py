import datetime
import random
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
    list_letters = [
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
    return random.choice(list_letters) + random.choice(list_letters) + random.choice(list_letters) + str(random.randint(10**3,10**(4)))

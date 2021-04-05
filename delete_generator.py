def generate_list(file:str):
    my_file = open(file, "r")
    content_list = [line.strip() for line in my_file.readlines()]
    return content_list

if __name__ == "__main__":
    file = input("Digite o nome do arquivo que cria o banco de dados: ")

    file_lines = generate_list(file)

    tables = []
    use_line = ''
    for line in file_lines:
        if "CREATE TABLE" in line.upper():
            words = line.split()
            tables.append(words[2])
        elif "USE" in line.upper():
            use_line = line

    print(use_line)
    for index in range(len(tables)-1,-1,-1):
        print(f"DROP TABLE {tables[index]};")

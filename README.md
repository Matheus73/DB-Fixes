# DB Fixes

Repositório dedicado a scripts que automatizem tarefas da disciplina de
Sistemas de Banco de Dados 1 e 2 da Universidade de Brasília (UNB).

## Populador de tabelas (tuple generator)

![tuple generator example](assets/example.gif)
Script criado com o intuito de automatizar a tarefa de popular uma tabela com
dados de alta repetitividade como nome, CPF, cnpj.

### Funcionamento

O script irá solicitar uma série de dados obrigatórios para a geração de um 
script SQL, são esses:

* Nome da tabela
* Quantidade de tuplas que deseja criar
* Atributos das tuplas

este ultimo podendo ser:

* cpf

    Gera um cpf aleatório

* nome

    Gera um nome de pessoa aleatório

* data
    
    Gera uma data aleatória entre 1980 e 2015 podendo ser alterado o esse 
    range no script function.py

* cnpj
    
    Gera um cnpj aleatório

* random(n)
    
    Gera um codigo contendo um numero com **n** algarismos.

* estado-cidade

    Gera dois atributos para a tabela sendo um Estado do Brasil e um cidade deste estado

* placa

    Gera a placa de um veiculo aleatoriamente

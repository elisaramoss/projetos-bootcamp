#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).

import sqlite3

conexao = sqlite3.connect('banco.db2')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

2 Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES)(1, "João", 18, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES)(2, "Maria", 22, "Nutricao")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES)(3, "Pedro", 19, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES)(4, "Carla", 20, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES)(5, "Ana", 20, "Direito")')

3. Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
a) Selecionar todos os registros da tabela "alunos".
b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
d) Contar o número total de alunos na tabela

cursor.execute('SELECT * FROM alunos')
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
cursor.execute('SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome')
cursor.execute('SELECT COUNT(*) FROM alunos')

4 Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#b) Remova um aluno pelo seu ID.

#cursor.execute('UPDATE alunos SET idade = 23 WHERE id =1)
#cursor.execute('DELETE FROM alunos WHERE id = 2)

#5 Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(1,'João', 30, 1000.50);')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(2, "Maria", 20, 5000.50);')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES(3, "Pedro", 28, 15000.50);')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#b) Calcule o saldo médio dos clientes.
#c) Encontre o cliente com o saldo máximo.
#d) Conte quantos clientes têm saldo acima de 1000.

#cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
#cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#cursor.execute('SELECT COUNT(*) FROM cliente WHERE saldo > 1000')
conexao.commit()
conexao.close
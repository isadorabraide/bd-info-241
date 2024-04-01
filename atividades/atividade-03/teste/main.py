import sqlite3

# Conectar ao banco de dados (ou criar um, caso nao exista)

conexao = sqlite3.connect("TB_MUNICIPIOS.db")

# Criar uma tabela chamada municipio
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_municipios (
    id INTEGER PRIMARY KEY,
    nome_municipio TEXT NOT NULL,
    longitude_municipio TEXT NOT NULL,
    latitude_municipio TEXT NOT NULL
    )
""")

conexao.commit()

# Solicita a entrada do usuario
print("Informe o nome do municipio: ")
nomeMunicipio = input()

print("Informe  a latitude do municipio: ")
latitudeMunicipio = input()

print("Informe a longitude do municipio: ")
longitudeMunicipio = input()

# Inserir as informacoes na tabela

cursor.execute("INSERT INTO tb_municipios (nome_municipio, longitude_municipio, latitude_municipio) VALUES (?, ?, ?)", (nomeMunicipio, longitudeMunicipio, latitudeMunicipio))
conexao.commit()

# Encerra a conexao
conexao.close()

print("Dados inseridos com sucesso!")
print("Conexao com o banco de dados encerrada!")

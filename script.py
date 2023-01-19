# importando banco de dados sqlite3
import  sqlite3

# Criando conexão com banco de dados
conn = sqlite3.connect('crud.db')

# Cria um cursor para executar comando SQL
cursor = conn.cursor()

# Cria uma tabela
# cursor.execute("""CREATE TABLE crudpy (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")

# Inserindo dados na tabela
cursor.execute("INSERT INTO crudpy (name,age) VALUES  ('João', 30)" )
cursor.execute("INSERT INTO crudpy (name,age) VALUES  ('Maria', 29)" )


# Confirma
# conn.commit()


# Atualiza um dado da tabela
cursor.execute("UPDATE crudpy SET name ='Maria José' WHERE id = 2 ")
conn.commit()

# Deleta um dado da tabela
cursor.execute("DELETE FROM crudpy WHERE id = 1")
conn.commit()


# Visualizando os dados ta tabela crudpy
cursor.execute("SELECT * FROM crudpy")
print(cursor.fetchall())

# Fecha a conexão
conn.close()


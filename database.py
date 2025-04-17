import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def conectar_banco():
    conexao = sqlite3.connect("tarefas.db")
    return conexao



def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key, nome text, senha text)''')
    
    cursor.execute('''create table if not exists projetos_musicais
                   (id integer primary key, nome text, artista text, status text, letra text, caminho_capa text, email text,
                    FOREIGN KEY(email) REFERENCES usuarios(email))''')

    conexao.commit()




if __name__ == '__main__': 
    criar_tabelas()
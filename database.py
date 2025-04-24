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
    
    cursor.execute('''create table if not exists produtos
                   (id integer primary key, nome text, preco real, imagem text, email text,
                    FOREIGN KEY(email) REFERENCES usuarios(email))''')

    conexao.commit()


def fazer_login(formulario):
    # Ver se já existe esse email no banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT count(email) FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()

    quantidade_de_emails_cadastrados = cursor.fetchone()
    print(quantidade_de_emails_cadastrados)
    if (quantidade_de_emails_cadastrados[0] <= 0):
        print("LOG: Não existe esse e-mail cadastrado no banco!")
        return False
    else:
        cursor = conexao.cursor()
        cursor.execute('''SELECT senha FROM usuarios WHERE email=?''', (formulario['email'],))
        conexao.commit()
        senha_criptografada = cursor.fetchone()
        resultado_verificacao = check_password_hash(senha_criptografada[0], formulario['password'])
        return resultado_verificacao


def criar_usuarios(formulario):
    # Ver se já existe esse email no banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT count(email) FROM usuarios WHERE email=?''', (formulario['email'],))
    conexao.commit()
    
    quantidade_de_emails_cadastrados = cursor.fetchone()
    print(quantidade_de_emails_cadastrados)
    if (quantidade_de_emails_cadastrados[0 > 0]):
        print("LOG: Já existe esse e-mail cadastrado no banco!")
        return False
    
    senha_criptografada = generate_password_hash(formulario['senha'])
    cursor.execute('''INSERT INTO usuarios (email, nome, senha)
                    VALUES (?, ?, ?)''',
                    (formulario['email'], formulario['usuario'], senha_criptografada))
    conexao.commit() 
    return True


def selecionar_produtos(email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM produtos WHERE email=?''', (email,))
    return cursor.fetchall()


def selecionar_produto(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM produtos WHERE id=?''', (id,))
    return cursor.fetchone()


def criar_produto(nome, preco, caminho_imagem, email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO produtos (nome, preco, imagem, email)
                   VALUES (?, ?, ?, ?)''',
                    (nome, preco, caminho_imagem, email)) 
    conexao.commit()
    return True


def editar_produto(nome, preco, caminho_imagem, id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''UPDATE produtos SET nome=?, preco=?, imagem=? WHERE id=?''', (nome, preco, caminho_imagem, id))
    conexao.commit()
    cursor.close()


def excluir_produto(id):
    print(id)
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM produtos WHERE id=?''', (id,))
    conexao.commit()
    cursor.close()






if __name__ == '__main__': 
    criar_tabelas()
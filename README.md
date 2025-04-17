# 🛍️ Site de Produtos - Cadastro de Usuários

Este é um projeto simples de um site de produtos com sistema de autenticação de usuários. Ele permite que o usuário crie uma conta, faça login, edite suas informações e também exclua a conta, utilizando um visual moderno com efeito de fundo borrado (glassmorphism).


## Tecnologias Utilizadas

- Backend: Python com Flask
- Frontend: HTML, CSS e JavaScript
- Banco de Dados: SQLite3 com Python


## 🎨 Estilo visual

O site foi estilizado com **CSS puro**, utilizando a fonte **Poppins** e efeitos visuais como:
- Fundo com imagem em tela cheia.
- Efeito de vidro (blur) nas caixas de formulário.
- Ícones de formulário com **Font Awesome**.
- Estilo responsivo e minimalista.

## ✅ Casos de Uso

1.Criar conta

- Formulário: Nome, E-mail, Senha.
- Cadastro na tabela de usuários


2.Fazer login

- Verificação de e-mail e senha.
- Se válido, manter login com sessão (session do Flask).

3.Excluir conta

- Remover usuário da tabela.

4.Criar produtos 
- Formulário: Nome do produto e o preço.
- Opcional: Upload de uma capa de imagem.


5.Editar produtos
- Alterar informações: Nome, Preço e imagem.

## 📁 Estrutura de arquivos


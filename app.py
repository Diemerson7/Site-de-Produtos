from flask import Flask, render_template, request, session, url_for, redirect, flash

import database

app = Flask(__name__)
app.secret_key = "chave_muito_segura"



























if __name__ == '__main__':
    app.run(debug=True)
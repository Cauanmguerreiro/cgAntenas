from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('C:\Users\cauan\Documents\PROJETOS\cgAntenas\cgAntenas')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <title>Formulário</title>
        </head>
        <body>
            <h2>FALE <span>COMIGO</span></h2>
            <form action="/submit" method="post">
                <input type="text" name="name" placeholder="Seu nome" required>
                <input type="email" name="email" placeholder="Seu email" required>
                <textarea name="message" placeholder="Sua mensagem" required></textarea>
                <button type="submit">Enviar</button>
            </form>
        </body>
        </html>
    ''')

# Rota que lida com o envio do formulário
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return f'Obrigado, {name}. Entraremos em contato em breve.'

if __name__ == '__main__':
    app.run(debug=True)
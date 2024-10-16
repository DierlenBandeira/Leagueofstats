from flask import Blueprint, render_template, request, redirect, make_response
import requests

AIRTABLE_API_KEY = 'patzngZgXWMoCC5JB.d9a3cf3e0c393b75e51d8ff989891c9213e08557a8ddd420dbbcce4da6923ee3'
AIRTABLE_BASE_ID = 'appxqqYv5xlJbOQty'
AIRTABLE_TABLE_NAME = 'tblN3n7YikPGQPWcp'

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Pegando os dados do formulário corretamente
        user = request.form.get('user')
        password = request.form.get('password')

        # Verificar as credenciais no Airtable
        url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
        headers = {
            'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        }
        params = {
            'filterByFormula': f"AND(user = '{user}', password = '{password}')"
        }

        response = requests.get(url, headers=headers, params=params)
        records = response.json().get('records', [])

        if len(records) > 0:
            # Se as credenciais conferem, redireciona para o dashboard
            return redirect('/dashboard')
        else:
            # Caso contrário, retorna ao login com uma mensagem de erro
            return redirect(url_for('login.login', error='true'))

    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return render_template('login.html')


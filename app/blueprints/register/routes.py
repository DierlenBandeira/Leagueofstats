from flask import Blueprint, render_template, request, redirect
import requests

AIRTABLE_API_KEY = 'patzngZgXWMoCC5JB.d9a3cf3e0c393b75e51d8ff989891c9213e08557a8ddd420dbbcce4da6923ee3'
AIRTABLE_BASE_ID = 'appxqqYv5xlJbOQty'
AIRTABLE_TABLE_NAME = 'tblN3n7YikPGQPWcp'

register_bp = Blueprint('register', __name__)

@register_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        summoner = request.form.get('summoner')
        favorite_champion = request.form.get('favorite_champion')
        favorite_team = request.form.get('favorite_team')

        print("Dados recebidos do formulário:")
        print(f"User: {user}, Password: {password}, Summoner: {summoner}, Favorite Champion: {favorite_champion}, Favorite Team: {favorite_team}")

        # Enviar dados para o Airtable
        url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
        headers = {
            'Authorization': f'Bearer {AIRTABLE_API_KEY}',
            'Content-Type': 'application/json'
        }
        data = {
            'fields': {
                'user': user,
                'password': password,
                'summoner': summoner,
                'favorite_champion': favorite_champion,
                'favorite_team': favorite_team
            }
        }

        # Fazer a requisição para o Airtable
        print("Enviando dados para o Airtable...")
        response = requests.post(url, json=data, headers=headers)

        # Verificar o status da resposta
        print(f"Status da resposta do Airtable: {response.status_code}")
        print(f"Resposta do Airtable: {response.json()}")

        # Redirecionar de acordo com o resultado da requisição
        if response.status_code == 200:
            # Redirecionar para a página de login em caso de sucesso
            return redirect('/login')
        else:
            # Redirecionar para a página de registro com um parâmetro de erro
            return redirect('/register?error=true')

    # Renderizar a página de registro para requisições GET
    return render_template('register.html')

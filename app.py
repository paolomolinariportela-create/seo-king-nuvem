import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Credenciais do seu Painel de Parceiro (App ID: 24862)
CLIENT_ID = "24862"
CLIENT_SECRET = "COLE_AQUI_SEU_CLIENT_SECRET" # Importante!

@app.route('/auth/callback')
def auth_callback():
    # 1. Captura o código que a Nuvemshop envia
    code = request.args.get('code')
    
    if not code:
        return "Erro: Código de autorização não encontrado.", 400

    # 2. Troca o código pelo Access Token Permanente
    url = "https://www.nuvemshop.com.br/apps/authorize/token"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        token = data.get('access_token')
        user_id = data.get('user_id') # ID da loja instalada

        # 3. Aqui você salvaria o token no Banco de Dados
        print(f"✅ Loja {user_id} instalada! Token: {token}")
        
        return f"🚀 App SEO KING Instalado com Sucesso na Loja {user_id}!"
    else:
        return f"❌ Erro na autorização: {response.text}", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

<p align="center">
  
  <img src="https://i.pinimg.com/originals/b0/c2/98/b0c2988dae6c0f5b02e7433021a91f39.gif" width="100%">
</p>

---
# Bit a Bit - Tech Support Chatbot

## Desenvolvido para auxiliar e otimizar os estudos de acadêmicos em TI.  
**Autor:** IzaByte / [GitHub](https://github.com/IzaByte-Null)  
**Deploy / Link ao vivo:** [Render](https://bit-a-bit-quiz-1.onrender.com/)  
**Banco de dados / serviços externos:** [Neon](https://neon.com/)  



---

## 🔹 Visão Geral

Projeto acadêmico com backend completo em **Django REST Framework**, integrado a **Google Gemini API**, oferecendo um **chatbot inteligente** para suporte técnico e estudo.  
Hospedado de forma gratuita, com otimizações de banco de dados e gestão segura de chaves, mesmo enfrentando limitações de espaço no Render.

---

## ⚙️ Funcionalidades Principais

- CRUD de usuários  
- Autenticação e autorização segura  
- Integração com API externa (Google Gemini)  
- Regras de negócio personalizadas e validações  
- Chatbot de suporte a estudos em TI  
- Gerenciamento seguro de banco de dados, chaves e deploy gratuito

---

## 🛠 Tecnologias Utilizadas

**Backend / Python:**  
- Django 5.x  
- Django REST Framework  
- SimpleJWT, Gunicorn, Whitenoise  

**Bibliotecas auxiliares:**  
- Google Generative AI (Gemini)  
- Requests, Pydantic, Tenacity, Pillow, etc. 
- python-dotenv (Gestão de variáveis de ambiente)
- google-genai (SDK oficial do Gemini 2.0+)
- psycopg2-binary (Adaptador PostgreSQL para Neon) 

**Frontend:**  
- HTML, CSS, JavaScript  

**Banco de Dados:**  
- PostgreSQL (Neon)  

**Deploy:**  
- Render  

---

## 🏗 Estrutura do Projeto

```text
IzaByte-Null/
├── backend_api/         # Configuração do backend principal
├── fotos_perfil/        # Imagens de perfil ou assets
├── quiz/                # Módulo ou app específico do quiz
├── static/css/          # Arquivos CSS estáticos
├── templates/           # HTML templates
├── usuarios/            # App Django para gerenciamento de usuários
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---
## 🚀 Como Executar Localmente
#Pré-requisitos

#Python >= 3.9

#PIP atualizado

#Google Gemini API Key

## Passo a Passo
# 1. Criar virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar migrations
python manage.py migrate

# 4. Executar servidor
python manage.py runserver

http://[IP pessoal]

# Deploy no Render
- Build Command
- pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate

# Start Command
- gunicorn backend_api.wsgi:application
- Configurar GOOGLE_API_KEY nas Environment Variables no painel do Render

---
## 🧩 Lógica Principal / Diferenciais
from rest_framework.views import APIView
from rest_framework.response import Response
import google.generativeai as genai

genai.configure(api_key="YOUR_KEY_HERE")

class GeminiView(APIView):
    def post(self, request):
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({"error": "Prompt não fornecido"}, status=400)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return Response({"resposta": response.text})

- Recebe prompts do frontend e retorna respostas inteligentes focadas em TI / estudos.
Diferencial: integração do chatbot em backend totalmente funcional.

- O diferencial deste projeto é a capacidade de **observabilidade** e **rastreabilidade** das interações da IA. 

### Fluxo de Ingestão de Dados:
1. **Captura de Metadados:** O backend identifica o `IP de Origem` do usuário através do Header `HTTP_X_FORWARDED_FOR` (essencial para Cybersec).
2. **Processamento:** A pergunta é enviada ao Gemini 2.0 Flash com instruções de sistema (System Instructions) para manter o foco em T.I.
3. **Persistência (Sink):** A pergunta, a resposta da IA e os metadados do usuário são persistidos em tempo real na tabela `quiz_historicobot` no PostgreSQL (Neon).



```sql
-- Exemplo da Query de Monitoramento que utilizo no Neon:
SELECT u.username, h.pergunta_usuario, h.ip_origem, h.data_interacao
FROM quiz_historicobot h
JOIN auth_user u ON h.usuario_id = u.id
ORDER BY h.data_interacao DESC;

```

---
## 📚 Contribuições

IzaByte-Null: Backend completo, integração com Gemini API, regras de negócio, validações, CRUD de usuários, deploy no Render, gestão segura de banco de dados, JS.

Frontend / Design: Criado pelo grupo, HTML/CSS.

Diferencial: Chatbot de suporte aos estudos e integração de lógica de negócios personalizada.

---

# 🔹 Notas & Créditos

Google Gemini API usado sob Termos de Serviço

Projeto acadêmico e pessoal


<p align="center">                     <img src="https://i.pinimg.com/originals/68/43/cc/6843cc365df18febde115bc70eb15290.gif" width="100%"> </p> ```

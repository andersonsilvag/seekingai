🔥 Django + REST + DeepSeek + OpenAI Chat API
Um projeto integrado que permite escolher entre APIs de chat da DeepSeek e OpenAI diretamente na interface.

🛠️ Tecnologias Principais
Tecnologia	Versão
Python	3.11+
Django	5.2.4
Django REST Framework	3.16.0
🚀 Começando
Pré-requisitos
Git (como instalar)

Python 3.11+ (download)

Pip (vem com Python)

⚡ Instalação Rápida
bash
# Clone o repositório
git clone https://github.com/andersonsilvag/seekingai
cd projeto-chat-api

# Crie e ative o ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
🔐 Configuração de Chaves de API
Crie um arquivo .env baseado no exemplo:

bash
cp .env.example .env
Adquira suas chaves:

🔑 DeepSeek API Key: https://platform.deepseek.com/sign_in

🔑 OpenAI API Key: https://platform.openai.com/api-keys

Edite o .env:

env
OPENAI_API_KEY=sua_chave_aqui
DEEPSEEK_API_KEY=sua_chave_aqui
SECRET_KEY=sua_secret_key_django
🖥️ Executando o Projeto
bash
# Aplicar migrações
python manage.py migrate

# Criar superusuário (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
Acesse: http://localhost:8000

🌟 Recursos Principais
✅ Troca fácil entre APIs de chat

✅ Configuração via variáveis de ambiente

✅ Design minimalista com poucas dependências

✅ Fácil integração com outras APIs

⁉️ Suporte
Problemas? Abra uma issue

✨ Dica do Desenvolvedor
"Recomendo testar ambas APIs para comparar desempenho e resultados em diferentes cenários de chat!"

## 📜 Licença
Este projeto está licenciado sob a [MIT License](/LICENSE) - © 2025 [Anderson da Silva Gonçalves](https://github.com/andersonsilvag).
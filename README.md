# Drugstore Project - Infrastructure & Auth Service

## 📋 Sobre o Projeto
Este diretório contém a **Infraestrutura** e o **Microsserviço de Autenticação** do sistema **PharmaCare**. 
Seguindo as boas práticas de arquitetura de microsserviços, a autenticação foi desacoplada do backend principal para garantir maior segurança, escalabilidade e independência.

Este serviço é responsável por:
- Gerenciar o ciclo de vida dos usuários (Cadastro, Login).
- Emitir tokens de acesso (JWT) seguros.
- Validar credenciais.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Banco de Dados:** PostgreSQL (Conectado ao mesmo banco ou instância separada)
- **Autenticação:** JWT (JSON Web Tokens) + Passlib (Hashing)
- **Containerização:** Docker
- **Deploy:** Render (PaaS)

## 📂 Estrutura
- `app/`: Código fonte do serviço de autenticação.
- `Dockerfile`: Configuração para containerização do serviço.
- `requirements.txt`: Dependências do projeto.

## 🐳 Como Rodar Localmente (Docker)

1. **Navegue até a pasta:**
   ```bash
   cd Drugstore_Project/Infrastructure/Infrastructure
   ```

2. **Construa e inicie o container:**
   ```bash
   docker build -t drugstore-auth .
   docker run -p 8001:8000 --env-file .env drugstore-auth
   ```
   *Nota: Certifique-se de ter um arquivo `.env` configurado com as credenciais do banco.*

## ☁️ Como implantar no Render (Produção)

1.  **Crie um novo repositório no GitHub** apenas para este serviço (ou use um monorepo, mas configure o Root Directory).
    *   Se for um repositório separado:
        ```bash
        # Estando na pasta Infrastructure
        git init
        git add .
        git commit -m "Initial commit Auth Service"
        git remote add origin <SEU_NOVO_REPO_URL>
        git push -u origin main
        ```

2.  **Acesse o Render (dashboard.render.com)**.

3.  **Crie um novo Web Service**.

4.  **Conecte ao seu repositório GitHub** (o repositório Infrastructure).

5.  **Configure o serviço**:
    *   **Name**: `drugstore-auth`
    *   **Runtime**: `Docker`
    *   **Region**: Escolha a mais próxima (ex: Ohio ou Frankfurt).
    *   **Branch**: `main` (ou a branch que você estiver usando)
    *   **Root Directory**: `.` (pois o Dockerfile está na raiz deste repositório).

6.  **Variáveis de Ambiente (Environment Variables)**:
    Adicione as seguintes variáveis no Render:
    *   `DB_HOST`: Host do seu banco de dados (pode ser o mesmo do backend principal ou um novo).
    *   `DB_NAME`: Nome do banco.
    *   `DB_USER`: Usuário do banco.
    *   `DB_PASSWORD`: Senha do banco.
    *   `DB_PORT`: `5432`
    *   `SECRET_KEY`: A mesma chave usada no Backend principal (para que ele possa validar os tokens gerados aqui).
    *   `ACCESS_TOKEN_EXPIRE_MINUTES`: `60`

7.  **Deploy**: Clique em "Create Web Service".

## 🔗 Endpoints Principais

*   `POST /auth/register`: Cria um novo usuário.
*   `POST /auth/login`: Autentica e retorna um token JWT.
*   `GET /health`: Verifica a saúde do serviço.

# Auth Service

Este é o microsserviço de autenticação do Drugstore Project.

## Como implantar no Render

1.  **Crie um novo repositório no GitHub** apenas para este serviço (ou use um monorepo, mas configure o Root Directory).
    *   Se for um repositório separado:
        ```bash
        cd Drugstore_Project/Auth_Service
        git init
        git add .
        git commit -m "Initial commit Auth Service"
        git remote add origin <SEU_NOVO_REPO_URL>
        git push -u origin main
        ```

2.  **Acesse o Render (dashboard.render.com)**.

3.  **Crie um novo Web Service**.

4.  **Conecte ao seu repositório GitHub**.

5.  **Configure o serviço**:
    *   **Name**: `drugstore-auth`
    *   **Runtime**: `Docker`
    *   **Region**: Escolha a mais próxima (ex: Ohio ou Frankfurt).
    *   **Branch**: `main`
    *   **Root Directory**: `.` (se for repo separado) ou `Drugstore_Project/Auth_Service` (se for monorepo).

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

## Endpoints

*   `POST /auth/register`: Cria um novo usuário.
*   `POST /auth/login`: Retorna um token JWT.
*   `GET /health`: Verifica se o serviço está online.

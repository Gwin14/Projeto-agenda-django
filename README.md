# Projeto Agenda Django

Este é um projeto de agenda desenvolvido com Django. A aplicação permite aos usuários criar, editar e gerenciar contatos.

## Funcionalidades

- **Adicionar contatos:** Crie novos contatos com informações detalhadas.
- **Editar contatos:** Atualize as informações de contatos existentes.
- **Remover contatos:** Exclua contatos que não são mais necessários.
- **Visualizar contatos:** Veja a lista de todos os contatos e os detalhes de cada um.

## Estrutura do Projeto

```bash
Projeto-agenda-django-main/
├── base_static/
│   └── global/
│       └── css/
│           └── style.css
├── base_templates/
│   └── global/
│       └── base.html
│       └── partials/
│           └── _head.html
│           └── _header.html
├── contact/
│   ├── migrations/
│   ├── templates/
│   │   └── contact/
│   │       └── contact.html
│   │       └── create.html
│   │       └── index.html
│   │       └── login.html
│   │       └── register.html
│   │       └── user_update.html
│   │       └── partials/
│   │           └── _user-form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Requisitos

- Python 3.x
- Django 3.x

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Projeto-agenda-django.git
```

2. Navegue até o diretório do projeto:

```bash
cd Projeto-agenda-django-main
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate # No Windows, use `venv\Scripts\activate`
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Realize as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

7. Acesse a aplicação em seu navegador:

```
http://127.0.0.1:8000/
```

## Uso

1. Crie uma conta ou faça login.
2. Adicione novos contatos, edite os existentes e gerencie sua agenda de forma eficiente.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT.

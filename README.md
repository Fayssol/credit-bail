# Projet Askia
## installation de python-dotenv
https://myapollo.com.tw/en/blog/python-dotenv/

## Éxecution du projet

### Tirer le projet sur github

```bash
git clone https://github.com/Fayssol/askia.git
```
### Créer un env à la racine du projet et installer les dependances

```bash
virtualenv askia_env
source askia_env/bin/activate
pip install -r requirements.txt

```

### La base de données

1- Dupliquer le fichier `askia/askia_solution/askia_solution/.env.exemple` en `.env` et remplisser l'intérieur :

```
DB_NAME=dbname
DB_USER=username
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port

```

2- Les migrations

```bash
 python3 manage.py makemigrations
 python3 manage.py makemigrations askia_admin
 python3 manage.py migrate

```
### Création d'un user

```bash
python3 manage.py createsuperuser
```

### Démarrer le serveur

```bash
python3 manage.py runserver
```
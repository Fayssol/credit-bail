[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMjEuMTE2NjY4NzAxMTcxODgiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAyMjEuMTE2NjY4NzAxMTcxODggMzUiPjxyZWN0IHdpZHRoPSIxMzUuMzAwMDAzMDUxNzU3OCIgaGVpZ2h0PSIzNSIgZmlsbD0iIzMxQzRGMyIvPjxyZWN0IHg9IjEzNS4zMDAwMDMwNTE3NTc4IiB3aWR0aD0iODUuODE2NjY1NjQ5NDE0MDYiIGhlaWdodD0iMzUiIGZpbGw9IiMzODlBRDUiLz48dGV4dCB4PSI2Ny42NTAwMDE1MjU4Nzg5IiB5PSIyMS41IiBmb250LXNpemU9IjEyIiBmb250LWZhbWlseT0iJ1JvYm90bycsIHNhbnMtc2VyaWYiIGZpbGw9IiNGRkZGRkYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5DUkVBVEVEIFdJVEg8L3RleHQ+PHRleHQgeD0iMTc4LjIwODMzNTg3NjQ2NDg0IiB5PSIyMS41IiBmb250LXNpemU9IjEyIiBmb250LWZhbWlseT0iJ01vbnRzZXJyYXQnLCBzYW5zLXNlcmlmIiBmaWxsPSIjRkZGRkZGIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iOTAwIiBsZXR0ZXItc3BhY2luZz0iMiI+REpBTkdPPC90ZXh0Pjwvc3ZnPg==)](https://forthebadge.com)

[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyODkuMDk5OTk4NDc0MTIxMSIgaGVpZ2h0PSIzNSIgdmlld0JveD0iMCAwIDI4OS4wOTk5OTg0NzQxMjExIDM1Ij48cmVjdCB3aWR0aD0iNTkuNTk5OTk4NDc0MTIxMDk0IiBoZWlnaHQ9IjM1IiBmaWxsPSIjYjhlOTg2Ii8+PHJlY3QgeD0iNTkuNTk5OTk4NDc0MTIxMDk0IiB3aWR0aD0iMTIwLjgxNjY2NTY0OTQxNDA2IiBoZWlnaHQ9IjM1IiBmaWxsPSIjNTBlM2MyIi8+PHRleHQgeD0iMjkuNzk5OTk5MjM3MDYwNTQ3IiB5PSIyMS41IiBmb250LXNpemU9IjEyIiBmb250LWZhbWlseT0iJ1JvYm90bycsIHNhbnMtc2VyaWYiIGZpbGw9IiNGRkZGRkYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIyIj5VU0VTPC90ZXh0Pjx0ZXh0IHg9IjEyMC4wMDgzMzEyOTg4MjgxMiIgeT0iMjEuNSIgZm9udC1zaXplPSIxMiIgZm9udC1mYW1pbHk9IidNb250c2VycmF0Jywgc2Fucy1zZXJpZiIgZmlsbD0iI0ZGRkZGRiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC13ZWlnaHQ9IjkwMCIgbGV0dGVyLXNwYWNpbmc9IjIiPkpBVkFTQ1JJUFQ8L3RleHQ+PHJlY3QgeD0iMTgwLjQxNjY2NDEyMzUzNTE2IiB3aWR0aD0iMTA4LjY4MzMzNDM1MDU4NTk0IiBoZWlnaHQ9IjM1IiBmaWxsPSIjMjY3NEE0Ii8+PHRleHQgeD0iMjM0Ljc1ODMzMTI5ODgyODEyIiB5PSIxNy41IiBmb250LXNpemU9IjEyIiBmb250LWZhbWlseT0iJ1JvYm90bycsIHNhbnMtc2VyaWYiIGZpbGw9IiNGRkZGRkYiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtd2VpZ2h0PSI1MDAiIGFsaWdubWVudC1iYXNlbGluZT0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iMiI+SFRNTCAvIENTUzwvdGV4dD48L3N2Zz4=)](https://forthebadge.com)

# Projet Askia
Projet de gestion des contrats/paiements en django utilisant postgresql comme base de données

## Installation et Configuration de postgresql sous Linux
### Installation
```bash
sudo apt update
sudo apt install postgresql 
```
### vérification

```bash
sudo systemctl status postgresql 
```
Vous devriez voir que le service est "active (running)".
### Configuration
1. Se connecter en tant que postgres
``` bash
sudo su postgres
psql
```
2. Créons notre utilisateur postgresql
```sql 
create user <USER_NAME>;
alter user <USERNAME> createdb password '<USER_PASSWORD>';
```


3. Editons le fichier `/etc/postgresql/<NOTRE_VERSION>/main/pg_hba.conf` \
Dans ce fichier nous allons activer la connection par mot de passe pour tous les utilisateurs:

```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     md5
```
NB: Cette session est vers la fin du fichier

4. Redémarrer le serveur postgresql

```bash 
sudo systemctl restart postgresql 
```

5. Créons la base de données de notre app avec le user de l'étape 2.

```bash
 psql -U <USER_NAME> -d template1
 create database <DB_NAME>;
```
6. Remarque:\
Par défaut postgresql écoute sur le port `5432` et sur l'adresse locale `localhost`. Tous ces paramètres peuvent êtres modifiés dans le fichier `/etc/postgresql/<VERSION>/main/postgresql.conf`

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
## Ressouces
installation de python-dotenv
https://myapollo.com.tw/en/blog/python-dotenv/

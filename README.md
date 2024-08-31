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

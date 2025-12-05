📘 TP Flask API — Gestion des Utilisateurs & Authentification

🎯 Objectif du TP

Ce projet implémente une mini-API en Flask permettant la gestion d’utilisateurs avec :

Création d’un modèle relationnel SQLite

Routes API (inscription, connexion, logout)

Gestion de sessions utilisateurs (Flask-Login)

ORM SQLAlchemy (création, requêtes, insertion, commit)

Templates HTML avec formulaires

Structure propre d’application (app.py, forms.py, models.py, etc.)

Ce TP répond aux exigences suivantes :
✔️ Utiliser Flask 
✔️ Implémenter un système minimal d’authentification
✔️ Comprendre la relation entre routes, templates HTML et base de données

📁 Arborescence du projet
TP_API/
├── 📁 instance/   
│   ├── database.db                → BD de  1 table User crée au lacement de flask_app.py                   
├── 📁 templates/
│   ├── base.html                  → Template parent
│   ├── login.html                 → Formulaire de connexion
│   ├── register.html              → Formulaire d’inscription
│   └── home.html                  → Page d'accueil
│
├── flask_app.py                   → Application Flask principale
└── README.md                      → Documentation

🗄️ 1. Modèle relationnel

Le modèle contient 1 table principale : User.

Table USER
Colonne	Type	Description
id	Integer (PK)	Identifiant unique utilisateur
username	String	Nom d’utilisateur (unique)
password	String 	Mot de passe stocké


🧩 2. Gestion de la base SQLite
Création automatique des tables

Les tables sont créées via :
db.create_all() (dans flask_app.py)   


🔐 3. Authentification (Flask-Login)

Le projet utilise Flask-Login pour gérer :

✔ Connexion
✔ Déconnexion
✔ Session utilisateur persistante
✔ Protection des pages avec @login_required

Routes principales dans app.py :

/register → Inscription
/login → Connexion
/logout → Déconnexion
/home → Page protégée
/search → recherche et affiche des films

📝 4. Formulaires Flask-WTF

Les formulaires sont définis dans forms.py :
LoginForm
RegisterForm

Ils permettent de valider plusieurs champs.


🔥 5. API REST (optionnel)

Même si le projet est orienté HTML, quelques routes peuvent être utilisées comme API :

POST /register → création utilisateur
GET /login → connexion
GET  /search → recherche de films 

▶️ 6. Exécution du projet


Lancer l’application Flask :
python app.py


Serveur disponible sur :
👉 http://127.0.0.1:5000


🔄 6. Alternative : Connexion MySQL (version avancée)

Une deuxième implémentation montre comment remplacer SQLite + SQLAlchemy par une base MySQL, en utilisant mysql.connector et des requêtes SQL directes.

Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'test',
    'password': '123',
    'database': 'tp_flask_tmdb'
}
Création automatique de deux tables users et films. 
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

Gestion SQL manuelle

La fonction utilitaire :

def execute_sql(query, params=(), fetch=False):
    conn = mysql.connector.connect(**DB_CONFIG)
    ...


La logique d’inscription / connexion fonctionne avec :
requêtes SQL directes
hashing des mots de passe
gestion des sessions Flask simples (session["user_id"] = ...)
Cette variante démontre une alternative au modèle ORM et une approche plus proche du backend traditionnel.


📚 7. Sources et documentation

Ce projet s'appuie sur plusieurs ressources pédagogiques et documentations officielles :

🔹 Flask & Authentification

Tutoriel complet Flask – découverte et logique d’application

👉 https://www.youtube.com/watch?v=42OII6XQr2Q

Série d'introduction à Flask (routes, templates, formulaires, sessions)

👉 https://www.youtube.com/watch?v=Ihp_cG7c2Rk&list=PLV1TsfPiCx8PXHsHeJKvSSC8zfi4Kvcfs

🔹 API TMDB (recherche de films)

Documentation officielle de l'API TheMovieDB

👉 https://developer.themoviedb.org/

🔹 SQL & Requêtes MySQL
Référence SQL claire et accessible

👉 https://sql.sh/

🔹 MySQL / Python (connexion, gestion d’erreurs, requêtes)
Tutoriel MySQL + Python

👉 https://www.youtube.com/watch?v=u96rVINbAUI


👥 8. Travail collaboratif

Meddy Garcia   ->        Création de la base MySQL, connexion Flask–MySQL, développement des routes, intégration HTML, documentation. 
Amos Clegbaza  ->        Création de la base MySQL, connexion Flask–MySQL, développement des routes, intégration HTML, documentation.
Bathy Voguie   ->        Création de la table film en MySQL et insertion de données, intégration HTML, ajout des routes associées, documentation.  
Mathieu Ponnou  ->       Développement complet de la version SQLite, connexion Flask–SQLite, création des routes, intégration HTML, documentation et rédaction du README. 




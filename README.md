
# TextToSQL Streamlit App

Application web pour convertir des questions en langage naturel en requêtes SQL Redshift.
**Interface Streamlit multilingue avec IA Google Gemini** 🚀


## 🚀 Installation

```bash
# Cloner le repo
git clone https://github.com/m-proto/TestToSQL_simple.git
cd TestToSQL_simple

# Installer les dépendances
pip install -r requirements.txt

# Configurer l'environnement
cp .env.example .env
# Puis éditer .env avec vos vraies credentials
```


## ⚙️ Configuration

Configurer le fichier `.env` avec vos credentials :

```env
# Base de données Redshift
REDSHIFT_USER=your_username
REDSHIFT_PASSWORD=your_password
REDSHIFT_HOST=your_cluster.region.redshift.amazonaws.com
REDSHIFT_PORT=5439
REDSHIFT_DB=your_database
REDSHIFT_SCHEMA=your_schema

# API Google Gemini
GOOGLE_API_KEY=your_google_api_key

# Configuration
DEBUG=false
LOG_LEVEL=INFO
```


## 🎯 Utilisation

### 🌐 Interface Web Streamlit
```bash
# Démarrer l'application
streamlit run streamlit_app.py
```

L'interface sera disponible sur :
- http://localhost:8501
- Support multilingue (Français, English, 日本語)
- Interface intuitive et moderne


## 📁 Structure du projet

```
TestToSQL_simple/
├── streamlit_app.py            # Point d'entrée Streamlit
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation
├── .env.example                # Exemple de configuration
├── infrastructure/
│   ├── settings.py             # Configuration
│   ├── database.py             # Connexion Redshift
│   ├── llm.py                  # Intégration Gemini
│   ├── cache.py                # Cache mémoire
│   └── logging.py              # Logging structuré
├── langue/
│   ├── translator.py           # Gestion multilingue
│   └── translations/           # Fichiers de traduction
├── ui/
│   ├── components/             # Composants UI (header, sidebar, main_content, ...)
│   └── styles/                 # Thèmes et CSS custom
```


## 📊 Fonctionnalités principales

- ✅ Génération de requêtes SQL Redshift à partir de questions en langage naturel
- ✅ Multilingue (Français, Anglais, Japonais)
- ✅ Interface moderne et responsive (Streamlit)
- ✅ Cache mémoire pour accélérer les requêtes répétées
- ✅ Logging structuré pour le debug et la production
- ✅ Configuration centralisée via `.env` et secrets
- ✅ Architecture modulaire et claire


## 🛠️ Développement

```bash
# Lancer Streamlit en mode développement
streamlit run streamlit_app.py

# Linting (optionnel)
flake8 .
```


## 📝 Exemple d'utilisation

Lancez simplement l'interface web, posez une question en langage naturel, et obtenez la requête SQL correspondante !

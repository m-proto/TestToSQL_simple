# 🔄 TextToSQL Streamlit App

Application Streamlit multilingue pour convertir des questions en langage naturel vers des requêtes SQL Redshift.

## 🚀 Démarrage rapide

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Configuration
Assurez-vous que votre fichier `.env` est configuré avec :
```env
REDSHIFT_USER=your_username
REDSHIFT_PASSWORD=your_password
REDSHIFT_HOST=your_host
REDSHIFT_PORT=5439
REDSHIFT_DB=your_database
REDSHIFT_SCHEMA=your_schema
GOOGLE_API_KEY=your_google_api_key
```

### 3. Lancement
```bash
streamlit run streamlit_app.py
```

## 🏗️ Architecture

```
streamlit_app.py          # Point d'entrée principal
├── ui/                   # Interface utilisateur
│   ├── components/       # Composants UI réutilisables
│   │   ├── header.py     # En-tête
│   │   ├── sidebar.py    # Panneau latéral
│   │   ├── main_content.py # Zone principale
│   │   └── footer.py     # Pied de page
│   ├── styles/           # Styles et thèmes
│   │   └── themes.py     # CSS personnalisé
│   └── utils/            # Utilitaires UI
├── langue/               # Gestion multilingue
│   ├── translations/     # Fichiers de traduction
│   │   ├── fr.json       # Français
│   │   ├── en.json       # Anglais
│   │   └── ja.json       # Japonais
│   └── translator.py     # Moteur de traduction
├── infrastructure/       # RÉUTILISÉ (code existant)
│   ├── database.py       # Connexion Redshift
│   ├── llm.py           # LLM Google Gemini
│   └── settings.py      # Configuration
└── domain/              # RÉUTILISÉ (logique métier)
    └── sql/
        └── service.py    # Génération SQL
```

## 🌍 Langues supportées

- 🇫🇷 Français (par défaut)
- 🇬🇧 English
- 🇯🇵 日本語 (Japonais)

## ✨ Fonctionnalités

### Interface principale
- 📝 Zone de saisie pour questions en langage naturel
- 🚀 Génération SQL instantanée
- 📋 Copie et téléchargement des requêtes
- 💡 Exemples prédéfinis

### Panneau latéral
- 🌍 Sélecteur de langue
- 📊 Statut des connexions (DB, LLM)
- ⚙️ Paramètres avancés
- 🔍 Test de connectivité

### Historique
- 📜 Sauvegarde des requêtes générées
- 🔄 Réutilisation rapide
- 📊 Analyse des tendances

## 🎨 Thèmes

L'application inclut plusieurs thèmes :
- **Light** : Thème clair par défaut
- **Dark** : Mode sombre
- **Professional** : Style entreprise

## ☁️ Déploiement Streamlit Cloud

### Prérequis
1. Repository GitHub avec le code
2. Compte Streamlit Cloud
3. Configuration des secrets

### Étapes
1. **Push sur GitHub** :
```bash
git add .
git commit -m "Add Streamlit interface"
git push origin main
```

2. **Connecter à Streamlit Cloud** :
   - Aller sur [share.streamlit.io](https://share.streamlit.io)
   - Connecter votre repository
   - Sélectionner `streamlit_app.py` comme fichier principal

3. **Configurer les secrets** :
   Dans l'interface Streamlit Cloud, ajouter :
```toml
[secrets]
REDSHIFT_USER = "your_username"
REDSHIFT_PASSWORD = "your_password"
REDSHIFT_HOST = "your_host"
REDSHIFT_PORT = "5439"
REDSHIFT_DB = "your_database"
REDSHIFT_SCHEMA = "your_schema"
GOOGLE_API_KEY = "your_google_api_key"
```

4. **Déployer** : L'app sera automatiquement déployée !

## 🔧 Configuration avancée

### Variables d'environnement
Toutes les configurations sont gérées via `.env` :
```env
# Base de données
REDSHIFT_USER=username
REDSHIFT_PASSWORD=password
REDSHIFT_HOST=host
REDSHIFT_PORT=5439
REDSHIFT_DB=database
REDSHIFT_SCHEMA=schema

# LLM
GOOGLE_API_KEY=your_key

# App
DEBUG=false
LOG_LEVEL=INFO
```

### Customisation UI
- Modifier `ui/styles/themes.py` pour les styles
- Ajouter des langues dans `langue/translations/`
- Personnaliser les composants dans `ui/components/`

## 🐛 Dépannage

### Problème de connexion Redshift
- Vérifiez vos credentials dans `.env`
- Testez la connectivité réseau
- Consultez les logs dans la sidebar

### Erreur LLM
- Vérifiez votre `GOOGLE_API_KEY`
- Contrôlez les quotas API
- Ajustez les paramètres de température

### Interface ne charge pas
- Vérifiez les imports Python
- Consultez les logs d'erreur
- Rafraîchissez la page

## 📞 Support

- 📚 Documentation : Voir les commentaires dans le code
- 🐛 Issues : Créer une issue GitHub
- 💡 Suggestions : Ouvrir une discussion

---

**L'application réutilise 100% de votre infrastructure existante !** 🎉

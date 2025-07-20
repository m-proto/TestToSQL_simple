"""
Application Streamlit TextToSQL
Point d'entrée principal qui utilise l'infrastructure existante
"""
import streamlit as st
import sys
import os

# Ajouter le répertoire racine au PYTHONPATH pour les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Imports des composants UI
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.components.main_content import render_main_content
from ui.components.footer import render_footer
from ui.styles.themes import load_custom_css, apply_theme

# Imports pour l'initialisation
from langue.translator import get_text, set_language
from infrastructure.logging import logger

def initialize_app():
    """Initialise l'application Streamlit"""
    
    # Configuration de la page
    st.set_page_config(
        page_title="TextToSQL Generator",
        page_icon="🔄",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/your-repo/textosql',
            'Report a bug': "https://github.com/your-repo/textosql/issues",
            'About': "# TextToSQL Generator\nConvertissez vos questions en requêtes SQL avec l'IA!"
        }
    )
    
    # Initialisation de la langue par défaut
    if 'language' not in st.session_state:
        set_language('fr')
    
    # Application du thème
    apply_theme("light")
    
    # Chargement des styles personnalisés
    load_custom_css()
    
    # Log de démarrage
    logger.info("Streamlit application started")

def main():
    """Fonction principale de l'application"""
    
    # Initialisation
    initialize_app()
    
    # Interface utilisateur
    try:
        # En-tête
        render_header()
        
        # Sidebar
        render_sidebar()
        
        # Contenu principal
        render_main_content()
        
        # Pied de page
        render_footer()
        
    except Exception as e:
        st.error(f"Erreur dans l'interface: {str(e)}")
        logger.error("UI error", error=str(e))
        
        # Interface de fallback en cas d'erreur
        st.markdown("## 🔄 TextToSQL Generator")
        st.markdown("Une erreur s'est produite. Veuillez rafraîchir la page.")
        
        if st.button("🔄 Rafraîchir"):
            st.rerun()

if __name__ == "__main__":
    main()

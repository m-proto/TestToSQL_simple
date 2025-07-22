"""
Moteur de traduction pour l'interface multilingue
"""

import streamlit as st
import json
import os

# Langue par défaut
DEFAULT_LANGUAGE = "fr"


def load_translations(language):
    """Charge les traductions pour une langue"""
    file_path = f"langue/translations/{language}.json"

    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        st.error(f"Erreur de chargement des traductions {language}: {e}")

    # Fallback vers français
    try:
        with open("langue/translations/fr.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Erreur critique de chargement des traductions: {e}")
        return {}


def get_current_language():
    """Récupère la langue actuelle"""
    if "language" not in st.session_state:
        st.session_state.language = DEFAULT_LANGUAGE
    return st.session_state.language


def set_language(language):
    """Définit la langue"""
    if language in ["fr", "en", "ja"]:
        st.session_state.language = language
        st.session_state.translations = load_translations(language)
    else:
        st.warning(f"Langue non supportée: {language}")


def get_text(key, **kwargs):
    """Récupère un texte traduit"""
    if "translations" not in st.session_state:
        st.session_state.translations = load_translations(get_current_language())

    text = st.session_state.translations.get(key, key)

    # Support pour variables dans le texte
    if kwargs:
        try:
            return text.format(**kwargs)
        except Exception:
            return text

    return text


def get_available_languages():
    """Retourne la liste des langues disponibles"""
    return {"🇫🇷 Français": "fr", "🇬🇧 English": "en", "🇯🇵 日本語": "ja"}

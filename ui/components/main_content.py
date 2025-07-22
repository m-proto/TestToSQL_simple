"""
Zone de contenu principal de l'application
"""
import streamlit as st
from langue.translator import get_text

def render_main_content():
    """Affiche le contenu principal de l'application"""
    
    # Navigation par onglets
    tab1, tab2, tab3 = st.tabs([
        get_text("tab_generator"),
        get_text("tab_history"),
        get_text("tab_settings")
    ])
    
    with tab1:
        render_sql_generator()
    
    with tab2:
        render_query_history()
    
    with tab3:
        render_advanced_settings()

def render_sql_generator():
    """Interface principale de génération SQL"""
    
    # Zone de saisie de la question
    col1, col2 = st.columns([3, 1])
    
    with col1:
        question = st.text_area(
            get_text("question_label"),
            placeholder=get_text("question_placeholder"),
            height=120,
            key="question_input"
        )
    
    with col2:
        st.markdown(f"### {get_text('examples_title')}")
        
        # Boutons d'exemples
        if st.button("📊 " + get_text("example_sales"), use_container_width=True):
            st.session_state.question_input = "Combien de voitures ont été vendues au total ?"
            st.rerun()
        
        if st.button("📅 " + get_text("example_monthly"), use_container_width=True):
            st.session_state.question_input = "Montrez-moi les ventes par mois cette année"
            st.rerun()
        
        if st.button("🏆 " + get_text("example_brands"), use_container_width=True):
            st.session_state.question_input = "Quelles sont les 10 marques les plus vendues ?"
            st.rerun()
    
    # Boutons d'action
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        generate_clicked = st.button(
            get_text("generate_button"),
            type="primary",
            use_container_width=True,
            disabled=not question
        )
    
    with col2:
        if st.button(get_text("clear_button"), use_container_width=True):
            st.session_state.question_input = ""
            if 'generated_sql' in st.session_state:
                del st.session_state.generated_sql
            st.rerun()
    
    # Génération SQL
    if generate_clicked and question:
        generate_sql_query(question)
    
    # Affichage du résultat
    if 'generated_sql' in st.session_state and st.session_state.generated_sql:
        render_sql_result(st.session_state.generated_sql)

from infrastructure.cache import cache_manager  # ✅ à ajouter tout en haut

from infrastructure.cache import cache_manager  # en haut du fichier

def generate_sql_query(question):
    """Génère la requête SQL sans exécution via LangChain SQL Chain + cache"""
    try:
        with st.spinner(get_text("generating")):
            # Vérifie s’il y a déjà une entrée dans le cache
            cached_sql = cache_manager.get_cached_sql_result(question)

            if cached_sql:
                st.session_state.generated_sql = cached_sql

                # ✅ Ajouter dans l'historique même si c’est depuis le cache
                if 'query_history' not in st.session_state:
                    st.session_state.query_history = []

                st.session_state.query_history.insert(0, {
                    'question': question,
                    'sql': cached_sql,
                    'timestamp': str(st.session_state.get('current_time', 'now'))
                })

                st.success(get_text("success_cache"))
                return

            # Sinon → génération via LLM
            from infrastructure.database import connect_to_redshift
            from infrastructure.llm import get_sql_db, get_gemini_llm, create_sql_query_chain_only

            engine = connect_to_redshift()
            db = get_sql_db(engine)
            llm = get_gemini_llm()

            sql_chain = create_sql_query_chain_only(llm, db)
            result = sql_chain.invoke({"question": question})

            cleaned_sql = result.replace("```sql", "").replace("```", "").strip()

            if cleaned_sql:
                st.session_state.generated_sql = cleaned_sql
                cache_manager.cache_sql_result(question, cleaned_sql)

                # ✅ Ajouter dans l'historique même en génération directe
                if 'query_history' not in st.session_state:
                    st.session_state.query_history = []

                st.session_state.query_history.insert(0, {
                    'question': question,
                    'sql': cleaned_sql,
                    'timestamp': str(st.session_state.get('current_time', 'now'))
                })

                st.success(get_text("success_generated"))
            else:
                st.error(get_text("error_generation"))

    except Exception as e:
        st.error(f"{get_text('error_generation')}: {str(e)}")






def render_sql_result(sql):
    """Affiche le résultat SQL généré"""
    st.markdown(f"### {get_text('sql_generated')}")
    
    # Affichage du SQL avec coloration syntaxique
    st.code(sql, language="sql")
    
    # Boutons d'action sur le résultat
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.download_button(
            label=get_text("download_button"),
            data=sql,
            file_name="query.sql",
            mime="text/sql",
            use_container_width=True
        ):
            st.success("📥 SQL téléchargé !")
    
    with col2:
        if st.button(get_text("copy_button"), use_container_width=True):
            # Note: La copie dans le presse-papier nécessite JavaScript
            st.info(get_text("copied"))
    
    with col3:
        if st.button(get_text("execute_button"), use_container_width=True):
            st.info("⚡ Fonctionnalité d'exécution à venir...")

def render_query_history():
    """Affiche l'historique des requêtes"""
    st.markdown(f"### {get_text('query_history')}")

    if 'query_history' not in st.session_state or not st.session_state.query_history:
        st.info(get_text("no_history"))
        return

    # Affichage de l'historique (sans bouton de réutilisation)
    for i, entry in enumerate(st.session_state.query_history):
        with st.expander(f"{get_text('query_number')} {i+1}: {entry['question'][:50]}..."):
            st.markdown(get_text("question_label_history"))
            st.write(entry['question'])
            st.markdown(get_text("sql_label_history"))
            st.code(entry['sql'], language="sql")



def render_advanced_settings():
    """Paramètres avancés"""
    st.markdown(f"### {get_text('tab_settings')}")
    
    # Configuration LLM avec valeurs optimales officielles
    st.subheader(get_text("llm_config_title"))
    
    # Information importante
    st.info(get_text("llm_config_info"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        temperature = st.slider(
            get_text("temperature_label"),
            min_value=0.0,
            max_value=0.3,  # Limité pour SQL
            value=0.0,       # Valeur officielle recommandée
            step=0.05,
            help="**Recommandation officielle : 0.0 pour SQL**\n\n"
                 "• 0.0 = Déterministe, résultats cohérents (RECOMMANDÉ)\n"
                 "• 0.1-0.2 = Légères variations possibles\n"
                 "• 0.3+ = Trop créatif pour du SQL précis\n\n"
                 "Source: Documentation Google Gemini"
        )
    
    with col2:
        max_tokens = st.number_input(
            get_text("max_tokens_label"),
            min_value=500,
            max_value=2000,
            value=1000,      # Valeur officielle recommandée
            step=100,
            help="**Recommandation officielle : 1000 tokens**\n\n"
                 "• 500-800 = Requêtes SQL simples\n"
                 "• 1000 = Parfait pour la plupart des cas (RECOMMANDÉ)\n"
                 "• 1500+ = Requêtes SQL très complexes\n\n"
                 "1 token ≈ 4 caractères, 100 tokens ≈ 60-80 mots"
        )
    
    # Sauvegarder les paramètres dans session state
    st.session_state.llm_config = {
        'temperature': temperature,
        'max_tokens': max_tokens
    }
    
    # Alerte si paramètres non-optimaux
    if temperature > 0.2:
        st.warning(get_text("temp_warning"))
    
    if temperature == 0.0:
        st.success(get_text("temp_optimal"))
    
    # Actions
    st.subheader(get_text("actions_title"))
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(get_text("clear_history"), use_container_width=True):
            st.session_state.query_history = []
            st.success(get_text("history_cleared"))
    
    with col2:
        if st.button(get_text("reset_params"), use_container_width=True):
            # Reset aux valeurs optimales recommandées
            st.session_state.llm_config = {
                'temperature': 0.0,
                'max_tokens': 1000
            }
            st.success(get_text("params_reset"))

"""
Gestion des thèmes et styles personnalisés
"""

import streamlit as st

# Définition des thèmes
THEMES = {
    "light": {
        "primary_color": "#667eea",
        "background_color": "#ffffff",
        "secondary_background": "#f0f2f6",
        "text_color": "#262730",
        "accent_color": "#764ba2",
    },
    "dark": {
        "primary_color": "#ff6b6b",
        "background_color": "#0e1117",
        "secondary_background": "#262730",
        "text_color": "#fafafa",
        "accent_color": "#4ecdc4",
    },
    "professional": {
        "primary_color": "#2e86ab",
        "background_color": "#f8f9fa",
        "secondary_background": "#e9ecef",
        "text_color": "#212529",
        "accent_color": "#a23b72",
    },
}


def load_custom_css():
    """Charge les styles CSS personnalisés"""
    st.markdown(
        """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Variables CSS globales */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --accent-color: #f093fb;
        --text-color: #262730;
        --background-color: #ffffff;
        --card-background: #f8f9fa;
        --border-color: #e0e0e0;
        --shadow: 0 4px 12px rgba(0,0,0,0.1);
        --border-radius: 12px;
    }
    
    /* Styles généraux */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header styles */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        padding: 2.5rem;
        border-radius: var(--border-radius);
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: var(--shadow);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="white" opacity="0.1"><polygon points="0,100 100,0 200,50 300,0 400,100 500,50 600,0 700,100 800,50 900,0 1000,100 1000,100 0,100"/></svg>');
        background-size: cover;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.8rem;
        font-weight: 700;
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.3rem;
        opacity: 0.95;
        position: relative;
        z-index: 1;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Cards et containers */
    .metric-card {
        background: var(--card-background);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        border: 1px solid var(--border-color);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* SQL Output styling */
    .sql-output {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-left: 4px solid var(--primary-color);
        padding: 1.5rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
        margin: 1rem 0;
        position: relative;
    }
    
    .sql-output::before {
        content: "💻 SQL";
        position: absolute;
        top: -10px;
        left: 20px;
        background: var(--primary-color);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    /* Button enhancements */
    .stButton > button {
        border-radius: var(--border-radius);
        border: none;
        padding: 0.7rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
        box-shadow: var(--shadow);
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    /* Primary button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
    }
    
    /* Input fields */
    .stTextArea textarea,
    .stTextInput input,
    .stSelectbox select {
        border-radius: var(--border-radius);
        border: 2px solid var(--border-color);
        transition: border-color 0.2s ease;
    }
    
    .stTextArea textarea:focus,
    .stTextInput input:focus,
    .stSelectbox select:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 0.8rem 1.5rem;
        border: 1px solid var(--border-color);
        transition: all 0.2s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: var(--primary-color);
        color: white;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
    }
    
    /* Metrics styling */
    [data-testid="metric-container"] {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 1rem;
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--card-background);
        border-radius: var(--border-radius);
        border: 1px solid var(--border-color);
    }
    
    /* Footer divider */
    .header-divider {
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color), var(--primary-color));
        border: none;
        margin: 2rem 0;
        border-radius: 2px;
        box-shadow: var(--shadow);
    }
    
    /* Success/Error/Warning messages */
    .stSuccess {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border-left: 4px solid #28a745;
        border-radius: var(--border-radius);
    }
    
    .stError {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        border-left: 4px solid #dc3545;
        border-radius: var(--border-radius);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        border-left: 4px solid #ffc107;
        border-radius: var(--border-radius);
    }
    
    .stInfo {
        background: linear-gradient(135deg, #d1ecf1 0%, #bee5eb 100%);
        border-left: 4px solid #17a2b8;
        border-radius: var(--border-radius);
    }
    
    /* Code blocks */
    .stCodeBlock {
        border-radius: var(--border-radius);
        box-shadow: var(--shadow);
    }
    
    /* Spinner customization */
    .stSpinner {
        color: var(--primary-color);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display: none;}
    footer {visibility: hidden;}
    .stDecoration {display: none;}
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .main-header {
            padding: 1.5rem;
        }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


def apply_theme(theme_name="light"):
    """Applique un thème spécifique"""
    if theme_name not in THEMES:
        theme_name = "light"

    theme = THEMES[theme_name]

    # Injection des variables CSS du thème
    st.markdown(
        f"""
    <style>
    :root {{
        --primary-color: {theme['primary_color']};
        --background-color: {theme['background_color']};
        --secondary-background: {theme['secondary_background']};
        --text-color: {theme['text_color']};
        --accent-color: {theme['accent_color']};
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def get_available_themes():
    """Retourne la liste des thèmes disponibles"""
    return list(THEMES.keys())

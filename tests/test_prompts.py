import pytest
from infrastructure.prompts import PROMPT_TEMPLATE_EN

def test_prompt_template_structure():
    """Test la structure du template de prompt"""
    assert "WITH range_date AS (" in PROMPT_TEMPLATE_EN
    assert "LIMIT 10;" in PROMPT_TEMPLATE_EN
    assert "{question}" in PROMPT_TEMPLATE_EN

def test_prompt_template_rules():
    """Test la présence des règles importantes"""
    assert "price != 999999999" in PROMPT_TEMPLATE_EN
    assert "prefecture_name IS NOT NULL" in PROMPT_TEMPLATE_EN
    assert "to_date('YYYY-MM-DD', 'yyyy-mm-dd')" in PROMPT_TEMPLATE_EN

def test_prompt_template_tables():
    """Test la présence des tables requises"""
    required_tables = [
        "sold_cars",
        "display_cars",
        "clients",
        "estimates",
        "calls",
        "reservations",
        "car_effects",
        "client_effects",
        "history.salesforce_account"
    ]
    for table in required_tables:
        assert table in PROMPT_TEMPLATE_EN

def test_prompt_template_forbidden():
    """Test la présence des éléments interdits"""
    assert "BETWEEN 'xxx' AND 'xxx'" in PROMPT_TEMPLATE_EN
    assert "🚫 FORBIDDEN:" in PROMPT_TEMPLATE_EN

def test_prompt_template_formatting():
    """Test les instructions de formatage"""
    assert "Multi-line SQL" in PROMPT_TEMPLATE_EN
    assert "Each SELECT, JOIN, AND, OR, WHERE, GROUP BY" in PROMPT_TEMPLATE_EN
    assert "Proper indentation" in PROMPT_TEMPLATE_EN 
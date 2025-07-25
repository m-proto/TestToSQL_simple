"""Tests du module de traduction"""

import pytest
from unittest.mock import patch, mock_open
from langue.translator import load_translations

@patch("builtins.open", new_callable=mock_open, read_data='{"test_key": "Test Value"}')
def test_load_translations(mock_file):
    """Test le chargement des traductions depuis un fichier"""
    translations = load_translations("en")
    assert translations["test_key"] == "Test Value"
    mock_file.assert_called_once_with("langue/translations/en.json", "r", encoding="utf-8") 
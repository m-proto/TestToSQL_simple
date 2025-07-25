"""Tests des composants Streamlit"""

import pytest
from unittest.mock import Mock, patch
from ui.components.main_content import set_example_question

def test_set_example_question():
    """Test la définition d'une question exemple"""
    example = "Question exemple"
    set_example_question(example)
    assert example == "Question exemple" 
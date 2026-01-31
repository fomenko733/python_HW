# test_string_utils.py

import pytest
from string_utils import StringUtils

utils = StringUtils()

# === capitalize ===

def test_capitalize_positive():
    assert utils.capitalize("тест") == "Тест"

def test_capitalize_negative_empty_string():
    assert utils.capitalize("") == ""

def test_capitalize_negative_none():
    with pytest.raises(TypeError):
        utils.capitalize(None)

# === trim ===

def test_trim_positive():
    assert utils.trim("   Тест") == "Тест"

def test_trim_negative_empty_string():
    assert utils.trim("") == ""

def test_trim_negative_only_spaces():
    assert utils.trim("     ") == ""

def test_trim_negative_none():
    with pytest.raises(TypeError):
        utils.trim(None)

# === to_list ===

def test_to_list_positive():
    assert utils.to_list("a,b,c", ",") == ["a", "b", "c"]

def test_to_list_positive_empty_string():
    assert utils.to_list("", ",") == []

def test_to_list_negative_none():
    with pytest.raises(TypeError):
        utils.to_list(None, ",")

# === contains ===

def test_contains_positive():
    assert utils.contains("Тест", "с") is True
def test_contains_negative_not_found():
    assert utils.contains("Тест", "x") is False

def test_contains_negative_empty_string():
    assert utils.contains("", "a") is False

def test_contains_negative_invalid_symbol():
    with pytest.raises(ValueError):
        utils.contains("Тест", "ab")

def test_contains_negative_none_input():
    with pytest.raises(TypeError):
        utils.contains(None, "a")

# === delete_symbol ===

def test_delete_symbol_positive():
    assert utils.delete_symbol("Тест", "с") == "Тет"

def test_delete_symbol_negative_not_present():
    assert utils.delete_symbol("Тест", "x") == "Тест"

def test_delete_symbol_negative_empty_string():
    assert utils.delete_symbol("", "a") == ""

def test_delete_symbol_negative_invalid_symbol():
    with pytest.raises(ValueError):
        utils.delete_symbol("Тест", "ab")

# === starts_with ===

def test_starts_with_positive():
    assert utils.starts_with("Тест", "Т") is True

def test_starts_with_negative():
    assert utils.starts_with("Тест", "x") is False

def test_starts_with_empty_string():
    assert utils.starts_with("", "x") is False

# === end_with ===

def test_end_with_positive():
    assert utils.end_with("Тест", "т") is True

def test_end_with_negative():
    assert utils.end_with("Тест", "x") is False

def test_end_with_empty_string():    assert utils.end_with("", "x") is False

# === is_empty ===

def test_is_empty_positive_true():
    assert utils.is_empty("   ") is True

def test_is_empty_positive_false():
    assert utils.is_empty("Тест") is False

def test_is_empty_empty_string():
    assert utils.is_empty("") is True

def test_is_empty_none():
    with pytest.raises(TypeError):
        utils.is_empty(None)

# === list_to_string ===

def test_list_to_string_positive():
    assert utils.list_to_string([1, 2, 3], ", ") == "1, 2, 3"

def test_list_to_string_empty_list():
    assert utils.list_to_string([], ", ") == ""

def test_list_to_string_negative_none():
    with pytest.raises(TypeError):
        utils.list_to_string(None, ", ")
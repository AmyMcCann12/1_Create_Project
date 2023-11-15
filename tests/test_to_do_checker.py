import pytest
from lib.to_do_checker import *

def test_to_do_checker_empty_string():
    with pytest.raises(Exception) as e:
        to_do_checker("")
    error_message = str(e.value)
    assert error_message == "No text has been inputted!"

def test_to_do_checker_includes_todo():
    assert to_do_checker("TODO Walk the dog") == True

def test_to_do_checker_does_not_include_todo():
    assert to_do_checker("Shopping List") == False

def test_to_do_checker_includes_todo_lower_case():
    assert to_do_checker("todo: Walk the dog") == True
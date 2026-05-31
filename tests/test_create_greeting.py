import pytest
import create_greeting 

@pytest.mark.parametrize("name, system, language, expected_result", [
    ("Steven", "Pi 5", "german", "Hallo Steven, dein Python läuft auf dem Pi 5."),
    ("Steven", "Pi 5", "deutsch", "Hallo Steven, dein Python läuft auf dem Pi 5."),
    ("Steven", "Raspberry Pi 5", "english", "Hello Steven, your Python runs on a Raspberry Pi 5."),
    ("Steven", "Pi 5", "spain", "spain not supported")
])

def test_create_greeting(name: str, system: str, language: str, expected_result: str):
    result = create_greeting.create_greeting(name, system, language)
    assert result == expected_result
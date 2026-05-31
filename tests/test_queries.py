import queries


def test_query_language_normalizes_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: " GERMAN ")

    result = queries.query_language()
    assert result == "german"

def test_query_system_normalizes_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: " Raspberry Pi 5   ")

    result = queries.query_system()
    assert result == "Raspberry Pi 5"

def test_query_name_normalizes_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: " Steven   ")

    result = queries.query_name()
    assert result == "Steven"

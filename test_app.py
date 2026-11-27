import pytest
import main


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_database = tmp_path / "test.db"
    monkeypatch.setattr(main, "DATABASE", str(test_database))

    main.init_db()

    main.app.config["TESTING"] = True

    with main.app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Add Contact' in response.data
from main import app

def test_index_route():
    response = app.index().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello; from sample"
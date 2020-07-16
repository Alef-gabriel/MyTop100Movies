from flask import Flask
from src.blueprint.bp import bp as blueprint

def test_bp():
    app = Flask(__name__)

    app.register_blueprint(blueprint)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.get_data() == b'hello world'
    assert response.status_code == 200



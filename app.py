from api.v1.app import app
from os import getenv

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=getenv('PORT', 5000),
        load_dotenv=True,
        debug=getenv('DEBUG', False)
    )

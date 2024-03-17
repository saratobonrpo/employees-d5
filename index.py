from dotenv import load_dotenv
from src import init_app
import os

load_dotenv()

development_debug = os.environ.get('DEBUG', default='False') == 'True'
configuration = {'development': {'DEBUG': development_debug}}

app = init_app(configuration)

if __name__ == '__main__':
    app.run()
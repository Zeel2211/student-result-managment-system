import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app
from app.model import create_tables

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

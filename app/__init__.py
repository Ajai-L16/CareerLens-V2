from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)

# --- CONFIGS ---
# Set your secret key
app.config['SECRET_KEY'] = 'a-very-secret-key-that-you-should-change'

# Set your database URI
# FORMAT: mysql+<driver>://<user>:<password>@<host>/<dbname>
# We are using 'mysqlclient' as the driver
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlclient://root:Apassword@localhost/careerlensdb'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INITIALIZE EXTENSIONS ---
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# This tells Flask-Login which route to redirect to if a user
# tries to access a page that requires them to be logged in.
login_manager.login_view = 'login'
login_manager.login_message_category = 'info' # For flashing messages

# --- Import routes and models ---
# This is done *after* 'app' and 'db' are created to avoid circular imports.
from app import routes, models
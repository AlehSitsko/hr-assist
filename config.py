import os

# --- Module-level constants ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}   # add more if needed
MAX_CONTENT_LENGTH = 10 * 1024 * 1024                # 10 MB
EXPIRY_SOON_DAYS = 30                                 # days to expiry to consider "expiring soon"

# --- Flask config object  ---
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-will-never-guess")          # TODO: change to env
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "another-secret-key")    # TODO: change to env

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL")
        or f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # uploads / limits
    UPLOAD_FOLDER = UPLOAD_FOLDER
    MAX_CONTENT_LENGTH = MAX_CONTENT_LENGTH

    # simple admin creds (MVP). 
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "1234")  # TODO: change it later to env

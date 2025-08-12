import os
from werkzeug.exceptions import RequestEntityTooLarge

from app import create_app          
from config import UPLOAD_FOLDER    

app = create_app()

# create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 413: file too large
@app.errorhandler(RequestEntityTooLarge)
def handle_413(e):
    return {"error": "File too large"}, 413

if __name__ == "__main__":
    app.run(debug=True)

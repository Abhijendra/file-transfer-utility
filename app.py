from flask import Flask
from file_manager import filemanager_bp
from render import ui_bp

app = Flask(__name__)
app.register_blueprint(filemanager_bp)
app.register_blueprint(ui_bp)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Blueprint, request, jsonify, abort, send_from_directory
from werkzeug.utils import secure_filename
import hashlib
import os 

filemanager_bp = Blueprint('file_manager', __name__, url_prefix='/file_manager')
DEST_FOLDER = "dest"
CHUNK_SIZE = 8192

@filemanager_bp.route('/upload', methods=['POST'])
def upload_file():
    try:        
        file = request.files.get('file')
        
        if not file or file.filename == "":
            return jsonify({
                'success': False,
                'message': 'Missing file'
                }), 400
        
        filename = secure_filename(file.filename)
        os.makedirs(DEST_FOLDER, exist_ok=True)

        final_path = os.path.join(DEST_FOLDER, filename)
        temp_path = os.path.join(DEST_FOLDER, f".tmp_{filename}")
        
        hasher = hashlib.sha256()
        with open(temp_path, "wb") as f:
            while True:
                chunk = file.stream.read(CHUNK_SIZE)
                if not chunk:
                    break
                f.write(chunk)
                hasher.update(chunk)
        
        os.replace(temp_path, final_path)
        checksum = hasher.hexdigest()

        return jsonify({
        "success": True,
        "filename": filename,
        "checksum": checksum
    })

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

@filemanager_bp.route("/download/<path:filename>", methods=["GET"])
def download(filename):
    try:
        safe_name = secure_filename(filename)
        file_path = os.path.join(DEST_FOLDER, safe_name)
        
        if not os.path.exists(file_path):
            abort(404, description="File not found")

        return send_from_directory(
        DEST_FOLDER,
        safe_name,
        as_attachment=True
    )
    except Exception as e:
        print(f"Error uploading file: {e}")
        return jsonify({
            'success': False,
            'message': str(e)
            }), 500

        

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import model
import model2

env = "prod"

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

def handle_file_upload(request, detection_function):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        image = Image.open(io.BytesIO(file.read()))
        description = detection_function(image)
        return jsonify({'description': description}), 200
    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error processing file: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/detect', methods=['POST'])
def detect_fault():
    return handle_file_upload(request, model.detect_fault)

@app.route('/detect2', methods=['POST'])
def detect_fault2():
    return handle_file_upload(request, model2.detect_fault2)


if __name__ == '__main__':
    app.run(debug=True)

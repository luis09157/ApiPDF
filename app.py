from flask import Flask, jsonify, send_file, request
import os
import glob

app = Flask(__name__)

# Rutas de las carpetas
PDF_FOLDER = 'pdf'
IMAGE_FOLDER = 'images'

@app.route('/api/pdfs', methods=['GET'])
def list_pdfs():
    """Devuelve lista de PDFs con nombre y path"""
    try:
        pdf_files = []
        for file in glob.glob(os.path.join(PDF_FOLDER, '*.pdf')):
            pdf_files.append({
                'nombre': os.path.basename(file),
                'path': os.path.abspath(file)
            })
        return jsonify({'pdfs': pdf_files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/images', methods=['GET'])
def list_images():
    """Devuelve lista de imágenes con nombre y path"""
    try:
        image_files = []
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
        for ext in extensions:
            for file in glob.glob(os.path.join(IMAGE_FOLDER, ext)):
                image_files.append({
                    'nombre': os.path.basename(file),
                    'path': os.path.abspath(file)
                })
        return jsonify({'images': image_files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    """Descarga un PDF específico"""
    try:
        file_path = os.path.join(PDF_FOLDER, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True, download_name=filename)
        else:
            return jsonify({'error': 'PDF no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download/image/<filename>', methods=['GET'])
def download_image(filename):
    """Descarga una imagen específica"""
    try:
        file_path = os.path.join(IMAGE_FOLDER, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True, download_name=filename)
        else:
            return jsonify({'error': 'Imagen no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)

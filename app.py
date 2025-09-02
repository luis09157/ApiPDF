from flask import Flask, jsonify, send_file, request
import os
import glob
import random

app = Flask(__name__)

# Rutas de las carpetas
PDF_FOLDER = 'pdf'
IMAGE_FOLDER = 'images'

# URL base de la API (se puede configurar como variable de entorno)
BASE_URL = os.environ.get('BASE_URL', 'https://apipdf-rh0o.onrender.com')

# Base de datos simple de nóminas
NOMINAS_DB = {
    "L03548174": {
        "nombre": "Juan Pérez García",
        "departamento": "Ventas",
        "puesto": "Ejecutivo de Ventas",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548175": {
        "nombre": "María González López",
        "departamento": "Recursos Humanos",
        "puesto": "Especialista en RRHH",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548176": {
        "nombre": "Carlos Rodríguez Martínez",
        "departamento": "Tecnología",
        "puesto": "Desarrollador Senior",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548177": {
        "nombre": "Ana Fernández Ruiz",
        "departamento": "Contabilidad",
        "puesto": "Contador",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548178": {
        "nombre": "Luis Sánchez Díaz",
        "departamento": "Marketing",
        "puesto": "Coordinador de Marketing",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548179": {
        "nombre": "Carmen Jiménez Torres",
        "departamento": "Operaciones",
        "puesto": "Supervisor de Operaciones",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548180": {
        "nombre": "Roberto Herrera Vega",
        "departamento": "Ventas",
        "puesto": "Gerente de Ventas",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548181": {
        "nombre": "Isabel Morales Castro",
        "departamento": "Administración",
        "puesto": "Asistente Administrativo",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548182": {
        "nombre": "Miguel Ángel Flores",
        "departamento": "Tecnología",
        "puesto": "Arquitecto de Software",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548183": {
        "nombre": "Patricia Ramírez Silva",
        "departamento": "Recursos Humanos",
        "puesto": "Gerente de RRHH",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    },
    "L03548184": {
        "nombre": "Fernando Aguilar Rojas",
        "departamento": "Finanzas",
        "puesto": "Analista Financiero",
        "pdf_url": f"{BASE_URL}/api/download/pdf/gnp_bmw.pdf",
        "pdf_nombre": "gnp_bmw.pdf"
    }
}

@app.route('/api/pdfs', methods=['GET'])
def list_pdfs():
    """Devuelve lista de PDFs con nombre y URL directa"""
    try:
        pdf_files = []
        for file in glob.glob(os.path.join(PDF_FOLDER, '*.pdf')):
            filename = os.path.basename(file)
            pdf_files.append({
                'nombre': filename,
                'path': os.path.abspath(file),
                'url': f"{BASE_URL}/api/download/pdf/{filename}"
            })
        return jsonify({'pdfs': pdf_files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/images', methods=['GET'])
def list_images():
    """Devuelve lista de imágenes con nombre y URL directa"""
    try:
        image_files = []
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
        for ext in extensions:
            for file in glob.glob(os.path.join(IMAGE_FOLDER, ext)):
                filename = os.path.basename(file)
                image_files.append({
                    'nombre': filename,
                    'path': os.path.abspath(file),
                    'url': f"{BASE_URL}/api/download/image/{filename}"
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

@app.route('/api/nomina/<numero_nomina>', methods=['GET'])
def buscar_nomina(numero_nomina):
    """Busca empleado por número de nómina"""
    try:
        if numero_nomina in NOMINAS_DB:
            empleado = NOMINAS_DB[numero_nomina]
            return jsonify({
                'numero_nomina': numero_nomina,
                'empleado': empleado,
                'encontrado': True
            })
        else:
            return jsonify({
                'numero_nomina': numero_nomina,
                'empleado': None,
                'encontrado': False,
                'mensaje': 'Número de nómina no encontrado'
            }), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/nominas', methods=['GET'])
def listar_nominas():
    """Lista todas las nóminas disponibles"""
    try:
        nominas = []
        for numero, datos in NOMINAS_DB.items():
            nominas.append({
                'numero_nomina': numero,
                'nombre': datos['nombre'],
                'departamento': datos['departamento'],
                'puesto': datos['puesto']
            })
        return jsonify({
            'total_nominas': len(nominas),
            'nominas': nominas
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)

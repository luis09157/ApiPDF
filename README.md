# API PDF e Imágenes

API simple en Python con Flask para manejar PDFs e imágenes.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar la API

```bash
python app.py
```

La API estará disponible en: `http://localhost:5000`

## Endpoints

### 1. Listar PDFs
- **GET** `/api/pdfs`
- Devuelve lista de PDFs con nombre y path

### 2. Listar Imágenes
- **GET** `/api/images`
- Devuelve lista de imágenes con nombre y path

### 3. Descargar PDF
- **GET** `/api/download/pdf/<filename>`
- Descarga un PDF específico

### 4. Descargar Imagen
- **GET** `/api/download/image/<filename>`
- Descarga una imagen específica

## Estructura de carpetas

```
ApiPDF/
├── pdf/          # Coloca tus PDFs aquí
├── images/       # Coloca tus imágenes aquí
├── app.py        # API principal
└── requirements.txt
```

## Ejemplos de uso

```bash
# Listar PDFs
curl http://localhost:5000/api/pdfs

# Listar imágenes
curl http://localhost:5000/api/images

# Descargar PDF
curl -O http://localhost:5000/api/download/pdf/ejemplo.pdf

# Descargar imagen
curl -O http://localhost:5000/api/download/image/ejemplo.jpg
```

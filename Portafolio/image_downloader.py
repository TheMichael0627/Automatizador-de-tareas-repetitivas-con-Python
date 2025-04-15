import os
import requests

# Lista de URLs de ejemplo
image_urls = [
    "https://picsum.photos/150/150",    # Added height parameter
    "https://picsum.photos/200/200",
    "https://picsum.photos/250/250",
    "https://i.pinimg.com/736x/80/91/fa/8091fa8645608e28df09385156d29d03.jpg",
    "https://i.pinimg.com/736x/11/d5/5e/11d55ec70bb6fe4696960189f7ffe422.jpg"
]

output_folder = "imagenes_descargadas"

# Crear carpeta si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Descargar imágenes
for i, url in enumerate(image_urls):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Get content type and set proper extension
        content_type = response.headers.get('content-type', '')
        if 'jpeg' in content_type or 'jpg' in content_type:
            ext = '.jpg'
        elif 'png' in content_type:
            ext = '.png'
        else:
            ext = '.jpg'  # default to jpg
            
        filename = f"imagen_{i + 1}{ext}"
        filepath = os.path.join(output_folder, filename)
        
        with open(filepath, "wb") as f:
            f.write(response.content)
            
        print(f"✅ Imagen guardada: {filename}")
            
    except Exception as e:
        print(f"❌ Error al descargar la imagen {url}: {str(e)}")
# 🥀 vainilla_exif.py

Script OSINT creado por Vanille para extraer metadatos EXIF de imágenes (.jpg/.jpeg) desde la línea de comandos. Minimalista, directo, perfecto para Termux, nodos personales o auditorías discretas.

---

## 📥 Instalación

```bash
git clone https://github.com/vanilleghost/vainilla_exif.git
cd vainilla_exif
pip install -r requirements.txt

> Asegúrate de tener Python 3 y pip instalados.




---

🚀 Uso

python3 vainilla_exif.py ruta/a/imagen.jpg

Ejemplo:

python3 vainilla_exif.py /sdcard/DCIM/Camera/IMG_2048.jpg


---

📌 Salida esperada

[+] EXIF data de 'IMG_2048.jpg':

DateTime               : 2025:08:03 03:21:45
Make                   : Xiaomi
Model                  : 23129RN51X
Software               : Android 15
ExposureTime           : 1/20
ISOSpeedRatings        : 400
...


---

🛑 Notas

Si la imagen no contiene EXIF, mostrará un mensaje avisando.

Algunas apps como WhatsApp, Instagram o editores de galería eliminan metadatos automáticamente.

Este script no modifica nada. Solo lee.



---

📦 Dependencias

Pillow (incluida en requirements.txt)



---

🧠 Autor: Vanille 
> 🐚 "Cada byte cuenta una historia. Cada imagen oculta una firma."




---

📝 Licencia

Este proyecto usa la licencia MIT.

© Vanille 2025 🖤

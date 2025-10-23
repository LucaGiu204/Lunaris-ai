# Guía de configuración del entorno

Esta guía propone una configuración mínima para empezar a experimentar con Lunaris.

## 1. Requisitos previos

- Python 3.10 o superior.
- `ffmpeg` instalado en el sistema (recomendado para manipulación de audio).
- Acceso a una clave de API compatible con OpenAI o servicio equivalente.

## 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install --upgrade pip
```

## 3. Instalar dependencias

Las dependencias iniciales se listan en `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Notas sobre dependencias

- `faster-whisper` requiere PyTorch o similar para aprovechar aceleración por GPU; consulte su [documentación oficial](https://github.com/guillaumekln/faster-whisper#requirements).
- `sounddevice` puede necesitar librerías del sistema como `portaudio`.
- `pyttsx3` ofrece un TTS local que funciona sin conexión; puede reemplazarse por otro proveedor si se prefiere.

## 4. Variables de entorno

Cree un archivo `.env` (no se versiona) con las credenciales necesarias. Ejemplo:

```bash
OPENAI_API_KEY="tu-clave"
```

Puede usar bibliotecas como [`python-dotenv`](https://pypi.org/project/python-dotenv/) en el futuro para cargar este archivo automáticamente.

## 5. Scripts útiles (opcional)

Se recomienda crear un `Makefile` o scripts en `pyproject.toml`/`package.json` para comandos frecuentes (formato, pruebas, ejecución). Esto se puede incorporar cuando existan prototipos ejecutables.

## 6. Próximos pasos

Con el entorno listo, el siguiente paso es definir la estructura mínima del código en `src/` para cada módulo de Lunaris.


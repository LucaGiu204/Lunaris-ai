# Lunaris-ai
# Lunaris — IA educativa con pizarra en tiempo real 🎓✨

**Lunaris** es una idea en desarrollo: una inteligencia artificial capaz de **hablar, razonar y dibujar** al mismo tiempo.
El objetivo es transformar la forma de estudiar con IA, combinando voz, texto y visualizaciones en una misma experiencia, como si fuera un profesor digital con un pizarrón frente a vos.

## 💡 Visión

Lunaris busca unir tres modos de comunicación:
- 🗣️ **Voz:** explicaciones orales naturales y pausadas.
- ✍️ **Texto:** registro de lo que se dice y fórmulas.
- 🎨 **Visual:** un “pizarrón” que muestra lo que la IA está razonando.

## 🧠 Propósito

Explorar el potencial de las IAs multimodales en educación.
Lunaris pretende ser un espacio de experimentación para crear interfaces de aprendizaje **más humanas, visuales e interactivas**.

## ⚙️ Configuración del entorno

Consulta `docs/environment-setup.md` para pasos detallados sobre cómo preparar un entorno virtual, instalar dependencias y gestionar variables de entorno.

Resumen rápido:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## 🗂️ Estructura inicial del código

```
src/
├── board/          # Renderizadores y abstracciones de pizarra
├── core/           # Orquestador de conversaciones y estado global
├── interface/      # Helpers para bootstrap de sesiones y UI
└── speech/         # Transcripción y síntesis de voz
```

La carpeta `src/` incluye stubs funcionales mínimos para comenzar a conectar los módulos:
- `src/core/engine.py` define la clase `ConversationEngine` y estructuras de datos básicas.
- `src/speech/` contiene transcripción (`transcriber.py`) y síntesis (`synthesizer.py`) de prueba.
- `src/board/renderer.py` ofrece un renderizador de consola para validar comandos.
- `src/interface/session.py` agrupa componentes para prototipos rápidos.
- `src/main.py` ejecuta un flujo de demostración con los stubs actuales (`python -m src.main`).

Estos componentes actúan como punto de partida para iteraciones posteriores que incorporen modelos reales de voz, lenguaje y dibujo.


    ## Práctica calificada 1-CC0C2

    ### **Instrucciones generales**:
    - **Plazo**: 10 días. Entrega un repositorio Git con todos los entregables.
    - **Tiempo estimado**: Cada proyecto ~6 horas (3 h implementación, 1.5 h teoría, 1 h video, 0.5 h exposición). Planifica 1-2 h diarias para evitar procrastinación.
    - **Entregables**:
    - **Repositorio Git**:
        - `README.md`: Instrucciones de ejecución, dependencias, tiempos.
        - `notebook.ipynb`: Código, resultados, preguntas teóricas escritas.
        - `data/nlp_prueba_cc0c2_large.csv`: Dataset generado.
        - `out/`: Gráficos/tablas generadas.
        - `video.mp4`: Video de 5-10 min en formato sprint.
        - `requirements.txt`: Dependencias (Python 3.x, NumPy, Pandas, Matplotlib, opcionalmente NLTK/spaCy, tokenizers, sentence-transformers).
        - `SEEDS_AND_VERSIONS.md`: Semillas (e.g., `random.seed(42)`), versiones de bibliotecas.
        - Mínimo **5 commits** por proyecto con mensajes en español (ejemplo: "Implementar BPE para PC1").
    - **Video (5-10 min, formato sprint)-Sugerencia**:
        - 0:00-0:45: Objetivo, historias de usuario, DoD.
        - 0:45-3:00: Demostración en vivo (Notebook/CLI, ejecución de código).
        - 3:00-4:30: Métricas clave, gráficos, análisis.
        - 4:30-5:00+: Riesgos, next sprint, ubicación de código/datos.
    - **Exposición (10 min + 15 min preguntas)**: Usa Notebook como apoyo. Responde preguntas orales.
    - **Restricciones antiplagio**: No uses IA generativa ni copies de internet. Verificación con MOSS/Turnitin y commits. Dataset `nlp_prueba_cc0c2_large.csv` asegura soluciones únicas.
    - **Formato del Notebook**:
    -  Objetivo y historias usuario.
    -  Setup reproducible (semillas, versiones).
    -  Implementación (celdas cortas, comentadas).
    -  Experimentos y métricas (tablas/gráficos).
    -  Preguntas teóricas (respuestas escritas, 1-2 párrafos c/u).
    -  Trade-offs, riesgos, next sprint.
    -  Conclusiones técnicas y evidencias.

    Se presenta un script genera un dataset ampliado con 10,000 oraciones en español relacionadas con NLP/IA, etiquetadas como 'Positivo', 'Negativo', o 'Neutral'. 
    Combina oraciones sintéticas (basadas en plantillas) y ejemplos reales inspirados en el dataset original.  El script usa listas de palabras y estructuras para garantizar diversidad y realismo.

    **Dataset**: Usa `nlp_prueba_cc0c2_large.csv` (~10,000 oraciones) generado con el script proporcionado. Descarga desde el enlace del repositorio o genera localmente.

    **Ejemplo de `nlp_prueba_cc0c2_large.csv`**
    ```
    Texto,Categoría
    La tokenización es clave para procesar texto,Positivo
    No entiendo los embeddings vectoriales,Negativo
    Los LLMs son impresionantes pero complejos,Neutral
    El curso de NLP es fascinante y útil,Positivo
    La programación en Python es complicada al principio,Negativo
    Entender los embeddings resulta útil en el curso de NLP,Positivo
    No entiendo cómo funciona la regularización, es confuso,Negativo
    La lematización parece interesante pero fundamental,Neutral
    Implementar modelos de lenguaje es innovador en proyectos reales,Positivo
    Los transformers son complicados y limitados para datasets pequeños,Negativo
    ```


    ### **Proyectos**

    #### **Proyecto 3: Tokenización con BPE personalizado**
    **Temas**: Tokenización, algoritmo BPE.  
    **Implementación**: Entrena BPE (con `tokenizers` o manual) para 5,000 oraciones de `nlp_prueba_cc0c2_large.csv`, generando un vocabulario de 2,000 tokens. Muestra 15 merges y tokenización de 10 oraciones. Compara con `bert-base-multilingual-cased`.  
    **Teoría**:
    1. Pasos del algoritmo BPE.
    2. Impacto del tamaño de vocabulario en OOV.
    3. Define subword regularization.
    4. BPE vs. WordPiece (diferencias).
    5. Rol de BPE en latencia de LLMs.  
    **Métricas**: Tamaño de vocabulario, longitud promedio de tokens, ejemplos de segmentación.  
    **Entregables**:
        - **Notebook**: Código, merges, teoría. Commit: "BPE personalizado PC1".
        - **Video**: Muestra merges, tokenización.  
        - **Exposición**: Presenta resultados, riesgos. Explica aplicaciones de BPE. 

    #### Rúbrica de evaluación (20 puntos por proyecto)

    | **Criterio** | **Descripción** | **Puntos** | **Detalles** |
    |--------------|-----------------|------------|--------------|
    | **Trabajo (Notebook)** | Jupyter Notebook con código, resultados, teoría escrita. | 3 | - **Correctitud funcional (1.5)**: Código ejecuta, usa `nlp_prueba_cc0c2_large.csv`, resultados coherentes. <br> - **Reproducibilidad y organización (1)**: Semillas fijas, versiones en `SEEDS_AND_VERSIONS.md`, estructura clara (`data/`, `out/`), 5+ commits con mensajes en español. <br> - **Teoría escrita (0.5)**: Respuestas a 5 preguntas claras, conectadas a NLP. |
    | **Video de ejecución** | Video de 5-10 min en formato sprint. | 4 | - **Guion sprint (1)**: Introduce objetivo, Historía de usuario, DoD (0:00-0:45). <br> - **Demo en vivo (1.5)**: Ejecuta Notebook, muestra código/resultados (0:45-3:00). <br> - **Métricas y análisis (1)**: Interpreta gráficos/tablas, justifica decisiones (3:00-4:30). <br> - **Cierre (0.5)**: Resume riesgos, next sprint, ubicación de código/datos (4:30-5:00+). |
    | **Exposición y preguntas** | Presentación (10 min) + preguntas orales (15 min). | 13 | - **Estructura y narrativa (3)**: Presentación clara, usa Notebook, explica implementación/teoría. <br> - **Profundidad técnica (4)**: Demuestra comprensión de conceptos (e.g., BPE, perplejidad). <br> - **Respuesta a preguntas orales (5)**: Responde 2-3 preguntas con precisión (e.g., "¿Cómo mejorarías el modelo?"). <br> - **Visualizaciones (1)**: Gráficos legibles con títulos/ejes. |

    **Notas**:
    - **Plagio**: Detectado por MOSS, commits inconsistentes, o respuestas genéricas = 0 puntos.
    - **Video**: <5 min resta 0.5 puntos. Audio/pantalla poco claros resta 0.5 puntos.
    - **Commits**: Menos de 5 commits resta 0.5 puntos. Mensajes genéricos reducen claridad.
    - **Exposición**: Falta de preparación (no responder preguntas por ejemplo) impacta  puntos de preguntas orales.

    #### Cronograma recomendado (10 días)
    Para evitar procrastinación:
    - **Día 1**: Crea repositorio, estructura Notebook, genera/instala `nlp_prueba_cc0c2_large.csv`. Commit: "Inicializar PC1".
    - **Día 2**: Implementa prototipo básico con dataset. Commit: "Prototipo inicial PC1".
    - **Día 3-4**: Completa implementación, calcula métricas. Commit: "Implementación principal PC1".
    - **Día 5-6**: Responde preguntas teóricas, genera gráficos en `out/`. Commit: "Teoría y visualizaciones PC1".
    - **Día 7**: Graba borrador de video, revisa guion sprint. Commit: "Borrador video PC1".
    - **Día 8**: Pule Notebook, verifica reproducibilidad. Commit: "Notebook final PC1".
    - **Día 9**: Graba video final, sube a repositorio. Commit: "Video final PC1".
    - **Día 10**: Prepara exposición, ensaya respuestas orales. Entrega final.






La estructura que debes seguir para tu proyecto es la siguiente:

```
.
├── data/
│   └── nlp_prueba_cc0c2_large.csv
├── out/
├── .gitignore
├── SEEDS_AND_VERSIONS.md
├── README.md
├── requirements.txt
├── notebook.ipynb
└── video.mp4
```

-----

### Explicación de la Estructura

  - **`data/`**: Esta carpeta contendrá los datos. El archivo **`nlp_prueba_cc0c2_large.csv`** será tu dataset de 10,000 oraciones. Es importante mantener los datos separados del código para una mejor organización.
  - **`out/`**: Aquí almacenarás los resultados de tus experimentos. Por ejemplo, los **gráficos** de la longitud de los tokens o cualquier otra tabla que generes. Esto ayuda a mantener limpio el directorio principal.
  - **`.gitignore`**: Un archivo opcional pero muy recomendable. Con él, le indicas a Git qué archivos debe ignorar para no subirlos al repositorio (por ejemplo, archivos temporales, el video o el propio dataset si es muy grande y no quieres que se suba).
  - **`SEEDS_AND_VERSIONS.md`**: En este archivo de texto, documentarás las **semillas** que usaste para la reproducibilidad (`random.seed()`, `numpy.random.seed()`, etc.) y las **versiones exactas** de las librerías que instalaste. Esto es crucial para que otros puedan replicar tu entorno y resultados.
  - **`README.md`**: El "manual" de tu proyecto. Debe contener una breve descripción, las **instrucciones para ejecutar** el notebook, una lista de las **dependencias**, y una estimación de los **tiempos** dedicados a cada tarea.
  - **`requirements.txt`**: Este archivo lista todas las librerías de Python que usaste en tu proyecto, junto con sus versiones exactas. Puedes generarlo fácilmente con el comando `pip freeze > requirements.txt`.
  - **`notebook.ipynb`**: Es el corazón de tu proyecto. Aquí irá todo el **código** (`Python`) para cargar los datos, implementar el algoritmo de tokenización BPE, ejecutar los experimentos, generar los resultados y responder las **preguntas teóricas**.
  - **`video.mp4`**: Tu video de 5-10 minutos, en formato sprint, demostrando y explicando tu proyecto.

-----
1.  **Fundamentos de la Tokenización**: ¿Qué es la tokenización y por qué es un paso fundamental en el procesamiento del lenguaje natural (NLP)?
2.  **Algoritmo BPE (Byte-Pair Encoding)**:
      * **¿Cómo funciona?**: Comprende los pasos del algoritmo: desde la inicialización con caracteres individuales hasta la creación de pares de bytes/subpalabras más frecuentes.
      * **Entrenamiento de BPE**: Investiga cómo entrenar un tokenizador BPE en un corpus de texto. Puedes usar la librería **`tokenizers`** de Hugging Face, que simplifica mucho este proceso.
      * **Merges**: Entiende qué son las "uniones" o `merges` y por qué son importantes para el algoritmo.
3.  **Tamaño del Vocabulario y OOV**:
      * **Out-of-Vocabulary (OOV)**: ¿Qué es un token OOV?
      * **Impacto del tamaño del vocabulario**: ¿Cómo afecta el tamaño del vocabulario la frecuencia de tokens OOV? ¿Por qué un vocabulario más grande reduce los tokens OOV pero aumenta la complejidad del modelo?
4.  **Regularización de Subpalabras (Subword Regularization)**: Aprende qué es y por qué se usa para mejorar la robustez de los modelos de lenguaje.
5.  **BPE vs. WordPiece**: Investiga las diferencias clave entre estos dos algoritmos de tokenización de subpalabras.
6.  **Latencia en LLMs**: Comprende cómo la tokenización, y en particular el algoritmo BPE, influye en la velocidad y el costo computacional de los grandes modelos de lenguaje (LLMs).

-----

### Secuencia de Implementación (Flujo de Trabajo)

1.  **Configuración Inicial**:

      * Crea la estructura de carpetas (`data/` y `out/`).
      * Crea los archivos `README.md`, `requirements.txt`, y `SEEDS_AND_VERSIONS.md`.
      * Instala las librerías necesarias (`pip install pandas numpy matplotlib tokenizers`).

2.  **Preparación de Datos**:

      * Ejecuta el script generador de datos para crear el archivo **`nlp_prueba_cc0c2_large.csv`** dentro de la carpeta `data/`.
      * En tu `notebook.ipynb`, carga las primeras 5,000 oraciones de este dataset, ya que solo necesitas una parte para entrenar el tokenizador.

3.  **Implementación del BPE**:

      * En el `notebook.ipynb`, utiliza la librería `tokenizers` para entrenar un tokenizador BPE personalizado en el subconjunto de datos.
      * Configura el vocabulario para que tenga un tamaño de **2,000 tokens**.
      * Obtén y muestra los primeros **15 merges** del proceso de entrenamiento.

4.  **Experimentación y Análisis**:

      * Usa el tokenizador que entrenaste para tokenizar **10 oraciones** de ejemplo.
      * Compara la salida con la tokenización de un modelo pre-entrenado como `bert-base-multilingual-cased`.
      * Calcula y visualiza métricas clave como el **tamaño de vocabulario** y la **longitud promedio de tokens**. Genera un gráfico y guárdalo en la carpeta `out/`.

5.  **Parte Teórica**:

      * En celdas de Markdown dentro del `notebook.ipynb`, responde las **cinco preguntas teóricas** que se especifican en el proyecto.

6.  **Creación del Video**:

      * Graba tu pantalla mientras ejecutas las celdas clave del `notebook.ipynb`.
      * Sigue la estructura del video sprint (`Objetivo`, `Demo en vivo`, `Métricas`, `Cierre`). Asegúrate de que tu voz sea clara y expliques lo que estás haciendo en cada paso.
      * Guarda el video como **`video.mp4`** en el directorio principal.

7.  **Preparación Final**:

      * Revisa que el `README.md` y el `SEEDS_AND_VERSIONS.md` estén completos.
      * Asegúrate de tener al menos **5 commits** en tu repositorio, con mensajes descriptivos en español.
      * Prepara tu exposición oral basándote en el notebook.







# PROMPT (pega esto tal cual en el chat del tutor)


---

# OBJETIVOS que se lograrán con este prompt

* Diseñar y ejecutar una **ruta de aprendizaje completa, personalizada y repetible** para aprender tokenización y BPE desde cero hasta maestría.
* Entender conceptualmente y **prácticamente** qué es la tokenización, cuándo usar subwords, y cómo funciona BPE internamente.
* Aprender a **entrenar un tokenizador BPE** con la librería `tokenizers` (incluyendo `merges.txt` y `vocab.json`), y saber interpretar los resultados.
* Evaluar empíricamente el **impacto del tamaño del vocabulario** sobre OOV y sobre la complejidad del modelo.
* Conocer y aplicar **subword regularization** para mejorar robustez del modelo en entrenamiento/inferencia.
* Comparar y elegir entre **BPE y WordPiece** según el caso de uso, con ejemplos y recomendaciones prácticas.
* Medir y optimizar la **latencia y coste** asociado a la tokenización en LLMs, con métricas y ejemplos reproducibles.
* Obtener habilidad para **resolver ejercicios prácticos y de programación**, diagnosticar errores en tokenizadores y aplicar buenas prácticas de producción.
* Contar con un **mecanismo de evaluación** (exámenes variados y rúbricas) que garantice que el aprendizaje es efectivo antes de avanzar.

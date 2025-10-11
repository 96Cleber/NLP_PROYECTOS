# Proyecto 3: Embeddings contextuales y anisotropía

Este proyecto explora y compara embeddings estáticos (Word2Vec) y contextuales (Sentence-Transformers) en una tarea de recuperación de información. También se implementa la métrica CSLS para mitigar la anisotropía en los embeddings contextuales.

# Estructura Proyecto
```
PROYECTO3-PC2/
├── data/
├── out/
├── scripts/
│   └── make_dataset.py
├── .dockerignore
├── .gitignore
├── Dockerfile 
├── Makefile
├── nlp_proyecto3_pc2.ipynb
├── README.md
├── requirements.txt
├── SEEDS_AND_VERSIONS.md
└── video.mp4
```

## Dependencias

Las dependencias del proyecto se encuentran en el archivo `requirements.txt`. Para instalarlas, se recomienda crear un entorno virtual y ejecutar:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Generación del Dataset

Para generar el dataset de reseñas de productos, ejecutar el siguiente comando:

```bash
make data
```

Este comando ejecutará el script `scripts/make_dataset.py` y generará el archivo `data/nlp_prueba_cc0c2.csv`, así como un archivo de hash `data/nlp_prueba_cc0c2.sha256`.

El tiempo de ejecución de `make data` es de aproximadamente 1 segundo.

## Verificación de Reproducibilidad

Para verificar que la generación del dataset es reproducible, ejecutar:

```bash
make verify-repro
```

## Ejecución del Notebook

El análisis y la implementación del proyecto se encuentran en el notebook `proyecto_3.ipynb`. Para ejecutarlo, es necesario tener un servidor de Jupyter Notebook en ejecución.

## Diseño del Generador de Texto

El generador de texto (`scripts/make_dataset.py`) crea un corpus de reseñas de productos utilizando un sistema de plantillas y listas de palabras polarizadas. El script genera oraciones combinando plantillas con productos y adjetivos positivos, negativos o neutrales. Esto permite crear un dataset balanceado y controlado para la tarea de clasificación de sentimientos.



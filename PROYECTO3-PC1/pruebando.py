import pandas as pd
from transformers import AutoTokenizer

# 1. Tokenización de palabra
def tokenize_word(text):
    return text.split()

# 2. Tokenización de carácter
def tokenize_char(text):
    return list(text)

# 3. Tokenización de subpalabra (usando un modelo pre-entrenado)
# Explicación:
# `AutoTokenizer.from_pretrained` carga un tokenizador pre-entrenado de la librería de Hugging Face.
# El modelo 'bert-base-multilingual-cased' usa WordPiece, un algoritmo similar a BPE.
subword_tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

# Oración de prueba
oracion_ejemplo = "La tokenización es clave para el NLP."

# Resultados
tokens_palabra = tokenize_word(oracion_ejemplo)
tokens_caracter = tokenize_char(oracion_ejemplo)
tokens_subpalabra = subword_tokenizer.tokenize(oracion_ejemplo)

print(f"Oración original: '{oracion_ejemplo}'")
print(f"Tokens por palabra: {tokens_palabra}")
print(f"Tokens por carácter: {tokens_caracter}")
print(f"Tokens por subpalabra: {tokens_subpalabra}")
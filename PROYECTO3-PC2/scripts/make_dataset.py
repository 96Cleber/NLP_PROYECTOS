
import argparse
import random
import pandas as pd
from pathlib import Path

def generar_oracion(productos, adjetivos_pos, adjetivos_neg, adjetivos_neu, plantillas):
    categoria = random.choice(["Positivo", "Negativo", "Neutral"])
    producto = random.choice(productos)
    
    if categoria == "Positivo":
        adjetivo = random.choice(adjetivos_pos)
    elif categoria == "Negativo":
        adjetivo = random.choice(adjetivos_neg)
    else:
        adjetivo = random.choice(adjetivos_neu)
        
    plantilla = random.choice(plantillas)
    texto = plantilla.format(producto=producto, adjetivo=adjetivo)
    
    return texto, categoria

def main():
    parser = argparse.ArgumentParser(description="Generar corpus de reseñas de productos.")
    parser.add_argument("--seed", type=int, default=42, help="Semilla para la generación de números aleatorios.")
    parser.add_argument("--n-samples", type=int, default=5000, help="Número de muestras a generar.")
    parser.add_argument("--out", type=str, default="data/nlp_prueba_cc0c2.csv", help="Ruta del archivo de salida.")
    parser.add_argument("--balance", action="store_true", help="Balancear el número de muestras por categoría.")
    args = parser.parse_args()

    random.seed(args.seed)

    productos = [
        "celular", "laptop", "auriculares", "teclado", "ratón", "monitor", "cámara", "tablet", "smartwatch", "impresora"
    ]

    adjetivos_pos = [
        "excelente", "rápido", "increíble", "fantástico", "magnífico", "impresionante", "confiable", "eficiente", "duradero", "genial"
    ]

    adjetivos_neg = [
        "defectuoso", "lento", "caro", "frágil", "terrible", "decepcionante", "inestable", "ruidoso", "pobre", "malo"
    ]

    adjetivos_neu = [
        "normal", "estándar", "promedio", "funcional", "aceptable", "decente", "regular", "común", "simple", "básico"
    ]

    plantillas = [
        "El {producto} es {adjetivo}.",
        "Este {producto} me parece {adjetivo}.",
        "La calidad del {producto} es {adjetivo}.",
        "Estoy muy contento con mi {producto}, es {adjetivo}.",
        "No recomiendo este {producto}, es {adjetivo}.",
        "El rendimiento del {producto} es {adjetivo}.",
        "Mi experiencia con el {producto} ha sido {adjetivo}.",
        "El diseño del {producto} es {adjetivo}, pero podría mejorar.",
        "En general, el {producto} es {adjetivo}.",
        "Si buscas un {producto} {adjetivo}, este es para ti."
    ]

    data = []
    if args.balance:
        n_per_category = args.n_samples // 3
        for categoria in ["Positivo", "Negativo", "Neutral"]:
            count = 0
            while count < n_per_category:
                texto, cat = generar_oracion(productos, adjetivos_pos, adjetivos_neg, adjetivos_neu, plantillas)
                if cat == categoria:
                    data.append([texto, cat])
                    count += 1
    else:
        for _ in range(args.n_samples):
            texto, categoria = generar_oracion(productos, adjetivos_pos, adjetivos_neg, adjetivos_neu, plantillas)
            data.append([texto, categoria])

    df = pd.DataFrame(data, columns=["Texto", "Categoría"])
    
    output_path = Path(args.out)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()

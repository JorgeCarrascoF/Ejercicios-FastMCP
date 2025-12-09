from fastmcp import FastMCP
import os
import sys

# Solo importamos lo ligero al principio
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "modelo_nasa_full.pkl")

server = FastMCP("NASA-Quality-Auditor")

@server.tool()
def auditar_calidad_codigo(ruta_archivo: str) -> str:
    """
    Analiza un archivo local. Carga el modelo bajo demanda.
    """
    # --- IMPORTS LAZY (Para que el servidor arranque rápido) ---
    import joblib
    import pandas as pd
    import radon.raw as raw
    import radon.complexity as cc
    from radon.metrics import h_visit
    
    # 1. Validación de rutas
    clean_filename = os.path.basename(ruta_archivo)
    safe_path = os.path.join(BASE_DIR, clean_filename)

    if not os.path.exists(safe_path):
        return f"Error: No encuentro '{clean_filename}' en la carpeta."

    if not os.path.exists(MODEL_FILE):
        return "Error CRÍTICO: No encuentro modelo_nasa_full.pkl"

    try:
        # 2. Carga del modelo (Solo ocurre cuando llamas a la tool)
        sys.stderr.write("[DEBUG] Cargando modelo NASA...\n")
        model_data = joblib.load(MODEL_FILE)
        model = model_data["model"]
        feature_names = model_data["features"]

        # 3. Lectura y Análisis
        with open(safe_path, 'r', encoding='utf-8') as f:
            code = f.read()

        r_analysis = raw.analyze(code)
        blocks = cc.cc_visit(code)
        total_cc = sum(b.complexity for b in blocks) if blocks else 0
        
        try:
            h_obj = h_visit(code)
            val_h1 = h_obj.total.h1
            val_effort = h_obj.total.effort
        except:
            val_h1, val_effort = 0, 0

        metricas = {
            "loc": r_analysis.loc,
            "complexity": total_cc,
            "h_uniq_op": val_h1,
            "comments": r_analysis.comments,
            "h_effort": val_effort
        }
        
        input_row = {feat: metricas.get(feat, 0) for feat in feature_names}
        df_input = pd.DataFrame([input_row])

        prob = model.predict_proba(df_input)[0][1]
        porcentaje = round(prob * 100, 2)
        
        riesgo = "CRÍTICO" if porcentaje > 75 else "MEDIO" if porcentaje > 40 else "BAJO"

        return f"AUDITORIA COMPLETA: Riesgo {riesgo} ({porcentaje}% bug probability)."

    except Exception as e:
        return f"Error interno: {str(e)}"

if __name__ == "__main__":
    server.run()
"""Funciones reutilizables del análisis RedConecta."""
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import joblib

def cargar_datos(ruta):
    df = pd.read_excel(ruta)
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")
    return df

def evaluar_calidad(df):
    numericas = ["trafico_datos_gb", "latencia_ms", "incidencias_reportadas", "tickets_soporte", "tiempo_resolucion_hr", "clientes_afectados"]
    return {"filas":len(df), "columnas":len(df.columns), "nulos":df.isna().sum().to_dict(), "duplicados_exactos":int(df.duplicated().sum()), "negativos":{c:int((df[c]<0).sum()) for c in numericas}, "sla":df["cumplimiento_sla"].value_counts().to_dict()}

def indicadores(df):
    return {"latencia_promedio_ms":float(np.mean(df["latencia_ms"])), "resolucion_promedio_hr":float(np.mean(df["tiempo_resolucion_hr"])), "incidencias_promedio":float(np.mean(df["incidencias_reportadas"])), "incumplimiento_pct":float(np.mean(df["cumplimiento_sla"].eq("No cumple"))*100)}

def correlacion(df):
    resultado=spearmanr(df["latencia_ms"],df["clientes_afectados"],nan_policy="omit")
    return {"rho_spearman":float(resultado.statistic),"p_valor":float(resultado.pvalue)}

def guardar_cache(obj,ruta):
    joblib.dump(obj,ruta)

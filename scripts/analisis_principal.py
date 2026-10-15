"""Ejecutar desde la raíz: python scripts/analisis_principal.py"""
from pathlib import Path
import sys, json
import matplotlib.pyplot as plt
import pandas as pd
from funciones_analisis import cargar_datos,evaluar_calidad,indicadores,correlacion,guardar_cache
RAIZ=Path(__file__).resolve().parents[1]
df=cargar_datos(RAIZ/'datos/dataset_set_D_telecomunicaciones.xlsx')
calidad=evaluar_calidad(df); metricas=indicadores(df); relacion=correlacion(df)
(RAIZ/'reportes/calidad_datos.json').write_text(json.dumps(calidad,indent=2,ensure_ascii=False),encoding='utf-8')
(RAIZ/'reportes/indicadores.json').write_text(json.dumps({**metricas,**relacion},indent=2,ensure_ascii=False),encoding='utf-8')
guardar_cache(metricas,RAIZ/'reportes/indicadores.joblib')
df[['fecha_registro','region','tipo_servicio','incidencias_reportadas','tickets_soporte','tiempo_resolucion_hr']].to_excel(RAIZ/'reportes/soporte_tecnico.xlsx',index=False)
df[['fecha_registro','tipo_servicio','clientes_afectados','latencia_ms','cumplimiento_sla']].to_excel(RAIZ/'reportes/experiencia_clientes.xlsx',index=False)
for columna,grupo,nombre,titulo in [('latencia_ms','region','latencia_region.png','Latencia promedio por región (ms)'),('tiempo_resolucion_hr','tipo_servicio','resolucion_servicio.png','Resolución promedio por servicio (horas)'),('incidencias_reportadas','region','incidencias_region.png','Incidencias promedio por región')]:
    fig,ax=plt.subplots(figsize=(8,4));df.groupby(grupo)[columna].mean().plot(kind='bar',ax=ax);ax.set_title(titulo);ax.set_xlabel('');ax.tick_params(axis='x',rotation=0);fig.tight_layout();fig.savefig(RAIZ/'graficos'/nombre,dpi=160);plt.close(fig)
fig,ax=plt.subplots(figsize=(7,4));df['cumplimiento_sla'].value_counts().plot(kind='bar',ax=ax);ax.set_title('Cumplimiento SLA (registros)');ax.tick_params(axis='x',rotation=0);fig.tight_layout();fig.savefig(RAIZ/'graficos/sla.png',dpi=160);plt.close(fig)
print('Análisis terminado:',metricas,'correlación:',relacion,'calidad:',calidad)

# RedConecta Telecom — Ciencia de Datos, Semana 8

## Objetivo
Analizar latencia, incidencias, tickets, tiempos de resolución y SLA para apoyar decisiones operacionales.

## Preguntas
¿Cómo varía la latencia por región? ¿Cómo varía la resolución por servicio? ¿Qué proporción de registros cumple el SLA?

## Datos
Archivo `datos/dataset_set_D_telecomunicaciones.xlsx`, 200 registros y 10 columnas. Caso académico IACC.

## Metodología
Carga y validación → análisis descriptivo → correlación exploratoria Spearman → gráficos → exportación de reportes → documentación. La correlación no demuestra causalidad.

## Ejecución
Desde la raíz del proyecto:
```bash
python -m pip install -r requirements.txt
python scripts/analisis_principal.py
```

## Archivos
- `scripts/funciones_analisis.py`: funciones reutilizables (NumPy, SciPy y Joblib).
- `scripts/analisis_principal.py`: flujo principal.
- `graficos/`: visualizaciones PNG.
- `reportes/`: salidas por área, indicadores y validación.
- `datos/`: dataset original.
- `analisis_principal.ipynb`: notebook de reproducción.

## Resultados principales
Latencia promedio 64,86 ms; resolución promedio 25,33 h; 104 de 200 registros (52 %) no cumplen SLA. Son resultados descriptivos, no prueba de causa.

## Calidad y ética
Revisar nulos, duplicados, rangos y categorías; el origen de las etiquetas SLA y la representatividad no están verificados. No inferir causalidad ni aplicar decisiones individuales automáticas.

## Colaboración y control de versiones

El proyecto utiliza Git y GitHub como herramientas de control de versiones, documentación y gestión del código fuente.

La rama `main` se establece como la versión principal del proyecto, donde se mantienen los archivos del análisis, los scripts de Python, los dashboards, los reportes y la documentación técnica.

Para facilitar el trabajo colaborativo, se propone el siguiente procedimiento:

1. Crear ramas independientes para desarrollar nuevas funcionalidades o realizar modificaciones.
2. Registrar los cambios mediante commits descriptivos.
3. Utilizar pull requests para revisar e integrar modificaciones a la rama principal.
4. Mantener actualizado el archivo README.md con las instrucciones y características del proyecto.
5. Documentar las modificaciones realizadas para asegurar la trazabilidad y reproducibilidad del análisis.

Esta metodología permite mantener un desarrollo organizado, facilitar la revisión del código y preparar el proyecto para futuras colaboraciones.

El proyecto se encuentra estructurado para permitir la participación de otros integrantes, quienes podrán contribuir al análisis estadístico, la visualización de datos y la documentación técnica.

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

## Calidad de los datos y consideraciones éticas

### Evaluación de la calidad de los datos

Para garantizar la confiabilidad del análisis operacional de RedConecta Telecom S. A., realicé una evaluación de la calidad del dataset `dataset_set_D_telecomunicaciones.xlsx`, considerando criterios de integridad, consistencia, validez y duplicidad de los registros.

El conjunto de datos contiene 200 registros y 10 variables relacionadas con el desempeño de los servicios de telecomunicaciones.

Durante la revisión inicial obtuve los siguientes resultados:

- **Valores nulos:** no se identificaron valores faltantes en las columnas analizadas.
- **Registros duplicados:** no se detectaron filas completamente duplicadas.
- **Valores negativos:** no se encontraron valores negativos en las seis variables numéricas examinadas.
- **Integridad:** los registros presentan información suficiente para realizar el análisis exploratorio.
- **Consistencia:** las verificaciones iniciales no evidenciaron las anomalías mencionadas, aunque se requieren controles adicionales para validar la coherencia operacional.

### Limitaciones identificadas

Aunque el dataset presenta condiciones favorables para el análisis exploratorio, reconozco que existen algunas limitaciones:

1. La ausencia de valores nulos no garantiza que todos los datos sean correctos.
2. No se dispone de información detallada sobre las causas específicas de las incidencias.
3. Los indicadores de latencia y resolución deben interpretarse considerando las características de cada servicio y región.
4. No se cuenta con todos los antecedentes necesarios para determinar las causas de incumplimiento del SLA.
5. Los resultados representan los registros disponibles y no necesariamente el comportamiento completo de la infraestructura.

### Consideraciones éticas

Durante el desarrollo del proyecto considero fundamental aplicar principios de responsabilidad, transparencia y protección de la información.

En primer lugar, utilizo los datos exclusivamente con fines de análisis académico, evitando interpretaciones que puedan perjudicar injustificadamente a determinadas regiones, servicios o equipos de trabajo.

Asimismo, considero importante presentar los resultados de manera objetiva, incluyendo tanto los indicadores favorables como las limitaciones identificadas.

Desde una perspectiva de confidencialidad, reconozco la necesidad de proteger la información operacional y evitar la publicación de datos personales o sensibles sin autorización.

También considero que las decisiones relacionadas con la asignación de recursos, la priorización de incidencias y la evaluación del desempeño deben fundamentarse en información confiable y contextualizada.

### Reflexión final

A partir de este proyecto, comprendí que la calidad de los datos influye directamente en la confiabilidad de los resultados y en las decisiones que pueden adoptarse dentro de una organización.

Un análisis basado en información incorrecta o incompleta podría generar asignaciones inadecuadas de recursos, diagnósticos equivocados y dificultades para mejorar la experiencia de los clientes.

Por esta razón, considero fundamental mantener procedimientos de validación, documentación y revisión continua, promoviendo una utilización responsable y ética de la ciencia de datos.

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

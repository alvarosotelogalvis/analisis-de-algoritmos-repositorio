# Semana 02 - Entorno de trabajo en Python

Archivos de la sesion practica de la Semana 2 del curso.

## Crear y activar el entorno virtual

- Crear (desde la raiz del repositorio): `python -m venv venv`
- Activar (Windows/PowerShell): `venv\Scripts\Activate.ps1`
- Desactivar: `deactivate`

## Reproducir el entorno

Con el entorno virtual activado, desde la raiz del repositorio:

```
pip install -r requirements.txt
```

Esto reinstala las mismas dependencias del proyecto, fijadas en el archivo requirements.txt generado con `pip freeze`.
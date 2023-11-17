# Cash Flow

Aplicación para el control de flujo de caja.

## Requisitos Previos

Asegúrate de tener instalado Python y pip en tu sistema.

## Configuración del Entorno Virtual

1. Clona el repositorio desde GitHub:

    ```bash
    git clone https://github.com/AndriwRC/cash-flow.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd cash-flow
    ```

3. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En sistemas basados en Unix
    # O
    .\venv\Scripts\activate  # En sistemas Windows
    ```

## Instalación de Dependencias

Instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r req.txt

```

## Configuración de la Base de Datos

```bash
python manage.py migrate

```

## Ejecución del Servidor

```bash
python manage.py runserver
```

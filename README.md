# Aplicación de blog de cursos online
## Iniciar entorno virtual

Mac/Linux:
```bash
source venv/bin/activate
```

Windows:
```powershell
venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Migrar información a la base de datos

```bash
python manage.py migrate
```

## Crear superusuario

```bash
python manage.py createsuperuser
```

## Ejecutar servidor de desarrrollo

```bash
python manage.py runserver
```

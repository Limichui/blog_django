from django.core.exceptions import ValidationError

def validar_numeros_positivos(value):
    if value <= 0:  # Verifica que el valor sea mayor o igual a 1
        raise ValidationError(
            f'Este campo debe tener un valor igual o mayor a 1.',
            params = {
                'value': value,
            }
        )

def validar_numeros_valor_maximo(value):
    if value > 180:  # Verifica que el valor sea mayor o igual a 1
        raise ValidationError(
            f'Este campo debe tener maximo de 180.',
            params = {
                'value': value,
            }
        )
        
def validar_longitud_minima(value):
    if isinstance(value, str) and len(value.strip()) < 6:  # Verifica que tenga al menos 3 caracteres
        raise ValidationError(
            f'Este campo debe contener al menos 6 caracteres.',
            params={'value': value},
        )

def validar_longitud_maxima(value):
    if isinstance(value, str) and len(value.strip()) > 100:  # Verifica que tenga al menos 3 caracteres
        raise ValidationError(
            f'Este campo debe contener maixmo 100 caracteres.',
            params={'value': value},
        )
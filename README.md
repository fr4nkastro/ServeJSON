# Readme para el Servidor HTTP con Puntos de Control

Este es un script simple de servidor HTTP escrito en Python utilizando el módulo `http.server`. El servidor proporciona puntos de control para manipular varios parámetros como el estado de la bomba, caudal, estados de válvulas, humedad, temperatura, volumen, estados del ventilador, etc.

## Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script usando el siguiente comando:

   ```bash
   python <nombre_del_archivo>.py
   ```

   Reemplaza `<nombre_del_archivo>` con el nombre real de tu script de Python.

3. El servidor se iniciará en `http://127.0.0.1:8080/`.

## Puntos de Control

### `/action`

- **Método:** GET

Este punto de control se utiliza para realizar varias acciones proporcionando el parámetro `opt` en la URL.

#### Opciones disponibles:

- `pump`: Alternar el estado de la bomba.
- `caudal`: Aumentar el valor de caudal.
- `valve1`: Alternar el estado de la válvula1.
- `humidity`: Aumentar el valor de humedad.
- `temperature`: Aumentar el valor de temperatura.
- `volume`: Aumentar el valor de volumen.
- `fanIn`: Alternar el estado del ventilador de entrada (`fanIn`).
- `fanOut`: Alternar el estado del ventilador de salida (`fanOut`).
- `valve2`: Alternar el estado de la válvula2.
- `valve3`: Alternar el estado de la válvula3.

**Ejemplo:** Para alternar el estado de la bomba, realiza una solicitud GET a `http://127.0.0.1:8080/action?opt=pump`.

### Manejo de Errores

- Si el punto de control solicitado no se encuentra, el servidor devolverá un error 404.

## Configuración del Servidor

- El servidor se ejecuta en `http://127.0.0.1:8080/` de forma predeterminada.
- Se habilita el Intercambio de Recursos de Origen Cruzado (CORS) para permitir el acceso desde cualquier origen.

## Dependencias

El script utiliza los siguientes módulos de Python:

- `http.server`: Funcionalidad básica del servidor HTTP.
- `json`: Codificación y decodificación JSON.
- `re`: Operaciones de expresiones regulares.

## Nota Importante

Este script está destinado con fines educativos y puede requerir mejoras adicionales para su uso en producción. Siempre ten en cuenta las mejores prácticas de seguridad al implementar un servidor en un entorno de producción.

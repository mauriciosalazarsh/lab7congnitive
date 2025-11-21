# Lab 07 - AWS Lambda + Flask

## Estructura del Proyecto

```
lab07/
├── pregunta1/          # API de tipo de cambio
│   ├── app.py
│   ├── lambda_function.py
│   └── requirements.txt
│
└── pregunta2/          # Catálogo de vehículos
    ├── app.py
    ├── lambda_function.py
    ├── rds_config.py
    └── requirements.txt
```

## Pregunta 1: API Tipo de Cambio

### Despliegue

1. **Crear el ZIP:**
   ```bash
   cd pregunta1
   zip -r function.zip .
   ```

2. **Crear Lambda en AWS:**
   - Ir a AWS Lambda → Create function
   - Name: `tipocambio-flask`
   - Runtime: Python 3.12
   - Upload from `.zip file` → seleccionar `function.zip`

3. **Configurar Handler:**
   - Configuration → General → Handler: `lambda_function.handler`

4. **Crear API Gateway:**
   - API Gateway → Create API → HTTP API
   - Integration: seleccionar función Lambda
   - Copiar endpoint generado

5. **Probar:**
   - GET `https://tu-endpoint.execute-api.us-east-1.amazonaws.com/`

### Resultado Esperado
```json
{
  "dolar": 3.78,
  "euro": 3.51,
  "sol": 1.0
}
```

## Pregunta 2: Catálogo de Vehículos

### Configuración Previa

1. **Crear RDS MySQL:**
   - Engine: MySQL
   - Public access: Yes
   - Security Group: permitir puerto 3306

2. **Crear base de datos:**
   ```sql
   CREATE DATABASE vehiculosdb;
   USE vehiculosdb;

   CREATE TABLE vehiculos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       marca VARCHAR(50),
       modelo VARCHAR(50),
       precio DECIMAL(10,2)
   );

   INSERT INTO vehiculos (marca, modelo, precio) VALUES
   ('Toyota', 'Yaris', 12000),
   ('Kia', 'Rio', 13500),
   ('Honda', 'Civic', 18000);
   ```

3. **Actualizar credenciales:**
   - Editar `rds_config.py` con el endpoint RDS real

### Despliegue

1. **Crear el ZIP:**
   ```bash
   cd pregunta2
   zip -r function.zip .
   ```

2. **Crear Lambda en AWS:**
   - Name: `catalogo-vehiculos`
   - Runtime: Python 3.12
   - Upload `function.zip`
   - Handler: `lambda_function.handler`

3. **Crear API Gateway:**
   - HTTP API vinculada a la función Lambda

4. **Probar:**
   - GET `https://tu-endpoint.execute-api.us-east-1.amazonaws.com/catalogo`

### Resultado Esperado
```json
[
  {
    "id": 1,
    "marca": "Toyota",
    "modelo": "Yaris",
    "precio": 12000.0
  },
  {
    "id": 2,
    "marca": "Kia",
    "modelo": "Rio",
    "precio": 13500.0
  },
  {
    "id": 3,
    "marca": "Honda",
    "modelo": "Civic",
    "precio": 18000.0
  }
]
```

## Notas

- Las dependencias se instalan automáticamente desde `requirements.txt` al subir el ZIP
- Para AWS Instructure Sandbox, usar DynamoDB en lugar de RDS si no está disponible
- Los endpoints generados son únicos para cada despliegue

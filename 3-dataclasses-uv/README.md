# Tarea Práctica: Sistema de Análisis de Notas Universitarias

## Descripción General

Crear un sistema para gestionar y analizar notas de estudiantes universitarios utilizando dataclasses, `faker` para generar datos de prueba, y `pandas` para exportar en CSV.

## Objetivos

- Aplicar dataclasses para modelar datos estructurados
- Usar `faker` para generar datasets realistas
- Implementar estadísticas básicas
- Configurar proyecto con uv

## Parte 1: Modelado de Datos con Dataclasses

### 1.1 Carrera

- `codigo: str` - Código único (ej: "ING001")
- `nombre: str` - Nombre completo
- `facultad: str` - Facultad correspondiente
- `duracion_semestres: int` - Duración total

### 1.2 Estudiante

- `id: int` - Identificador único
- `nombre: str` y `apellido: str`
- `email: str` - Correo institucional
- `fecha_nacimiento: date`
- `carrera: Carrera` - Carrera que estudia
- `semestre_actual: int`
- `fecha_ingreso: date`

### 1.3 Prueba (Clase principal)

- `id: int` - Identificador único
- `nombre: str` - Nombre de la prueba
- `materia: str` - Materia correspondiente
- `fecha: date` - Fecha de aplicación
- `puntaje_maximo: float`
- `calificaciones: list[Calificacion]`

**Métodos requeridos:**

- `agregar_calificacion(calificacion: Calificacion)`
- `guardar_notas_csv(archivo: str = None) -> str` - Usar pandas para exportar a CSV
- `obtener_estadisticas() -> dict` - Estadísticas básicas con (promedio, nota mínima, nota máxnima)

### 1.4 Calificacion

- `estudiante: Estudiante`
- `prueba: Prueba`
- `puntaje: float`
- `fecha_calificacion: datetime` - Default: now

**Propiedades (@property):**

- `porcentaje: float` - (puntaje/puntaje_maximo \* 100)
- `nota_final: float` - Nota entre 1.0 y 7.0 (50% de exigencia)
- `aprobado: bool` - True si nota >= 4.0

## Parte 2: Generación de Datos con Faker

Implementar clase `GeneradorDatos`:

### 2.1 Carreras

- Crear mínimo 5 carreras diferentes
- Incluir distintas facultades

### 2.2 Estudiantes

- Generar 100-200 estudiantes
- Usar `Faker('es_CL')`
- Distribuir entre carreras aleatoriamente
- Fechas de nacimiento coherentes (18-25 años)

### 2.3 Pruebas y Calificaciones

- Crear pruebas para mínimo 8 materias
- 2-3 pruebas por materia de diferentes tipos
- Calificaciones para muestra aleatoria de estudiantes
- Distribuciones de notas realistas

## Parte 3: Análisis de datos

Implementar clase `AnalizadorRendimiento`:

### 3.1 Análisis Básicos

- Ranking de estudiantes: Top 10 con mejor promedio
- Análisis por materia: Nota promedio, porcentaje de aprobación

### 3.2 Exportación

- `guardar_notas_csv()` debe usar pandas para crear DataFrame estructurado
- Incluir información de estudiante, prueba y calificación
- Generar nombres de archivo automáticamente si es que no se indica como parámetro

## Programa Principal

Crear `main.py` que:

1. Genere dataset completo de ejemplo
2. Demuestre funcionamiento de todas las clases
3. Exporte mínimo 2 archivos CSV
4. Muestre análisis principales por pantalla

## Extras

1. Actualmente la materia para las pruebas se selecciona de una lista aleatoria general. Añade un atributo en Carrera que permita almacenar las materias específicas de cada carrera, y así poder hacer que las pruebas sean coherentes.
2. Genera IDs aleatorios no correlativos para cada estudiante, verificando que el ID no esté utilizado al momento de crear un nuevo estudiante.
3. Actualmente el puntaje de la calificación no tiene en consideración el puntaje de la prueba, por lo que puede ser mayor. Corrige la implementación para que al ingresar calificaciones la puntuación obtenida no pueda superar la máxima de prueba.
4. Añade validación en el constructor de Estudiante para verificar que el email termine con un dominio universitario válido (ej: @umag.cl).
5. Implementa un método `obtener_estudiantes_por_carrera(codigo_carrera: str)` en GeneradorDatos que retorne todos los estudiantes de una carrera específica.
6. En la implementación actual, las calificaciones se generan como un atributo de la clase GeneradorDatos. Modifica la implementación para que se añadan a cada prueba, y que no sean un atributo de la clase GeneradorDatos en sí.
7. Crea un método `obtener_pruebas_por_periodo(fecha_inicio: date, fecha_fin: date)` en GeneradorDatos para listar las pruebas en un rango de fechas determinado.
8. Implementar `AnalizadorRendimiento.ranking_estudiantes()`.
9. Implementar `AnalizadorRendimiento.analizar_materias()`.
10. Añade un atributo a `Estudiante` que indique las materias que está cursando. Al ingresar calificaciones en las pruebas, verifica que cada prueba tenga al menos el 60% de los estudiantes inscritos y que cada estudiante sólo tenga una calificación por materia.
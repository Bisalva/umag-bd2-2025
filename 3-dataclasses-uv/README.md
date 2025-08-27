# Tarea Práctica: Sistema de Análisis de Notas Universitarias

## Descripción General

Crear un sistema para gestionar y analizar calificaciones de estudiantes universitarios utilizando dataclasses, faker para generar datos de prueba, y pandas para exportar en CSV.

## Objetivos

- Aplicar dataclasses para modelar datos estructurados
- Usar `faker` para generar datasets realistas
- Implementar análisis de datos con pandas
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
- `tipo: str` - 'parcial', 'final', 'quiz', 'tarea'
- `fecha: date` - Fecha de aplicación
- `puntaje_maximo: float`
- `peso_porcentual: float` - Peso 0-100
- `calificaciones: List[Calificacion]`

**Métodos requeridos:**
- `agregar_calificacion(calificacion: Calificacion)`
- `guardar_notas_csv(archivo: str = None) -> str` - Usar pandas para exportar a CSV
- `obtener_estadisticas() -> dict` - Estadísticas básicas con pandas

### 1.4 Calificacion
- `estudiante: Estudiante`
- `prueba: Prueba`
- `puntaje: float`
- `fecha_calificacion: datetime` - Default: now

**Propiedades (@property):**
- `porcentaje: float` - (puntaje/puntaje_maximo * 100)
- `nota_final: float` - Nota entre 1.0 y 7.0 (50% de exigencia)
- `aprobado: bool` - True si nota >= 4.0

## Parte 2: Generación de Datos con Faker (25 puntos)

Implementar clase `GeneradorDatos`:

### 2.1 Carreras
- Crear mínimo 5 carreras diferentes
- Incluir distintas facultades

### 2.2 Estudiantes
- Generar 100-200 estudiantes
- Usar `Faker('es_ES')`
- Distribuir entre carreras aleatoriamente
- Fechas de nacimiento coherentes (18-25 años)

### 2.3 Pruebas y Calificaciones
- Crear pruebas para mínimo 8 materias
- 2-3 pruebas por materia de diferentes tipos
- Calificaciones para muestra aleatoria de estudiantes
- Distribuciones de notas realistas

## Parte 3: Análisis de datos (35 puntos)

Implementar clase `AnalizadorRendimiento`:

### 3.1 Análisis Básicos
- Ranking de estudiantes: Top 10 con mejor promedio
- Análisis por materia: Nota promedio, porcentaje de aprobación

### 3.2 Exportación
- `guardar_notas_csv()` debe usar pandas para crear DataFrame estructurado
- Incluir información de estudiante, prueba y calificación
- Generar nombres de archivo automáticamente

## Programa Principal

Crear `main.py` que:
1. Genere dataset completo de ejemplo
2. Demuestre funcionamiento de todas las clases
3. Exporte mínimo 2 archivos CSV
4. Muestre análisis principales por pantalla

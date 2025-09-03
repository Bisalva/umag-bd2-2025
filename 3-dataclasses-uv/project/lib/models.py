from dataclasses import dataclass, field
from datetime import date, datetime
from statistics import mean

import pandas as pd


@dataclass
class Carrera:
    """Representa una carrera universitaria.

    Attributes:
        codigo (str): Código único de la carrera (por ejemplo, "INF").
        nombre (str): Nombre oficial de la carrera.
        facultad (str): Facultad o unidad académica a la que pertenece.
        duracion_semestres (int): Duración nominal en semestres.
    """

    codigo: str
    nombre: str
    facultad: str
    duracion_semestres: int


@dataclass
class Estudiante:
    """Representa a un estudiante.

    Attributes:
        id (int): Identificador único del estudiante.
        nombre (str): Nombres del estudiante.
        apellido (str): Apellidos del estudiante.
        email (str): Correo electrónico institucional o personal.
        fecha_nacimiento (date): Fecha de nacimiento.
        carrera (Carrera): Carrera a la que pertenece.
        semestre_actual (int): Semestre que cursa actualmente.
        fecha_ingreso (date): Fecha de ingreso a la institución.
    """

    id: int
    nombre: str
    apellido: str
    email: str
    fecha_nacimiento: date
    carrera: Carrera
    semestre_actual: int
    fecha_ingreso: date


@dataclass
class Prueba:
    """Representa una evaluación o prueba aplicada a estudiantes.

    Attributes:
        id (int): Identificador único de la prueba.
        nombre (str): Nombre de la prueba (p. ej., "Control 1").
        materia (str): Asignatura a la que corresponde la prueba.
        fecha (date): Fecha en que se rinde la prueba.
        puntaje_maximo (float): Puntaje máximo posible de la prueba.
        calificaciones (list[Calificacion]): Lista de calificaciones registradas.
    """

    id: int
    nombre: str
    materia: str
    fecha: date
    puntaje_maximo: float
    calificaciones: list["Calificacion"]

    def agregar_calificacion(self, calificacion: "Calificacion"):
        """Agrega una calificación a la prueba.

        Args:
            calificacion (Calificacion): Calificación a incorporar.

        Returns:
            None: La calificación se agrega a ``self.calificaciones``.
        """
        self.calificaciones.append(calificacion)

    def guarda_notas_csv(self, archivo: str | None = None) -> str:
        """Guarda las notas de la prueba en un archivo CSV.

        Args:
            archivo (str | None): Ruta del archivo CSV de salida. Si es ``None``,
                se construye un nombre base automáticamente.

        Returns:
            str: Ruta/nombre del archivo utilizado para guardar el CSV.

        Side Effects:
            Crea o sobrescribe el archivo CSV en el sistema de archivos.
        """
        if archivo is None:
            archivo = f"{self.fecha.strftime('%d%m%Y')}_{self.nombre}"

        calificaciones_guardar = []
        for calificacion in self.calificaciones:
            estudiante = calificacion.estudiante
            calificaciones_guardar.append(
                {
                    "prueba": self.nombre,
                    "estudiante": f"{estudiante.nombre} {estudiante.apellido}",
                    "nota": calificacion.nota_final,
                    "aprobado": calificacion.aprobado,
                }
            )

        df_notas = pd.DataFrame(calificaciones_guardar)
        df_notas.to_csv(archivo)

        return archivo

    def obtener_estadisticas(self) -> dict[str, float]:
        """Calcula estadísticas básicas de las calificaciones de la prueba.

        Calcula el promedio, la nota mínima y la nota máxima considerando
        ``Calificacion.nota_final`` de cada registro.

        Returns:
            dict[str, float]: Diccionario con las claves ``"promedio"``,
            ``"nota mínima"`` y ``"nota máxima"``.

        Raises:
            statistics.StatisticsError: Si no hay calificaciones al calcular el
                promedio.
            ValueError: Si no hay calificaciones al calcular mínimos/máximos.
        """
        notas = [calificacion.nota_final for calificacion in self.calificaciones]
        return {
            "promedio": mean(notas),
            "nota mínima": min(notas),
            "nota máxima": max(notas),
        }


@dataclass
class Calificacion:
    """Representa la calificación de un estudiante en una prueba.

    Attributes:
        estudiante (Estudiante): Estudiante evaluado.
        prueba (Prueba): Prueba asociada a la calificación.
        puntaje (float): Puntaje bruto obtenido (mismo dominio que ``puntaje_maximo``).
        fecha_calificacion (datetime): Momento en que se registró la calificación.
    """

    estudiante: Estudiante
    prueba: Prueba
    puntaje: float
    fecha_calificacion: datetime = field(default_factory=datetime.now)

    @property
    def porcentaje(self) -> float:
        """Porcentaje obtenido respecto del puntaje máximo de la prueba.

        Returns:
            float: Porcentaje en el rango 0-100.
        """
        return self.puntaje / self.prueba.puntaje_maximo * 100

    @property
    def nota_final(self) -> float:
        """Nota final en escala 1.0-7.0 derivada del porcentaje obtenido.

        Se aplica una transformación lineal: ``1 + 6 * (porcentaje / 100)``.

        Returns:
            float: Nota final en el intervalo [1.0, 7.0].
        """
        return 1 + (6 * self.porcentaje / 100)

    @property
    def aprobado(self) -> bool:
        """Indica si la calificación es aprobatoria.

        Returns:
            bool: ``True`` si ``nota_final >= 4.0``, en caso contrario ``False``.
        """
        return self.nota_final >= 4.0

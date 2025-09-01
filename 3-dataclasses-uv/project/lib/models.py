from dataclasses import dataclass, field
from datetime import date, datetime
from statistics import mean

import pandas as pd


@dataclass
class Carrera:
    codigo: str
    nombre: str
    facultad: str
    duracion_semestres: int


@dataclass
class Estudiante:
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
    id: int
    nombre: str
    materia: str
    fecha: date
    puntaje_maximo: float
    calificaciones: list["Calificacion"]

    def agregar_calificacion(self, calificacion: "Calificacion"):
        """Agrega una calificación a la lista de calificaciones de la prueba."""
        self.calificaciones.append(calificacion)

    def guarda_notas_csv(self, archivo: str | None = None) -> str:
        """Guarda las notas de la prueba en un archivo CSV.
        Si no se indica un nombre de archivo, se genera uno automáticamente.
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
        """Obtiene estadísticas de las calificaciones de la prueba (promedio, mínima, máxima)."""
        notas = [calificacion.nota_final for calificacion in self.calificaciones]
        return {
            "promedio": mean(notas),
            "nota mínima": min(notas),
            "nota máxima": max(notas),
        }


@dataclass
class Calificacion:
    estudiante: Estudiante
    prueba: Prueba
    puntaje: float
    fecha_calificacion: datetime = field(default_factory=datetime.now)

    @property
    def porcentaje(self) -> float:
        """Obtiene el porcentaje de la calificación."""
        return self.puntaje / self.prueba.puntaje_maximo * 100

    @property
    def nota_final(self) -> float:
        """Obtiene la nota final (1.0 a 7.0) de la calificación."""
        return 1 + (6 * self.porcentaje / 100)

    @property
    def aprobado(self) -> bool:
        """Determina si la calificación fue aprobada (nota final >= 4.0)."""
        return self.nota_final >= 4.0

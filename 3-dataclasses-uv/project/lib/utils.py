from random import choice, randint

from faker import Faker

from lib.models import Calificacion, Carrera, Estudiante, Prueba


class GeneradorDatos:
    """Genera datos de ejemplo de carreras, estudiantes y pruebas.

    Esta clase inicializa colecciones con información realista usando Faker.

    Attributes:
        carreras (list[Carrera]): Catálogo base de carreras.
        estudiantes (list[Estudiante]): Conjunto de estudiantes generados.
        pruebas (list[Prueba]): Conjunto de pruebas generadas.
        calificaciones (list[Calificacion]): Lista de calificaciones generadas.
        _materias (list[str]): Lista de nombres de asignaturas disponibles.
        _fake (Faker): Generador de datos configurado para `es_CL`.
    """

    def __init__(self, n_estudiantes=150, n_pruebas=30) -> None:
        """Inicializa el generador y crea datos de ejemplo.

        Args:
            n_estudiantes (int): Cantidad de estudiantes a generar.
            n_pruebas (int): Cantidad de pruebas a generar.

        Returns:
            None
        """
        self._fake = Faker("es_CL")

        # carreras
        self.carreras = [
            Carrera("ING001", "Ingeniería en Computación", "Ingeniería", 8),
            Carrera("ING002", "Ingeniería Química", "Ingeniería", 8),
            Carrera("SAL001", "Medicina", "Salud", 10),
            Carrera("HUM010", "Pedagogía en Historia", "Humanidades", 8),
            Carrera("ING007", "Arquitectura", "Ingeniería", 10),
        ]

        # materias
        self._materias = [
            "Matemáticas I",
            "Matemáticas II",
            "Física",
            "Base de Datos II",
            "Taller de comunicaciones",
            "Ingeniería y Sociedad",
            "Proyecto I",
            "Electivo II",
        ]

        self.estudiantes = []
        self.pruebas = []
        self.calificaciones = []

        self._genera_estudiantes(n_estudiantes)
        self._genera_pruebas(n_pruebas)
        self._genera_calificaciones(n_estudiantes * 2)

    def _genera_estudiantes(self, n_estudiantes: int) -> None:
        """Genera y agrega múltiples estudiantes de una sola vez.

        Args:
            n_estudiantes (int): Cantidad de estudiantes a generar (>= 0).

        Returns:
            None
        """
        for _ in range(n_estudiantes):
            self.estudiantes.append(
                Estudiante(
                    id=len(self.estudiantes) + 1,
                    nombre=self._fake.first_name(),
                    apellido=self._fake.last_name(),
                    email=self._fake.email(),
                    fecha_ingreso=self._fake.date_between("-3y", "-1y"),
                    fecha_nacimiento=self._fake.date_between("-25y", "-18y"),
                    semestre_actual=randint(1, 8),
                    carrera=choice(self.carreras),
                )
            )

    def _genera_pruebas(self, n_pruebas: int) -> None:
        """Genera y agrega múltiples pruebas de una sola vez.

        Args:
            n_pruebas (int): Cantidad de pruebas a generar (>= 0).

        Returns:
            None
        """
        for _ in range(n_pruebas):
            _id = len(self.pruebas) + 1
            self.pruebas.append(
                Prueba(
                    id=_id,
                    nombre=f"Prueba {_id}",
                    fecha=self._fake.date_between("-1y", "today"),
                    materia=choice(self._materias),
                    puntaje_maximo=randint(50, 100),
                    calificaciones=[],
                )
            )

    def _genera_calificaciones(self, n_calificaciones: int) -> None:
        """Genera y agrega múltiples calificaciones de una sola vez.

        Args:
            n_calificaciones (int): Cantidad de calificaciones a generar (>= 0).

        Returns:
            None
        """
        for _ in range(n_calificaciones):
            self.calificaciones.append(
                Calificacion(
                    estudiante=choice(self.estudiantes),
                    prueba=choice(self.pruebas),
                    puntaje=randint(40, 100),
                    fecha_calificacion=self._fake.date_time_between("-1y", "now"),
                )
            )


class AnalizadorRendimiento:
    """Analiza el rendimiento académico de estudiantes y materias.

    Esta clase proporciona métodos para generar rankings de estudiantes,
    analizar el rendimiento por materia y obtener estadísticas académicas
    a partir de los datos generados por GeneradorDatos.

    Attributes:
        datos (GeneradorDatos): Instancia del generador que contiene los datos
            de estudiantes, pruebas y calificaciones a analizar.
    """

    def __init__(self, datos: GeneradorDatos) -> None:
        """Inicializa el analizador con los datos a procesar.

        Args:
            datos (GeneradorDatos): Instancia del generador que contiene
                estudiantes, pruebas y calificaciones para analizar.

        Returns:
            None
        """
        self.datos = datos

    def ranking_estudiantes(self, n: int = 10) -> list[tuple[Estudiante, float]]:
        """Genera un ranking de los mejores estudiantes según su promedio.

        Args:
            n (int): Cantidad de estudiantes a incluir en el ranking.

        Returns:
            list[tuple[Estudiante, float]]: Lista de tuplas con estudiante y su promedio.
        """
        pass

    def analizar_materias(self) -> list[dict[str, float]]:
        """Analiza el rendimiento de los estudiantes por materia.

        Returns:
            list[dict[str, float]]: Diccionario con el promedio de notas por materia.
        """
        pass

from lib.utils import AnalizadorRendimiento, GeneradorDatos


def main():
    datos = GeneradorDatos()
    analizador = AnalizadorRendimiento(datos=datos)

    print(analizador.ranking_estudiantes())
    print(analizador.analizar_materias())


if __name__ == "__main__":
    main()

import math

# Que es un 'dict'?
# Un 'dict' es un tipo de variable en python, la cual agrupa mas variables.
# Su uso es simple:
diccionario = {"nombre": "John Doe"}
# Como puedes observar, los diccionarios se componen de un nombre y un valor asignado.
# El valor puede ser de cualquier tipo y se asigna asi:
# Podemos leer los diccionarios con el comando .get
print(diccionario.get("nombre"))
# Tambien puedes accederlo como una lista
print(diccionario["nombre"])


def calculadora_media_onda(vef_1: int, vef_2: int, resistencia: int) -> dict:
    """
    :rtype: dict
    :param vef_1: Voltaje Eficaz del transformador
    :param vef_2: Voltaje Eficaz transformado
    :param resistencia: Resistencia del circuito.
    :return: Calculos de la fuente de alimentacion.
    """
    v_max_1 = vef_1 * math.sqrt(2)
    v_max_2 = vef_2 * math.sqrt(2)

    v_med_diode = v_max_2 / math.pi

    intensity_diode = v_med_diode / resistencia

    return {
        'voltaje maximo 1': v_max_1,
        'voltaje maximo 2': v_max_2,
        'voltaje medio diodo': v_med_diode,
        'intensidad diodo': intensity_diode
    }


def calculo_onda_completa(vef_1: int, vef_2: int, resistencia: int) -> dict:
    """
    :rtype dict
    :param vef_1: Voltaje Eficaz del transformador
    :param vef_2: Voltaje Eficaz transformado
    :param resistencia: Resistencia del circuito.
    :return: Calculos de la fuente de alimentacion.
    """
    v_max_1 = vef_1 * math.sqrt(2)
    v_max_2 = vef_2 * math.sqrt(2)

    v_med_diode = (2 * v_max_2) / math.pi

    intensity_mid = v_med_diode / resistencia

    return {
        'voltaje maximo 1': v_max_1,
        'voltaje maximo 2': v_max_2,
        'voltaje medio diodo': v_med_diode,
        'intensidad diodo': intensity_mid  # why no work
    }


def main():
    print("Calculadora media onda: ")
    resultados_media_onda: dict = calculadora_media_onda(220, 12, 1000)
    print(f"Voltaje Maximo 1: {resultados_media_onda['voltaje maximo 1']} Voltios")
    print(f"Voltaje Maximo 2: {resultados_media_onda['voltaje maximo 2']} Voltios")
    print(f"Voltaje Medio del Diodo: {resultados_media_onda['voltaje medio diodo']} Voltios")
    print(f"Intensidad del Diodo: {resultados_media_onda['intensidad diodo']} Amperios")
    print("---------------------------------------------------------------------------")
    print("Calculadora onda completa: ")
    resultados_onda_completa: dict = calculo_onda_completa(220, 24, 1000)
    print(f"Voltaje Maximo 1: {resultados_media_onda['voltaje maximo 1']} Voltios")
    print(f"Voltaje Maximo 2: {resultados_media_onda['voltaje maximo 2']} Voltios")
    print(f"Voltaje Medio del Diodo: {resultados_media_onda['voltaje medio diodo']} Voltios")
    print(f"Intensidad del Diodo: {resultados_media_onda['intensidad diodo']} Amperios")


if __name__ == "__main__":
    main()

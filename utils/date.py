def get_plant_month(month, tempo_de_frutificacao):
    positions = 11
    result = month - tempo_de_frutificacao

    if result < 0:
        while result < 0:
            result += positions + 1

        return result

    return result


def convert_float_to_hour(hours_float: float):
    hours = int(hours_float)
    minutes = int((hours_float - hours) * 60)

    return f"{hours}h {minutes:02d}min"

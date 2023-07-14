def getPlantMonth(month, tempo_de_frutificacao):
    positions = 11
    result = month - tempo_de_frutificacao

    if result < 0:
        while result < 0:
            result += positions + 1

        return result

    return result

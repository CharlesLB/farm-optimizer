def getPlantMonth(month, tempo_de_frutificação):
    positions = 11
    result = month - tempo_de_frutificação

    while result < 0:
        result += positions

    return result + 1

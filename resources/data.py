import json
import sys
from lib.plant import Plant
from lib.animal import Animal

arguments = sys.argv


def is_json_file(file):
    return file.endswith(".json")


if arguments.__len__() == 1:
    print("No input file provided")
    print("Usage: python -u index.py <input_file>")
    exit()

if not is_json_file(arguments[1]):
    print("Input file must be a json file")
    exit()

input_file = arguments[1]

with open(input_file, "r") as file:
    json_data = json.load(file)

plants_array = json_data["plants"]
plants = []

for plant in plants_array:
    new_plant = Plant(
        plant["nome"],
        plant["producao_da_casa"],
        plant["valor"],
        plant["estacao_da_colheita"],
        plant["tempo_de_frutificacao"],
        plant["tempo_de_colheita"],
        plant["tempo_de_plantio"],
        plant["tempo_de_venda"],
        plant["custo_de_muda"],
        plant["producao_por_muda"],
        plant["remessa"],
        plant["max"],
    )
    plants.append(new_plant)

animals_array = json_data["animals"]
animals = []

for animal in animals_array:
    new_animal = Animal(
        animal["nome"],
        animal["producao_da_casa"],
        animal["valor"],
        animal["tempo_de_cuidado"],
        animal["custo_por_animal"],
        animal["tempo_de_venda"],
        animal["tempo_de_producao"],
        animal["remessa"],
        animal["numero_de_femeas"],
        animal["numero_de_machos"],
    )
    animals.append(new_animal)

print("Data loaded successfully")

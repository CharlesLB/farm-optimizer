# python -u ./scripts/create_json_file.py

import json
import sys
from pathlib import Path

parent_directory = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_directory)
from resources.plants._all import plants
from resources.animals._all import animals

plants_array = []

for plant in plants:
    new_plant = {
        "nome": plant.nome,
        "producao_da_casa": plant.producao_da_casa,
        "valor": plant.valor,
        "estacao_da_colheita": plant.estacao_da_colheita,
        "tempo_de_frutificacao": plant.tempo_de_frutificacao,
        "tempo_de_colheita": plant.tempo_de_colheita,
        "tempo_de_plantio": plant.tempo_de_plantio,
        "tempo_de_venda": plant.tempo_de_venda,
        "custo_de_muda": plant.custo_de_muda,
        "producao_por_muda": plant.producao_por_muda,
        "remessa": plant.remessa,
        "max": plant.max,
    }
    plants_array.append(new_plant)

    # nome,
    #     producao_da_casa: float,
    #     valor: float,
    #     tempo_de_cuidado: float,
    #     custo_por_animal: float,
    #     tempo_de_venda: float,
    #     tempo_de_producao: float,
    #     remessa: float,
    #     numero_de_femeas: int,
    #     numero_de_machos: int,

animals_array = []

for animal in animals:
    new_animal = {
        "nome": animal.nome,
        "producao_da_casa": animal.producao_da_casa,
        "valor": animal.valor,
        "tempo_de_cuidado": animal.tempo_de_cuidado,
        "custo_por_animal": animal.custo_por_animal,
        "tempo_de_venda": animal.tempo_de_venda,
        "tempo_de_producao": animal.tempo_de_producao,
        "remessa": animal.remessa,
        "numero_de_femeas": animal.numero_de_femeas,
        "numero_de_machos": animal.numero_de_machos,
    }
    animals_array.append(new_animal)

data = {"plants": plants_array, "animals": animals_array}

json_data = json.dumps(data, indent=4)

with open("./input.json", "w") as file:
    file.write(json_data)

print("JSON file created successfully.")

import json

def update_json():
    lachesis_data = [
        "Lachesis = Sun/Vulcan -0 45' S d",
        "Lachesis = Vulkanus/Daedalus -0 45' S",
        "Lachesis = Part of Fortune/Zeus -0 45' A",
        "Lachesis = Pallas/Vesta -0 45' S",
        "Lachesis = Apollon/Hebe -0 44' S",
        "Lachesis = Atlantis/Bienor -0 44' S d",
        "Lachesis = Asbolus/Hekate -0 43' S",
        "Lachesis = Sedna/Sisyphus -0 43' S",
        "Lachesis = Venus/Pholus -0 43' A",
        "Lachesis = Priapus/Apollo -0 41' S",
        "Lachesis = Black Moon/Apollo -0 41' S d",
        "Lachesis = Venus/Kronos -0 41' A d",
        "Lachesis = Psyche/Vesta -0 40' S",
        "Lachesis = Apollon/Nemesis -0 39' S",
        "Lachesis = Ascendant/Isis -0 39' A d",
        "Lachesis = Descendant/Isis -0 39' A",
        "Lachesis = Sisyphus/Siwa -0 39' S",
        "Lachesis = Astraea/Pholus -0 39' S d",
        "Lachesis = Ceres/Persephone -0 38' S d",
        "Lachesis = Ceres/Minerva -0 38' S d",
        "Lachesis = Daedalus/Hopi -0 38' S d",
        "Lachesis = Venus/Neptune -0 38' A",
        "Lachesis = Eris/Orpheus -0 38' S",
        "Lachesis = Hephaistos/Pandora -0 37' S",
        "Lachesis = Admetos/Pelion -0 37' S",
        "Lachesis = Eris/Nostalgia -0 37' S d",
        "Lachesis = Kronos/Astraea -0 37' S",
        "Lachesis = Apollo/Tantalus -0 36' A",
        "Lachesis = Ophelia/Persephone -0 36' S d",
        "Lachesis = Minerva/Ophelia -0 36' S d",
        "Lachesis = Chariklo/Circe -0 35' S",
        "Lachesis = Hidalgo/Toro -0 35' A",
        "Lachesis = Saturn/Bienor -0 35' S",
        "Lachesis = Ascendant/Sedna -0 35' A",
        "Lachesis = Descendant/Sedna -0 35' A d"
    ]

    with open('/home/ubuntu/astrology_data.json', 'r') as f:
        data = json.load(f)

    data['lachesis_midpoints'] = lachesis_data

    with open('/home/ubuntu/astrology_data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update_json()

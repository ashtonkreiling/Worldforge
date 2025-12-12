import random


CULTURAL_QUESTIONS = [
    "What is a major holiday the people celebrate, and what event does it commemorate?",  # 11 (index 0)
    "What moral value does the community consider most important?",  # 12 (index 1)
    "What natural feature (river, tree, mountain, star, etc.) holds symbolic meaning for the people?",  # 13 (index 2)
    "What form of art or storytelling is most cherished by the community?",  # 14 (index 3)
    "What creature, real or mythical, plays an important role in local folklore?",  # 15 (index 4)
    "What childhood rite marks the transition into adulthood?",  # 16 (index 5)
    "What reputation does the settlement have among outsiders?",  # 21 (index 6)
    "What food or drink is considered a local specialty?",  # 22 (index 7)
    "What taboo action is strongly condemned by local custom?",  # 23 (index 8)
    "What seasonal event affects the people's lifestyle the most?",  # 24 (index 9)
    "What gesture, greeting, or social ritual is unique to the culture?",  # 25 (index 10)
    "What traditional craft or trade are the people widely known for?",  # 26 (index 11)
    "What historical tragedy or hardship shaped the identity of the community?",  # 31 (index 12)
    "What legendary hero, ancestor, or founder do the people remember?",  # 32 (index 13)
    "What form of humor or comedic tradition is especially popular among the people?",  # 33 (index 14)
    "What type of conflict most commonly arises within the settlement?",  # 34 (index 15)
    "What shared fear or superstition influences daily behavior?",  # 35 (index 16)
    "What architectural style or building material defines the settlement's appearance?",  # 36 (index 17)
    "What resource is considered the lifeblood of the settlement?",  # 41 (index 18)
    "What neighboring culture has the strongest influence on local customs?",  # 42 (index 19)
    "What sport, contest, or competitive tradition is most popular?",  # 43 (index 20)
    "What symbol, sigil, or emblem represents the community?",  # 44 (index 21)
    "What major law or rule is most strongly enforced?",  # 45 (index 22)
    "What tradition governs how leaders are chosen, honored, or replaced?",  # 46 (index 23)
    "What role do elders or respected figures play in community decisions?",  # 51 (index 24)
    "What public space (market, shrine, amphitheater, etc.) is the settlement's social heart?",  # 52 (index 25)
    "What sort of education or informal training do young people receive?",  # 53 (index 26)
    "What aspect of hospitality or guest-right is considered very important?",  # 54 (index 27)
    "What invention, tool, or innovation originated in the community?",  # 55 (index 28)
    "What type of music or rhythmic expression is most important to the community's identity?",  # 56 (index 29)
    "What annual challenge or pilgrimage do some members undertake?",  # 61 (index 30)
    "What festival or ceremony brings the entire community together?",  # 62 (index 31)
    "What oath, motto, or shared saying reflects the culture's identity?",  # 63 (index 32)
    "What fashion, ornament, or cosmetic practice is distinctive?",  # 64 (index 33)
    "What environmental threat (storms, predators, magic, etc.) shapes local life?",  # 65 (index 34)
    "What secret tradition or hidden practice is known only to long-term residents?",  # 66 (index 35)
]


def ask_cultural_question():
    roll = random.randint(0, 35)
    return determine_question(roll)


def determine_question(roll):
    if 0 <= roll <= 35:
        return CULTURAL_QUESTIONS[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 35, got {roll}")


import random


CULTURAL_QUESTIONS = [
    "What is a major holiday the people celebrate, and what event does it commemorate?",
    "What moral value does the community consider most important?",
    "What natural feature (river, tree, mountain, star, etc.) holds symbolic meaning for the people?",
    "What form of art or storytelling is most cherished by the community?",
    "What creature, real or mythical, plays an important role in local folklore?",
    "What childhood rite marks the transition into adulthood?",
    "What reputation does the settlement have among outsiders?",
    "What food or drink is considered a local specialty?",
    "What taboo action is strongly condemned by local custom?",
    "What seasonal event affects the people's lifestyle the most?",
    "What gesture, greeting, or social ritual is unique to the culture?",
    "What traditional craft or trade are the people widely known for?",
    "What historical tragedy or hardship shaped the identity of the community?",
    "What legendary hero, ancestor, or founder do the people remember?",
    "What form of humor or comedic tradition is especially popular among the people?",
    "What type of conflict most commonly arises within the settlement?",
    "What shared fear or superstition influences daily behavior?",
    "What architectural style or building material defines the settlement's appearance?",
    "What resource is considered the lifeblood of the settlement?",
    "What neighboring culture has the strongest influence on local customs?",
    "What sport, contest, or competitive tradition is most popular?",
    "What symbol, sigil, or emblem represents the community?",
    "What major law or rule is most strongly enforced?",
    "What tradition governs how leaders are chosen, honored, or replaced?",
    "What role do elders or respected figures play in community decisions?",
    "What public space (market, shrine, amphitheater, etc.) is the settlement's social heart?",
    "What sort of education or informal training do young people receive?",
    "What aspect of hospitality or guest-right is considered very important?",
    "What invention, tool, or innovation originated in the community?",
    "What type of music or rhythmic expression is most important to the community's identity?",
    "What annual challenge or pilgrimage do some members undertake?",
    "What festival or ceremony brings the entire community together?",
    "What oath, motto, or shared saying reflects the culture's identity?",
    "What fashion, ornament, or cosmetic practice is distinctive?",
    "What environmental threat (storms, predators, magic, etc.) shapes local life?",
    "What secret tradition or hidden practice is known only to long-term residents?",
]


def ask_cultural_question():
    roll = random.randint(0, 35)
    return determine_question(roll)


def determine_question(roll):
    if 0 <= roll <= 35:
        return CULTURAL_QUESTIONS[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 35, got {roll}")


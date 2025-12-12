import random

RANDOM_EVENTS = [
    "A traveling merchant caravan arrives with rare goods and unusual news.",
    "An outbreak of sickness spreads through the settlement.",
    "A skilled craftworker or family of artisans moves into the settlement.",
    "A sudden drought affects wells, streams, or farmland.",
    "A local youth performs a feat that brings pride to the community.",
    "A mysterious fire damages a key structure or field. No culprit is found.",
    "A minor faction—bandits, raiders, or troublemakers—targets travelers near the settlement.",
    "A bumper harvest occurs, filling granaries beyond expectation.",
    "A charismatic performer, mystic, or storyteller visits, captivating the community.",
    "A beloved elder or leader passes away, leaving a difficult vacancy.",
    "A long-lost traveler or relative unexpectedly returns home.",
    "Tools, livestock, or supplies begin quietly disappearing. A thief is at work.",
    "A strange weather pattern persists—fog, heat, cold—causing confusion and hardship.",
    "A generous benefactor donates land, materials, or wealth to the community.",
    "A sudden influx of settlers or refugees expands the population.",
    "An infestation of pests or blight threatens crops or stored food.",
    "A child or animal is born with unusual markings believed to be an omen.",
    "A dangerous animal or monster begins stalking the outskirts.",
    "A traveling scholar or sage shares knowledge that improves local practices.",
    "A flood or landslide reshapes part of the settlement or surrounding land.",
    "A local invention or breakthrough increases productivity or safety.",
    "An unexpected tax collector, official, or noble imposes new burdens.",
    "A hidden resource—clay, timber, herbs, ore—comes to light nearby.",
    "A rash of mischief, illusion, or prank-like hauntings disturbs residents.",
    "A wandering healer cures several lingering ailments.",
    "A destructive storm tears roofs, fences, and fields apart.",
    "A festival or celebration becomes the most joyful in recent memory.",
    "A trusted figure is caught in a scandal, fraud, or betrayal.",
    "A natural landmark—spring, grove, cavern—gains sudden importance or beauty.",
    "A strange celestial event (comet, eclipse, lights) causes awe and worry.",
    "A prosperous trade route opens temporarily, bringing wealth and contact.",
    "A building collapse, mine cave-in, or construction failure injures workers.",
    "A series of helpful coincidences or uncanny luck blesses the community.",
    "A cursed item, unsettling relic, or magical contamination is discovered.",
    "A traveling judge, inspector, or mediator resolves ongoing disputes.",
    "A local legend awakens—spirit, creature, or mythic threat—causing fear and unrest.",
]


def roll_random_event():
    roll = random.randint(0, 35)
    return determine_event(roll)


def determine_event(roll):
    if 0 <= roll <= 35:
        return RANDOM_EVENTS[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 35, got {roll}")


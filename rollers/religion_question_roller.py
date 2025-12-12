import random

RELIGION_QUESTIONS = [
    "What is the dominant belief system followed by the people?",
    "What is the origin story of the world according to local faith?",
    "What sacred sound, word, or call is believed to hold spiritual power?",
    "What sacred text, tradition, or collection of stories guides religious practice?",
    "What miracle or supernatural event is said to have occurred near the settlement?",
    "What taboo action is considered a spiritual offense rather than a legal one?",
    "What holy site, shrine, or natural landmark is considered sacred?",
    "What ritual must people perform at birth or adoption?",
    "What offering, sacrifice, or symbolic gift is commonly presented in worship?",
    "What daily practice (prayer, meditation, cleansing, etc.) is widely observed?",
    "What omen or signs do people look for when making major decisions?",
    "What religious attire, markings, or adornments are worn during ceremonies?",
    "What festival or holy day is the most important in the religious calendar?",
    "What is the traditional method of disposing of the dead?",
    "What afterlife or reincarnation belief shapes people's worldview?",
    "What divine law or spiritual rule influences everyday behavior?",
    "What class of priests, shamans, monks, or mystics serves the community?",
    "What sacred object, artifact, or relic is deeply revered?",
    "What moral or spiritual virtue do the people view as the highest good?",
    "What everyday object or tool is used symbolically in local rituals?",
    "What pilgrimage or spiritual journey do followers undertake?",
    "What vision, prophecy, or revelation is central to local belief?",
    "What religious conflict or schism divided followers in the past?",
    "What practice marks the transition from childhood to spiritual adulthood?",
    "What natural phenomenon (eclipse, comet, aurora, earthquake, etc.) carries special religious meaning?",
    "What prayer, mantra, or chant is most often repeated?",
    "What sacred symbol or sigil represents the faith?",
    "What role does music, drumming, or chanting play in ceremony?",
    "What place of worship is the center of religious activity?",
    "What healing, blessing, or divination practice is commonly used?",
    "What prohibition or dietary rule is rooted in spiritual tradition?",
    "What ritual is performed before major journeys, hunts, or battles?",
    "What myth explains why suffering or misfortune exists?",
    "What sect, cult, or minor belief group exists alongside the main faith?",
    "What supernatural threat (demon, curse, ill spirit) do the people fear?",
    "What mystery, sacred secret, or esoteric teaching is known only to the faithful?",
]


def ask_religion_question():
    roll = random.randint(0, 35)
    return determine_question(roll)


def determine_question(roll):
    if 0 <= roll <= 35:
        return RELIGION_QUESTIONS[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 35, got {roll}")


import random


RELIGION_QUESTIONS = [
    "What is the dominant belief system followed by the people?",  # 11 (index 0)
    "What is the origin story of the world according to local faith?",  # 12 (index 1)
    "What sacred sound, word, or call is believed to hold spiritual power?",  # 13 (index 2)
    "What sacred text, tradition, or collection of stories guides religious practice?",  # 14 (index 3)
    "What miracle or supernatural event is said to have occurred near the settlement?",  # 15 (index 4)
    "What taboo action is considered a spiritual offense rather than a legal one?",  # 16 (index 5)
    "What holy site, shrine, or natural landmark is considered sacred?",  # 21 (index 6)
    "What ritual must people perform at birth or adoption?",  # 22 (index 7)
    "What offering, sacrifice, or symbolic gift is commonly presented in worship?",  # 23 (index 8)
    "What daily practice (prayer, meditation, cleansing, etc.) is widely observed?",  # 24 (index 9)
    "What omen or signs do people look for when making major decisions?",  # 25 (index 10)
    "What religious attire, markings, or adornments are worn during ceremonies?",  # 26 (index 11)
    "What festival or holy day is the most important in the religious calendar?",  # 31 (index 12)
    "What is the traditional method of disposing of the dead?",  # 32 (index 13)
    "What afterlife or reincarnation belief shapes people's worldview?",  # 33 (index 14)
    "What divine law or spiritual rule influences everyday behavior?",  # 34 (index 15)
    "What class of priests, shamans, monks, or mystics serves the community?",  # 35 (index 16)
    "What sacred object, artifact, or relic is deeply revered?",  # 36 (index 17)
    "What moral or spiritual virtue do the people view as the highest good?",  # 41 (index 18)
    "What everyday object or tool is used symbolically in local rituals?",  # 42 (index 19)
    "What pilgrimage or spiritual journey do followers undertake?",  # 43 (index 20)
    "What vision, prophecy, or revelation is central to local belief?",  # 44 (index 21)
    "What religious conflict or schism divided followers in the past?",  # 45 (index 22)
    "What practice marks the transition from childhood to spiritual adulthood?",  # 46 (index 23)
    "What natural phenomenon (eclipse, comet, aurora, earthquake, etc.) carries special religious meaning?",  # 51 (index 24)
    "What prayer, mantra, or chant is most often repeated?",  # 52 (index 25)
    "What sacred symbol or sigil represents the faith?",  # 53 (index 26)
    "What role does music, drumming, or chanting play in ceremony?",  # 54 (index 27)
    "What place of worship is the center of religious activity?",  # 55 (index 28)
    "What healing, blessing, or divination practice is commonly used?",  # 56 (index 29)
    "What prohibition or dietary rule is rooted in spiritual tradition?",  # 61 (index 30)
    "What ritual is performed before major journeys, hunts, or battles?",  # 62 (index 31)
    "What myth explains why suffering or misfortune exists?",  # 63 (index 32)
    "What sect, cult, or minor belief group exists alongside the main faith?",  # 64 (index 33)
    "What supernatural threat (demon, curse, ill spirit) do the people fear?",  # 65 (index 34)
    "What mystery, sacred secret, or esoteric teaching is known only to the faithful?",  # 66 (index 35)
]


def ask_religion_question():
    roll = random.randint(0, 35)
    return determine_question(roll)


def determine_question(roll):
    if 0 <= roll <= 35:
        return RELIGION_QUESTIONS[roll]
    else:
        raise ValueError(f"Roll must be between 0 and 35, got {roll}")


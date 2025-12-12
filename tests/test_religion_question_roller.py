import unittest
import sys
import os

# Add parent directory to path to import religion_question_roller
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rollers.religion_question_roller import determine_question, RELIGION_QUESTIONS


class TestDetermineQuestion(unittest.TestCase):
    
    def test_roll_0_returns_correct_question(self):
        """Test that rolling 0 returns the first question (11)"""
        self.assertEqual(determine_question(0), RELIGION_QUESTIONS[0])
        self.assertEqual(determine_question(0), "What is the dominant belief system followed by the people?")
    
    def test_roll_1_returns_correct_question(self):
        """Test that rolling 1 returns the second question (12)"""
        self.assertEqual(determine_question(1), RELIGION_QUESTIONS[1])
        self.assertEqual(determine_question(1), "What is the origin story of the world according to local faith?")
    
    def test_roll_2_returns_correct_question(self):
        """Test that rolling 2 returns the third question (13)"""
        self.assertEqual(determine_question(2), RELIGION_QUESTIONS[2])
        self.assertEqual(determine_question(2), "What sacred sound, word, or call is believed to hold spiritual power?")
    
    def test_roll_3_returns_correct_question(self):
        """Test that rolling 3 returns the fourth question (14)"""
        self.assertEqual(determine_question(3), RELIGION_QUESTIONS[3])
        self.assertEqual(determine_question(3), "What sacred text, tradition, or collection of stories guides religious practice?")
    
    def test_roll_4_returns_correct_question(self):
        """Test that rolling 4 returns the fifth question (15)"""
        self.assertEqual(determine_question(4), RELIGION_QUESTIONS[4])
        self.assertEqual(determine_question(4), "What miracle or supernatural event is said to have occurred near the settlement?")
    
    def test_roll_5_returns_correct_question(self):
        """Test that rolling 5 returns the sixth question (16)"""
        self.assertEqual(determine_question(5), RELIGION_QUESTIONS[5])
        self.assertEqual(determine_question(5), "What taboo action is considered a spiritual offense rather than a legal one?")
    
    def test_roll_6_returns_correct_question(self):
        """Test that rolling 6 returns the seventh question (21)"""
        self.assertEqual(determine_question(6), RELIGION_QUESTIONS[6])
        self.assertEqual(determine_question(6), "What holy site, shrine, or natural landmark is considered sacred?")
    
    def test_roll_7_returns_correct_question(self):
        """Test that rolling 7 returns the eighth question (22)"""
        self.assertEqual(determine_question(7), RELIGION_QUESTIONS[7])
        self.assertEqual(determine_question(7), "What ritual must people perform at birth or adoption?")
    
    def test_roll_8_returns_correct_question(self):
        """Test that rolling 8 returns the ninth question (23)"""
        self.assertEqual(determine_question(8), RELIGION_QUESTIONS[8])
        self.assertEqual(determine_question(8), "What offering, sacrifice, or symbolic gift is commonly presented in worship?")
    
    def test_roll_9_returns_correct_question(self):
        """Test that rolling 9 returns the tenth question (24)"""
        self.assertEqual(determine_question(9), RELIGION_QUESTIONS[9])
        self.assertEqual(determine_question(9), "What daily practice (prayer, meditation, cleansing, etc.) is widely observed?")
    
    def test_roll_10_returns_correct_question(self):
        """Test that rolling 10 returns the eleventh question (25)"""
        self.assertEqual(determine_question(10), RELIGION_QUESTIONS[10])
        self.assertEqual(determine_question(10), "What omen or signs do people look for when making major decisions?")
    
    def test_roll_11_returns_correct_question(self):
        """Test that rolling 11 returns the twelfth question (26)"""
        self.assertEqual(determine_question(11), RELIGION_QUESTIONS[11])
        self.assertEqual(determine_question(11), "What religious attire, markings, or adornments are worn during ceremonies?")
    
    def test_roll_12_returns_correct_question(self):
        """Test that rolling 12 returns the thirteenth question (31)"""
        self.assertEqual(determine_question(12), RELIGION_QUESTIONS[12])
        self.assertEqual(determine_question(12), "What festival or holy day is the most important in the religious calendar?")
    
    def test_roll_13_returns_correct_question(self):
        """Test that rolling 13 returns the fourteenth question (32)"""
        self.assertEqual(determine_question(13), RELIGION_QUESTIONS[13])
        self.assertEqual(determine_question(13), "What is the traditional method of disposing of the dead?")
    
    def test_roll_14_returns_correct_question(self):
        """Test that rolling 14 returns the fifteenth question (33)"""
        self.assertEqual(determine_question(14), RELIGION_QUESTIONS[14])
        self.assertEqual(determine_question(14), "What afterlife or reincarnation belief shapes people's worldview?")
    
    def test_roll_15_returns_correct_question(self):
        """Test that rolling 15 returns the sixteenth question (34)"""
        self.assertEqual(determine_question(15), RELIGION_QUESTIONS[15])
        self.assertEqual(determine_question(15), "What divine law or spiritual rule influences everyday behavior?")
    
    def test_roll_16_returns_correct_question(self):
        """Test that rolling 16 returns the seventeenth question (35)"""
        self.assertEqual(determine_question(16), RELIGION_QUESTIONS[16])
        self.assertEqual(determine_question(16), "What class of priests, shamans, monks, or mystics serves the community?")
    
    def test_roll_17_returns_correct_question(self):
        """Test that rolling 17 returns the eighteenth question (36)"""
        self.assertEqual(determine_question(17), RELIGION_QUESTIONS[17])
        self.assertEqual(determine_question(17), "What sacred object, artifact, or relic is deeply revered?")
    
    def test_roll_18_returns_correct_question(self):
        """Test that rolling 18 returns the nineteenth question (41)"""
        self.assertEqual(determine_question(18), RELIGION_QUESTIONS[18])
        self.assertEqual(determine_question(18), "What moral or spiritual virtue do the people view as the highest good?")
    
    def test_roll_19_returns_correct_question(self):
        """Test that rolling 19 returns the twentieth question (42)"""
        self.assertEqual(determine_question(19), RELIGION_QUESTIONS[19])
        self.assertEqual(determine_question(19), "What everyday object or tool is used symbolically in local rituals?")
    
    def test_roll_20_returns_correct_question(self):
        """Test that rolling 20 returns the twenty-first question (43)"""
        self.assertEqual(determine_question(20), RELIGION_QUESTIONS[20])
        self.assertEqual(determine_question(20), "What pilgrimage or spiritual journey do followers undertake?")
    
    def test_roll_21_returns_correct_question(self):
        """Test that rolling 21 returns the twenty-second question (44)"""
        self.assertEqual(determine_question(21), RELIGION_QUESTIONS[21])
        self.assertEqual(determine_question(21), "What vision, prophecy, or revelation is central to local belief?")
    
    def test_roll_22_returns_correct_question(self):
        """Test that rolling 22 returns the twenty-third question (45)"""
        self.assertEqual(determine_question(22), RELIGION_QUESTIONS[22])
        self.assertEqual(determine_question(22), "What religious conflict or schism divided followers in the past?")
    
    def test_roll_23_returns_correct_question(self):
        """Test that rolling 23 returns the twenty-fourth question (46)"""
        self.assertEqual(determine_question(23), RELIGION_QUESTIONS[23])
        self.assertEqual(determine_question(23), "What practice marks the transition from childhood to spiritual adulthood?")
    
    def test_roll_24_returns_correct_question(self):
        """Test that rolling 24 returns the twenty-fifth question (51)"""
        self.assertEqual(determine_question(24), RELIGION_QUESTIONS[24])
        self.assertEqual(determine_question(24), "What natural phenomenon (eclipse, comet, aurora, earthquake, etc.) carries special religious meaning?")
    
    def test_roll_25_returns_correct_question(self):
        """Test that rolling 25 returns the twenty-sixth question (52)"""
        self.assertEqual(determine_question(25), RELIGION_QUESTIONS[25])
        self.assertEqual(determine_question(25), "What prayer, mantra, or chant is most often repeated?")
    
    def test_roll_26_returns_correct_question(self):
        """Test that rolling 26 returns the twenty-seventh question (53)"""
        self.assertEqual(determine_question(26), RELIGION_QUESTIONS[26])
        self.assertEqual(determine_question(26), "What sacred symbol or sigil represents the faith?")
    
    def test_roll_27_returns_correct_question(self):
        """Test that rolling 27 returns the twenty-eighth question (54)"""
        self.assertEqual(determine_question(27), RELIGION_QUESTIONS[27])
        self.assertEqual(determine_question(27), "What role does music, drumming, or chanting play in ceremony?")
    
    def test_roll_28_returns_correct_question(self):
        """Test that rolling 28 returns the twenty-ninth question (55)"""
        self.assertEqual(determine_question(28), RELIGION_QUESTIONS[28])
        self.assertEqual(determine_question(28), "What place of worship is the center of religious activity?")
    
    def test_roll_29_returns_correct_question(self):
        """Test that rolling 29 returns the thirtieth question (56)"""
        self.assertEqual(determine_question(29), RELIGION_QUESTIONS[29])
        self.assertEqual(determine_question(29), "What healing, blessing, or divination practice is commonly used?")
    
    def test_roll_30_returns_correct_question(self):
        """Test that rolling 30 returns the thirty-first question (61)"""
        self.assertEqual(determine_question(30), RELIGION_QUESTIONS[30])
        self.assertEqual(determine_question(30), "What prohibition or dietary rule is rooted in spiritual tradition?")
    
    def test_roll_31_returns_correct_question(self):
        """Test that rolling 31 returns the thirty-second question (62)"""
        self.assertEqual(determine_question(31), RELIGION_QUESTIONS[31])
        self.assertEqual(determine_question(31), "What ritual is performed before major journeys, hunts, or battles?")
    
    def test_roll_32_returns_correct_question(self):
        """Test that rolling 32 returns the thirty-third question (63)"""
        self.assertEqual(determine_question(32), RELIGION_QUESTIONS[32])
        self.assertEqual(determine_question(32), "What myth explains why suffering or misfortune exists?")
    
    def test_roll_33_returns_correct_question(self):
        """Test that rolling 33 returns the thirty-fourth question (64)"""
        self.assertEqual(determine_question(33), RELIGION_QUESTIONS[33])
        self.assertEqual(determine_question(33), "What sect, cult, or minor belief group exists alongside the main faith?")
    
    def test_roll_34_returns_correct_question(self):
        """Test that rolling 34 returns the thirty-fifth question (65)"""
        self.assertEqual(determine_question(34), RELIGION_QUESTIONS[34])
        self.assertEqual(determine_question(34), "What supernatural threat (demon, curse, ill spirit) do the people fear?")
    
    def test_roll_35_returns_correct_question(self):
        """Test that rolling 35 returns the thirty-sixth question (66)"""
        self.assertEqual(determine_question(35), RELIGION_QUESTIONS[35])
        self.assertEqual(determine_question(35), "What mystery, sacred secret, or esoteric teaching is known only to the faithful?")


if __name__ == '__main__':
    unittest.main()


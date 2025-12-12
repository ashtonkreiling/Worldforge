import unittest
import sys
import os

# Add parent directory to path to import cultural_question_roller
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rollers.cultural_question_roller import determine_question, CULTURAL_QUESTIONS


class TestDetermineQuestion(unittest.TestCase):
    
    def test_roll_0_returns_correct_question(self):
        """Test that rolling 0 returns the first question (11)"""
        self.assertEqual(determine_question(0), CULTURAL_QUESTIONS[0])
        self.assertEqual(determine_question(0), "What is a major holiday the people celebrate, and what event does it commemorate?")
    
    def test_roll_1_returns_correct_question(self):
        """Test that rolling 1 returns the second question (12)"""
        self.assertEqual(determine_question(1), CULTURAL_QUESTIONS[1])
        self.assertEqual(determine_question(1), "What moral value does the community consider most important?")
    
    def test_roll_2_returns_correct_question(self):
        """Test that rolling 2 returns the third question (13)"""
        self.assertEqual(determine_question(2), CULTURAL_QUESTIONS[2])
        self.assertEqual(determine_question(2), "What natural feature (river, tree, mountain, star, etc.) holds symbolic meaning for the people?")
    
    def test_roll_3_returns_correct_question(self):
        """Test that rolling 3 returns the fourth question (14)"""
        self.assertEqual(determine_question(3), CULTURAL_QUESTIONS[3])
        self.assertEqual(determine_question(3), "What form of art or storytelling is most cherished by the community?")
    
    def test_roll_4_returns_correct_question(self):
        """Test that rolling 4 returns the fifth question (15)"""
        self.assertEqual(determine_question(4), CULTURAL_QUESTIONS[4])
        self.assertEqual(determine_question(4), "What creature, real or mythical, plays an important role in local folklore?")
    
    def test_roll_5_returns_correct_question(self):
        """Test that rolling 5 returns the sixth question (16)"""
        self.assertEqual(determine_question(5), CULTURAL_QUESTIONS[5])
        self.assertEqual(determine_question(5), "What childhood rite marks the transition into adulthood?")
    
    def test_roll_6_returns_correct_question(self):
        """Test that rolling 6 returns the seventh question (21)"""
        self.assertEqual(determine_question(6), CULTURAL_QUESTIONS[6])
        self.assertEqual(determine_question(6), "What reputation does the settlement have among outsiders?")
    
    def test_roll_7_returns_correct_question(self):
        """Test that rolling 7 returns the eighth question (22)"""
        self.assertEqual(determine_question(7), CULTURAL_QUESTIONS[7])
        self.assertEqual(determine_question(7), "What food or drink is considered a local specialty?")
    
    def test_roll_8_returns_correct_question(self):
        """Test that rolling 8 returns the ninth question (23)"""
        self.assertEqual(determine_question(8), CULTURAL_QUESTIONS[8])
        self.assertEqual(determine_question(8), "What taboo action is strongly condemned by local custom?")
    
    def test_roll_9_returns_correct_question(self):
        """Test that rolling 9 returns the tenth question (24)"""
        self.assertEqual(determine_question(9), CULTURAL_QUESTIONS[9])
        self.assertEqual(determine_question(9), "What seasonal event affects the people's lifestyle the most?")
    
    def test_roll_10_returns_correct_question(self):
        """Test that rolling 10 returns the eleventh question (25)"""
        self.assertEqual(determine_question(10), CULTURAL_QUESTIONS[10])
        self.assertEqual(determine_question(10), "What gesture, greeting, or social ritual is unique to the culture?")
    
    def test_roll_11_returns_correct_question(self):
        """Test that rolling 11 returns the twelfth question (26)"""
        self.assertEqual(determine_question(11), CULTURAL_QUESTIONS[11])
        self.assertEqual(determine_question(11), "What traditional craft or trade are the people widely known for?")
    
    def test_roll_12_returns_correct_question(self):
        """Test that rolling 12 returns the thirteenth question (31)"""
        self.assertEqual(determine_question(12), CULTURAL_QUESTIONS[12])
        self.assertEqual(determine_question(12), "What historical tragedy or hardship shaped the identity of the community?")
    
    def test_roll_13_returns_correct_question(self):
        """Test that rolling 13 returns the fourteenth question (32)"""
        self.assertEqual(determine_question(13), CULTURAL_QUESTIONS[13])
        self.assertEqual(determine_question(13), "What legendary hero, ancestor, or founder do the people remember?")
    
    def test_roll_14_returns_correct_question(self):
        """Test that rolling 14 returns the fifteenth question (33)"""
        self.assertEqual(determine_question(14), CULTURAL_QUESTIONS[14])
        self.assertEqual(determine_question(14), "What form of humor or comedic tradition is especially popular among the people?")
    
    def test_roll_15_returns_correct_question(self):
        """Test that rolling 15 returns the sixteenth question (34)"""
        self.assertEqual(determine_question(15), CULTURAL_QUESTIONS[15])
        self.assertEqual(determine_question(15), "What type of conflict most commonly arises within the settlement?")
    
    def test_roll_16_returns_correct_question(self):
        """Test that rolling 16 returns the seventeenth question (35)"""
        self.assertEqual(determine_question(16), CULTURAL_QUESTIONS[16])
        self.assertEqual(determine_question(16), "What shared fear or superstition influences daily behavior?")
    
    def test_roll_17_returns_correct_question(self):
        """Test that rolling 17 returns the eighteenth question (36)"""
        self.assertEqual(determine_question(17), CULTURAL_QUESTIONS[17])
        self.assertEqual(determine_question(17), "What architectural style or building material defines the settlement's appearance?")
    
    def test_roll_18_returns_correct_question(self):
        """Test that rolling 18 returns the nineteenth question (41)"""
        self.assertEqual(determine_question(18), CULTURAL_QUESTIONS[18])
        self.assertEqual(determine_question(18), "What resource is considered the lifeblood of the settlement?")
    
    def test_roll_19_returns_correct_question(self):
        """Test that rolling 19 returns the twentieth question (42)"""
        self.assertEqual(determine_question(19), CULTURAL_QUESTIONS[19])
        self.assertEqual(determine_question(19), "What neighboring culture has the strongest influence on local customs?")
    
    def test_roll_20_returns_correct_question(self):
        """Test that rolling 20 returns the twenty-first question (43)"""
        self.assertEqual(determine_question(20), CULTURAL_QUESTIONS[20])
        self.assertEqual(determine_question(20), "What sport, contest, or competitive tradition is most popular?")
    
    def test_roll_21_returns_correct_question(self):
        """Test that rolling 21 returns the twenty-second question (44)"""
        self.assertEqual(determine_question(21), CULTURAL_QUESTIONS[21])
        self.assertEqual(determine_question(21), "What symbol, sigil, or emblem represents the community?")
    
    def test_roll_22_returns_correct_question(self):
        """Test that rolling 22 returns the twenty-third question (45)"""
        self.assertEqual(determine_question(22), CULTURAL_QUESTIONS[22])
        self.assertEqual(determine_question(22), "What major law or rule is most strongly enforced?")
    
    def test_roll_23_returns_correct_question(self):
        """Test that rolling 23 returns the twenty-fourth question (46)"""
        self.assertEqual(determine_question(23), CULTURAL_QUESTIONS[23])
        self.assertEqual(determine_question(23), "What tradition governs how leaders are chosen, honored, or replaced?")
    
    def test_roll_24_returns_correct_question(self):
        """Test that rolling 24 returns the twenty-fifth question (51)"""
        self.assertEqual(determine_question(24), CULTURAL_QUESTIONS[24])
        self.assertEqual(determine_question(24), "What role do elders or respected figures play in community decisions?")
    
    def test_roll_25_returns_correct_question(self):
        """Test that rolling 25 returns the twenty-sixth question (52)"""
        self.assertEqual(determine_question(25), CULTURAL_QUESTIONS[25])
        self.assertEqual(determine_question(25), "What public space (market, shrine, amphitheater, etc.) is the settlement's social heart?")
    
    def test_roll_26_returns_correct_question(self):
        """Test that rolling 26 returns the twenty-seventh question (53)"""
        self.assertEqual(determine_question(26), CULTURAL_QUESTIONS[26])
        self.assertEqual(determine_question(26), "What sort of education or informal training do young people receive?")
    
    def test_roll_27_returns_correct_question(self):
        """Test that rolling 27 returns the twenty-eighth question (54)"""
        self.assertEqual(determine_question(27), CULTURAL_QUESTIONS[27])
        self.assertEqual(determine_question(27), "What aspect of hospitality or guest-right is considered very important?")
    
    def test_roll_28_returns_correct_question(self):
        """Test that rolling 28 returns the twenty-ninth question (55)"""
        self.assertEqual(determine_question(28), CULTURAL_QUESTIONS[28])
        self.assertEqual(determine_question(28), "What invention, tool, or innovation originated in the community?")
    
    def test_roll_29_returns_correct_question(self):
        """Test that rolling 29 returns the thirtieth question (56)"""
        self.assertEqual(determine_question(29), CULTURAL_QUESTIONS[29])
        self.assertEqual(determine_question(29), "What type of music or rhythmic expression is most important to the community's identity?")
    
    def test_roll_30_returns_correct_question(self):
        """Test that rolling 30 returns the thirty-first question (61)"""
        self.assertEqual(determine_question(30), CULTURAL_QUESTIONS[30])
        self.assertEqual(determine_question(30), "What annual challenge or pilgrimage do some members undertake?")
    
    def test_roll_31_returns_correct_question(self):
        """Test that rolling 31 returns the thirty-second question (62)"""
        self.assertEqual(determine_question(31), CULTURAL_QUESTIONS[31])
        self.assertEqual(determine_question(31), "What festival or ceremony brings the entire community together?")
    
    def test_roll_32_returns_correct_question(self):
        """Test that rolling 32 returns the thirty-third question (63)"""
        self.assertEqual(determine_question(32), CULTURAL_QUESTIONS[32])
        self.assertEqual(determine_question(32), "What oath, motto, or shared saying reflects the culture's identity?")
    
    def test_roll_33_returns_correct_question(self):
        """Test that rolling 33 returns the thirty-fourth question (64)"""
        self.assertEqual(determine_question(33), CULTURAL_QUESTIONS[33])
        self.assertEqual(determine_question(33), "What fashion, ornament, or cosmetic practice is distinctive?")
    
    def test_roll_34_returns_correct_question(self):
        """Test that rolling 34 returns the thirty-fifth question (65)"""
        self.assertEqual(determine_question(34), CULTURAL_QUESTIONS[34])
        self.assertEqual(determine_question(34), "What environmental threat (storms, predators, magic, etc.) shapes local life?")
    
    def test_roll_35_returns_correct_question(self):
        """Test that rolling 35 returns the thirty-sixth question (66)"""
        self.assertEqual(determine_question(35), CULTURAL_QUESTIONS[35])
        self.assertEqual(determine_question(35), "What secret tradition or hidden practice is known only to long-term residents?")


if __name__ == '__main__':
    unittest.main()


import unittest
import sys
import os

# Add project root to path to import rollers
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from rollers.random_events_roller import determine_event, RANDOM_EVENTS


class TestDetermineEvent(unittest.TestCase):
    
    def test_roll_0_returns_correct_event(self):
        """Test that rolling 0 returns the first event (11)"""
        self.assertEqual(determine_event(0), RANDOM_EVENTS[0])
        self.assertEqual(determine_event(0), "A traveling merchant caravan arrives with rare goods and unusual news.")
    
    def test_roll_1_returns_correct_event(self):
        """Test that rolling 1 returns the second event (12)"""
        self.assertEqual(determine_event(1), RANDOM_EVENTS[1])
        self.assertEqual(determine_event(1), "An outbreak of sickness spreads through the settlement.")
    
    def test_roll_2_returns_correct_event(self):
        """Test that rolling 2 returns the third event (13)"""
        self.assertEqual(determine_event(2), RANDOM_EVENTS[2])
        self.assertEqual(determine_event(2), "A skilled craftworker or family of artisans moves into the settlement.")
    
    def test_roll_3_returns_correct_event(self):
        """Test that rolling 3 returns the fourth event (14)"""
        self.assertEqual(determine_event(3), RANDOM_EVENTS[3])
        self.assertEqual(determine_event(3), "A sudden drought affects wells, streams, or farmland.")
    
    def test_roll_4_returns_correct_event(self):
        """Test that rolling 4 returns the fifth event (15)"""
        self.assertEqual(determine_event(4), RANDOM_EVENTS[4])
        self.assertEqual(determine_event(4), "A local youth performs a feat that brings pride to the community.")
    
    def test_roll_5_returns_correct_event(self):
        """Test that rolling 5 returns the sixth event (16)"""
        self.assertEqual(determine_event(5), RANDOM_EVENTS[5])
        self.assertEqual(determine_event(5), "A mysterious fire damages a key structure or field. No culprit is found.")
    
    def test_roll_6_returns_correct_event(self):
        """Test that rolling 6 returns the seventh event (21)"""
        self.assertEqual(determine_event(6), RANDOM_EVENTS[6])
        self.assertEqual(determine_event(6), "A minor faction—bandits, raiders, or troublemakers—targets travelers near the settlement.")
    
    def test_roll_7_returns_correct_event(self):
        """Test that rolling 7 returns the eighth event (22)"""
        self.assertEqual(determine_event(7), RANDOM_EVENTS[7])
        self.assertEqual(determine_event(7), "A bumper harvest occurs, filling granaries beyond expectation.")
    
    def test_roll_8_returns_correct_event(self):
        """Test that rolling 8 returns the ninth event (23)"""
        self.assertEqual(determine_event(8), RANDOM_EVENTS[8])
        self.assertEqual(determine_event(8), "A charismatic performer, mystic, or storyteller visits, captivating the community.")
    
    def test_roll_9_returns_correct_event(self):
        """Test that rolling 9 returns the tenth event (24)"""
        self.assertEqual(determine_event(9), RANDOM_EVENTS[9])
        self.assertEqual(determine_event(9), "A beloved elder or leader passes away, leaving a difficult vacancy.")
    
    def test_roll_10_returns_correct_event(self):
        """Test that rolling 10 returns the eleventh event (25)"""
        self.assertEqual(determine_event(10), RANDOM_EVENTS[10])
        self.assertEqual(determine_event(10), "A long-lost traveler or relative unexpectedly returns home.")
    
    def test_roll_11_returns_correct_event(self):
        """Test that rolling 11 returns the twelfth event (26)"""
        self.assertEqual(determine_event(11), RANDOM_EVENTS[11])
        self.assertEqual(determine_event(11), "Tools, livestock, or supplies begin quietly disappearing. A thief is at work.")
    
    def test_roll_12_returns_correct_event(self):
        """Test that rolling 12 returns the thirteenth event (31)"""
        self.assertEqual(determine_event(12), RANDOM_EVENTS[12])
        self.assertEqual(determine_event(12), "A strange weather pattern persists—fog, heat, cold—causing confusion and hardship.")
    
    def test_roll_13_returns_correct_event(self):
        """Test that rolling 13 returns the fourteenth event (32)"""
        self.assertEqual(determine_event(13), RANDOM_EVENTS[13])
        self.assertEqual(determine_event(13), "A generous benefactor donates land, materials, or wealth to the community.")
    
    def test_roll_14_returns_correct_event(self):
        """Test that rolling 14 returns the fifteenth event (33)"""
        self.assertEqual(determine_event(14), RANDOM_EVENTS[14])
        self.assertEqual(determine_event(14), "A sudden influx of settlers or refugees expands the population.")
    
    def test_roll_15_returns_correct_event(self):
        """Test that rolling 15 returns the sixteenth event (34)"""
        self.assertEqual(determine_event(15), RANDOM_EVENTS[15])
        self.assertEqual(determine_event(15), "An infestation of pests or blight threatens crops or stored food.")
    
    def test_roll_16_returns_correct_event(self):
        """Test that rolling 16 returns the seventeenth event (35)"""
        self.assertEqual(determine_event(16), RANDOM_EVENTS[16])
        self.assertEqual(determine_event(16), "A child or animal is born with unusual markings believed to be an omen.")
    
    def test_roll_17_returns_correct_event(self):
        """Test that rolling 17 returns the eighteenth event (36)"""
        self.assertEqual(determine_event(17), RANDOM_EVENTS[17])
        self.assertEqual(determine_event(17), "A dangerous animal or monster begins stalking the outskirts.")
    
    def test_roll_18_returns_correct_event(self):
        """Test that rolling 18 returns the nineteenth event (41)"""
        self.assertEqual(determine_event(18), RANDOM_EVENTS[18])
        self.assertEqual(determine_event(18), "A traveling scholar or sage shares knowledge that improves local practices.")
    
    def test_roll_19_returns_correct_event(self):
        """Test that rolling 19 returns the twentieth event (42)"""
        self.assertEqual(determine_event(19), RANDOM_EVENTS[19])
        self.assertEqual(determine_event(19), "A flood or landslide reshapes part of the settlement or surrounding land.")
    
    def test_roll_20_returns_correct_event(self):
        """Test that rolling 20 returns the twenty-first event (43)"""
        self.assertEqual(determine_event(20), RANDOM_EVENTS[20])
        self.assertEqual(determine_event(20), "A local invention or breakthrough increases productivity or safety.")
    
    def test_roll_21_returns_correct_event(self):
        """Test that rolling 21 returns the twenty-second event (44)"""
        self.assertEqual(determine_event(21), RANDOM_EVENTS[21])
        self.assertEqual(determine_event(21), "An unexpected tax collector, official, or noble imposes new burdens.")
    
    def test_roll_22_returns_correct_event(self):
        """Test that rolling 22 returns the twenty-third event (45)"""
        self.assertEqual(determine_event(22), RANDOM_EVENTS[22])
        self.assertEqual(determine_event(22), "A hidden resource—clay, timber, herbs, ore—comes to light nearby.")
    
    def test_roll_23_returns_correct_event(self):
        """Test that rolling 23 returns the twenty-fourth event (46)"""
        self.assertEqual(determine_event(23), RANDOM_EVENTS[23])
        self.assertEqual(determine_event(23), "A rash of mischief, illusion, or prank-like hauntings disturbs residents.")
    
    def test_roll_24_returns_correct_event(self):
        """Test that rolling 24 returns the twenty-fifth event (51)"""
        self.assertEqual(determine_event(24), RANDOM_EVENTS[24])
        self.assertEqual(determine_event(24), "A wandering healer cures several lingering ailments.")
    
    def test_roll_25_returns_correct_event(self):
        """Test that rolling 25 returns the twenty-sixth event (52)"""
        self.assertEqual(determine_event(25), RANDOM_EVENTS[25])
        self.assertEqual(determine_event(25), "A destructive storm tears roofs, fences, and fields apart.")
    
    def test_roll_26_returns_correct_event(self):
        """Test that rolling 26 returns the twenty-seventh event (53)"""
        self.assertEqual(determine_event(26), RANDOM_EVENTS[26])
        self.assertEqual(determine_event(26), "A festival or celebration becomes the most joyful in recent memory.")
    
    def test_roll_27_returns_correct_event(self):
        """Test that rolling 27 returns the twenty-eighth event (54)"""
        self.assertEqual(determine_event(27), RANDOM_EVENTS[27])
        self.assertEqual(determine_event(27), "A trusted figure is caught in a scandal, fraud, or betrayal.")
    
    def test_roll_28_returns_correct_event(self):
        """Test that rolling 28 returns the twenty-ninth event (55)"""
        self.assertEqual(determine_event(28), RANDOM_EVENTS[28])
        self.assertEqual(determine_event(28), "A natural landmark—spring, grove, cavern—gains sudden importance or beauty.")
    
    def test_roll_29_returns_correct_event(self):
        """Test that rolling 29 returns the thirtieth event (56)"""
        self.assertEqual(determine_event(29), RANDOM_EVENTS[29])
        self.assertEqual(determine_event(29), "A strange celestial event (comet, eclipse, lights) causes awe and worry.")
    
    def test_roll_30_returns_correct_event(self):
        """Test that rolling 30 returns the thirty-first event (61)"""
        self.assertEqual(determine_event(30), RANDOM_EVENTS[30])
        self.assertEqual(determine_event(30), "A prosperous trade route opens temporarily, bringing wealth and contact.")
    
    def test_roll_31_returns_correct_event(self):
        """Test that rolling 31 returns the thirty-second event (62)"""
        self.assertEqual(determine_event(31), RANDOM_EVENTS[31])
        self.assertEqual(determine_event(31), "A building collapse, mine cave-in, or construction failure injures workers.")
    
    def test_roll_32_returns_correct_event(self):
        """Test that rolling 32 returns the thirty-third event (63)"""
        self.assertEqual(determine_event(32), RANDOM_EVENTS[32])
        self.assertEqual(determine_event(32), "A series of helpful coincidences or uncanny luck blesses the community.")
    
    def test_roll_33_returns_correct_event(self):
        """Test that rolling 33 returns the thirty-fourth event (64)"""
        self.assertEqual(determine_event(33), RANDOM_EVENTS[33])
        self.assertEqual(determine_event(33), "A cursed item, unsettling relic, or magical contamination is discovered.")
    
    def test_roll_34_returns_correct_event(self):
        """Test that rolling 34 returns the thirty-fifth event (65)"""
        self.assertEqual(determine_event(34), RANDOM_EVENTS[34])
        self.assertEqual(determine_event(34), "A traveling judge, inspector, or mediator resolves ongoing disputes.")
    
    def test_roll_35_returns_correct_event(self):
        """Test that rolling 35 returns the thirty-sixth event (66)"""
        self.assertEqual(determine_event(35), RANDOM_EVENTS[35])
        self.assertEqual(determine_event(35), "A local legend awakens—spirit, creature, or mythic threat—causing fear and unrest.")


if __name__ == '__main__':
    unittest.main()


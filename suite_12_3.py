import unittest
import module_12_1
import module_12_2

test_suit = unittest.TestSuite()
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
test_suit.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)                                   #уровень детализации вывода тестов
runner.run(test_suit)


import unittest
import tests_12_1
import tests_12_2

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runer = unittest.TextTestRunner(verbosity=2)

runer.run(runST)

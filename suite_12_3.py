import unittest
import tests_12_32
import tests_12_31
tournamentST = unittest.TestSuite()
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_32.TournamentTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_31.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)

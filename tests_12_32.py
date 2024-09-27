import unittest
import runner_and_tournament
from pprint import pprint

class TournamentTest(unittest.TestCase):
    x = True
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def tearDown(self):
        for key, value in TournamentTest.all_results.items():
            print(key, value, '  ', end='')
        print()

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def test_tournament1(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def test_tournament2(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def test_tournament3(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def test_tournament4(self):
        tour1 = runner_and_tournament.Tournament(6, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    @unittest.skipIf(x, 'Тесты в этом кейсе заморожены.')
    def test_tournament5(self):
        tour1 = runner_and_tournament.Tournament(8, self.runner3, self.runner2, self.runner1)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')




if __name__ == '__main__':
    unittest.main()

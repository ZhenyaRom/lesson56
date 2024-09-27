import unittest
import runner


class RunnerTest(unittest.TestCase):
    y = False
    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        test_petr = runner.Runner('Petr')
        for _ in range(10):
            test_petr.walk()
        self.assertEqual(test_petr.distance, 50)

    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        test_petr = runner.Runner('Petr')
        for _ in range(10):
            test_petr.run()
        self.assertEqual(test_petr.distance, 100)

    @unittest.skipIf(y, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        test_petr = runner.Runner('Petr')
        test_vasya = runner.Runner('Vasya')
        for _ in range(10):
            test_petr.walk()
            test_vasya.run()
        self.assertNotEqual(test_petr.distance, test_vasya.distance)


if __name__ == '__main__':
    unittest.main()

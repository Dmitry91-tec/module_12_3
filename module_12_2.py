import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):  # хранит результаты всех тестов в виде словаря
        # print("setUpClass")
        cls.all_results = []
        # print("создание списка участников")

    def setUp(self):  # создаются три бегуна
        # print('setUp')
        self.obj1 = Runner('Усэйн', 10)
        # print(f'{self.first}')
        self.obj2 = Runner('Андрей', 9)
        # print(f'{self.second}')
        self.obj3 = Runner('Ник', 3)
        # print(f'{self.third}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.obj1, self.obj3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.obj2, self.obj3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.obj1, self.obj2, self.obj3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):  # выводит результаты всех забегов из all_results
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}.', end=' ')
            for place, runner in elem.items():
                print(f'{place}: {runner.name} (speed: {runner.speed})', end=' ')
            print()


if __name__ == '__main__':
    unittest.main()

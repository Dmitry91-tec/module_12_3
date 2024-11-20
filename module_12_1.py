import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        obj=Runner('Васька')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance,50)
        return

    def test_run(self):
        obj2=Runner('Петька')
        for i in range(10):
            obj2.run()
        self.assertEqual(obj2.distance,100)
        return

    def test_callenge(self):
        obj3=Runner('Люська')
        obj4=Runner('Петрович')
        for i in range(10):
            obj3.run()
        for i in range(10):
            obj4.walk()
        self.assertNotEqual(obj3.distance,obj4.distance)
        return
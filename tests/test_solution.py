from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        array = [10, 10, 20, 20, 30, 30]

        res = solution(array)

        self.assertNotEqual(None, res)

        self.assertEqual(res[0], 10)
        self.assertEqual(res[1], 20)
        self.assertEqual(res[2], 30)

        array = [[1, 1], [2, 3]]

        res = solution(array)

        self.assertNotEqual(None, res)

        self.assertEqual(res[0], 1)
        self.assertEqual(res[1], 2)
        self.assertEqual(res[2], 3)



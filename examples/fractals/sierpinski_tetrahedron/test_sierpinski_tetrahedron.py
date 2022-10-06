import unittest
from sierpinski_tetrahedron import Tetrahedron


TEST_FIND_MEDIUM = [
    ([(0, 0, 0), (3, 6, 10)], [1.5, 3.0, 5.0]),
    ([(-1, -6, -18), (3, 6, 10)], [1.0, 0, -4.0]),
    ([(25.25, -1.5, 0), (3.25, 6, -2.2)], [14.25, 2.25, -1.1])
]


class TestFindMedium(unittest.TestCase):
    """Test case for method find_medium of Tetrahedron class"""
    def test_find_medium(self):
        for data, expected in TEST_FIND_MEDIUM:
            with self.subTest():
                self.assertEqual(Tetrahedron.find_medium(*data), expected)


if __name__ == '__main__':
    unittest.main()

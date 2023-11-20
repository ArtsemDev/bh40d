# import unittest

import pytest

from lesson15 import Math


# class MathTestCase(unittest.TestCase):
#
#     def setUp(self):
#         self.m = Math(a=6, b=2)
#
#     def test_mul(self):
#         self.assertEqual(self.m.mul(), 10)
#
#     def test_sum(self):
#         self.assertEqual(self.m.sum(), 8)


@pytest.fixture
def set_up():
    return Math(a=4, b=2)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "a, b, c",
    (
            (4, 2, 8),
            (3, 3, 9)
    )
)
async def test_mul(a, b, c, set_up):
    assert await set_up.mul(a=a, b=b) == c

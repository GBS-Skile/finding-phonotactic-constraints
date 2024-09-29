import unittest
from phoncon.constraints import NaturalClass, Constraint, parse_constraint


class TestConstraints(unittest.TestCase):
    def test_str_conversion(self):
        c = Constraint([
            NaturalClass([("voice", "-"), ("anterior", "+"), ("strident", "+")], complement=True),
            NaturalClass([("approximant", "-")]),
        ])
        self.assertEqual(str(c), "*[^-voice,+anterior,+strident][-approximant]")

    def test_parse_constraint(self):
        q = "*[^-voice,+anterior,+strident][-approximant]"
        c1 = parse_constraint(q)
        c2 = Constraint([
            NaturalClass([("voice", "-"), ("anterior", "+"), ("strident", "+")], complement=True),
            NaturalClass([("approximant", "-")]),
        ])
        self.assertEqual(c1, c2)

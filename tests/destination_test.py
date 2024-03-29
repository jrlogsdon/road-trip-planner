import unittest
from datetime import timedelta
import graphdestination

class MyTestCase(unittest.TestCase):
    def test_destination(self):
        d = graphdestination.GraphDestination(name="Denver, Colorado", time='15 hours', distance='1000 miles')
        t_expected = timedelta(hours=15)
        self.assertEqual(t_expected, d.time)
        self.assertEqual("Denver, Colorado", d.name)
        self.assertEqual('1000 miles', d.distance)

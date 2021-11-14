import unittest
import explorer
import parse_response_to_graph
import json

class MyTestCase(unittest.TestCase):
    def test_explore(self):
        actual_graph = None
        cincinnati = 'Cincinnati, OH, USA'
        denver = 'Denver, CO, USA'
        yosemite = 'Yosemite National Park, California, USA'
        with open('smaller_sample.json') as f:
            response = json.load(f)
            actual_graph = parse_response_to_graph.create_graph(response)

        actual_order_to_explore = explorer.explore(actual_graph, starting_location=cincinnati)
        expected_order_to_explore = [cincinnati, denver, yosemite]
        self.assertEqual(expected_order_to_explore, actual_order_to_explore)

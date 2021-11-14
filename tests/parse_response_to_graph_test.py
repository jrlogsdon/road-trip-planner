import unittest
import parse_response_to_graph
import json
import node
import graphdestination

class MyTestCase(unittest.TestCase):

    def test_parse_of_graph(self):
        cincinnati = 'Cincinnati, OH, USA'
        denver = 'Denver, CO, USA'
        yosemite = 'Yosemite National Park, California, USA'
        actual_graph = None
        dest1 = graphdestination.GraphDestination(name=cincinnati, distance=0, time=0)
        dest2 = graphdestination.GraphDestination(name=denver, distance=1916804, time=62215)
        dest3 = graphdestination.GraphDestination(name=yosemite, distance=3521898, time=117620)
        destinations = [dest1, dest2, dest3]
        expected_node_cinci = node.Node(cincinnati, destinations)

        dest1_yosemite = graphdestination.GraphDestination(name=cincinnati, distance=3520487, time=117016)
        dest2_yosemite = graphdestination.GraphDestination(name=denver, distance=1607428, time=55850)
        dest3_yosemite = graphdestination.GraphDestination(name=yosemite, distance=0, time=0)
        yosemite_destinations = [dest1_yosemite, dest2_yosemite, dest3_yosemite]
        expected_node_yose = node.Node(yosemite, yosemite_destinations)


        with open('smaller_sample.json') as f:
            response = json.load(f)
            actual_graph = parse_response_to_graph.get_graph(response)

        actual_node_cinci = actual_graph[cincinnati]
        actual_node_yosemite = actual_graph[yosemite]
        self.assertEqual(expected_node_cinci, actual_node_cinci)
        self.assertEqual(expected_node_yose, actual_node_yosemite)





import unittest
import google_distance_matrix_service

class MyTestCase(unittest.TestCase):
    def test_url(self):
        origins = ['Yosemite National Park', 'Cincinnati']
        destinations = ['Sequoia National Park']
        url = google_distance_matrix_service.build_distance_url(origins=origins, destinations=destinations, key='key')
        expected_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Yosemite%20National%20Park|Cincinnati&destinations=Sequoia%20National%20Park&key=key"
        self.assertEqual(expected_url, url)


if __name__ == '__main__':
    unittest.main()

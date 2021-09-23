import unittest
import requests
import parsermod
import cache
import json


class ApiTest(unittest.TestCase):
    with open("test_output_data.json") as json_file:
        test_output_data = json.load(json_file)
    with open("test_raw_data.json") as json_file:
        test_raw_data = json.load(json_file)

    def test_1_get_boston_status_code(self):
        city, country = "Boston", "us"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        r = requests.get(api_url)
        self.assertEqual(r.status_code, 200)

    def test_2_get_boston_location_name(self):
        city, country = "Boston", "us"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        r = requests.get(api_url)
        self.assertEqual(r.json()["location_name"], "Boston,US")

    def test_3_get_mumbai_status_code(self):
        city, country = "Mumbai", "in"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        r = requests.get(api_url)
        self.assertEqual(r.status_code, 200)

    def test_4_get_mumbai_location_name(self):
        city, country = "Mumbai", "in"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        r = requests.get(api_url)
        self.assertEqual(r.json()["location_name"], "Mumbai,IN")

    def test_5_content_type(self):
        city, country = "Salta", "ar"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        headertocheck = {"content-type": "application/json"}
        r = requests.get(api_url)
        self.assertDictEqual(r.json()["headers"], headertocheck)

    def test_6_getresponsedata(self):
        return_from_getresponsedata = {"location_name": "Mumbai,IN"}
        return_from_getresponsedata = parsermod.getresponsedata(ApiTest.test_raw_data, return_from_getresponsedata)
        test_output_data = ApiTest.test_output_data
        del (test_output_data["requested_time"])  # as requested_time is not coming from getresponsedata function
        self.assertDictEqual(return_from_getresponsedata, test_output_data)

    def test_7_gettempdata(self):
        return_from_gettempdata = parsermod.gettempdata(ApiTest.test_raw_data)
        test_output_temp_data = ApiTest.test_output_data["temperature"]
        self.assertListEqual(return_from_gettempdata, test_output_temp_data)

    def test_8_getgeocoordinates(self):
        return_from_getgeocoordinates = parsermod.getgeocoordinates(ApiTest.test_raw_data)
        test_output_coord_data = ApiTest.test_output_data["geo_coordinates"]
        self.assertListEqual(return_from_getgeocoordinates, test_output_coord_data)

    def test_9_checkincache_ifabsent(self):
        location = "London,UK"
        return_from_checkincache = cache.checkincache(location)
        self.assertEqual(return_from_checkincache, False)

    def test_10_checkincache_ifpresent(self):
        location = "Mumbai,IN"
        test_output_data = ApiTest.test_output_data
        cache.updatecache(location, test_output_data)
        return_from_checkincache = cache.checkincache(location)
        self.assertDictEqual(return_from_checkincache, test_output_data)

    def test_11_wrong_city(self):
        city, country = "Bossston", "us"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        res = requests.get(api_url).json()
        res_message = res["message"]
        self.assertEqual(res_message, "city not found")

    def test_12_blank_city(self):
        city, country = "", "us"
        api_url = f'http://127.0.0.1:5000/weather?city={city}&country={country}&'
        res = requests.get(api_url).json()
        res_message = res["message"]
        self.assertEqual(res_message, "Blank entry for city or country")


if __name__ == "__main__":
    unittest.main()

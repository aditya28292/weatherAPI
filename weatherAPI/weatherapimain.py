"""
Product Name : Weather API
Version : 0.1
Developer : Aditya
created on Sep 23, 2021

"""

from flask import Flask, request
import requests
import configparser
import cache
import logger
import parsermod
from datetime import datetime

config = configparser.ConfigParser()
config.read('env_variable.ini')
logc = logger.LoggingClass()

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def weather():
    """ This function will give weather data or error in form of json object"""
    try:
        base_url = config['ENV_VARIABLES']['BASE_URL']
        city = request.args.get('city').title()
        country = request.args.get('country').upper()
        api_key = config['ENV_VARIABLES']['API_KEY']

        if city != '' and country != '':
            returnres = {"location_name": city + "," + country}
            logc.logwriter(f"Location is {returnres['location_name']}")
            url = base_url + "q=" + city + "," + country + "&appid=" + api_key
            # print(url)
            if not cache.checkincache(returnres["location_name"]):
                logc.logwriter(f"complete URL is {url}")
                response = requests.get(url)
                if response.status_code == 200:
                    logc.logwriter(f"status code is {response.status_code}")
                    data = response.json()
                    print("coming from openweathermap api")
                    logc.logwriter("coming from openweathermap api")
                    returnres = parsermod.getresponsedata(data, returnres)
                    cache.updatecache(returnres["location_name"], returnres)
                    returnres["requested_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    logc.logwriter(f"Final response object is {returnres}")
                    return returnres
                else:
                    print(response.status_code)
                    logc.logwriter(f"status code is {response.status_code}")
                    return response.json()
            else:
                print("coming from cache")
                logc.logwriter("coming from cache")
                returnres = cache.checkincache(returnres["location_name"])
                returnres["requested_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logc.logwriter(f"Final response object is {returnres}")
                return returnres
        else:
            logc.logerror("Blank entry for city or country")
            error_response_for_blank = {
                "cod": "400",
                "message": "Blank entry for city or country"
            }
            return error_response_for_blank
    except BaseException as msg:
        print(msg)
        logc.logerror(msg)
        error_response_for_exception = {
            "cod": "400",
            "message": "Something went wrong"
        }
        return error_response_for_exception


if __name__ == '__main__':
    app.run(debug=True)

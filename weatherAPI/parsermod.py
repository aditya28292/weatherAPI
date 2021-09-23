import logger
from datetime import datetime
logc = logger.LoggingClass()


def gettempdata(rawdata):
    """ This function will take rawdata i.e. get response from base url as argument and return a list of
        temperature in both Celsius and Fahrenheit  """
    final_temp = []
    in_k = rawdata["main"]["temp"]
    in_c = round((float(in_k) - 273.15), 2)
    in_f = round(((in_c * (9 / 5)) + 32), 2)
    final_temp.append(str(in_c) + "C")
    final_temp.append(str(in_f) + "F")
    return final_temp


def getgeocoordinates(rawdata):
    """ This function will take rawdata i.e. get response from base url as argument and return a list of
        latitude and longitude """
    final_geo_coordinates = []
    lat = rawdata["coord"]["lat"]
    lon = rawdata["coord"]["lon"]
    final_geo_coordinates.append(lat)
    final_geo_coordinates.append(lon)
    return final_geo_coordinates


def getresponsedata(rawdata, responseobj):
    """ This function will take rawdata i.e. get response from base url and responseobj dictionary as argument
        and will return only those attributes that is needed in human readable format"""
    try:
        logc.logwriter("in getresponsedata")
        responseobj["temperature"] = gettempdata(rawdata)
        responseobj["wind"] = str(rawdata["wind"]["speed"]) + "m/s"
        responseobj["cloudiness"] = str(rawdata["clouds"]["all"]) + "%"
        responseobj["pressure"] = str(rawdata["main"]["pressure"]) + "hpa"
        responseobj["humidity"] = str(rawdata["main"]["humidity"]) + "%"
        responseobj["geo_coordinates"] = getgeocoordinates(rawdata)
        responseobj["sunrise"] = datetime.utcfromtimestamp(rawdata["sys"]["sunrise"]).strftime('%H:%M')
        responseobj["sunset"] = datetime.utcfromtimestamp(rawdata["sys"]["sunset"]).strftime('%H:%M')
        responseobj["forecast"] = rawdata["weather"][0]["description"]
        responseobj["headers"] = {"content-type": "application/json"}
        logc.logwriter("getting response data from getresponsedata")
        return responseobj
    except BaseException as msg:
        print(msg)
        logc.logerror(msg)
        error_response_for_exception = {
            "cod": "400",
            "message": "Something went wrong"
        }
        return error_response_for_exception

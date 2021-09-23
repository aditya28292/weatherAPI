from datetime import datetime
import logger

logc = logger.LoggingClass()

cache_dict = {}


def checkincache(val):
    """ This function will take location as argument example: 'Boston,US' and will function as below:
        1. if location is not available in cache_dict keys i.e. not availabl ein cache memory, it will return False
        2. if location is available in cache then it will function as below:
            2.1. if the data is cached before 2 minutes it will return False
            2.2. if the data is cached in last 2 minutes then function will return the data dictionary
     """
    try:
        logc.logwriter("in checkingcache")
        logc.logwriter(f"location is {val} and cache is {cache_dict}")
        if val in cache_dict.keys():
            difference_in_sec = (datetime.now() - cache_dict[val]["time"]).total_seconds()
            if difference_in_sec > 120:
                logc.logwriter(f"{val} : data is older than 2 minutes. will get updated")
                return False
            else:
                logc.logwriter("returning data from cache")
                return cache_dict[val]["body"]
        else:
            logc.logwriter(f"data for location {val} is not found in cache")
            return False
    except BaseException as msg:
        print(msg)
        logc.logerror(msg)
        error_response_for_exception = {
            "cod": "400",
            "message": "Something went wrong"
        }
        return error_response_for_exception


def updatecache(loc, data):
    """ This function will update cache. time is also added as key to check 2 minutes cache condition
        in checkincache function"""
    cache_dict[loc] = {
        "time": datetime.now(),
        "body": data
    }
    logc.logwriter(f"Cache is updated with location: {loc}")

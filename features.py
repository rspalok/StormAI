import wikipedia
import webbrowser
import stormApp
import requests
import datetime
import calendar
from webbrowser import Chrome

def searchonWiki(query):
    return wikipedia.summary(query,sentences='2')

def openGoogle():
    webbrowser.open('www.google.com')
    return

def openYoutube():
    webbrowser.open('www.youtube.com')
    return

def Googlesearch(query = "What is python ?"):
    tabUrl = "http://google.com/?#q="
    webbrowser.open(tabUrl + query , new= 2)
    return

def getDate():
    now = datetime.datetime.now()
    my_date =datetime.datetime.today()
    weakday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    MONTHS = ['January', 'February' , 'March' , 'April' , 'May' , 'June' ,
                   'July' , 'August' , 'September' , 'October' , 'November' ,'December']

    ordinalNumbers = ['1st' , '2nd' , '3rd' , '4th' , '5th ', '6th' , '7th' , '8th' , '9th' , '10th' , '11th',
                      '12th' , '13th' , '14th' , '15th' , '16th' , '17th' ,'18th' , '19th' , '20th' , '21st' ,
                      '22nd', '23rd' , '24th' , '25th' , '26th', '27th' , '28th' , '29th' , '30th' , '31st'
                     ]

    return 'Today is {} of {} {}'.format(ordinalNumbers[dayNum -1],MONTHS[monthNum -1],weakday)


def getweather(city_name):
    # Python program to find current
    # weather details of any city
    # using openweathermap api
    #Api key
    api_key = "038ba22ab190db58ec1fa9acac5123a7"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y

        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        stormApp.speak(" Currunt Temperature is " +
                       str(int(current_temperature - 274.15) ) + "Degree Centigrades" +
              "\n atmospheric pressure is  " +
                       str(current_pressure) +"HPA" +
              "\n humidity is " +
                       str(current_humidiy) + "percent"
              "\n description is  " +
                       str(weather_description))

    else:
        stormApp.speak(" City Not Found Sir !!!")
    return
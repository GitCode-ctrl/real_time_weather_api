import requests #this library will help in making http requests i.e. to access weather API

def get_weather(city): #define a function that takes one parameter which is city!
    API_KEY = "27bdb39026f94d92dbe5182de24d9cd6"  # <- Replace this with your real API key that you have generated from weather API
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather" #API endpoint or web address the program will connect to for the weather info

    #following are the information that the API will need to give the program what it wants to fetch
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # metric for celsius/ imperial for fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params) #this will send actual http request
        data = response.json() #converting the response which is in JSON format into a python data

        if response.status_code != 200:  #In HTTP, status codes are used to communicate the result of a server's response to a client's request. 200 OK is the standard success status code.
            print("Error:", data.get("message", "Something went wrong.")) #ries to find the key "message". If it's there, it returns its value. If not, it returns "Something went wrong.".
            return

        weather = data["weather"][0]["description"].title()  #Get the weather description (like ‘clear sky’), and capitalize it.
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤️ Weather in {city.title()}:\n"
              f"Condition: {weather}\n"
              f"Temperature: {temp}°C\n"
              f"Humidity: {humidity}%\n"
              f"Wind Speed: {wind_speed} m/s\n")

    except Exception as e:
        # is the variable that holds the error message. This message will tell you what went wrong.
        # For example, it could be a connection error, invalid API key, or any other issue that prevents the data from being fetched.
        print("Failed to retrieve weather data. Reason:", e)

if __name__ == "__main__": #Only run the code below if this file is being run directly (not imported elsewhere).
    city_name = input("Enter a city name: ")
    get_weather(city_name)

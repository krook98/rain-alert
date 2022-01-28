# General info
An app that sends SMS notifications warning about incoming rain.

### API used
I got weather data thanks to OpenWeather API (https://openweathermap.org/)
I send SMS notifications with Twilio API (https://www.twilio.com/)


### Technology
Python 3.9.10
I run the code as a scheduled task on PythonAnywhere (https://www.pythonanywhere.com)

### Setup
To run this project you might need your own API keys. Twilio and OpenWeather accounts are neccessary.  
requests, twilio and os Python libraries are required

### Launch
Firstly, you need to add your own API keys, phone number and notification number from Twilio. You set environment variables in terminal with:
`export 'YOUR_ENV_VAR_NAME'=value`
Then you can access it in code with:
`os.environ.get('YOU_ENV_VAR_NAME')`
Run app with:
`python3 main.py` 




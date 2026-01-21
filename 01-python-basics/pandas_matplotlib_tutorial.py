import pandas as pd
from datetime import datetime, timedelta                                  #timedelta is used to calcluate the date/time with specific difference provided by the user
import streamlit as st
from temprature_project.services.temprature_api import range_of_data as rod  #if you will not give temprature_api it will give error because temprature_project is a package and when path is mentioned till parent folder then pyton looks for file inside __init__.py (package rule)
'''from .temprature_api import get_weather '''                            #---> You can also use this

today = datetime.now()
week_later = today + timedelta(days=7)

start_date = today.strftime("%Y-%m-%d")   #strigify date in specific format accepted by API (%Y-2025, %y-25, %m-month in number, %B-month in alphabet, %d-date)
end_date = week_later.strftime("%Y-%m-%d")

latitude = 22.7196
longitude = 75.8577

data = rod(latitude, longitude, start_date,end_date)
daily_data = data['hourly']
dataFrame = pd.DataFrame({
    "Date and Time": daily_data['time'],
    "Temprature" : daily_data['temperature_2m']
})

dataFrame['Date and Time'] = pd.to_datetime(dataFrame['Date and Time'])
print(dataFrame)







from pyowm import OWM
API_key = 'b19cc0c64f569ba9eefd6b3e9ff1b2eb'
owm = OWM(API_key)
obs=owm.weather_at_id(1843564)
w=obs.get_weather()

print(w.get_status(),w.get_temperature(unit='celsius')['temp'])

# sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'
sentence = 'Becoming Cloud Engineer Training requires commitment of time and engaging in coding with passion'
words_list = sentence.split(' ')
print(words_list)
result = {word: len(word) for word in words_list}
print(result)
##################################################################
weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}
print(f'Temp in Fahrenheit: {weather_f}')
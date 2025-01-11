import random

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.moods = ["весёлый", "грустный", "злой", "сонный", "энергичный"]
        self.current_mood = random.choice(self.moods)
    
    def greet(self):
        print(f"Привет, {self.name}! Я бот с настроением. У меня сегодня {self.current_mood} настроение.")
    
    def process_input(self, user_input):
        if user_input.lower() in ["пока", "выход", "до свидания"]:
            return self.farewell()
        
        if "как дела" in user_input.lower():
            return f"У меня {self.current_mood} настроение. А у тебя?"
        
        if "что делаешь" in user_input.lower():
            return "Я болтаю с тобой, это весело!"
        
        return self.random_response()

    def random_response(self):
        mood_response = {
            "весёлый": "Ха-ха! Мне так весело!",
            "грустный": "Сегодня какой-то грустный день...",
            "злой": "Не дразни меня!",
            "сонный": "Хочу спать...",
            "энергичный": "У меня столько энергии! Готов к приключениям!"
        }
        return mood_response.get(self.current_mood, "Интересно... Расскажи ещё что-нибудь!")

    def farewell(self):
        return f"Пока, {self.name}! Хорошего дня!"

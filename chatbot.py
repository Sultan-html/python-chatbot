class ChatBot:
    def __init__(self, name):
        self.name = name
        self.moods = ["весёлый", "грустный", "злой", "сонный", "энергичный"]
        self.current_mood = random.choice(self.moods)
        self.history = []
    
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
    
    def save_history(self, message):
        self.history.append(message)

    def show_history(self):
        print("\nИстория чата:")
        for idx, msg in enumerate(self.history, 1):
            print(f"{idx}. {msg}")
def main():
    user_name = input("Как тебя зовут? ")
    bot = ChatBot(user_name)
    bot.greet()
    
    while True:
        try:
            user_input = input(f"{user_name}: ")
            response = bot.process_input(user_input)
            print(f"Бот: {response}")
            
            if user_input.lower() in ["пока", "выход", "до свидания"]:
                break
            
            bot.save_history(f"Пользователь: {user_input}")
            bot.save_history(f"Бот: {response}")
        
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            break
    
    bot.show_history()

if __name__ == "__main__":
    main()

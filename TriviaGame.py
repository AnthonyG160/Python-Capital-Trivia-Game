import sqlite3
import random

class TriviaGame:
    def __init__(self, db_name='trivia_app.db'):
        with sqlite3.connect(db_name) as self.conn:
            self.cursor = self.conn.cursor()
            self.create_table()
            if self.check_if_table_is_empty():
                self.insert_questions()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                answer_a TEXT NOT NULL,
                answer_b TEXT NOT NULL,
                answer_c TEXT NOT NULL,
                answer_d TEXT NOT NULL,
                correct_answer TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_questions(self):
        questions = [
            ("What is the capital of France?", "Berlin", "Madrid", "Rome", "Paris", "D"),
            ("What is the capital of Germany?", "Vienna", "Berlin", "Zurich", "Amsterdam", "B"),
            ("What is the capital of Italy?", "Madrid", "Rome", "Berlin", "Florence", "B"),
            ("What is the capital of Spain?", "Barcelona", "Lisbon", "Madrid", "Paris", "C"),
            ("What is the capital of Japan?", "Seoul", "Tokyo", "Bangkok", "Beijing", "B"),
            ("What is the capital of Australia?", "Sydney", "Melbourne", "Brisbane", "Canberra", "D"),
            ("What is the capital of Canada?", "Toronto", "Montreal", "Vancouver", "Ottawa", "D"),
            ("What is the capital of the United Kingdom?", "Cardiff", "Edinburgh", "London", "Dublin", "C"),
            ("What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Chennai", "B"),
            ("What is the capital of Russia?", "Moscow", "Kazan", "St. Petersburg", "Sochi", "A"),
            ("What is the capital of China?", "Shanghai", "Beijing", "Guangzhou", "Shenzhen", "B"),
            ("What is the capital of Brazil?", "Rio de Janeiro", "São Paulo", "Brasilia", "Salvador", "C"),
            ("What is the capital of South Africa?", "Pretoria", "Cape Town", "Durban", "Johannesburg", "A"),
            ("What is the capital of Mexico?", "Guadalajara", "Tijuana", "Mexico City", "Cancun", "C"),
            ("What is the capital of Egypt?", "Cairo", "Giza", "Alexandria", "Luxor", "A"),
            ("What is the capital of Argentina?", "Lima", "Santiago", "Buenos Aires", "Montevideo", "C"),
            ("What is the capital of Saudi Arabia?", "Jeddah", "Mecca", "Riyadh", "Dammam", "C"),
            ("What is the capital of Turkey?", "Ankara", "Istanbul", "Izmir", "Antalya", "A"),
            ("What is the capital of Thailand?", "Krabi", "Phuket", "Chiang Mai", "Bangkok", "D"),
            ("What is the capital of Greece?", "Athens", "Thessaloniki", "Crete", "Rhodes", "A"),
            ("What is the capital of Norway?", "Trondheim", "Bergen", "Stavanger", "Oslo", "D"),
            ("What is the capital of Italy?", "Milan", "Rome", "Venice", "Florence", "B"),
            ("What is the capital of Finland?", "Helsinki", "Oslo", "Stockholm", "Tallinn", "A"),
            ("What is the capital of Portugal?", "Lisbon", "Madrid", "Barcelona", "Seville", "A"),
            ("What is the capital of Sweden?", "Oslo", "Copenhagen", "Helsinki", "Stockholm", "D"),
            ("What is the capital of Denmark?", "Stockholm", "Oslo", "Copenhagen", "Helsinki", "C"),
            ("What is the capital of Hungary?", "Budapest", "Prague", "Warsaw", "Bratislava", "A"),
            ("What is the capital of Czech Republic?", "Prague", "Budapest", "Vienna", "Bratislava", "A"),
            ("What is the capital of Austria?", "Vienna", "Berlin", "Zurich", "Ljubljana", "A"),
            ("What is the capital of Russia?", "Sochi", "St. Petersburg", "Moscow", "Kazan", "C"),
            ("What is the capital of Romania?", "Bucharest", "Sofia", "Belgrade", "Zagreb", "A"),
            ("What is the capital of Bulgaria?", "Sofia", "Bucharest", "Budapest", "Prague", "A"),
            ("What is the capital of Slovakia?", "Prague", "Bratislava", "Budapest", "Vienna", "B"),
            ("What is the capital of Indonesia?", "Jakarta", "Bali", "Banda Aceh", "Surabaya", "A"),
            ("What is the capital of Malaysia?", "Jakarta", "Bangkok", "Singapore", "Kuala Lumpur", "D"),
        ]
        self.cursor.executemany(
            "INSERT INTO questions (question_text, answer_a, answer_b, answer_c, answer_d, correct_answer) VALUES (?, ?, ?, ?, ?, ?)",
            questions
        )
        self.conn.commit()

    def check_if_table_is_empty(self):
        self.cursor.execute("SELECT COUNT(*) FROM questions")
        count = self.cursor.fetchone()[0]
        return count == 0

    def get_random_question(self):
        self.cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 1")
        return self.cursor.fetchone()

    def get_valid_number_input(self, prompt, min_value=1, max_value=40):
        while True:
            user_input = input(prompt)
            try:
                number = int(user_input)
                if min_value <= number <= max_value:
                    return number
                else:
                    print(f"Please enter a number between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    def play_trivia(self):
        print("Welcome to the Country Capital Trivia Game!")

        num_questions = self.get_valid_number_input("How many questions would you like to answer (1-40)? ", 1, 40)

        score = 0 
        asked_questions = set() 

        while len(asked_questions) < num_questions:
            question = self.get_random_question()
            
            if question:
                question_id = question[0] 
                if question_id not in asked_questions: 
                    asked_questions.add(question_id)  

                    print("\n" + question[1]) 
                    print("A:", question[2])
                    print("B:", question[3])
                    print("C:", question[4])
                    print("D:", question[5])
                   
                    while True:
                        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
                        if user_answer in ['A', 'B', 'C', 'D']:
                            break 
                        else:
                            print("Invalid input. Please enter A, B, C, or D.")
                           
                            print("\n" + question[1]) 
                            print("A:", question[2])
                            print("B:", question[3])
                            print("C:", question[4])
                            print("D:", question[5])

                    if user_answer == question[6]:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Incorrect! The correct answer was: {question[6]}.")

        print(f"\nYour total score is: {score}/{num_questions}")
        self.conn.close()

if __name__ == "__main__":
    game = TriviaGame()
    game.play_trivia()

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.score = 0

    def score_up(self):
        self.score += 1




user_1 = User(input("Enter user id"), input("Enter username"))
user_2 = User(input("Enter user id"), input("Enter username"))

user_1.score_up()

print(f"Score 1:- {user_1.score}\nscore 2:- {user_2.score}")

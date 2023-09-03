class Brain:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list  # receiving the qn_bank list filled with qn and ans and storing in q_list
        self.ans = ""
        self.score = 0

    def next_q(self, q_no):  # q_no is passed with function call
        print(self.q_list[q_no].text)   # prints the corresponding qn wrt to q_no
        self.ans = input("Enter Your answer here:- ").lower()  # receiving ans

    def checker(self, q_no):  # q_no passed with function call
        if self.ans == self.q_list[q_no].answer.lower():  # checking ans
            self.score += 1
        print(f"Current score = {self.score}/{q_no + 1}")

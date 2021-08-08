class CustomsForm():
    """
    Customs forms have 26 yes-or-no questions a...z.
    This is encoded by having the letter all positive answers present in a string.

    Example:
    For the form `abc`, questions a,b, and c have the answer `yes`, others are
    answered `no`.
    """

    @property
    def yes_count(self):
        yes_answers = 0
        for answer in self.answers.values():
            if answer is True:
                yes_answers += 1
        return yes_answers


    @property
    def no_count(self):
        return 26 - self.yes_count

    def __init__(self, encoded_answers: str):
        self.answers = {}
        self.encoded_answers = encoded_answers
        for letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                       "n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            self.answers[letter] = False
        self.decode_question_string(encoded_answers)

    def __eq__(self, other):
        if isinstance(other, CustomsForm):
            return self.answers == other.answers
        else:
            return False

    def decode_question_string(self, yes_questions:str):
        for char in yes_questions:
            self.answers[char] = True

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"CustomsForm({self.encoded_answers})"

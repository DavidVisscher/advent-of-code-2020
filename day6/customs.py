from typing import List
from functools import total_ordering


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


class CustomsGroup():

    def __repr__(self):
        out = "CustomsGroup {"
        for form in self.customs_forms:
            out += f"{repr(form)},"
        out += "}"
        return out


    @property
    def size(self):
        return len(self.customs_forms)

    @property
    def yes_count(self):
        out = 0
        for form in self.customs_forms:
            out += form.yes_count
        return out

    @property
    def no_count(self):
        out = 0
        for form in self.customs_forms:
            out += form.no_count
        return out

    def __init__(self, customs_forms: List):
        self.customs_forms = customs_forms

    def __eq__(self, other):
        if isinstance(other, CustomsGroup):
            return self.customs_forms == other.customs_forms
        else:
            return False

    @classmethod
    def from_str(cls, groups_encoded_forms):
        forms = []
        for line in groups_encoded_forms.split("\n"):
            forms.append(CustomsForm(line.strip()))
        return cls(forms)

    @classmethod
    def multiple_from_str(cls, multiple_encoded_groups):
        out_groups = []
        for encoded_group in multiple_encoded_groups.split("\n\n"):
            out_groups.append(cls.from_str(encoded_group))
        return out_groups

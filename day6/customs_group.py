import copy
from typing import List
from day6 import CustomsForm

class CustomsGroup():

    def __init__(self, customs_forms: List):
        self.customs_forms = customs_forms

    def __eq__(self, other):
        if isinstance(other, CustomsGroup):
            return self.customs_forms == other.customs_forms
        else:
            return False
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
    def unique_yes_count(self):
        yes_questions = {}
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                       "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            for form in self.customs_forms:
                if form.answers[letter] is True:
                    yes_questions[letter] = True

        return len(yes_questions)

    @property
    def common_yes_count(self):
        """
        Returns the amount of "yes" answers everyone in the group has in common
        """
        common_yesses = copy.deepcopy(self.customs_forms[0].answers)

        for form in self.customs_forms:
            for letter, answer in form.answers.items():
                if common_yesses[letter] is True and answer is True:
                    common_yesses[letter] = True
                else:
                    common_yesses[letter] = False

        count_of_common_yesses = 0
        for letter, answer in common_yesses.items():
            if answer is True:
                count_of_common_yesses += 1

        return count_of_common_yesses

    @property
    def no_count(self):
        out = 0
        for form in self.customs_forms:
            out += form.no_count
        return out


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

from typing import List
from day6 import CustomsForm

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

from day6 import CustomsGroup, CustomsForm


class TestCustomsGroup:
    group_of_one_str = "a"
    group_of_three_str = "abc\nbc\nqwerty"

    group_of_three = CustomsGroup(
        [CustomsForm("abc"), CustomsForm("bc"), CustomsForm("qwerty")]
    )

    group_of_one = CustomsGroup([CustomsForm("a")])

    def test_form_count(self):
        assert self.group_of_three.size == 3
        assert self.group_of_one.size == 1

    def test_yes_count(self):
        assert self.group_of_three.yes_count == 11
        assert self.group_of_one.yes_count == 1

    def test_no_count(self):
        assert self.group_of_one.no_count == 25
        assert self.group_of_three.no_count == 67

    def test_equality(self):
        assert not CustomsGroup([]) == 12
        assert CustomsGroup([CustomsForm("abc")]) == \
            CustomsGroup([CustomsForm("abc")])
        assert CustomsGroup([CustomsForm("ab")]) == \
            CustomsGroup([CustomsForm("ab")])
        assert not CustomsGroup([CustomsForm("ab")]) == CustomsGroup(
            [CustomsForm("abc")]
        )
        assert not CustomsGroup([CustomsForm("abc")]) == CustomsGroup(
            [CustomsForm("ab")]
        )

    def test_create_from_string(self):
        assert CustomsGroup.from_str(self.group_of_one_str) == \
            self.group_of_one
        assert CustomsGroup.from_str(self.group_of_three_str) == \
            self.group_of_three

    def test_create_multiple_from_string(self):
        assert CustomsGroup.multiple_from_str(
            self.group_of_one_str + "\n\n" + self.group_of_three_str
        ) == [self.group_of_one, self.group_of_three]
from day6 import CustomsForm, CustomsGroup


class TestCustomsForm:
    def test_answer_decode(self):
        form = CustomsForm("abcdf")
        assert form.answers["a"] is True
        assert form.answers["b"] is True
        assert form.answers["e"] is False
        assert form.answers["z"] is False

        form2 = CustomsForm("yz")
        for key, answer in form2.answers.items():
            if key == "y" or key == "z":
                assert answer is True
            else:
                assert answer is False

    def test_yes_answer_count(self):
        assert CustomsForm("a").yes_count == 1
        assert CustomsForm("").yes_count == 0
        assert CustomsForm("ad").yes_count == 2
        assert CustomsForm("abcdefghijklmnopqrstuvwxyz").yes_count == 26
        assert CustomsForm("aaaaaaaaaaaaaaaaaaaaaaaaaa").yes_count == 1
        assert CustomsForm("abb").yes_count == 2
        assert CustomsForm("abc").yes_count == 3
        assert CustomsForm("ap").yes_count == 2

    def test_no_answer_count(self):
        assert CustomsForm("a").no_count == 25
        assert CustomsForm("").no_count == 26
        assert CustomsForm("ad").no_count == 24
        assert CustomsForm("abcdefghijklmnopqrstuvwxyz").no_count == 0
        assert CustomsForm("aaaaaaaaaaaaaaaaaaaaaaaaaa").no_count == 25
        assert CustomsForm("abb").no_count == 24
        assert CustomsForm("abc").no_count == 23
        assert CustomsForm("ap").no_count == 24

    def test_empty_input(self):
        form = CustomsForm("")
        assert len(form.answers) == 26
        for answer in form.answers.values():
            assert answer is False

    def test_equality(self):
        assert CustomsForm("abc") == CustomsForm("abc")
        assert CustomsForm("ab") == CustomsForm("ab")
        assert CustomsForm("z") == CustomsForm("z")
        assert not CustomsForm("abc") == CustomsForm("ab")
        assert not CustomsForm("abc") == 12


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

from day6 import CustomsForm


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
from day6 import CustomsGroup, CustomsForm
from day6.customs import sum_unique_yes_answers_for_multiple_groups, count_unique_yes_answers_in_file, \
    count_common_yes_answers_in_file, sum_common_yes_answers_for_multiple_groups


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

    def test_unique_yes_count(self):
        assert self.group_of_three.unique_yes_count == 9
        assert self.group_of_one.unique_yes_count == 1

    def test_common_yes_count(self):
        assert self.group_of_one.common_yes_count == 1
        assert self.group_of_three.common_yes_count == 0

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

    def test_unique_count(self):
        groups = CustomsGroup.multiple_from_str(self.group_of_one_str + "\n\n" + self.group_of_three_str)
        assert sum_unique_yes_answers_for_multiple_groups(groups) == 10
        assert sum_unique_yes_answers_for_multiple_groups([self.group_of_one]) == 1
        assert sum_unique_yes_answers_for_multiple_groups([self.group_of_three]) == 9

    def test_common_count(self):
        groups_from_str = CustomsGroup.multiple_from_str(self.group_of_one_str + "\n\n" + self.group_of_three_str)
        assert sum_common_yes_answers_for_multiple_groups(groups_from_str) == 1
        assert sum_common_yes_answers_for_multiple_groups([self.group_of_one]) == 1
        assert sum_common_yes_answers_for_multiple_groups([self.group_of_three]) == 0

        group1 = CustomsGroup([CustomsForm("ovuxdgiheszjbaltw"), CustomsForm("oxwjiubhfylzavst")])
        group2 = CustomsGroup([CustomsForm("abcdefgxyz"), CustomsForm("abcdefg")])
        group3 = CustomsGroup([CustomsForm("abcdefgxyz"), CustomsForm("abcdfg")])
        group4 = CustomsGroup([CustomsForm("abcdefgxyz"), CustomsForm("acdfg"), CustomsForm("acdf")])
        group5 = CustomsGroup([CustomsForm("abcdefgxyz"), CustomsForm("acdfg"), CustomsForm("acdf"), CustomsForm("y")])
        assert group1.common_yes_count == 14
        assert group2.common_yes_count == 7
        assert group3.common_yes_count == 6
        assert group4.common_yes_count == 4
        assert group5.common_yes_count == 0

        assert sum_common_yes_answers_for_multiple_groups([group1, group2, group3, group4, group5]) == 31


    def test_count_unique_from_test_file(self):
        assert count_unique_yes_answers_in_file("day6/data/testdata.txt") == 11
        assert count_unique_yes_answers_in_file("day6/data/input.txt") == 6534

    def test_count_common_from_test_file(self):
        assert count_common_yes_answers_in_file("day6/data/testdata.txt") == 6
        assert count_common_yes_answers_in_file("day6/data/testdata_custom.txt") == 32
        assert count_common_yes_answers_in_file("day6/data/input.txt") == 3402

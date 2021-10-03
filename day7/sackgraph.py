from day7.exceptions import UnknownBagException

from typing import AnyStr, Set, Dict


class SackGraph:
    def __init__(self):
        self._links = {}  # Contains all links of type outer_bag contains X inner bags

    @property
    def colors_in_graph(self) -> Set[AnyStr]:
        """
        Returns all colors currently in the graph.
        """
        return set(self._links.keys())

    def add_link(self, outer_bag_color: str, amount_contained: int, inner_bag_color: str):
        """
        Adds a bag to the graph.
        """
        if not self.contains_bag_of_color(outer_bag_color):
            self._links[outer_bag_color] = []
        if not self.contains_bag_of_color(inner_bag_color):
            self._links[inner_bag_color] = []
        self._links[outer_bag_color].append({"contains": inner_bag_color, "amount": amount_contained})

    def contains_bag_of_color(self, color: str) -> bool:
        """
        Returns True if graph contains a bag of this color.
        """
        return color in self._links.keys()

    def parse_link(self, link_string):
        """
        Parses a link from a given string of the form:
        {color} bag(s) contain (amount) {color} bag, ... .
        for example:
        light red bags contain 1 bright white bag, 2 muted yellow bags.
        """
        outer_bag_string, contained_bags_string = link_string.split("contain")
        outer_bag_color = outer_bag_string.replace("bags", "").strip()

        for contained_bag in contained_bags_string.split(","):
            contained_bag = contained_bag.strip()
            amount_string, color_string = contained_bag.split(" ", 1)
            color_string = color_string.split("bag")[0].strip()
            self.add_link(outer_bag_color, int(amount_string), color_string)

    def get_contents(self, outer_bag_color) -> Dict:
        """
        Returns a dict with the total amount of bags that can be contained in the given color bag
        for each color of inner bag.
        For example:
        if a red bag can contain 2 blue bags
        and a blue bag can contain 2 yellow bags

        the result for get_contents("red") will be:
        {"blue": 2, "yellow": 4}
        """
        if not self.contains_bag_of_color(outer_bag_color):
            raise UnknownBagException(f"There is no bag of color {outer_bag_color} in the graph.")

        out = dict()
        for link in self._links[outer_bag_color]:
            inner_bag_color = link["contains"]
            inner_bag_amount = link["amount"]
            out[inner_bag_color] = inner_bag_amount

            recursed_contents = self.get_contents(inner_bag_color)
            for contained_bag_color, contained_bag_amount in recursed_contents.items():
                contained_bag_amount *= inner_bag_amount
                out[contained_bag_color] = contained_bag_amount

        return out

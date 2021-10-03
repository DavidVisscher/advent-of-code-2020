from day7.sackgraph import SackGraph
from day7.exceptions import UnknownBagException

import pytest


def test_create_sackgraph():
    SackGraph()


def test_create_link():
    graph = SackGraph()
    with pytest.raises(UnknownBagException):
        graph.get_contents("tangerine")
    graph.add_link("red", 12, "blue")
    assert graph.get_contents("red") == {"blue": 12}
    assert graph.colors_in_graph == {"red", "blue"}
    graph.add_link("red", 2, "yellow")
    assert graph.get_contents("red") == {"blue": 12, "yellow": 2}
    assert graph.colors_in_graph == {"red", "blue", "yellow"}
    graph.add_link("yellow", 2, "orange")
    assert graph.get_contents("yellow") == {"orange": 2}
    assert graph.get_contents("red") == {"blue": 12, "yellow": 2, "orange": 4}
    assert graph.colors_in_graph == {"red", "blue", "yellow", "orange"}
    graph.add_link("orange", 2, "mauve")
    assert graph.get_contents("red") == {"blue": 12, "mauve": 8, "orange": 4, "yellow": 2}
    assert graph.colors_in_graph == {"red", "blue", "yellow", "orange", "mauve"}


def test_bag_parsing():
    graph = SackGraph()
    graph.parse_link("light red bags contain 1 bright white bag, 2 muted yellow bags.")
    assert graph.get_contents("light red") == {"bright white": 1, "muted yellow": 2}
    graph.parse_link("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
    assert graph.get_contents("dark orange") == {"bright white": 3, "muted yellow": 4}
    graph.parse_link("bright white bags contain 1 shiny gold bag.")
    assert graph.get_contents("bright white") == {"shiny gold": 1}
    assert graph.get_contents("dark orange") == {"bright white": 3, "muted yellow": 4, "shiny gold": 3}
    graph.parse_link("shiny gold bags contain no other bags.")
    assert graph.get_contents("bright white") == {"shiny gold": 1}
    assert graph.get_contents("dark orange") == {"bright white": 3, "muted yellow": 4, "shiny gold": 3}


def test_file_parsing():
    graph = SackGraph.from_file("day7/test/test.txt")
    assert graph.get_contents("light red")["bright white"] == 1
    assert graph.get_contents("light red")["muted yellow"] == 2
    assert graph.get_contents("dark orange")["bright white"] == 3
    assert graph.get_contents("dark orange")["muted yellow"] == 4
    assert graph.get_contents("bright white")["shiny gold"] == 1
    assert graph.get_contents("muted yellow")["shiny gold"] == 2
    assert graph.get_contents("muted yellow")["faded blue"] == 9
    assert graph.get_contents("shiny gold")["dark olive"] == 1
    assert graph.get_contents("shiny gold")["vibrant plum"] == 2
    assert graph.get_contents("dark olive")["faded blue"] == 3
    assert graph.get_contents("dark olive")["dotted black"] == 4
    assert graph.get_contents("vibrant plum")["faded blue"] == 5
    assert graph.get_contents("vibrant plum")["dotted black"] == 6
    assert graph.get_contents("faded blue") == {}
    assert graph.get_contents("dotted black") == {}


def test_possible_outer_bags():
    graph = SackGraph.from_file("day7/test/test.txt")
    assert graph.possible_outer_bags("dark orange") == set()
    assert graph.possible_outer_bags("light red") == set()
    assert graph.possible_outer_bags("bright white") == {"dark orange", "light red"}
    assert graph.possible_outer_bags("muted yellow") == {"dark orange", "light red"}
    assert graph.possible_outer_bags("shiny gold") == {"dark orange", "light red", "bright white", "muted yellow"}


def test_content_count():
    graph = SackGraph.from_file("day7/test/content_count_test.txt")
    assert graph.get_content_count("shiny gold") == 126

    graph2 = SackGraph.from_file("day7/test/test.txt")
    assert graph2.get_content_count("dark olive") == 7
    assert graph2.get_content_count("vibrant plum") == 11
    assert graph2.get_content_count("shiny gold") == 32

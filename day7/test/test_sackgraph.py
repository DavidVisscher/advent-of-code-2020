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

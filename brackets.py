from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Generator

from enum import Enum


class Bracket(Enum):

    ROUND_OPEN          = '('
    ROUND_CLOSE         = ')'
    SQUARE_OPEN         = '['
    SQUARE_CLOSE        = ']'
    FIGURE_OPEN         = '{'
    FIGURE_CLOSE        = '}'
    SINGLE_QUOTE_OPEN   = '\''
    SINGLE_QUOTE_CLOSE  = '\''
    DOUBLE_QUOTE_OPEN   = '\"'
    DOUBLE_QUOTE_CLOSE  = '\"'
    CORNER_OPEN         = '<'
    CORNER_CLOSE        = '>'


class BracketTreeNode(ABC):

    open_bracket:   str
    close_bracket:  str
    nested_nodes: List[BracketTreeNode]

    def __init__(self):
      self.nested_nodes = []


class BracketParser:

    def parse(source_string: str) -> Generator[BracketTreeNode]:
        yield []


class BracketTree:
    _tree: List[BracketTreeNode]

    def parse_from_string(self, source_string: str, parser: BracketParser):
        self._tree = []
        next_node = parser().parse(source_string)

    def clear(self):
        self._tree = []

    def validate(self):
        ...


class RoundBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.ROUND_OPEN
    close_bracket   = Bracket.ROUND_CLOSE


class SquareBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.SQUARE_OPEN
    close_bracket   = Bracket.SQUARE_CLOSE


class FigureBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.FIGURE_OPEN
    close_bracket   = Bracket.FIGURE_CLOSE


class SingleQuoteBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.SINGLE_QUOTE_OPEN
    close_bracket   = Bracket.SINGLE_QUOTE_CLOSE


class DoubleQuoteBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.DOUBLE_QUOTE_OPEN
    close_bracket   = Bracket.DOUBLE_QUOTE_CLOSE


class CornerBracketTreeNode(BracketTreeNode):
    open_bracket    = Bracket.CORNER_OPEN
    close_bracket   = Bracket.CORNER_CLOSE


class BracketTreeNodeFactory:

    @classmethod
    def create(cls, open_bracket: str):
        bracket_classes = {
            Bracket.ROUND_OPEN:         RoundBracketTreeNode,
            Bracket.SQUARE_OPEN:        SquareBracketTreeNode,
            Bracket.FIGURE_OPEN:        FigureBracketTreeNode,
            Bracket.SINGLE_QUOTE_OPEN:  SingleQuoteBracketTreeNode,
            Bracket.DOUBLE_QUOTE_OPEN:  DoubleQuoteBracketTreeNode,
            Bracket.CORNER_OPEN:        CornerBracketTreeNode,
        }

        return bracket_classes[open_bracket]()


class BracketTreePrinter:

    @classmethod
    def print(tree: BracketTree):
        ...
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BracketTreeNode(ABC):
    
    open_bracket:   str
    close_bracket:  str
    nested_nodes: List[BracketTreeNode]

    def __init__(self):
      self.nested_nodes = []


class BracketParser:

    def parse(source_string: str) -> List[BracketTreeNode]:
        return []


class BracketTree:
    _tree: List[BracketTreeNode]

    def parse_from_string(self, source_string: str, parser: BracketParser):
        self._tree = parser().parse(source_string)

    def clear(self):
        self._tree = []

    def validate(self):
        ...


class RoundBracketTreeNode(BracketTreeNode):
    open_bracket    = '('
    close_bracket   = ')'


class SquareBracketTreeNode(BracketTreeNode):
    open_bracket    = '['
    close_bracket   = ']'


class FigureBracketTreeNode(BracketTreeNode):
    open_bracket    = '{'
    close_bracket   = '}'


class SingleQuoteBracketTreeNode(BracketTreeNode):
    open_bracket    = '\''
    close_bracket   = '\''


class DoubleQuoteBracketTreeNode(BracketTreeNode):
    open_bracket    = '\"'
    close_bracket   = '\"'


class CornerBracketTreeNode(BracketTreeNode):
    open_bracket    = '<'
    close_bracket   = '>'



# class BracketTreeNode, BracketTreeNodeFactory, 
# BracketParser - should use generator with yeld symbol
# BracketTreePrinter
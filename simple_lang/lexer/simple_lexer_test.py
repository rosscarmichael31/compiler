import unittest

from ply.lex import LexToken

import simple_lexer


def _token(value):
    token = LexToken()
    token.value = value


class MyTestCase(unittest.TestCase):

    def _num_token(self, value):
        pass

    def test_lex(self):
        tokens = simple_lexer.lex_string("if 3=3    then  print 1=0 else begin print 1=1 end")
        self.assertEqual([t.type for t in tokens], [
            "IF",
            "NUM",
            "EQUALS",
            "NUM",
            "THEN",
            "PRINT",
            "NUM",
            "EQUALS",
            "NUM",
            "ELSE",
            "BEGIN",
            "PRINT",
            "NUM",
            "EQUALS",
            "NUM",
            "END",
        ])


if __name__ == '__main__':
    unittest.main()

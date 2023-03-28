import unittest

from simple_lang.parser import simple_parser
from simple_lang.ast.e import E
from simple_lang.ast.if_node import If
from simple_lang.ast.num import Num
from simple_lang.ast.print import Print


class MyTestCase(unittest.TestCase):
    class MyTestCase(unittest.TestCase):
        def test_parse(self):
            ast = simple_parser.parse("""
                        if 3=3    
                        then
                            begin
                                print 1=0
                            end 
                        else 
                            begin 
                                print 1=1 
                            end
                    """)
            self.assertEqual(ast, If(E(Num(3), Num(3)), [Print(E(Num(1), Num(0)))], [Print(E(Num(1), Num(1)))]))


if __name__ == '__main__':
    unittest.main()

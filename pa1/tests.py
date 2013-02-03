from fsm_lexer import lex, tokenize_ignore
from fsm_parser import parse
from fsm import fsm
import pa1
import unittest

class TestFSM(unittest.TestCase):

    def test_simple(self):
        string = 'a'
        start_state = 'A'
        transitions = {
            'A': (('a', 'W'),),
            'W': ()
        }
        final_states = ('W')
        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

    def test_empty(self):
        string = ''
        start_state = 'A'
        transitions = {
            'A': (('a', 'W'),),
            'W': ()
        }
        final_states = ('A')
        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

    def test_not_accepted(self):
        string = 'a'
        start_state = 'A'
        transitions = {
            'A': (('a', 'W'),),
            'W': ()
        }
        final_states = ('A')        
        result = fsm(string, start_state, transitions, final_states)
        self.assertFalse(result)

    def test_multiple_transitions_to_state(self):
        string = 'b'
        start_state = 'A'
        transitions = {
            'A': ((r"[ab]", 'W'),),
            'W': ()
        }
        final_states = ('W')
        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)


    def test_multiple_final_states(self):
        string = 'b'
        start_state = 'A'
        transitions = {
            'A': ((r"[ab]", 'W'),),
            'W': ()
        }
        final_states = ('A', 'W')
        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

    def test_pa1_4a(self):
        string = '10101010'
        string2 = '10'
        fail_string = '00101010'
        fail_string2 = '11'

        start_state = 'A'
        transitions = {
            'A': (
                ('0', 'D'),
                ('1', 'B'),
            ),
            'D': (
                (r"[01]", 'D'),
            ),
            'B': (
                ('0', 'C'),
                ('1', 'B'),
            ),
            'C': (
                ('0', 'C'),
                ('1', 'B'),
            )       
        }
        
        final_states = ('C')
        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(string2, start_state, transitions, final_states)
        self.assertTrue(result) 

        result = fsm(fail_string, start_state, transitions, final_states)
        self.assertFalse(result)        

        result = fsm(fail_string2, start_state, transitions, final_states)
        self.assertFalse(result)

    def test_pa1_4b(self):
        string = '00010001000110'
        fail_string = '000100010000'

        start_state = 'A'
        transitions = {
            'A': (
                ('0', 'A'),
                ('1', 'B'),
            ),
            'B': (
                ('0', 'B'),
                ('1', 'C'),
            ),
            'C': (
                ('0', 'C'),
                ('1', 'D'),
            ),
            'D': (
                ('0', 'D'),
                ('1', 'D'),
            )       
        }
        final_states = ('D')

        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(fail_string, start_state, transitions, final_states)
        self.assertFalse(result)

    def test_pa1_4c(self):
        string = '00101'
        string2 = ''
        fail_string = '110111'

        start_state = 'A'

        transitions = {
            'A': (
                (r"[01]", 'B'),
            ),
            'B': (
                (r"[01]", 'C'),
            ),
            'C': (
                (r"[01]", 'D'),
            ),
            'D': (
                (r"[01]", 'E'),
            ),
            'E': (
                (r"[01]", 'F'),
            ),
            'F': (
                (r"[01]", 'G'),
            ),
            'G': (
                (r"[01]", 'G'),
            ),                                                                      
        }

        final_states = ('A', 'B', 'C', 'D', 'E', 'F')

        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(string2, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(fail_string, start_state, transitions, final_states)
        self.assertFalse(result)        

    def test_pa1_4d(self):
        string = '0101100'
        string2 = '110'
        fail_string = ''
        fail_string2 = '0010'

        start_state = 'A'

        transitions = {
            'A': (
                (r"[01]", 'B'),
            ),
            'B': (
                (r"[01]", 'C'),
            ),
            'C': (
                ('0', 'D'),
                ('1', 'E')
            ),
            'D': (
                (r"[01]", 'D'),
            ),
            'E': (
                (r"[01]", 'E'),
            ),                                                                  
        }

        final_states = ('D')

        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(string2, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(fail_string, start_state, transitions, final_states)
        self.assertFalse(result)

        result = fsm(fail_string2, start_state, transitions, final_states)
        self.assertFalse(result)

    def test_pa1_4e(self):
        string = '00111'
        string2 = '0010010011'
        fail_string = '110'
        fail_string2 = '0001110000'

        start_state = 'A'

        transitions = {
            'A': (
                ('0', 'A'),
                ('1', 'B'),
            ),
            'B': (
                ('0', 'A'),
                ('1', 'C')
            ),
            'C': (
                ('0', 'D'),
                ('1', 'C')
            ),
            'D': (
                (r"[01]", 'D'),
            ),                                                              
        }

        final_states = ('C')

        result = fsm(string, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(string2, start_state, transitions, final_states)
        self.assertTrue(result)

        result = fsm(fail_string, start_state, transitions, final_states)
        self.assertFalse(result)

        result = fsm(fail_string2, start_state, transitions, final_states)
        self.assertFalse(result)

class TestFSMLexer(unittest.TestCase):

    def test_basic(self):
        string = 'test 11a 110 test 111'

        start_state = 'A'

        tokenize_events = {
            'B': tokenize_ignore
        }

        transitions = {
            'A': (
                (r'[^01 ]', 'H'),
                (' ', 'B'),
                ('0', 'C'),
                ('1', 'G'),
            ),
            'B': (
                (' ', 'B'),
            ),
            'C': (
                (r'[^01 ]', 'H'),       
                ('0', 'C'),
                ('1', 'D'),

            ),
            'D': (
                (r'[^01 ]', 'H'),                   
                ('0', 'C'),
                ('1', 'E'),
            ),
            'E': (
                (r'[^01 ]', 'H'),                       
                ('0', 'F'),
                ('1', 'E'),
            ),
            'F': (
                (r'[^01 ]', 'H'),                   
                (r"01", 'F'),
            ),
            'G': (
                (r'[^01 ]', 'H'),       
                ('0', 'C'),
                ('1', 'E')
            ),
            'H': (
                (r'[^ ]', 'H'),
            ),                                                              
        }

        final_states = ('B', 'E')

        result = (('ERROR', 'test'), ('ERROR', '11a'), ('ERROR', '110'), ('ERROR', 'test'), ('E', '111'))

        tokens = lex(string, start_state, transitions, final_states, tokenize_events)
        self.assertEqual(tokens, result)


class TestFSMParser(unittest.TestCase):
    
    def test_simple(self):
        tokens = (
            ('OPEN_PAREN', '('),
            ('INT', '3'),
            ('CLOSE_PAREN', ')'),
        )

        start_state = 'A'

        transitions = {
            'A': (
                ('OPEN_PAREN', 'B'),
            ),
            'B': (
                ('INT', 'C'),
            ),
            'C': (
                ('CLOSE_PAREN', 'D'),
            ),
            'D': (),                         
        }

        final_states = ('D')

        result = parse(tokens, start_state, transitions, final_states)
        self.assertEqual(result, ('(3)',))

class TestTimeParserAutomaton(unittest.TestCase):

    def test_lexer_not_token(self):
        string = 'test 12:2a'
        tokens = lex(string, pa1.lexer_q0, pa1.lexer_transitions, pa1.lexer_F, pa1.tokenize_events)
        self.assertEqual(tokens, (('NOT_TOKEN', 'test'), ('NOT_TOKEN', '12:2a')))

    def test_lexer_12_hour(self):
        string = '11:00 12:00am 12:00 AM 24:00 08:22 PM.'
        tokens = lex(string, pa1.lexer_q0, pa1.lexer_transitions, pa1.lexer_F, pa1.tokenize_events)
        result = (
            ('12HOUR_TIME', '11:00'), 
            ('NOT_TOKEN', '12:00am'),
            ('12HOUR_TIME', '12:00'),
            ('AM_PM', ' AM'),
            ('NOT_TOKEN', '24:00'),
            ('12HOUR_TIME', '08:22'),
            ('AM_PM', ' PM'),                        
        )
        self.assertEqual(tokens, result)

    def test_lexer_24_hour(self):
        string = '0000 at 2400 1233 1260'
        tokens = lex(string, pa1.lexer_q0, pa1.lexer_transitions, pa1.lexer_F, pa1.tokenize_events)
        result = (
            ('24HOUR_TIME', '0000'), 
            ('AT', ''),
            ('NOT_TOKEN', '2400'),
            ('24HOUR_TIME', '1233'),
            ('NOT_TOKEN', '1260'),                       
        )
        self.assertEqual(tokens, result)

    def test_lexer_informal_dash(self):
        string = '1. to - 24. 13; 11'
        tokens = lex(string, pa1.lexer_q0, pa1.lexer_transitions, pa1.lexer_F, pa1.tokenize_events)
        result = (
            ('INFORMAL_TIME', '1'),
            ('TO', ' to '), 
            ('DASH', '-'),
            ('NOT_TOKEN', '24'),
            ('NOT_TOKEN', '13'),
            ('INFORMAL_TIME', '11'),                       
        )
        self.assertEqual(tokens, result)

    def test_parser_empty(self):
        tokens = (
            ('NOT_TOKEN', 'dsfsf'),
            ('TO', ' to '),
            ('AM_PM', ' PM'),                                    
        )
        result = ()        
        stmts = parse(tokens, pa1.parser_q0, pa1.parser_transitions, pa1.parser_F)
        self.assertEqual(stmts, result)

    def test_parser_informal_time(self):
        tokens = (
            ('INFORMAL_TIME', '1'),
            ('TO', ' to '), 
            ('NOT_TOKEN', 'dsfsf'),
            ('INFORMAL_TIME', '12'),
            ('DASH', '-'),
            ('INFORMAL_TIME', '11'),
            ('INFORMAL_TIME', '8'),
            ('TO', ' to '),
            ('INFORMAL_TIME', '11'),
            ('AM_PM', ' PM'),                                    
        )
        result = (
            '12-11',
            '8 to 11 PM',
        )        
        stmts = parse(tokens, pa1.parser_q0, pa1.parser_transitions, pa1.parser_F)
        self.assertEqual(stmts, result)

    def test_parser_24_hour(self):
        tokens = (
            ('24HOUR_TIME', '2322'),
            ('TO', ' to '), 
            ('NOT_TOKEN', 'dsfsf'),
            ('24HOUR_TIME', '2300'),
            ('AT', ''),
            ('24HOUR_TIME', '1133'),
            ('24HOUR_TIME', '0028'),
            ('TO', ' to '),
            ('24HOUR_TIME', '1100'),
            ('AM_PM', ' PM'),                                    
        )
        result = (
            '1133',
            '0028 to 1100',
        )        
        stmts = parse(tokens, pa1.parser_q0, pa1.parser_transitions, pa1.parser_F)
        self.assertEqual(stmts, result)

    def test_parser_12_hour(self):
        tokens = (
            ('12HOUR_TIME', '12:22'),
            ('TO', ' to '), 
            ('24HOUR_TIME', '2300'),
            ('12HOUR_TIME', '12:00'),
            ('AM_PM', ' PM'),            
            ('DASH', '-'),
            ('12HOUR_TIME', '1:12'),
            ('TO', ' to '),                                
        )
        result = (
            '12:22',
            '12:00 PM',
            '1:12',
        )        
        stmts = parse(tokens, pa1.parser_q0, pa1.parser_transitions, pa1.parser_F)
        self.assertEqual(stmts, result)

    def test_parser_backtracking(self):
        tokens = (
            ('24HOUR_TIME', '2322'),
            ('TO', ' to '), 
            ('12HOUR_TIME', '11:00'), 
            ('AT', ''), 
            ('12HOUR_TIME', '11:00'),                                                      
        )
        result = (
            '11:00',
            '11:00',
        )        
        stmts = parse(tokens, pa1.parser_q0, pa1.parser_transitions, pa1.parser_F)
        self.assertEqual(stmts, result)
                                             
if __name__ == '__main__':
    unittest.main()
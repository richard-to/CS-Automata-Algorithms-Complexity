from fsm_lexer import lex, tokenize_ignore
from fsm_parser import parse

"""
Time Parser Automaton DFA 5-tuple
---------------------------------

Q = { A, NOT_TOKEN, SPACE, DASH, PUNCTUATION, B, AT, C, AM_PM, D, INFORMAL_TIME_1, INFORMAL_TIME_2,
    E, INFORMAL_TIME_10_12, G, H, I, 24HOUR_TIME, 12HOUR_TIME }

sigma = Set of all ascii characters not including newline and carriage return.

delta = See variable named transitions

q0 = A

F = {SPACE, DASH, PUNCTUATION, AT, AM_PM, INFORMAL_TIME_1, INFORMAL_TIME_2, INFORMAL_TIME_3_9, 
    INFORMAL_TIME_10_12, 24HOUR_TIME, 12HOUR_TIME}


Lexer Result
------------

(('NOT_TOKEN', '"Hello'), ('NOT_TOKEN', 'Myra'), ('NOT_TOKEN', 'the'), ('NOT_TOKEN', 'meeting'), 
('NOT_TOKEN', 'is'), ('NOT_TOKEN', 'on'), ('NOT_TOKEN', '2/5'), ('NOT_TOKEN', 'in'), 
('NOT_TOKEN', 'room'), ('24HOUR_TIME', '1300'), ('NOT_TOKEN', 'It'), ('NOT_TOKEN', 'will'), 
('NOT_TOKEN', 'last'), ('NOT_TOKEN', 'from'), ('INFORMAL_TIME', '1'), ('DASH', '-'), 
('INFORMAL_TIME', '2'), ('AM_PM', 'PM'), ('NOT_TOKEN', 'There'), ('NOT_TOKEN', 'will'), 
('NOT_TOKEN', 'be'), ('NOT_TOKEN', 'a'), ('NOT_TOKEN', 'sumptuous'), ('NOT_TOKEN', 'banquet'), 
('NOT_TOKEN', 'afterward'), ('AT', 'at'), ('24HOUR_TIME', '1800'), ('NOT_TOKEN', 'hours'), 
('NOT_TOKEN', 'The'), ('NOT_TOKEN', 'address'), ('NOT_TOKEN', 'is'), ('24HOUR_TIME', '2300'), 
('NOT_TOKEN', 'Sycamore'), ('NOT_TOKEN', 'Lane'), ('NOT_TOKEN', 'Please'), ('NOT_TOKEN', 'RSVP'), 
('NOT_TOKEN', 'by'), ('12HOUR_TIME', '5:30'), ('AM_PM', 'PM'), ('NOT_TOKEN', 'on'), 
('NOT_TOKEN', 'February'), ('INFORMAL_TIME', '1'), ('AT', 'at'), ('NOT_TOKEN', '786'), ('DASH', '-'), 
('NOT_TOKEN', '4819'), ('NOT_TOKEN', 'You'), ('NOT_TOKEN', 'can'), ('NOT_TOKEN', 'check'), 
('NOT_TOKEN', 'out'), ('NOT_TOKEN', 'our'), ('NOT_TOKEN', 'new'), ('NOT_TOKEN', 'wide'), 
('NOT_TOKEN', 'screen'), ('NOT_TOKEN', 'set'), ('NOT_TOKEN', 'with'), ('NOT_TOKEN', 'the'), 
('NOT_TOKEN', '16:9'), ('NOT_TOKEN', 'aspect'), ('NOT_TOKEN', 'ratio'), ('NOT_TOKEN', '"'))


Parser Result
-------------
['1-2 PM', '1800', '5:30 PM']

"""

string = '"Hello Myra, the meeting is on 2/5 in room 1300. It will last from 1-2 PM. There will be a sumptuous banquet afterward at 1800 hours. The address is 2300 Sycamore Lane. Please RSVP by 5:30 PM on February 1 at 786-4819. You can check out our new wide screen set with the 16:9 aspect ratio!"'

lexer_q0 = 'A'

lexer_transitions = {
    'A': (
        (r'[^\-\.\?!,; aAPt0-9]', 'NOT_TOKEN'),
        (r'[\.\?!,;]', 'PUNCTUATION'),
        (' ', 'SPACE'),
        ('-', 'DASH'),
        ('a', 'B'),
        (r'[AP]', 'C'),
        ('t', 'J'),
        ('0', 'D'),
        ('1', 'INFORMAL_TIME_1'),
        ('2', 'INFORMAL_TIME_2'),
        (r'[3-9]', 'INFORMAL_TIME_3_9'),                
    ),
    'NOT_TOKEN': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),
    'SPACE': (
        (' ', 'SPACE'),
    ),
    'DASH': (),
    'PUNCTUATION': (),
    'B': (
        (r'[^t\-\.\?!,; ]', 'NOT_TOKEN'),
        ('t', 'AT'),
    ),
    'AT': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),
    'C': (
        (r'[^M\-\.\?!,; ]', 'NOT_TOKEN'),        
        ('M', 'AM_PM'),
    ),
    'AM_PM': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),
    'D': (
        (r'[^[0-9]\-\.\?!,; ]', 'NOT_TOKEN'),
        ('0', 'F'),
        (r'[1-9]', 'E'),
    ),
    'INFORMAL_TIME_1': (
        (r'[^0-9:\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-2]', 'INFORMAL_TIME_10_12'),
        (r'[3-9]', 'F'),
        (':', 'H'),        
    ),    
    'INFORMAL_TIME_2': (
        (r'[^0-3:\-\.\?!,; ]', 'NOT_TOKEN'),
        (':', 'H'),
        (r'[0-3]', 'F'),        
    ),
    'INFORMAL_TIME_3_9': (
        (r'[^:\-\.\?!,; ]', 'NOT_TOKEN'),
        (':', 'H'),
    ),           
    'E': (
        (r'[^0-5:\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-5]', 'G'),
        (':', 'H'),
    ),
    'F': (
        (r'[^0-5\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-5]', 'G'),
    ),
    'INFORMAL_TIME_10_12': (
        (r'[^0-5:\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-5]', 'G'),
        (':', 'H'),
    ),
    'G': (
        (r'[^0-9\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-9]', '24HOUR_TIME'),
    ),
    'H': (
        (r'[^0-5\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-5]', 'I'),
    ),
    'I': (
        (r'[^0-9\-\.\?!,; ]', 'NOT_TOKEN'),
        (r'[0-9]', '12HOUR_TIME'),
    ),        
    '24HOUR_TIME': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),     
    '12HOUR_TIME': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),
    'J': (
        (r'[^o\-\.\?!,; ]', 'NOT_TOKEN'),        
        ('o', 'TO'),
    ),
    'TO': (
        (r'[^\-\.\?!,; ]', 'NOT_TOKEN'),
    ),                
}

lexer_F = ('SPACE', 'DASH', 'TO', 'PUNCTUATION', 'AT', 'AM_PM', 'INFORMAL_TIME_1', 'INFORMAL_TIME_2', 'INFORMAL_TIME_3_9', 
    'INFORMAL_TIME_10_12', '24HOUR_TIME', '12HOUR_TIME')

def tokenize_leftpad(token):
    return (token[0], ''.join([' ', token[1]]))

def tokenize_pad(token):
    return (token[0], ''.join([' ', token[1], ' ']))

def tokenize_remove(token):
    return (token[0], '')

def tokenize_informal_time(token):
    return ('INFORMAL_TIME', token[1])

def tokenize_rename_error(token):
    return ('NOT_TOKEN', token[1])
    
tokenize_events = {
    'SPACE': tokenize_ignore,
    'PUNCTUATION': tokenize_ignore,
    'ERROR': tokenize_rename_error,
    'INFORMAL_TIME_1': tokenize_informal_time,
    'INFORMAL_TIME_2': tokenize_informal_time, 
    'INFORMAL_TIME_3_9': tokenize_informal_time, 
    'INFORMAL_TIME_10_12': tokenize_informal_time,
    'AT': tokenize_remove,
    'TO': tokenize_pad,
    'AM_PM': tokenize_leftpad,              
}

tokens = lex(string, lexer_q0, lexer_transitions, lexer_F, tokenize_events)

parser_q0 = 'A'

parser_transitions = {
    'A': (
        ('AT', 'B'),
        ('INFORMAL_TIME', 'F'),        
        ('12HOUR_TIME', 'J'),
        ('24HOUR_TIME', 'D'),
        (r'NOT_TOKEN|TO|DASH|AM_PM', 'E'),                              
    ),
    'B': (
        ('24HOUR_TIME', 'C'),                             
    ),
    'C': (),
    'D': (
        (r'TO|DASH', 'B'),
    ),                             
    'E': (),
    'F': (
        (r'TO|DASH', 'G'),
    ),
    'G': (
        ('INFORMAL_TIME', 'H'),
    ),
    'H': (
        ('AM_PM', 'I'),
    ),
    'I': (),
    'J': (
        ('AM_PM', 'I'),        
        (r'TO|DASH', 'K'),
    ), 
    'K': (
        ('12HOUR_TIME', 'L'),                             
    ),
    'L': (
        ('AM_PM', 'I'),
    ),                   
}

parser_F = ('C', 'H', 'I', 'J', 'L')

print parse(tokens, parser_q0, parser_transitions, parser_F)

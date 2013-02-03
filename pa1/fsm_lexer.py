import re

"""
Very simple lexer that breaks string into named tokens using a "DFA"

This is not a true DFA. A few adjustments have been made for tokenizing substrings correctly.

The main change is that not all "letters" in "alphabet" have a transition. The missing transitions 
signal the end of a token, whether in an accepted state or not. From there the DFA resumes from
the start state. Think of these as delimiters.

Any substring that ends in a non-accepting state is in an error state and will be stored as a 
token called "ERROR."

There is no backtracking implemented.

Uses maximal munch rule, so longest substring will be tokenized.

Note: Make sure that the start state of the DFA has transitions for all letters. If not there
will be an infinite loop.

Args:
    string: String to be broken into tokens
    state: State state
    transitions: See example transitions structure
    final_states: Accepting states
    tokenize_events: A dict of functions for specialized handling of a token

Returns:
    A tuple of tuples. Inner tuples contain two values. The name of the token and the value.

Example Usage:
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
    tokens = lex(string, start_state, dfa, final_states, tokenize_events)
"""
def lex(string, state, transitions, final_states, tokenize_events):
    meta = {
        'tokens': [],
        'current_token': [],
        'accepted_token': None,
        'start_state': state
    }
    result = fsm_lexer(string, state, transitions, final_states, meta)

    return tokenize(result['tokens'], tokenize_events)

"""
Helper for post processing of tokens.

Args:
    tokens: A list of (name, value) tokens
    tokenize_events: A dict of functions for specialized handling of tokens
Returns:
    A tuple of tuples. Inner tuples contain two values. The name of the token and the value.
"""
def tokenize(tokens, tokenize_events):
    new_tokens = []
    for token in tokens:
        state = token[0]
        if state in tokenize_events:
            result = tokenize_events[state](token)
            if result:
                new_tokens.append(result)
        else:
            new_tokens.append(token)

    return tuple(new_tokens)

"""
Commnon tokenize function that ignores a token and
thus prevents it from being added to list of tokens.

Can be used to ignore spaces and other punctuation.
"""
def tokenize_ignore(token):
    return

"""
A modified finite state machine that can parse substring tokens from a string.

Note: Make sure that the start state of the DFA has transitions for all letters. If not there
will be an infinite loop.

Args:
    string: String to be broken into tokens
    state: State state
    transitions: See example transitions structure
    final_states: Accepting states
    meta: Dict that keeps track of found tokens, start state, current substring, and current accepted_token   

Return:
    List of (name, value) tokens
"""
def fsm_lexer(string, state, transitions, final_states, meta):  

    if state in final_states:
        meta['accepted_token'] = (state, ''.join(meta['current_token']))
    else:
        meta['accepted_token'] = ("ERROR", ''.join(meta['current_token']))

    if len(string) == 0:
        if meta['accepted_token']:
            meta['tokens'].append(meta['accepted_token'])
        return meta

    state_transitions = transitions[state]
    next_state = None

    for state_transition in state_transitions:
        if re.match(state_transition[0], string[0]):
            next_state = state_transition[1]
            break

    if next_state:
        meta['current_token'].append(string[0])
        return fsm_lexer(string[1:], next_state, transitions, final_states, meta)
    else:
        if meta['accepted_token']:
            meta['tokens'].append(meta['accepted_token'])
        meta['current_token'] = []
        return fsm_lexer(string, meta['start_state'], transitions, final_states, meta)

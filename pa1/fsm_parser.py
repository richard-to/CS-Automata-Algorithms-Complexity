import re

"""
Simple parser that uses a DFA.

This method only works for very simple grammars.

Args:
    tokens: A tuple of (name, value) tuples that you would get from using my fsm_lexer module
    state: Start state
    transitions: See example for transition structure
    final_states: A tuple of accepting states

Return:
    A tuple of strings

Example:
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
"""
def parse(tokens, state, transitions, final_states):
    token_index = 0
    meta = {
        'stmts': [],
        'current_stmt': [],
        'accepted_stmt': None,
        'start_state': state
    }
    result = fsm_parser(tokens, token_index, state, transitions, final_states, meta)
    return tuple(result['stmts'])


"""
The fsm_parser is called by the parse function.

There are some differences between this function and the fsm_lexer.

The first difference is that a tuple of tokens is used instead of a string.
Instead of going character by character, we go token by token.

The other big difference is that fsm_parser will backtrack to the last accepted state 
if the parser errors out before reaching another accepted state.

Args:
    tokens: A tuple of (name, value) tuples that you would get from using my fsm_lexer module
    token_index: Current index position in tokens tuple
    state: Start state
    transitions: See example for transition structure
    final_states: A tuple of accepting states
    meta: A dictionary with the following keys: stmts, current_stmt, accepted_stmt, start_state
Return:
    A dictionary with the following keys: stmts, current_stmt, accepted_stmt, start_state.
    The key of interest is the stmts list.
"""
def fsm_parser(tokens, token_index, state, transitions, final_states, meta):  

    if state in final_states:
        meta['accepted_stmt'] = ''.join(meta['current_stmt'])

    if token_index >= len(tokens):
        if meta['accepted_stmt']:
            meta['stmts'].append(meta['accepted_stmt'])
        return meta

    state_transitions = transitions[state]
    next_state = None

    for state_transition in state_transitions:
        if re.match(state_transition[0], tokens[token_index][0]):
            next_state = state_transition[1]
            break

    if next_state:
        meta['current_stmt'].append(tokens[token_index][1])
        token_index += 1
        return fsm_parser(tokens, token_index, next_state, transitions, final_states, meta)
    else:
        if meta['accepted_stmt']:
            meta['stmts'].append(meta['accepted_stmt'])
        meta['accepted_stmt'] = None            
        meta['current_stmt'] = []
        return fsm_parser(tokens, token_index, meta['start_state'], transitions, final_states, meta)

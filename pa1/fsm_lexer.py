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

Args:
    string: String to be broken into tokens
    state: State state
    dfa: See example DFA structure
    final_states: Accepting states
    tokenize_events: A dict of functions for specialized handling of a token
Returns:
    A tuple of tuples. Inner tuples contain two values. The name of the token and the value.
"""
def lex(string, state, dfa, final_states, tokenize_events):
    meta = {
        'tokens': [],
        'current_token': [],
        'accepted_token': None,
        'start_state': state
    }
    result = fsm_lexer(string, state, dfa, final_states, meta)

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

Args:
    string: String to be broken into tokens
    state: State state
    dfa: See example DFA structure
    final_states: Accepting states
    meta: Dict that keeps track of found tokens, start state, current substring, and current accepted_token   

Return:
    List of (name, value) tokens
"""
def fsm_lexer(string, state, dfa, final_states, meta):  

    if state in final_states:
        meta['accepted_token'] = (state, ''.join(meta['current_token']))
    else:
        meta['accepted_token'] = ("ERROR", ''.join(meta['current_token']))

    if len(string) == 0:
        if meta['accepted_token']:
            meta['tokens'].append(meta['accepted_token'])
        return meta

    transitions = dfa[state]
    next_state = None

    for transition in transitions:
        if re.match(transition[0], string[0]):
            next_state = transition[1]
            break

    if next_state:
        meta['current_token'].append(string[0])
        return fsm_lexer(string[1:], next_state, dfa, final_states, meta)
    else:
        if meta['accepted_token']:
            meta['tokens'].append(meta['accepted_token'])
        meta['current_token'] = []
        return fsm_lexer(string, meta['start_state'], dfa, final_states, meta)

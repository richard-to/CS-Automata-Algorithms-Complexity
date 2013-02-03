import re

"""
Finite state machine implementation for DFA's.

This FSM cheats a bit in that error states are implicit. This 
means that if a transition is not in the state, then this is counted
as an error state.

Args:
    string: A string to check as valid for a given DFA
    state: The starting state for the given DFA
    transitions: See examples for transitions structure
    final_states: A tuple of accepting states

Returns:
    True if the string is a valid for the given DFA.
    False if the string is invalid.

Example Usage:
    
    string = '00111'

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
"""
def fsm(string, state, transitions, final_states):  
    if len(string) == 0:
        return state in final_states

    state_transitions = transitions[state]
    next_state = None

    for state_transition in state_transitions:
        if re.match(state_transition[0], string[0]):
            next_state = state_transition[1]

    if next_state:
        return fsm(string[1:], next_state, transitions, final_states)
    else:
        return False
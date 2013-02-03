import re

def parse(tokens, state, transitions, final_states):
    token_index = 0
    meta = {
        'stmts': [],
        'current_stmt': [],
        'accepted_stmt': None,
        'start_state': state
    }
    result = fsm_parser(tokens, token_index, state, transitions, final_states, meta)
    return result['stmts']

def fsm_parser(tokens, token_index, state, transitions, final_states, meta):  

    if state in final_states:
        meta['accepted_stmt'] = ''.join(meta['current_stmt'])
    else:
        meta['accepted_stmt'] = None

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
        meta['current_stmt'] = []
        return fsm_parser(tokens, token_index, meta['start_state'], transitions, final_states, meta)

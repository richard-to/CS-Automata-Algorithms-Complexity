def fsm(string, state, dfa, final_states):	
	if len(string) == 0:
		return state in final_states

	transitions = dfa[state]
	next_state = None

	for transition in transitions:
		if isinstance(transition[0], str):
			if transition[0] == string[0]:
				next_state = transition[1]
				break
		else:
			for transition_path in transition[0]:
				if transition_path == string[0]:
					next_state = transition[1]
					break

	if next_state:
		return fsm(string[1:], next_state, dfa, final_states)
	else:
		return False
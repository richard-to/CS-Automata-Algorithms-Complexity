from fsm import fsm
import unittest

class TestFSM(unittest.TestCase):

	def test_simple(self):
		string = 'a'
		start_state = 'A'
		dfa = {
			'A': (('a', 'W'),),
			'W': ()
		}
		final_states = ('W')
		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

	def test_empty(self):
		string = ''
		start_state = 'A'
		dfa = {
			'A': (('a', 'W'),),
			'W': ()
		}
		final_states = ('A')
		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

	def test_not_accepted(self):
		string = 'a'
		start_state = 'A'
		dfa = {
			'A': (('a', 'W'),),
			'W': ()
		}
		final_states = ('A')		
		result = fsm(string, start_state, dfa, final_states)
		self.assertFalse(result)

	def test_multiple_transitions_to_state(self):
		string = 'b'
		start_state = 'A'
		dfa = {
			'A': ((('a', 'b'), 'W'),),
			'W': ()
		}
		final_states = ('W')
		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)
				
if __name__ == '__main__':
    unittest.main()
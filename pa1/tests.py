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


	def test_multiple_final_states(self):
		string = 'b'
		start_state = 'A'
		dfa = {
			'A': ((('a', 'b'), 'W'),),
			'W': ()
		}
		final_states = ('A', 'W')
		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

	def test_pa1_4a(self):
		string = '10101010'
		string2 = '10'
		fail_string = '00101010'
		fail_string2 = '11'

		start_state = 'A'
		dfa = {
			'A': (
				('0', 'D'),
				('1', 'B'),
			),
			'D': (
				(('0', '1'), 'D'),
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
		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(string2, start_state, dfa, final_states)
		self.assertTrue(result)	

		result = fsm(fail_string, start_state, dfa, final_states)
		self.assertFalse(result)		

		result = fsm(fail_string2, start_state, dfa, final_states)
		self.assertFalse(result)

	def test_pa1_4b(self):
		string = '00010001000110'
		fail_string = '000100010000'

		start_state = 'A'
		dfa = {
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

		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(fail_string, start_state, dfa, final_states)
		self.assertFalse(result)

	def test_pa1_4c(self):
		string = '00101'
		string2 = ''
		fail_string = '110111'

		start_state = 'A'

		dfa = {
			'A': (
				(('0', '1'), 'B'),
			),
			'B': (
				(('0', '1'), 'C'),
			),
			'C': (
				(('0', '1'), 'D'),
			),
			'D': (
				(('0', '1'), 'E'),
			),
			'E': (
				(('0', '1'), 'F'),
			),
			'F': (
				(('0', '1'), 'G'),
			),
			'G': (
				(('0', '1'), 'G'),
			),																		
		}

		final_states = ('A', 'B', 'C', 'D', 'E', 'F')

		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(string2, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(fail_string, start_state, dfa, final_states)
		self.assertFalse(result)		

	def test_pa1_4d(self):
		string = '0101100'
		string2 = '110'
		fail_string = ''
		fail_string2 = '0010'

		start_state = 'A'

		dfa = {
			'A': (
				(('0', '1'), 'B'),
			),
			'B': (
				(('0', '1'), 'C'),
			),
			'C': (
				('0', 'D'),
				('1', 'E')
			),
			'D': (
				(('0', '1'), 'D'),
			),
			'E': (
				(('0', '1'), 'E'),
			),																	
		}

		final_states = ('D')

		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(string2, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(fail_string, start_state, dfa, final_states)
		self.assertFalse(result)

		result = fsm(fail_string2, start_state, dfa, final_states)
		self.assertFalse(result)

	def test_pa1_4e(self):
		string = '00111'
		string2 = '0010010011'
		fail_string = '110'
		fail_string2 = '0001110000'

		start_state = 'A'

		dfa = {
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
				(('0', '1'), 'D'),
			),																
		}

		final_states = ('C')

		result = fsm(string, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(string2, start_state, dfa, final_states)
		self.assertTrue(result)

		result = fsm(fail_string, start_state, dfa, final_states)
		self.assertFalse(result)

		result = fsm(fail_string2, start_state, dfa, final_states)
		self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
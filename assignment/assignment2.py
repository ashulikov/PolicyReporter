class FSM:
    def __init__(self, states, alphabet, start_state, final_states):
        self.__current_state = start_state
        self.__alphabet = alphabet
        self.__states = states
        self.transitions = {state: {} for state in states}
        self.__final_states = final_states

    def add_transition(self, from_state, symbol, to_state):
        """Adds a transition from one state to another."""
        if from_state not in self.__states or to_state not in self.__states or symbol not in self.__alphabet:
            raise ValueError("Wrong values")
        if from_state in self.transitions and symbol in self.transitions[from_state]:
            raise ValueError("Duplicate transition")
        self.transitions[from_state][symbol] = to_state
    
    def add_transitions(self, transitionList):
        """Adds multiple transitions from one state to another."""
        for transition in transitionList:
            if len(transition) != 3:
                raise ValueError("Wrong number of values for transition")
            self.add_transition(*transition)

    def transition(self, symbol):
        """Transitions to the next state based on the input symbol."""
        if self.__current_state in self.transitions and symbol in self.transitions[self.__current_state]:
            self.__current_state = self.transitions[self.__current_state][symbol]
        else:
            raise ValueError(f"Invalid transition from state {self.__current_state} with symbol {symbol}")

    def get_current_state(self):
        """Returns the current state of the FSM."""
        return self.__current_state
    
    def finalize(self):
        if self.__current_state not in self.__final_states:
            raise Exception("Machine error")
        return self.__current_state
    
class Modulo3:
    def __init__(self):
        self.FSM = FSM([0, 1, 2], ["0", "1"], 0, [0, 1, 2])
        self.FSM.add_transitions([[0, "0", 0],
                                  [0, "1", 1],
                                  [1, "0", 2],
                                  [1, "1", 0],
                                  [2, "0", 1],
                                  [2, "1", 2]])
        
    def calc(self, number: str):
        if not number:
            raise Exception("Empty number")
        for c in number:
            self.FSM.transition(c)
        return self.FSM.finalize()
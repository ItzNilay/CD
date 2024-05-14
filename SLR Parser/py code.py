class SLRParser:
    def __init__(self, grammar, terminals, nonterminals, start_symbol):
        self.grammar = grammar
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.start_symbol = start_symbol
        self.action_table = {}
        self.goto_table = {}

    def construct_parsing_tables(self):
        self._construct_lr0_items()
        self._construct_closures()
        self._construct_goto_table()
        self._construct_action_table()

    def _construct_lr0_items(self):
        # Initialize LR(0) items
        pass

    def _construct_closures(self):
        # Construct closures of LR(0) items
        pass

    def _construct_goto_table(self):
        # Construct GOTO table
        pass

    def _construct_action_table(self):
        # Construct ACTION table
        pass

    def parse(self, input_string):
        stack = [0]
        input_string += '$'
        input_index = 0

        while True:
            state = stack[-1]
            next_input = input_string[input_index]

            if next_input not in self.action_table[state]:
                print("Error: No action defined for state {} and input {}".format(state, next_input))
                return False

            action = self.action_table[state][next_input]

            if action[0] == 'S':
                stack.append(next_input)
                stack.append(action[1])
                input_index += 1
            elif action[0] == 'R':
                production = self.grammar[action[1]]
                for _ in range(len(production[1])):
                    stack.pop()
                    stack.pop()
                stack.append(production[0])
                stack.append(self.goto_table[stack[-2]][stack[-1]])
            elif action[0] == 'ACC':
                print("Input string accepted!")
                return True
            else:
                print("Error: Invalid action {}".format(action))
                return False

    # Other methods for constructing LR(0) items, closures, GOTO table, and ACTION table

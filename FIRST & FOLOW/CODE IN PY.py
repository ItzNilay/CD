# Function to compute First set
def compute_first(grammar, non_terminal, first_set):
    if non_terminal not in grammar:
        first_set.add(non_terminal)
        return
    for production in grammar[non_terminal]:
        first_symbol = production[0]
        if first_symbol.islower() or first_symbol not in grammar:
            first_set.add(first_symbol)
        else:
            compute_first(grammar, first_symbol, first_set)

# Function to compute Follow set
def compute_follow(grammar, non_terminal, follow_set, start_symbol):
    if non_terminal == start_symbol:
        follow_set.add('$')  # $ represents end of input
    for nt in grammar:
        for production in grammar[nt]:
            if non_terminal in production:
                index = production.index(non_terminal)
                if index < len(production) - 1:
                    next_symbol = production[index + 1]
                    if next_symbol.islower():
                        follow_set.add(next_symbol)
                    else:
                        first_of_next = set()
                        compute_first(grammar, next_symbol, first_of_next)
                        follow_set |= first_of_next - {'epsilon'}
                        if 'epsilon' in first_of_next:
                            follow_set |= compute_follow(grammar, nt, follow_set, start_symbol)
                elif index == len(production) - 1 and nt != non_terminal:
                    follow_set |= compute_follow(grammar, nt, follow_set, start_symbol)
    return follow_set

# Example grammar
grammar = {
    'S': ['AB', 'BC'],
    'A': ['aA', 'epsilon'],
    'B': ['bB', 'epsilon'],
    'C': ['c']
}

start_symbol = 'S'

# Compute First sets
first_sets = {}
for nt in grammar:
    first_sets[nt] = set()
    compute_first(grammar, nt, first_sets[nt])

print("First sets:")
for nt, first_set in first_sets.items():
    print(nt, ':', first_set)

# Compute Follow sets
follow_sets = {}
for nt in grammar:
    follow_sets[nt] = set()
    compute_follow(grammar, nt, follow_sets[nt], start_symbol)

print("\nFollow sets:")
for nt, follow_set in follow_sets.items():
    print(nt, ':', follow_set)

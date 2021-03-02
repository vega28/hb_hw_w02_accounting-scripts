"""Print out all the melons in our inventory."""


from melons import melons_info


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')

# structure per melon: 'melon_name' = {'price':, 'seedlessness':, 
#                       'flesh_color':, 'rind_color':, 'avg_weight':}

for melon in melons_info:
    print_melon(melon, 
        melons_info[melon]['seedlessness'], 
        melons_info[melon]['price'])

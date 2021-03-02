"""Print out all the melons in our inventory."""


from melons import melons_info


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon in melons:
        print('\n'+melon.upper())
        for attribute in melons[melon]:
            if attribute == 'price':
                print(f'    {attribute}: {melons[melon][attribute]:.2f}')
            else:
                print(f'    {attribute}: {melons[melon][attribute]}')


print_melons(melons_info)

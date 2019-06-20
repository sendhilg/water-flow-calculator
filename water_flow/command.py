from .flow import Flow


class Command(object):
    def __init__(self):
        self.flow = Flow()

    def parse(self):
        try:
            qty_poured = float(input('\nEnter water quantity poured in litres:\n'))
            query_row = int(input('\nEnter row number:\n'))
            query_glass = int(input('\nEnter glass number:\n'))
        except ValueError:
            print('\nError: Enter numeric values for qty, row number, glass number.')
        else:
            if query_glass > query_row:
                print('\nError: Glass number cannot be greater than row number.')
            else:
                qty = self.flow.calculate_quantity(qty_poured, query_row, query_glass)
                print(f'\nAmount of water in glass number {query_glass} of row number {query_row} is:\n{qty}')

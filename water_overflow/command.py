class InvalidInputError(Exception):
    pass

class Command(object):
    def parse(self):
        while True:
            try:
                qty_poured = int(input('\nEnter water quantity poured in litres:\n'))
                query_row = int(input('\nEnter row number:\n'))
                query_glass = int(input('\nEnter glass number:\n'))
                qty = self.find_water_qty(qty_poured, query_row, query_glass)
                print(
                    f'\nAmount of water in glass number {query_glass} '
                    f'of row number {query_row} is:\n{qty}')
            except ValueError:
                print(
                    '\nError: Enter numeric values for qty, '
                    'row number, glass number.'
                        )
                continue
            except InvalidInputError as e:
                print(f'\nError: {e}')
                continue

    def find_water_qty(self, qty_poured, query_row, query_glass):
        if (query_glass > query_row):
            raise InvalidInputError('Glass number cannot be greater than row number.')

        fill_array = [[0] * k for k in range(1, 5)]
        fill_array[0][0] = qty_poured
        for row in range(query_row + 1):
            for col in range(row+1):
                remaining_qty = (fill_array[row][col] - 0.25) / 2.0
                if remaining_qty > 0:
                    fill_array[row+1][col] += remaining_qty
                    fill_array[row+1][col+1] += remaining_qty

        return min(0.25, fill_array[query_row][query_glass])
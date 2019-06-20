class Flow(object):
    glass_capacity_in_ltrs = 0.25

    def calculate_quantity(self, qty_poured, query_row, query_glass):
        fill_array = [[0] * k for k in range(1, 6)]
        fill_array[0][0] = qty_poured
        for row in range(query_row+1):
            for col in range(row+1):
                remaining_qty = (fill_array[row][col] - self.glass_capacity_in_ltrs) / 2.0
                if remaining_qty > 0:
                    fill_array[row+1][col] += remaining_qty
                    fill_array[row+1][col+1] += remaining_qty

        value = min(self.glass_capacity_in_ltrs, fill_array[query_row][query_glass])
        return round(value, 4)

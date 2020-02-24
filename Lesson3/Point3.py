def sum_max_val(val_1, val_2, val_3):
    a, b = max(val_1, val_2), max(min(val_1, val_2), val_3)
    return a + b

print(sum_max_val(3, 8, 7))
degree = list(map(int, input().split(" ")))

valid_ = [c for c in degree if not c == -999]
kelvin_ = [c + 273 for c in valid_]
labels_ = ['H' if c >= 30 else 'O' if c > 0 else 'C' for c in valid_]
errors = len(degree) - len(valid_)
if all([v > 0 for v in valid_]):
    all_above_zero = "yes"
else:
    all_above_zero = "no"

valid = " ".join(list(map(str,valid_)))
kelvin = " ".join(list(map(str,kelvin_)))
labels = " ".join(list(map(str,labels_)))

print(f"valid: {valid}")
print(f"kelvin: {kelvin}")
print(f"labels: {labels}")
print(f"errors: {errors}")
print(f"all_above_zero: {all_above_zero}")
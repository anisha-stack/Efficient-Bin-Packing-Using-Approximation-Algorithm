# Bin Packing Approximation Algorithms
# 1. First Fit (FF)
# 2. First Fit Decreasing (FFD)
# 3. Best Fit Decreasing (BFD)


# -------------------------------
# First Fit (FF)
# -------------------------------
def first_fit(items, capacity):
    bins = []

    for item in items:
        placed = False

        # Try to place item in the first bin where it fits
        for i in range(len(bins)):
            if bins[i]["remaining"] >= item:
                bins[i]["items"].append(item)
                bins[i]["remaining"] -= item
                placed = True
                break

        # Create new bin if item cannot fit
        if not placed:
            bins.append({
                "items": [item],
                "remaining": capacity - item
            })

    return bins


# -------------------------------
# First Fit Decreasing (FFD)
# -------------------------------
def first_fit_decreasing(items, capacity):
    # Sort items in decreasing order
    items = sorted(items, reverse=True)

    return first_fit(items, capacity)


# -------------------------------
# Best Fit Decreasing (BFD)
# -------------------------------
def best_fit_decreasing(items, capacity):
    # Sort items in decreasing order
    items = sorted(items, reverse=True)

    bins = []

    for item in items:

        best_bin = -1
        min_remaining = capacity + 1

        # Find the bin with the smallest remaining space
        # after placing the item
        for i in range(len(bins)):
            if bins[i]["remaining"] >= item:
                remaining = bins[i]["remaining"] - item

                if remaining < min_remaining:
                    min_remaining = remaining
                    best_bin = i

        # Put item in the best-fitting bin
        if best_bin != -1:
            bins[best_bin]["items"].append(item)
            bins[best_bin]["remaining"] -= item

        # Otherwise create a new bin
        else:
            bins.append({
                "items": [item],
                "remaining": capacity - item
            })

    return bins


# -------------------------------
# Display Result
# -------------------------------
def display_result(name, bins, capacity):
    print("\n" + "=" * 40)
    print(name)
    print("=" * 40)

    for i, bin_data in enumerate(bins, 1):
        used = capacity - bin_data["remaining"]

        print(
            "Bin", i,
            ":", bin_data["items"],
            "| Used =", used,
            "| Remaining =", bin_data["remaining"]
        )

    print("Total bins used:", len(bins))


# -------------------------------
# Main Program
# -------------------------------
items = [10, 9, 8, 7, 6, 5, 4, 3, 2]
capacity = 15

print("Items:", items)
print("Bin Capacity:", capacity)


# First Fit
ff_bins = first_fit(items, capacity)
display_result("FIRST FIT (FF)", ff_bins, capacity)


# First Fit Decreasing
ffd_bins = first_fit_decreasing(items, capacity)
display_result("FIRST FIT DECREASING (FFD)", ffd_bins, capacity)


# Best Fit Decreasing
bfd_bins = best_fit_decreasing(items, capacity)
display_result("BEST FIT DECREASING (BFD)", bfd_bins, capacity)
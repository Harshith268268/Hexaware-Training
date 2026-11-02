"""
SET 3 - TASK 4: Find the 4-hour window with the highest average parcel count.
Run: python task4_sliding_window_delivery_counts.py
"""

def highest_average_window(counts, window_size=4):
    if window_size <= 0 or window_size > len(counts):
        raise ValueError("Window size must be between 1 and the number of counts.")

    # Sum the first window.
    current_sum = sum(counts[:window_size])
    best_sum = current_sum
    best_start = 0

    # Slide one position at a time: remove outgoing value, add incoming value.
    for end in range(window_size, len(counts)):
        current_sum += counts[end] - counts[end - window_size]
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = end - window_size + 1

    best_counts = counts[best_start:best_start + window_size]
    average = best_sum / window_size
    return best_start, best_counts, best_sum, average


def main():
    hourly_counts = [42, 48, 51, 60, 75, 80, 72, 68, 55, 50, 46, 40]
    window_size = 4

    start, values, total, average = highest_average_window(hourly_counts, window_size)

    print("SET 3 - TASK 4: PEAK 4-HOUR DELIVERY WINDOW")
    print("Hourly parcel counts:", hourly_counts)
    print(f"Window size: {window_size} hours")
    print(f"Best window: hours {start + 1} to {start + window_size}")
    print("Parcel counts in best window:", values)
    print("Total parcels:", total)
    print(f"Average parcels per hour: {average:.2f}")


if __name__ == "__main__":
    main()

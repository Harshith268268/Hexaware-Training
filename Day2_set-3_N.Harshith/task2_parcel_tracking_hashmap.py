"""
SET 3 - TASK 2: Parcel tracking lookup using a hash map.
Detects a parcel scanned more than once at the SAME hub.
Run: python task2_parcel_tracking_hashmap.py
"""

def process_scans(scan_events):
    # tracking number -> set of hubs where it has been scanned
    parcel_hubs = {}

    print("SET 3 - TASK 2: PARCEL TRACKING HASH MAP")
    for tracking_no, hub in scan_events:
        hubs_seen = parcel_hubs.setdefault(tracking_no, set())

        if hub in hubs_seen:
            print(f"DUPLICATE SCAN: parcel {tracking_no} scanned again at {hub}")
        else:
            print(f"SCAN ACCEPTED: parcel {tracking_no} at {hub}")
            hubs_seen.add(hub)

    print("\nParcel lookup map:")
    for tracking_no, hubs in parcel_hubs.items():
        print(f"{tracking_no}: {sorted(hubs)}")

    # Demonstrate constant-time average lookup by tracking number.
    lookup_id = "PX1002"
    print(f"\nLookup {lookup_id}:", parcel_hubs.get(lookup_id, "Tracking number not found"))


def main():
    sample_scans = [
        ("PX1001", "HUB-A"),
        ("PX1002", "HUB-B"),
        ("PX1001", "HUB-A"),  # duplicate at same hub
        ("PX1001", "HUB-C"),  # valid scan at a different hub
        ("PX1002", "HUB-B"),  # duplicate at same hub
        ("PX1003", "HUB-A"),
    ]
    process_scans(sample_scans)


if __name__ == "__main__":
    main()

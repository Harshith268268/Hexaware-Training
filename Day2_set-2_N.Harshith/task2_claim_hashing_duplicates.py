"""SET 2 TASK 2: Hashing for duplicate and near-duplicate claims."""
def normalize_policy(policy):
    return "".join(policy.split()).casefold()

def detect_claims(claims):
    seen={}
    output=[]
    for claim in claims:
        key=(normalize_policy(claim["policy_number"]),claim["incident_date"].strip())
        if key in seen:
            output.append(f"DUPLICATE / NEAR-DUPLICATE: {claim['claim_id']} matches {seen[key]}")
        else:
            seen[key]=claim["claim_id"]
            output.append(f"ACCEPTED: {claim['claim_id']}")
    return output

if __name__ == "__main__":
    claims=[
      {"claim_id":"CLM-101","policy_number":"POL 7788","incident_date":"2026-10-12"},
      {"claim_id":"CLM-102","policy_number":"pol7788","incident_date":"2026-10-12"},
      {"claim_id":"CLM-103","policy_number":"POL-7788","incident_date":"2026-10-12"},
      {"claim_id":"CLM-104","policy_number":"POL 7788","incident_date":"2026-10-13"},
      {"claim_id":"CLM-105","policy_number":"POL 9911","incident_date":"2026-10-12"}]
    print("SET 2 - TASK 2: CLAIM DUPLICATE DETECTION")
    for line in detect_claims(claims): print(line)
    print("Empty-input test:",detect_claims([]))
    test=[{"claim_id":"A","policy_number":"Ab 123","incident_date":"2026-01-01"},
          {"claim_id":"B","policy_number":"ab123","incident_date":"2026-01-01"}]
    print("Near-duplicate test:",detect_claims(test))
    print("Collision handling: Python dictionaries compare key equality when hashes collide;")
    print("different keys remain distinguishable. Collision resolution is handled internally.")

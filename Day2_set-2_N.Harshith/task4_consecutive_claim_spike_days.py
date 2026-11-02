"""SET 2 TASK 4: Longest consecutive run of days with more than 100 claims."""
def longest_spike_streak(counts, threshold=100):
    best_start=None; best_len=0; current_start=None; current_len=0
    for i,count in enumerate(counts):
        if count>threshold:
            if current_len==0: current_start=i
            current_len+=1
            if current_len>best_len: best_start=current_start; best_len=current_len
        else:
            current_start=None; current_len=0
    if best_start is None: return None,0
    return (best_start,best_start+best_len-1),best_len

if __name__=="__main__":
    counts=[85,110,125,140,95,130,150,160,170,90,105]
    period,length=longest_spike_streak(counts)
    print("SET 2 - TASK 4: CONSECUTIVE CLAIM SPIKE DAYS")
    print("Daily claim counts:",counts)
    if period:
        a,b=period
        print(f"Longest run above 100: {length} consecutive days")
        print(f"Window: Day-{a+1} to Day-{b+1}")
        print("Counts in window:",counts[a:b+1])
    else: print("No day exceeded 100.")
    print("Empty-input test:",longest_spike_streak([]))
    print("No-spike test:",longest_spike_streak([20,100,75,99]))

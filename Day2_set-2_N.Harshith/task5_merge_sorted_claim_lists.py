"""SET 2 TASK 5: Merge two sorted claim lists using two pointers."""
def merge_sorted(first,second):
    i=j=0; merged=[]
    while i<len(first) and j<len(second):
        if first[i]<=second[j]: merged.append(first[i]); i+=1
        else: merged.append(second[j]); j+=1
    merged.extend(first[i:]); merged.extend(second[j:])
    return merged

if __name__=="__main__":
    a=[101,105,112,130,145]; b=[100,105,118,125,150]
    print("SET 2 - TASK 5: MERGE SORTED CLAIM LISTS")
    print("Regional Office A:",a)
    print("Regional Office B:",b)
    print("Merged sorted list:",merge_sorted(a,b))
    print("Empty-input test:",merge_sorted([],[]))
    print("One empty list:",merge_sorted([10,20,30],[]))
    print("Duplicate-values test:",merge_sorted([1,3,5],[1,3,4]))

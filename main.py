import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]
  
  elif S == "":
    return len(T)
  
  elif T == "":
    return len(S)
  
  elif S[0] == T[0]:
    return fast_MED(S[1:], T[1:], MED)
  
  else:
    return 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))

def fast_align_MED(S, T, MED={}):
  
  # Check memoization dictionary for previously computed results
  if (S, T) in MED:
    return MED[(S, T)]
  
  # If S is empty, align it with '-' for each character in T
  if not S:
    return len(T), "-" * len(T), T
  
  # If T is empty, align it with '-' for each character in S
  elif not T:
    return len(S), S, "-" * len(S)
  
  else:
    if S[0] == T[0]:
        # If first characters match, continue with the next parts
        distance, S_align, T_align = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = distance, S[0] + S_align, T[0] + T_align

    else:
        # Compute costs and alignments for inserting, deleting, and substituting
        ins_distance, ins_S_align, ins_T_align = fast_align_MED(S, T[1:], MED)
        del_distance, del_S_align, del_T_align = fast_align_MED(S[1:], T, MED)
        sub_distance, sub_S_align, sub_T_align = fast_align_MED(S[1:], T[1:], MED)
        min_distance = min(ins_distance, del_distance, sub_distance)

        # Select the operation with the minimum cost and adjust the alignment
        if min_distance == ins_distance:
            MED[(S, T)] = 1 + ins_distance, "-" + ins_S_align, T[0] + ins_T_align
        
        elif min_distance == del_distance:
            MED[(S, T)] = 1 + del_distance, S[0] + del_S_align, "-" + del_T_align
        
        else:
            MED[(S, T)] = 1 + sub_distance, S[0] + sub_S_align, T[0] + sub_T_align
    
    # Return only the alignments
    return MED[(S, T)]
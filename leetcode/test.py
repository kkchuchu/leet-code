# abbbccca -> abca
# abcbcbcd -> abcd


def f(input_):
    result = []
    pattern_found_indexer = 0
    while pattern_found_indexer < len(input_):
        a = input_[pattern_found_indexer]
        pattern_found = False
        for length in range(1, len(input_)):
            start = pattern_found_indexer
            end = start + length
            if input_[start: end] == input_[end:end+length]:
                # pattern found
                pattern_found = True
                pattern = input_[start: end]
                j = pattern_found_indexer
                # find max repeat pattern
                while j < len(input_):
                    if input_[j:j+length] == pattern:
                        j = j+length
                    else:
                        pattern_found_indexer = j  
                        break
                result.append(pattern)
                break
            else:
                continue
        if not pattern_found:
            pattern_found_indexer += 1
            result.append(a)
                    
    print(result)
        
f("abcbcbcd")        
f("abbbccca")
            
def duplicate_protein_remover(protein_list):
    blank_list=[]
    for p in protein_list:
        if p not in blank_list:
            blank_list.append(p)
    return blank_list

def single_protein_averager(protein_list):

    if protein_list=='0':
        zero_dict={}
        for p in protein_letters:
            zero_dict[p]=0
        return zero_dict

    else:
        letter_counts={}
        final_letter_counts={}
        total_letter_count=0

        for p in protein_letters:
            letter_counts[p]=0
        for protein in protein_list:
            for p in protein:
                letter_counts[p]+=1
                total_letter_count+=1

        assert total_letter_count==sum(list(letter_counts.values()))

        for k,v in letter_counts.items():
            final_letter_counts[k]=v/total_letter_count

        return final_letter_counts
    
def single_letter_averager(protein_dict):
    return protein_dict[letter]
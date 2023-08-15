def duplicate_protein_remover(protein_list):
    blank_list=[]
    for p in protein_list:
        if p not in blank_list:
            blank_list.append(p)
    return blank_list

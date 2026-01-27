from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

def unique_koala_facts(aantal_facts):
        count_loops, max_loops = 0, 1000
        factlist = []
        while len(factlist) < aantal_facts and count_loops < max_loops:
            fact = random_koala_fact()
            if fact not in factlist:
                factlist.append(fact)
            count_loops += 1
            #if count_loops >= max_loops:
            if len(factlist) == aantal_facts:
                 break
        return factlist
print(unique_koala_facts(6))

# def unique_koala_facts(x):
#     i = 0
#     x = 2
#     if x < 1:
#         return []
#     unique_facts = []
#     while i < 1000:
#         all_facts = random_koala_fact()
#         i += 1
#         if all_facts not in unique_facts:
#             unique_facts.append(all_facts)
#             if len(unique_facts) == x:
#                 break
#         return unique_facts
# print(unique_koala_facts(0))

def num_joey_facts():
    #count_loops = 10
    first_fact = random_koala_fact()
    seen = 0
    max_loops = 1000
    joey_fact_count = 0
    unique_facts=[]
    while seen < 10:
        fact = random_koala_fact()
        if fact == first_fact:
            seen +=1
        if "joey" in fact.lower():
            joey_fact_count += 1
        if "joey" in fact.lower() and fact not in unique_facts:
            unique_facts.append(fact)
        # count_loops += 1
    return len(unique_facts)#joey_fact_count
print(num_joey_facts())

def koala_weight():
    weight_fact = random_koala_fact()
    while "kg" not in weight_fact:
        weight_fact = random_koala_fact()
    split_weight=weight_fact.split("kg")
    split_weight=split_weight[0]
    split_weight=split_weight.split()
    split_weight=split_weight[-1]
    
    return int(split_weight)
print(koala_weight())

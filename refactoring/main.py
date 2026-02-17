# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Add your code after this line

# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]

class Homeowner:
    def __init__(self, HO_name, HO_address, HO_needs):
        self.name = HO_name
        self.address = HO_address
        self.needs = HO_needs

    def __repr__ (self):
        return f"Homeowner(name='{self.name}', address='{self.address}', needs='{self.needs}')"

HO1 = Homeowner("Alfred Alfredson", "Alfredslane 123",["painter", "plumber"])
HO2 = Homeowner("Bert Bertson", "Bertslane 231",["plumber"])
HO3 = Homeowner("Candice Candicedottir", "Candicelane 312", ["electrician", "painter"])

# print([HO1, HO2, HO3])

class Specialist:
    def __init__(self, SP_name):
        self.name = SP_name
        self.specialty = self.__class__.__name__.lower()
        self.contracts = []

    def __repr__(self):
        return f"{self.specialty}(name='{self.name}',contracts={len(self.contracts)})"

class Electrician(Specialist):
        pass

class Painter(Specialist):
        pass

class Plumber(Specialist):
        pass

SP01 = Electrician("Alice Aliceville")
SP02 = Painter("Bob Bobsville")
SP03 = Plumber("Peter Pipe")

specialists = [SP01, SP02, SP03]

def match_specialists(homeowner, specialists):
    matches = []
    for specialist in specialists:
        if specialist.specialty in homeowner.needs:
            matches.append(specialist)
    return matches

class Contract:
     def __init__(self, homeowner, specialty):
          self.homeowener = homeowner
          self.specialty = specialty

     def __repr__(self):
          return f"Contract(homeowner='{self.homeowener.name}', specialty='{self.specialty}')"
      
def assign_contracts(homeowner, specialists):
    assigned = []
    for specialist in specialists:
        if specialist.specialty in homeowner.needs:
            contract = Contract(homeowner, specialist.specialty)
            specialist.contracts.append(contract)
            assigned.append((specialist, contract))
    return assigned
assign_contracts(HO1,specialists)
assign_contracts(HO2,specialists)
assign_contracts(HO3,specialists)

print(SP01, SP01.contracts)
print(SP02, SP02.contracts)
print(SP03, SP03.contracts)

# print(match_specialists(HO1, specialists))
# print(match_specialists(HO2, specialists))
# print(match_specialists(HO3, specialists))

# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)

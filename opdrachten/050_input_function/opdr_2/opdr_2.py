# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...


gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print("Lijst met gasten:", gasten)

gasten.remove("Marie")
print("Lijst na annulering van Marie:", gasten)

index_van_kees = gasten.index("Kees") 
gasten.insert(index_van_kees + 1, "George") 
print("Lijst na toevoeging van George:", gasten)

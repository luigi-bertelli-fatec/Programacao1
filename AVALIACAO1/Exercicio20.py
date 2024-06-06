dictd = {
    "1": "primeiro",
    "2": "segundo",
    "3": "terceiro",
    "4": "quarto",
    "5": "quinto"}

print("=" * 20, " CHAVES ", "=" * 20)
for key in dictd.keys():
    print(key)
    
print("\n", "=" * 20, " VALORES ", "=" * 20)
for val in dictd.values():
    print(val)
    
print("\n", "=" * 20, " ITENS ", "=" * 20)
for item in dictd.items():
    print(item)

print("\n", "=" * 20, " SEGUNDO ITEM ", "=" * 20)
print(list(dictd.items())[1])

print("\n", "=" * 20, " DICIONÁRIO COMPLETO ", "=" * 20)
print(dictd.items())

print("\n", "=" * 20, " ITERANDO DICIONÁRIO ", "=" * 20)
for key in dictd:
    print(f"{key} tem como valor {dictd[key]}")
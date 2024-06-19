Config = {
    'n' : 1500,
    'CLUSTERS' : 3,
    'TER' : 1000,
    'METHOD' : 'DCA CLUSTERING',
    'MEASURE' : 'EUCLIDEAN',
    'YEARS' : 9,
    'MAX' : 200
}
print("Nội  dung của từ điển: ")
for k, v in Config.items():
    print(k, ":", v)
Config ['MEASURE'] = 'MANHATAN'
#print("Nội  dung của từ điển sau khi sửa chữa: ", Config, sep="\n")
Config ['LOSS FUNCTION'] = 'SOFT MAX'
#print("Nội  dung của từ điển sau khi sửa chữa: ", Config, sep="\n")

del Config['YEARS']
print("Nội  dung của từ điển sau khi sửa chữa: ")
for k, v in Config.items():
    print(k, ":", v)

S = input('Mời bạn nhập xâu: ')
for k, v in Config.items():
    if S == str(k):
        print(f"S trung voi thong so key cua value: '{v}' trong Config")
    elif S == str(v):
        print(f"S trung voi thong so value cua key: '{k}' trong Config")
    else:
        print("KHoong trung")
        break
           

Config_set = set(Config.items())
print(Config_set)
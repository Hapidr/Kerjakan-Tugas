import pandas as pd

nama = []
nilai = []

for i in range(5):
    name = input("Masukkan Nama: ")
    mark = input("Masukkan Nilai: ")
    nama.append(name)
    nilai.append(mark)

vi = pd.DataFrame({
    "Nama":[nama[0], nama[1], nama[2], nama[3], nama[4]],
    "Nilai":[nilai[0], nilai[1], nilai[2], nilai[3], nama[4]]
})
vi.index = [1,2,3,4,5]
print("="*20)
print(vi)
'''
DONE
'''

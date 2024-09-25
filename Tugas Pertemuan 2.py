# Menghitung Jarak fokus lensa
n = float(input('Input nilai n = '))
R1 = float(input('Input nilai R1 = '))
R2 = float(input('Input nilai R2 = '))

#Mencari nilai 1/f
f_inv = (n - 1) * (1/R1 + 1/R2)

#Mencari nilai f
f = 1 / f_inv  

# Output the result
print(f"Nilai f = {f:.2f} cm")
print(f"Nilai f_inv = {f_inv:.2f} cm")

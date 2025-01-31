import math

def aprekinat_trijsturi(A, B, C):
   
    if A(0) == B(0) or A(1) == B(1): 
        taisnais_lenkis = A
        katete1 = abs(B(0) - C(0))
        katete2 = abs(B(1) - C(1))
    elif B(0) == C(0) or B(1) == C(1):
        taisnais_lenkis = B
        katete1 = abs(A(0) - C(0))
        katete2 = abs(A(1) - C(1))
    else:
        taisnais_lenkis = C
        katete1 = abs(A(0) - B(0))
        katete2 = abs(A(1) - B(1))

    # Aprēķinām laukumu
    laukums = 0.5 * katete1 * katete2

    # Aprēķinām hipotenūzu
    hipotenūza = math.sqrt(katete1**2 + katete2**2)

    # Aprēķinām augstumu pret hipotenūzu
    augstums = (2 * laukums) / hipotenūza

    return laukums, augstums

# Piemērs: trijstūris ar virsotnēm (0,0), (4,0), (0,3)
A = (0, 0)
B = (4, 0)
C = (0, 3)

laukums, augstums = aprekinat_trijsturi(A, B, C)

print("Trijstūra laukums:", laukums)
print("Augstums pret hipotenūzu:", augstums)

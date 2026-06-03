pu=float(input("saisir le prix :"))
q=int(input("saisir la quantité :"))
THT= pu*q
TVA=0.20
TTC = THT * (1+TVA)
print(f"le total hors taxe est : {THT:.2f}")
print(f"le total tout taxes comprises est : {TTC:.2f}")
import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

cena_teraz = 120000 
stopa_wzrostu_ceny = 0.05  
lata = 5
okresy = lata * 12  

fv_mieszkania = cena_teraz * (1 + stopa_wzrostu_ceny) ** lata

stopa_nominalna_roczna = 0.12  
stopa_miesieczna = stopa_nominalna_roczna / 12  

miesieczna_wplata = -npf.pmt(rate=stopa_miesieczna, nper=okresy, pv=0, fv=fv_mieszkania)

miesiace = np.arange(1, okresy + 1)
ceny_mieszkania = cena_teraz * (1 + stopa_wzrostu_ceny) ** (miesiace / 12)

wartosci_lokaty = npf.fv(rate=stopa_miesieczna, nper=miesiace, pmt=-miesieczna_wplata, pv=0)


print(f"Przyszła cena mieszkania za 5 lat: {fv_mieszkania:,.2f} zł")
print(f"Wymagana miesięczna wpłata: {miesieczna_wplata:,.2f} zł")


plt.plot(ceny_mieszkania, label='Cena mieszkania')
plt.plot(wartosci_lokaty, label='Wartość kapitalu na lokacie')
plt.legend()
plt.xlabel('Miesiąc')
plt.ylabel('Kwota (zł)')

plt.show()
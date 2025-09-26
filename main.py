import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
pv = 120000
rate = 0.05
years = 5
freq = 12
rate = rate / freq
nper = years * freq
rata = 0.12
rata = rata / freq
bieda = 0

wartosc_przyszla = -np.around(npf.fv(rate, nper, 1, pv))

wplata = (-npf.pmt(rata,nper,bieda,wartosc_przyszla))
wplata = wplata.round(2)

np.set_printoptions(suppress = True)
principal_decreasing = np.around(np.zeros(nper)+(wartosc_przyszla/nper),2)

balance = np.zeros(nper)
balance_close = np.around(balance + np.cumsum(principal_decreasing),2)

print(f"za {years} cena mieszkania bedzie wynosiła {wartosc_przyszla}zł")
print(f"Na lokate w banku nalezy co miesią wpłacać {wplata}zł")

punkt_poczatkowy_x = 0
punkt_poczatkowy_y = pv
punkt_koncowy_x = nper
punkt_koncowy_y = wartosc_przyszla

x_wspolrzedne = [punkt_poczatkowy_x, punkt_koncowy_x]
y_wspolrzedne = [punkt_poczatkowy_y, punkt_koncowy_y]

plt.plot(balance_close,label='suma zgromadzanego kapitału')
plt.plot(x_wspolrzedne, y_wspolrzedne,label='cena mieszkania')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('waluta "zł"')

plt.show()
  
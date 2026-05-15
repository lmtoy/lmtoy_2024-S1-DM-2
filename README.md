# 2024-S1-DM-2

this DDT project observes the Taurus Molecular Cloud-1 (calls MWC1 here)
with an interesting spectral setup

bank=1 observed 12CO and CN in two "freq1" and "freq2" source names.

bank=0 is tuned to a "fake" restfreq of 109.992,trying to find signal at 109.782 (C18O) and 110.201 (C13CO),
for both the "freq1" and "freq2" setup, thus increasing the observing time by a factor of 2 compared
to the 12CO and CN lines.

Tuned to vlsr=163 km/s

- 12CO:  115.271  strong     
- 13CO:  110.210  clear      at vlsr ~ -405 for 109.992   
- C18O:  109.782  maybe      at vlsr ~ +734 for 109.992
- CN:    113.491  nothing yet

## Multiple lines

In the current pipeline only a single line, picked by vlsr=, dv= and dw= can be choosen.
The keyword oid= has not been implemented, but was intended to given an alternative
ID to an obsnum. For example using oid=__CO we would see obsnums like 123456__CO.

An alternative approach would be cut a full cube including both the two lines in bank=0.
This has the problem that data size increases, baseline subtraction covers a large range
and a low order may not be sufficient anymore. The PI will then need to cut the line cubes
and adjust the restfreq.

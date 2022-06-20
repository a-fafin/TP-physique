import numpy as np
from matplotlib import pyplot as plt

# import données - temps en s, volume en L, pression en Pa
t, v, p = np.loadtxt("exo_stirling_mesures.dat", unpack=True, skiprows=1)

# spectre simplifié
nfreqs, freqs = 3, [0, 5.5, 11]
amp_v, amp_p = [27.416e-2, 7.2606e-2, 0], [1.48266, 0.642436, 0.1247256]
phi_v, phi_p = [0, 1.2054, 0], [0, -2.22834, 1.820505]

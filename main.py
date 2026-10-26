#DAH CP 6 pre-code

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats as st
from scipy.signal import find_peaks 

# Something about a histogram 
#entries, binedges, patches = plt.hist( xmass, bins= 10, range = [MIN,MAX])

# Read the data from the file


### 6.1

mass_array= np.loadtxt(r"upsilons-mass-xaa.txt", dtype=float)
#print(mass_array)
def hist_plot():
    plt.hist(mass_array, bins = 100, range = [8,11.5])
    plt.xlabel("Mass (Gev/c^2)")
    plt.ylabel("Frequency")
    plt.title("Invariant masses of muon pairs")
    plt.show()

#hist_plot()
####6.2
#Take limits of the area to find the mode in the three regions where the particle mass is highest 

#T_1= np.clip(mass_array, 9.1 ,9.75)
# Use bincount in numpy to count number of bins with each number?
#c_1 = np.bincount(T_1)
#print(np.argmax(T_1))
#No the bincount method only works with integers
##CLIP JUST MOVES ALL THE OTHER DATA POINTS TO THE LIMITS SO THOSE ARE THE MODES NOW THIS IS ALL WRONGNGGNGNGNGNG

#print(mass_1)


mass_1_seg = mass_array[(mass_array >= 9.1) & (mass_array <= 9.75)]
#print(mass_1)
Upsilon_1=st.mode(mass_1_seg)
print(Upsilon_1)

mass_2_seg = mass_array[(mass_array >= 9.75) & (mass_array <= 10.25)]
#print(mass_1)
Upsilon_2=st.mode(mass_2_seg)
print(Upsilon_2)

mass_3_seg = mass_array[(mass_array >= 10.25) & (mass_array <= 11)]
#print(mass_1)
Upsilon_3=st.mode(mass_3_seg)
print(Upsilon_3)

def BintoMass(peaks, range=[9,11], bins=125):
    masses = np.linspace(range[0], range[1], bins)
    return np.array([masses[peak] for peak in peaks])


def findPeaks(x):
    hist = np.histogram(x, bins=125, range = [9,11])
    peaks = find_peaks(hist[0], distance=5, width=3)
    print(f"peaks: {peaks}")
    # convert peaks from histogram to energies
    peaks_M = BintoMass(peaks[0])

    plt.hist(x, bins=125, range=[9, 11])
    plt.vlines(peaks_M, ymin=[0], ymax=[6000], colors=["red"], label=f"peaks: {peaks_M}")

    plt.legend()
    plt.xlabel(r"Mass $\frac{Gev}{c^2}$")
    plt.ylabel("Frequency")
    plt.title("Invariant masses of muon pairs")
    plt.show()

findPeaks(mass_array)

###I dont understand the mass differences equation
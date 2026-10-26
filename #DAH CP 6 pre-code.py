#DAH CP 6 pre-code

import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats as st

# Something about a histogram 
#entries, binedges, patches = plt.hist( xmass, bins= 10, range = [MIN,MAX])

# Read the data from the file


### 6.1

mass_array= np.loadtxt(r"C:\Users\user\Documents\Edinburgh year 4\DAH\upsilons-mass-xaa.txt", dtype=float)
#print(mass_array)
def hist_plot():
    plt.hist(mass_array, bins = 75, range = [8,11.5])
    plt.xlabel("Mass (Gev/c^2)")
    plt.ylabel("Frequency")
    plt.title("Invariant masses of muon pairs")
    plt.show()

####6.2
#Take limits of the area to find the mode in the three regions where the particle mass is highest 

#T_1= np.clip(mass_array, 9.1 ,9.75)
# Use bincount in numpy to count number of bins with each number?
#c_1 = np.bincount(T_1)
#print(np.argmax(T_1))
#No the bincount method only works with integers
##CLIP JUST MOVES ALL THE OTHER DATA POINTS TO THE LIMITS SO THOSE ARE THE MODES NOW THIS IS ALL WRONGNGGNGNGNGNG

#print(mass_1)


""" mass_1_seg = mass_array[(mass_array >= 9.1) & (mass_array <= 9.75)]
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
 """
###I dont understand the mass differences equation 

###6.3 Suitable region around T(1)

def sixpointthree_1():    ##Say his name when you make a function "FINLAY"
    mass_1_seg = mass_array[(mass_array >= 9.1) & (mass_array <= 9.75)]
    mean_1=np.mean(mass_1_seg)
    print("The mean of Upsilon 1 = " ,mean_1)

#VARIANCE
    var_1=np.var(mass_1_seg)
    print("The variance of Upsilon 1 = " ,var_1)

#STD
    std_1=np.std(mass_1_seg)
    print("The standard deviation of Upsilon 1 = ", std_1)

#STD of the mean 

    std_1_mean= std_1/np.sqrt(len(mass_1_seg))
    print("The standard deviation of the mean = ",std_1_mean)

##Biases with method, Mass spectrum is continuous, bins arent, so we get a systematic uncertainty from the bin width
##No subtraction of background activity
##The window of data selected is abritrary giving a systematic shift in mean and what not 

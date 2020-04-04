q1=float(input("Enter first charge: "))#In multiples of electronic charge 'e'
q2=float(input("Enter second charge: "))#In multiples of electronic charge 'e'
from scipy.constants import epsilon_0 as h, pi, e
def ElectricForce(q1,q2):
    z=1
    s=4*pi*h
    k=1/s
    z=k*q1*q2*e*e
    return z
f=ElectricForce(q1,q2)
print(f,"C/m^2")


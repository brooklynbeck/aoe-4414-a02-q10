# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg long_deg hae_km
#  Converts LLH to ECEF vector components
# Parameters:
#  lat_deg: latitude in degrees
#  long_deg: longitude in degrees
#  hae_km: height above the ellipsoid in km
# Output:
#  Prints ECEF x-component (km), ECEF y-component (km), and ECEF z-component (km)
#
# Written by Brooklyn Beck
# Other contributors: Boilerplate by Brad Denby
#

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions

## calculated denominator
def calc_denom(ecc,lat_rad):
  return math.sqrt(1.0-ecc**2*math.sin(lat_rad)**2)

# initialize script arguments
lat_deg = float('nan') # latitude in degrees
long_deg = float('nan') # longitude in degrees
hae_km = float('nan') # height above the reference ellipsoid

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  long_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
    'Usage: '\
    'python3 llh_to_ecef.py lat_deg long_deg hae_km'\
  )
  exit()

# write script below this line

#convert degrees to radians
lat_rad = lat_deg * math.pi/180.0
long_rad = long_deg * math.pi/180.0

#calculate intermediary values
denom = calc_denom(E_E, lat_rad)
C_E = R_E_KM / denom
S_E = R_E_KM * (1.0-E_E**2)/denom

#calculate x, y, and z components
r_x_km = (C_E + hae_km)*math.cos(lat_rad)*math.cos(long_rad)
r_y_km = (C_E + hae_km)*math.cos(lat_rad)*math.sin(long_rad)
r_z_km = (S_E + hae_km)*math.sin(lat_rad)

#print outputs
print(r_x_km)
print(r_y_km)
print(r_z_km)






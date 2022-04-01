import numpy as np
import matplotlib.pyplot as plt

from astropy.io import ascii
import astropy.coordinates as coord
import astropy.units as u
from astropy.coordinates import Angle

import io
import requests
from rich import print

def plot():
    url="https://raw.githubusercontent.com/astrohitc/GSNST-sky-coverage/main/GSNST_sky.csv"
    s=requests.get(url).content
    d1=pd.read_csv(io.StringIO(s.decode('utf-8')))


    ra = Angle(d1['RA'], unit=u.deg)
    ra = ra.wrap_at(180*u.deg)
    dec = Angle(d1['DEC'], unit=u.deg)

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.scatter(ra.radian, dec.radian)
    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    ax.grid(True)
    plt.title('GSNST discoveries')

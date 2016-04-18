
# coding: utf-8

# # Analysing flight data from a _csv_ file
# ## Dawid Gerstel, 18.04.2016
# 
# This page provides project description combined with fully executable code (enabled only in interactive mode).

# Import the necessary libraries and setup some cosmetics.

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap    # for geographic world map
import itertools    # for iterator-based python functions

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'


# The class __MapDrawer__ serves building a geographical map with aircraft's trajectory obtained from longitude and latitude coordinates.

# In[2]:

class MapDrawer(object):
        """ draws trajectory (=f(lon,lat)) on a geographic map """

        def __init__(self, lon, lat, ax, zoom):
            self.ax = ax
            self.zoom = zoom

            self.lon = lon
            self.lat = lat

            self.setMapBoundaries()

            self.initMap()

            self.drawTrajectory()

            self.addMoreGeography()        


        def setMapBoundaries(self):
    
            if self.zoom:
                EPS_lat = np.std(self.lat) * 10
                EPS_lon = np.std(self.lon) * 10

                self.llc_lat, self.urc_lat = min(self.lat) - EPS_lat, max(self.lat) + EPS_lat
                self.llc_lon, self.urc_lon = min(self.lon) - EPS_lon, max(self.lon) + EPS_lon

            else:
                lon_big_interval = 90
                lat_big_interval = 30

                mean_lon = np.mean(self.lon)
                mean_lat = np.mean(self.lat)

                self.llc_lat, self.urc_lat = mean_lat - .5 * lat_big_interval, mean_lat + .5 * lat_big_interval
                self.llc_lon, self.urc_lon  = mean_lon - .5 * lon_big_interval, mean_lon + .5 * lon_big_interval



        def initMap(self):
            self.themap = Basemap(projection='merc',
                  llcrnrlon = self.llc_lon,              # lower-left corner longitude
                  llcrnrlat = self.llc_lat,              # lower-left corner latitude
                  urcrnrlon = self.urc_lon,              # upper-right corner longitude
                  urcrnrlat = self.urc_lat,              # upper-right corner latitude
                  resolution = 'i',
                  area_thresh = 1.0,
                  lon_0 = 0.5*(self.llc_lon+self.urc_lon),
                  lat_0 = 0.5*(self.llc_lat+self.urc_lat),
                  ax = self.ax
                  )    

        def drawTrajectory(self):            
            x, y = self.themap(self.lon, self.lat)
            self.themap.plot(x, y, 
                        '-',                    # marker shape
                        color='yellow',         # marker colour
                        linewidth=3             # marker size
                        )

        def addMoreGeography(self):
            self.themap.drawcoastlines()
            self.themap.drawcountries()
            self.themap.fillcontinents(color = 'gainsboro')
            self.themap.drawmapboundary(fill_color='steelblue')

            numPar, numMer = 7, 7

            stepPar = (self.urc_lat - self.llc_lat) / numPar
            stepMer = (self.urc_lon - self.llc_lon) / numMer

            self.themap.drawparallels(np.arange(10,90,stepPar),labels=[1,0,0,1])
            self.themap.drawmeridians(np.arange(-180,180,stepMer), labels=[1,1,0,1])            


# The class __GPStoGroundDisplacementConverter__ solves problem of projecting longitude and latitude displacements onto the ground (in metres). The operation is not trivial and it exploits the Haversine formula (https://en.wikipedia.org/wiki/Haversine_formula).

# In[3]:

from math import radians, cos, sin, asin, sqrt
import time  
from itertools import izip

class GPStoGroundDisplacementConverter(object):
    """ converts lists of subsequent longitude and latitude increments to corresponding
        ground projection (in metres) """
    
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
        
    def haversine(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        #r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        r = 6371000 # Radius of earth in meters. Use 3956 for miles
        return c * r

    def projectGPSontoGroundDisplacements(self):
        """
        Converts GPS position (lists of longitudes and latitudes) to a list of displacements 
        (rel. to ground) in metres
        """
        
        # get list of increments in metres
        delta_Pos = np.zeros(len(self.lon) - 1)
        lon_prev, lat_prev = self.lon[0], self.lat[0]
        
        # convert subsequent self.lon and self.lat to ground increments [m]
        for enum, coords in enumerate( izip(self.lon[1:], self.lat[1:]) ):
            delta_Pos[enum] = self.haversine(lon_prev, lat_prev, coords[0], coords[1])
            lon_prev, lat_prev = coords

        return delta_Pos


# The third class, __FlightDataAnalyser__ is actual manager of the project. It benefits from the two above classes and performs analysis that consists of:
# - displaying a few initial __csv__ file lines (to get an idea of the data),
# - drawing plane's trajectory on a geographic map,
# - plotting available parameters (from the __csv__ file) as a function of time and plotting their histograms
# - calculating 1st and 2nd derivatives of the parameters and displaying them

# In[4]:

class FlightDataAnalyser(object):
    """ reads and analyses flight data from a csv file """

    def __init__(self, dataFile):
        self.fl_data = pd.read_csv(dataFile, sep=',', encoding='latin1', index_col='Time',
                                   parse_dates=['Time'])
        
        self.lon = self.fl_data['Longitude'].tolist()
        self.lat = self.fl_data['Latitude'].tolist()
        
        self.time = self.fl_data.index.tolist()
        
        # time increments [s]
        self.dts = np.diff(self.time)
        
    def dataHead(self, numInd=15):
        """ displays first numInd rows of the data """
        print self.fl_data[:numInd]
        
    def histPlotRawData(self, dataLabel, ax):
        self.fl_data[dataLabel].hist(ax=ax, alpha=0.5, normed=True)
        
    def timePlotRawData(self, dataLabel, ax):
        """ plot a raw data parameter as a function of time """
        self.fl_data[dataLabel].plot(ax=ax)

    def timePlot(self, label, ax, data=None):
        # param vs time
        ylabel = label
        title = label + " as a function of time"
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        
        if data == None:
            self.timePlotRawData(label, ax)
        else:
            ax.plot(data[0], data[1])
            
    def histPlot(self, label, ax, data=None):            
        xlabel = label
        title = "histogram of " + label
        ylabel = "relative freq."
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.set_title(title)

        if data == None:
            self.histPlotRawData(label, ax)
        else:
            ax.hist(data[1], bins=np.linspace(min(data[1]), max(data[1]), numBins), normed=True)            
            
    def plotTimeAndHist(self, label, data=None, figsize=(16, 5), shallHist=True, numBins=100):
        """ Plot param vs time and histogram of param stacked vertically """
        
        # stack dimensions
        if shallHist:
            fig, ax = plt.subplots(2, figsize=(16, 5))        
        else:
            fig, ax = plt.subplots(1, figsize=(16, 2.5))        
        
        if shallHist:
            self.timePlot(label, ax[0], data)
            self.histPlot(label, ax[1], data)
        else:    # only param as a func of time
            self.timePlot(label, ax, data)
        
        
    def plotRawData(self):
        """ plot params (only those from input file) as a function of time and plot their histograms """
        
        for key in self.fl_data.keys():
            self.plotTimeAndHist(key)
            
    def plotDerivedData(self, also_2nd = True):
        """ plot 1st and 2nd derivatives of data """
        
        # first derivatives
        for label, val in self.derivs.iteritems():
            data = (self.time[1:], val) # 1st der. uses time without 1st point
            self.plotTimeAndHist("derivative of " + label, data, shallHist=False)
            
        # second derivatives    
        if also_2nd:
            for label, val in self.derivs2.iteritems():
                print label
                data = (self.time[2:], val) # 1st der. uses time without 1st and 2nd points
                self.plotTimeAndHist("2nd derivative of " + label, data, shallHist=False)          
        

    def plotMap(self):
        """ draw geographic map of the aircraft trajectory.
            2 maps are plotted: zoomed-in and zoomed-out view
        """
        
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # zoomed-in map
        MapDrawer(lon=self.lon, lat=self.lat, ax=axes[0], zoom=True)
        axes[0].set_title("Zoomed in")

        # zoomed-out map
        MapDrawer(lon=self.lon, lat=self.lat, ax=axes[1], zoom=False)                   
        axes[1].set_title("Zoomed out")      
        
    def calcDerivatives(self):
        """ calculates 1st and 2nd order derivatives of:
            - Roll, Pitch, Yaw
            - ground speed.
        """

        self.derivs, self.derivs2 = {}, {}
        for item in self.fl_data.keys():
            self.derivs[item] = np.diff(self.fl_data[item]) / self.dts
            self.derivs2[item] = np.diff(self.derivs[item]) / np.diff(self.dts) # odd t: {t1, t3...}
    
        self.calcGroundSpeedandAcceleration()
    
                    
    def calcGroundDisplacements(self):
        """ convert GPS (lon, lat) to ground-projected displacements [metres] """
        gps_cnv = GPStoGroundDisplacementConverter(lon=self.lon, lat=self.lat)    
        self.gnd_dist = gps_cnv.projectGPSontoGroundDisplacements()
        
    def calcGroundSpeedandAcceleration(self):
        """ [km/h] """

        self.derivs["Gnd distance"] = self.gnd_dist / self.dts * 3.6 # 3.6 for m/s -> km/h conversion
        self.derivs2["Gnd distance"] = np.diff(self.derivs["Gnd distance"]) / np.diff(self.dts)    
        
    def doAnalysis(self, shallPlot = True):
        """ performs default analysis """
        self.dataHead()

        if shallPlot:
            self.plotMap()    # this takes a minute
        self.calcGroundDisplacements()
        
        self.plotRawData()
        self.calcDerivatives()
        self.plotDerivedData(also_2nd = False)


# ### Two examples
# 
# #### Example 1

# In[5]:

dataFile = '../data/Tacview-CSV-Samples/A-4E (Viper) [Red].csv'

fda = FlightDataAnalyser(dataFile)
fda.doAnalysis(shallPlot = True)


# ### Example 2
# 
# The second example shows that the project is flexible enough to analyse data from a different file (as opposed to being custom-made only for one specific input file).
# Morever, were the data different (but properly formatted) -- the program should cope with that challenge.

# In[6]:

dataFile2 = '../data/Tacview-CSV-Samples/F-14A (Maverick & Goose) [Blue].csv'

fda2 = FlightDataAnalyser(dataFile2)
fda2.doAnalysis(shallPlot = True)


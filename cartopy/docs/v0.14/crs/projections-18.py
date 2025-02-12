import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(1.6153846153846154, 3))
ax = plt.axes(projection=ccrs.OSGB())
ax.coastlines(resolution='50m')
ax.gridlines()
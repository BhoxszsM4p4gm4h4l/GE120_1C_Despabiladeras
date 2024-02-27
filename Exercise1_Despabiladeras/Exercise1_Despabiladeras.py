"""
hello world it's me mario
""" 

dms = 118.42069
deg = int(dms)
print("Degrees to be converted to DMS: ", dms)


#for minutes we need to...
mins=(dms - deg)*60
mins_frac = int(mins)

#for seconds we get...
sec = (mins - mins_frac)*60
rsec = round(sec,2)
dems = [deg,mins_frac,rsec]
print("The resulting DMS is " + str(deg) + "-" + str(mins_frac)+"-"+ str(rsec))
#were now done for deg to dms!

#now lets punta from deg to dms
degdms = "118-25-14.48"
values = degdms.split("-")
print("DMS to be converted to degrees: " + degdms)
deg1 = int(values[0])
min1 = int(values [1])
sec1 = float(values [2])

resdeg = deg1 + (min1/60) + (sec1/3600)
print ("The resulting degree is ", round(resdeg,2))
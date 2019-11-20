import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date
import csv
import calendar

    
#function for adding months to sourcedate
def add_months(sourcedate,months):
     month = sourcedate.month - 1 + months
     year = int(sourcedate.year + month / 12 )
     month = month % 12 + 1
     day = min(sourcedate.day,calendar.monthrange(year,month)[1])
     return date(year,month,day)
    
    
# Create empty lists to store input data from csv files
data=[]#control data per run
controls=[]#Imported SD ranges for controls

         
#Read in data from csv for raw data
with open(r"C:\Users\Kristi\Documents\test.csv",'r') as fIn:
    reader=csv.reader(fIn)
    for line in reader:
        data.append(line)

# Remove header line from data csv
data.remove(data[0])

# Parse data into numpy compatible formats
# (datetime64, float, float, float)
for i in range(len(data)):
    for n in range(len(data[i])):
        if n==0:
            data[i][n]=np.datetime64(data[i][n]).astype(datetime)
        else:
            data[i][n]=float(data[i][n])
            
#Read in data from csv for control ranges
with open(r"C:\Users\Kristi\Documents\controlsd.csv",'r') as cIn:
    reader=csv.reader(cIn)
    for line in reader:
        controls.append(line)
# Remove header line from control csv
controls.remove(controls[0])

# Plot imported SD data
for i in range(len(controls)):
    for n in range(len(controls[i])):
        if n==0:
            controls[i][n]=np.datetime64(controls[i][n]).astype(datetime)
        else:
            controls[i][n]=float(controls[i][n])
# Parse data into numpy compatible formats
# (datetime64, float, float, float,float)

# Create np array of all valid data
f = np.array(data)#for raw data
c=np.array(controls)#for controls


# Find min date
minDate = min(f[:,0])
print('minDate', minDate)
 # Find max date
maxDate = max(f[:,0])
print('maxDate', maxDate)

#minCDate = min(c[:,0])
#print('minCDate', minCDate)
# # Find max date
#maxCDate = max(c[:,0])
#print('maxCDate', maxCDate)
#finds startdate of the numpy array
startDate = date(minDate.year, minDate.month, 1)
print('sd',startDate)
#finds the end date of numpy array
endDate = add_months(startDate,2)
print('ed', endDate)
##finds startdate of the numpy array
#startCDate = date(minCDate.year, minCDate.month, 1)
#print('sdc',startCDate)
##finds the end date of numpy array
#endCDate = add_months(startCDate,2)
#print('edc', endCDate)

#test of two month range for data
print('raw data',f[(f[:,0] >= startDate) & (f[:,0] < endDate)])
twoMonthData = f[(f[:,0] >= startDate) & (f[:,0] < endDate)]

#print('raw control data',c[(c[:,0] >= startCDate) & (c[:,0] < endCDate)])
#twoMonthCData = c[(c[:,0] >= startCDate) & (c[:,0] < endCDate)]



#Graph titles
titles={1:'LPC',2:'HPC', 3:'Slope'}
ylabels={1:'Log10 Value', 2:'Log10 Value'}
colors={1:'b',2:'g',3:'purple'}


# 2 Month for loop
for i in range(12):
    currentstart=add_months(startDate,i)
    currentenddate=add_months(endDate,i)
    twoMonthData = f[(f[:,0] >= currentstart) & (f[:,0] < currentenddate)]
    print('data',currentstart,currentenddate,twoMonthData)
#    currentstartc=add_months(startCDate,i)
#    currentenddatec=add_months(endCDate,i)
    twoMonthCData = c[(c[:,0] >= currentstart) & (c[:,0] < currentenddate)]
#    print('control', currentstartc,currentenddatec, twoMonthCData)
    #outliers=twoMonthData[]
    for n in range(1,4):
        LPCData=twoMonthData[:,1]
        HPCData=twoMonthData[:,2]
        LPC_Control_Data=twoMonthCData[:,1]
        HPC_Control_Data=twoMonthCData[:,2]
        LPC_Outliers=np.all(LPCData>LPC_Control_Data) and (LPCData<LPC_Control_Data)
        
        # Calculate 2SD for data sets
        m=np.mean(f[:,n])
        print('mean',m)
        sd=np.std(f[:,n])
        print('sd',sd)
        sd2=sd*2
    
        print('sd2',sd2)
        psd2=m+sd2
        nsd2=m-sd2
        print('psd2',psd2,'nsd2',nsd2)
        
        # Create figure
        plt.figure(figsize=(10,10))
        
        # Add title
        title=plt.title(titles[n])
        
        # X Label
        plt.xlabel('Date')
        
        # Y Label(s)
        if n in ylabels:
            plt.ylabel(ylabels[n])
            
        # Plot data from csv
        datas=plt.plot_date(twoMonthData[:,0], twoMonthData[:,n], '-o',color=colors[n],label=titles[n] + ' Data')#plots data from lpc/ 1st 2nd col of array f

        # Autoformat X tick date labels
        plt.gcf().autofmt_xdate()
        
        # Plot +2SD 2 month analysis line
        calcp=plt.axhline(y=psd2, label="+2SD (2-Month Analysis)", color='black')
        
        # Plot -2SD 2 month analysis line
        calcn=plt.axhline(y=nsd2, label="-2SD (2-Month Analysis)",color='black')
        
        # Plot Slope specific SD lines
        if n==3:
            expps=plt.axhline(y=-3.100, label="+2SD (Acceptable Performance Range)", color ='r')
            exns=plt.axhline(y=-3.700, label="-2SD (Acceptable Performance Range)", color='r')
#sdlegend=plt.legend([expps, calcp],["+/-2SD (Acceptable Performance Range)","+/-2SD (2-Month Analysis)"],bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
        elif n == 2: # Plot HC SD lines
            print("I'm plotting HC SD lines!")
            #Plot both lines           
            plt.plot_date(twoMonthCData[:,0], twoMonthCData[:,3], '-', label="-2SD (Acceptable Performance Range)",color='r')
            plt.plot_date(twoMonthCData[:,0], twoMonthCData[:,4], '-', label="+2SD (Acceptable Performance Range)",color='r')
        else:
            print("I'm plotting LC SD lines!" )
            plt.plot_date(twoMonthCData[:,0], twoMonthCData[:,1], '-',label="-2SD (Acceptable Performance Range)",color='r')
            plt.plot_date(twoMonthCData[:,0], twoMonthCData[:,2], '-',label="+2SD (Acceptable Performance Range)",color='r')
            
        
        # Plot legend
        plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
        #plt.plot_date(twoMonthCData[:,0],twoMonthCData[:,1], '-', color='r')
        
        
        
        plt.show()
        plt.close()

import json
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

fpath= os.path.dirname(os.path.realpath(__file__)).replace('\\','/')
fname=fpath+'/dati-json/dpc-covid19-ita-andamento-nazionale.json'
with open(fname) as json_data:
    print('file open')
    l = json.load(json_data)
    
print(l[0].keys())
    
start_date = datetime.strptime(l[0]['data'], "%Y-%m-%dT%H:%M:%S")
Ndays=len(l)
print('start:',start_date, 'Number of days:',Ndays)

t=np.array( [start_date + timedelta(days=i) for i in range(Ndays)] )
xlab=np.array( [start_date + timedelta(days=i) for i in range(0,Ndays,20)] )

var1=['totale_positivi','totale_ospedalizzati','terapia_intensiva','deceduti']

fig=plt.figure(figsize=(15,8))
plt.title('COVID-19 Italia - Monitoraggio situazione')
#plt.subplot(211)

for x in var1:
    y=np.array([d[x] for d in l])
    plt.plot(t,y,label=x)

plt.legend(loc='upper left',fontsize=23)
plt.xticks(xlab,fontsize=10)
plt.yticks(fontsize=16)
#plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0),useMathText=True)
plt.grid()

'''
plt.subplot(212)
var2=['nuovi_attualmente_positivi']
for x in var2:
    y=np.array([d[x] for d in l])
    plt.plot(t,y,label=x)

print(l[0]['tamponi'],l[1]['tamponi']-l[0]['tamponi'])
ytemp = [None] * Ndays
ytemp[0]=l[0]['tamponi']
for i in range(1,Ndays):
    ytemp[i]=l[i]['tamponi']-l[i-1]['tamponi']
ytamp=np.array(ytemp)
plt.plot(t,ytamp,label='nuovi tamponi')

    
plt.legend(loc='upper left',fontsize=23)
plt.xticks(xlab,fontsize=16)
plt.yticks(fontsize=16)
plt.grid()
'''

plt.tight_layout()

fig.savefig('covid-19_Italy-StatusMonitor.png')

#fig.set_size_inches(30, 30)
#fig.savefig('covid-19_Italy-Status_'+datetime.now().strftime('%Y-%m-%d')+'.png')

plt.show()

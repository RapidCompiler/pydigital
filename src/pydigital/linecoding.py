import matplotlib.pyplot as plt
import numpy as np

class LineCoding:
    def plot(self, bits, data, name, z):
        clock = 1 - np.arange(len(data)) % 2
        t = 0.5 * np.arange(len(data))
        
        for p in range(len(bits)+1):
            plt.axvline(p, color='.5', linewidth=2)
        for p in [z,2]:
            plt.axhline(p, color='.5', linewidth=2)
        plt.step(t, clock + 2, 'r', linewidth = 2, where='post')
        plt.step(t, data, 'r', linewidth = 2, where='post')
        plt.ylim([-1,3.5])

        for tbit, bit in enumerate(bits):
            plt.text(tbit + 0.5, -0.5, str(bit))
        
        plt.text((-len(bits))/6,2,'Clock')
        plt.text(3.5,-1.25,name)


        plt.gca().axis('off')
        plt.show()
        
    def unipolar_nrz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data = np.repeat(bits, 2)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Unipolar NRZ',0)

    def unipolar_rz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        for i in bits:
            data.append(i)
            l=0
            data.append(l)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Unipolar RZ',0)

    def polar_nrz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data = np.repeat(bits, 2)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Polar NRZ',0.5)

    def polar_nrzl(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        dat1=[]
        for i in bits:
            if i==1:
                l=0
                dat1.append(l)
            else:
                l=1
                dat1.append(l)
        data = np.repeat(dat1, 2)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Polar NRZ-L',0.5)

    def polar_nrzi(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        for i in range(0,len(bits)):
            if i==0:
                if bits[i]==1:
                    l=0
                    data.append(l)
                else:
                    l=1
                    data.append(l)
            elif bits[i]==0:
                l=data[i-1]
                data.append(l)
            elif bits[i]==1:
                if data[i-1]==1:
                    l=0
                    data.append(l)
                else:
                    l=1
                    data.append(l)
        data = np.repeat(data, 2)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Polar NRZ-I',0.5)

    def polar_rz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        for i in bits:
            data.append(i)
            l=0.5
            data.append(l)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Polar RZ',0.5)

    def bipolar_nrz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        su=0
        for i in bits:
            if i==0:
                q=0.5
                data.append(q)
                data.append(q)
            else:
                su=su+1
                if(su%2==0):
                    q=0
                    data.append(q)
                    data.append(q)
                else:
                    q=1
                    data.append(q)
                    data.append(q)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Bipolar NRZ',0.5)

    def bipolar_rz(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        su=0
        for i in bits:
            if i==0:
                q=0.5
                data.append(q)
                data.append(q)
            else:
                su=su+1
                if(su%2==0):
                    q=0
                    data.append(q)
                    q=0.5
                    data.append(q)
                else:
                    q=1
                    data.append(q)
                    q=0.5
                    data.append(q)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Bipolar RZ',0.5)

    def pseudoternary(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        su=0
        for i in bits:
            if i==1:
                q=0.5
                data.append(q)
                data.append(q)
            else:
                su=su+1
                if(su%2==0):
                    q=0
                    data.append(q)
                    data.append(q)
                else:
                    q=1
                    data.append(q)
                    data.append(q)
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Pseudoternary',0.5)

    def manchester_ieee(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data = np.repeat(bits, 2)
        data=np.insert(data,len(data),0)
        clock = 1 - np.arange(len(data)) % 2
        manchester = 1 - np.logical_xor(clock, data)
        self.plot(bits,manchester,'Manchester-G.E.T',0.5)

    def manchester_gethomas(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data = np.repeat(bits, 2)
        data=np.insert(data,len(data),0)
        clock = 1 - np.arange(len(data)) % 2
        manchester = np.logical_xor(clock, data)
        manchester=np.logical_not(manchester)
        self.plot(bits,manchester,'Manchester-IEEE',0.5)

    def diffmanchester(self, code):
        bits=[]
        for i in code:
            q=int(i)
            bits.append(q)
        data=[]
        for i in range(len(bits)):
            if i==0:
                if bits[i]==0:
                    q=0
                    data.append(q)
                    q=1
                    data.append(q)
                else:
                    q=1
                    data.append(q)
                    q=0
                    data.append(q)
            else:
                if bits[i]==1:
                    q=data[-1]
                    data.append(q)
                    q=1-data[-1]
                    data.append(q)
                else:
                    q=1-data[-1]
                    data.append(q)
                    q=1-data[-1]
                    data.append(q)
                    
        data=np.insert(data,len(data),0)
        self.plot(bits,data,'Differential Manchester',0.5)
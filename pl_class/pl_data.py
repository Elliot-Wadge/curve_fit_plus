#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PL_data():
    
    #takes a list of filenames like as above
    def __init__(self, filenames, **kwargs):
        self.dict, self.samples, self.dates = self.make_dictionary(filenames,**kwargs)
        
        
    def make_dictionary(self,filenames, **kwargs):
        samples = []#store the individual sample names
        unique_ids = []#store the unique dates+run
        dictionary = {}#dictionary to for convienance

        for filename in filenames:
            #get the unique ids by filtering out any non-digits
            numeric_filter = filter(str.isdigit, filename)
            date_runs = ''.join(numeric_filter)
            
            #open the filename and read header
            f = open(filename, 'r')
            header = f.readline()
            f.close()
            
            #extract the sample id from header
            start = header.find('\t') + 2
            length = header[start:].find('_')
            if length == -1:#also check if it was done using spacing instead of underscores
                length = header[start:].find(' ')
            
            #do the extraction
            sample = header[start: start + length]

            #load the data
            data = np.genfromtxt(filename, **kwargs)
            data1 = data[0,:]
            data2 = data[1,:]
            
            #if this is a duplicate sample
            if sample in samples:
                #add it to the dictionary in the sub dictionary under the unique ids
                dictionary[sample][date_runs] = [data1,data2]

            else:
                #if its the first 
                samples.append(sample)#append it to the sample lst
                dictionary[sample] = {date_runs: [data1,data2]} #add the subdictionary with the unique id to the existing dictionary
                
            unique_ids.append(date_runs)

        print(samples)
        print(unique_ids)
        return dictionary, samples, unique_ids
    
    
    #plots any amount of samples by name
    def plot_sample(self,sample_names,*args, **kwargs):
        leg = []
        fig = plt.figure(figsize = [14,8])
        for key in sample_names:
            ID_sub_dict = self.dict[key]
            for sub_key in ID_sub_dict.keys():
                data = ID_sub_dict[sub_key]
                plt.plot(data[0], data[1],*args,**kwargs)
                leg.append(key + '-' + sub_key)
                
        plt.legend(leg)
        plt.show()
        
        
    #plots by id name
    def plot_id(self,IDs,*args, **kwargs):
        leg = []
        fig = plt.figure(figsize = [14,8])
        for ID in IDs:
            values = self.dict.values()
            keys = list(self.dict.keys())
            for i,value in enumerate(values):
                key = keys[i]
                if ID in value.keys():
                    data = value[ID]
                    plt.plot(data[0], data[1],*args, **kwargs)
                    leg.append(key + '-' + ID)
        plt.show()
        
        
    #plots all of the samples                
    def plot_all(self,*args, **kwargs):
        leg = []
        fig = plt.figure(figsize = [14,8])
        for i, dates in enumerate(self.dict.values()):
            keys = list(self.dict.keys())
            for j, data in enumerate(dates.values()):
                sub_keys = list(self.dict[keys[i]].keys())
                plt.plot(data[0],data[1],*args,**kwargs)
                leg.append(keys[i] + '-' + sub_keys[j])
        plt.legend(leg)
        plt.show()
        
        
    #append a new sample to the dictionary
    def append(self,sample,ID,data):
        
        if sample in self.samples:
            self.dict[sample][ID] = [data[:,0],data[:,1]]
        else:
            self.dict[sample] = {ID: [data[:,0],data[:,1]]}
    
    
    #get a sample
    def __getitem__(self,key):
        return self.dict[key]
    
    
    #get the length of the dictionary
    def __len__(self):
        return len(self.dict)


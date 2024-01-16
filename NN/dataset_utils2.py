import torch                                                                                # Library: Pytorch 
import torch.utils.data as utils                                                            # Library: Pytorch Dataset

class Format_Dataset(utils.Dataset):

    def __init__(self, data_params, choice):
        
        self.choice = choice 
        self.samples = torch.Tensor(data_params['samples'])             # Gather: Data Samples
        if(self.choice.lower() == 'train'): 
            self.labels = torch.Tensor(data_params['labels'])           # Gather: Data Labels
        
    def __getitem__(self, index):                                                           
        
        if(self.choice.lower() == 'train'): 
            return self.samples[index], self.labels[index]                                  # Return: Next (Sample, Label) 
        else:
            return self.samples[index]                                                     

    def __len__(self):                                                                      
        
        return len(self.samples)
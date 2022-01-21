import numpy as np

def calculate(list):
  while True:
        try:
            str = input("Enter 9 digit numbers separated by comma: ")
            result = [int(float(i)) for i in str.split(',')]
        
        except ValueError:
            print('There was no valid 9 numbers separated by comma, please try again.')
    
        else:
            if len(result) == 9:
            #print(result)

                #arrange array dimension
                na = np.reshape(result,(3,3))    
                ## mean of each row
                ma = na.mean(axis=0, keepdims=False)

                #mean of each column
                ma2 = na.mean(axis=1, keepdims=False)

                #mean of flattened matrix
                maf = np.mean(na)
                a_mean = [ma.tolist(),ma2.tolist(),maf]

                ##variance
                #variance each row
                va = np.var(na, axis=0)
                
                #variance each column
                va2 = np.var(na, axis=1)

                #variance of flattened
                vaf=np.var(na)

                #column_variace
                a_variance = [va.tolist(), va2.tolist() , vaf]
                #print(a_variance)


                #standard deviation
                #std each row
                std_a = np.std(na,axis=0, keepdims = False)

                #std each column
                std_a2=np.std(na,axis=1, keepdims = False)

                #std flattened
                std_af=np.std(na)
                #print(std_af)

                #column_std
                a_std = [std_a.tolist(), std_a2.tolist(), std_af]
                #print(a_std)
                #print(column_std)
        
                #max value 
                max_a = np.max(na, axis=0, keepdims = False)
                #print(max_a)
                max_a2 = np.max(na, axis=1, keepdims = False)
                #print(max_a2)
                max_af = np.max(na)
                #print(max_af)
                a_max = [max_a.tolist(),max_a2.tolist(),max_af]
            
                #min value 
                min_a = np.min(na, axis=0, keepdims = False)
                #print(min)
                min_a2 = np.min(na, axis=1, keepdims = False)
                #print(min)
                min_af = np.min(na)
                #print(min_af)
                a_min = [min_a.tolist(),min_a2.tolist(),min_af]
            
            
                #sum value
                sum_a = np.sum(na, axis=0, keepdims = False)
                #print(sum_a)
                sum_a2 = np.sum(na, axis=1, keepdims = False)
                #print(sum_a2)
                sum_af = np.sum(na)
                #print(sum_af)
                a_sum = [sum_a.tolist(), sum_a2.tolist() , sum_af]
            
                #dictionary using collections
                dict_array = {'mean' : a_mean,
                'variance': a_variance,
                'standard deviation': a_std,
                'max': a_max,
                'min': a_min,
                'sum': a_sum
                }
                print(dict_array)


                break
            else:
                print('Incorrect input. Try inputing 9 numbers, separated by comma')
                



    
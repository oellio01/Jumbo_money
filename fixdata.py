
import json
import math

with open('THEIRFORMAT.json', 'r') as f:
    j = json.load(f)

    for k in j:
        if (k['income'][1][1] < k['income'][0][1]): #2008
            k['income'][1][1] = math.floor((k['income'][0][1] + k['income'][2][1])/2)
        if (k['income'][2][1] < k['income'][1][1]): #2009
            k['income'][2][1] = math.floor((k['income'][1][1] + k['income'][3][1])/2)
        if (k['income'][3][1] < k['income'][2][1]): #2010
            k['income'][3][1] = math.floor((k['income'][2][1] + k['income'][4][1])/2)      
        if (k['income'][4][1] < k['income'][3][1]): #2011
            k['income'][4][1] = math.floor((k['income'][3][1] + k['income'][5][1])/2)    
        if (k['income'][5][1] < k['income'][4][1]): #2012
            k['income'][5][1] = math.floor((k['income'][4][1] + k['income'][6][1])/2)   
        if (k['income'][6][1] < k['income'][5][1]): #2013
            k['income'][6][1] = math.floor((k['income'][5][1] + k['income'][7][1])/2)  
        if (k['income'][7][1] < k['income'][6][1]): #2014
            k['income'][7][1] = math.floor((k['income'][6][1] + k['income'][8][1])/2)
        if (k['income'][8][1] < k['income'][7][1]): #2015
            k['income'][8][1] = k['income'][7][1];

        if (k['lifeExpectancy'][1][1] < k['lifeExpectancy'][0][1]): #2008
            k['lifeExpectancy'][1][1] = math.floor((k['lifeExpectancy'][0][1] + k['lifeExpectancy'][2][1])/2)
        if (k['lifeExpectancy'][2][1] < k['lifeExpectancy'][1][1]): #2009
            k['lifeExpectancy'][2][1] = math.floor((k['lifeExpectancy'][1][1] + k['lifeExpectancy'][3][1])/2)
        if (k['lifeExpectancy'][3][1] < k['lifeExpectancy'][2][1]): #2010
            k['lifeExpectancy'][3][1] = math.floor((k['lifeExpectancy'][2][1] + k['lifeExpectancy'][4][1])/2)      
        if (k['lifeExpectancy'][4][1] < k['lifeExpectancy'][3][1]): #2011
            k['lifeExpectancy'][4][1] = math.floor((k['lifeExpectancy'][3][1] + k['lifeExpectancy'][5][1])/2)    
        if (k['lifeExpectancy'][5][1] < k['lifeExpectancy'][4][1]): #2012
            k['lifeExpectancy'][5][1] = math.floor((k['lifeExpectancy'][4][1] + k['lifeExpectancy'][6][1])/2)  
        if (k['lifeExpectancy'][6][1] < k['lifeExpectancy'][5][1]): #2013
            k['lifeExpectancy'][6][1] = math.floor((k['lifeExpectancy'][5][1] + k['lifeExpectancy'][7][1])/2)
        if (k['lifeExpectancy'][7][1] < k['lifeExpectancy'][6][1]): #2014
            k['lifeExpectancy'][7][1] = math.floor((k['lifeExpectancy'][6][1] + k['lifeExpectancy'][8][1])/2)
        if (k['lifeExpectancy'][8][1] < k['lifeExpectancy'][7][1]): #2015
            k['lifeExpectancy'][8][1] = k['lifeExpectancy'][7][1];

with open('THEIRFORMAT2.json', 'w') as f:
    f.write(json.dumps(j))



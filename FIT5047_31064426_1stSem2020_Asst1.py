
 
import numpy as np
import sys

outcome = ''

def read_from_file(file_name):
    file_handle = open(file_name)
    map = file_handle.readlines()

    currentMap = []
    for line in map[1:]:
        line = list(line.strip())
        line = np.array(line)
        currentMap.append(line)
    currentMap = np.array(currentMap)
    return currentMap

currentMap=read_from_file(sys.argv[1])


        

def graphsearch(currentMap):
    
  
    #find the start point
    start_point = np.argwhere(currentMap == 'S')[0].tolist()
    start_xvalue = start_point[0]
    start_yvalue = start_point[1]
 

    #find the end point 
    end_point = np.argwhere(currentMap == 'G')[0].tolist()
    end_xvalue = end_point[0]
    end_yvalue = end_point[1]
    

    
    
    #some initialization

    CLOSED = {}
    unrepeatedCheck = []
    mountains = []
    for a in range(len(currentMap)):
        for b in range(len(currentMap)):       
            if currentMap[a][b] == 'X':
                mountains.append([a,b])
              
     
    
    map_lineCount = currentMap.shape[0]
    pointCount = 0
    h = int(((start_xvalue - end_xvalue)**2 + (start_yvalue - end_yvalue)**2)**0.5)
    g = 0
    f = g+h
    startPoint = {'N'+str(pointCount):['S',[start_xvalue,start_yvalue],g,h,f]}
    unrepeatedCheck.append([start_xvalue,start_yvalue])

   
    OPEN= startPoint
    i=0
    
 
    while i==0:
        
        #current node
        if len(OPEN)>0:
            for j1 in OPEN:
                referenceValue = OPEN[j1][4]
             
            for j2 in OPEN:
                if OPEN[j2][4] <= referenceValue:
                    referenceValue = OPEN[j2][4]
                    current_pointCount = j2


            currentPoint={current_pointCount:OPEN[current_pointCount]}
            print('current point')
            print(currentPoint)
            CLOSED[current_pointCount]= OPEN[current_pointCount]
            del OPEN[current_pointCount]
       
            x = currentPoint[current_pointCount][1][0]
            y = currentPoint[current_pointCount][1][1]
            unrepeatedCheck.append([x,y])
          
            
            
            if x != end_xvalue or y != end_yvalue:
                child = {}
                nextStep = {'R':[x,y+1],'RD':[x+1,y+1],'D':[x+1,y],'LD':[x+1,y-1],'L':[x,y-1],'LU':[x-1,y-1],'U':[x-1,y],'RU':[x-1,y+1]}
                #mountianLimitCheck & boundaryCheck
               
                if [x,y+1] in mountains:
                    for d1 in list(nextStep):
                        if d1 == 'R' or d1 == 'RD' or d1 == 'RU':
                            del nextStep[d1]
                            
 

 
 
                if [x,y-1] in mountains:
                    for d2 in list(nextStep):
                        if d2 == 'L' or d2 == 'LD' or d2 == 'LU':
                            del nextStep[d2]
          

                        
                if [x+1,y] in mountains:
                    for d3 in list(nextStep):
                        if d3 == 'D' or d3 == 'RD' or d3 == 'LD':
                            del nextStep[d3]
     
                  
   
                if [x-1,y] in mountains:
                    for d4 in list(nextStep):
                        if d4 == 'U' or d4 == 'LU' or d4 == 'RU':
                            del nextStep[d4]
                     
                  
                        
                for l in list(nextStep):
                    if nextStep[l] in mountains:
                        del nextStep[l]
             
        
                for k in list(nextStep):
                    if nextStep[k][0] >= map_lineCount or nextStep[k][1] >= map_lineCount or nextStep[k][0] < 0 or nextStep[k][1] < 0:
                        del nextStep[k]
                        
    

                
                
                for m in nextStep:
                    #unrepeatedCheck
                   if len(m) == 2:
                            child_gvalue = currentPoint[current_pointCount][2]+1
                   elif len(m) == 1:
                            child_gvalue = currentPoint[current_pointCount][2]+2
                   child_hvalue = int(((nextStep[m][0] - end_xvalue)**2 + (nextStep[m][1] - end_yvalue)**2)**0.5)
                   child_fvalue = child_gvalue + child_hvalue
                   selectedStep = currentPoint[current_pointCount][0]
                   pointCount+=1
                   child['N'+str(pointCount)]=[selectedStep+'-'+m,nextStep[m],child_gvalue,child_hvalue,child_fvalue]
                   for z in list(child):
                       if child[z][1] in unrepeatedCheck:
                           del child[z]
                           
                OPEN.update(child)
                print('child')
                print(child)
                print('OPEN')
                print(OPEN)
                print('CLOSED')
                print(CLOSED)
                print()
                
                
            else:
                print('Mission Completed!')
                currentPoint[current_pointCount][0] = currentPoint[current_pointCount][0] + '-G'
                print(currentPoint)
                outcome = currentPoint[current_pointCount][0] + ' ' + str(currentPoint[current_pointCount][2])
                file_out = open(sys.argv[2],'w')
                print(outcome,file = file_out)
                file_out.close()             
                i=1
        else:
            print('ERROR! Cant find available path!')
            outcome = 'NO-PATH'
            file_out = open(sys.argv[2],'w')
            print(outcome,file = file_out)
            file_out.close()
            i=1

graphsearch(currentMap)


 
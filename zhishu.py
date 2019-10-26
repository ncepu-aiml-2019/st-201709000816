#zhishu.py
c=1
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            c=0       
    if c==1:
         print(i)
    c=1
    
            
        

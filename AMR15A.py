n = int(input())

weapon = input().split()
weapon = list(map(int, weapon))

lucky = 0
unlucky = 0

for x in weapon:
    
    if x%2 == 0:
        lucky += 1 
        
    else:
        unlucky += 1 
        
if lucky>unlucky:
    print("READY FOR BATTLE")
    
else:
    print("NOT READY")

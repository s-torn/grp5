start=int(input('hur mycket sätter du in på kontot? '))
interest_rate=float(input('vad är räntan? '))
years=int(input('hur många år sparar du?'))
savings=start
i=0

while i<years:
    savings*=interest_rate
    i+=1
print(f' Efter {years} års sparande hardu {round(savings,2)} kr på kontot.') 

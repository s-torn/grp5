start=int(input('Hur mycket sätter du in på kontot? '))
interest_rate=float(input('Vad är räntan? '))
years=int(input('Hur många år sparar du? '))
savings=start
i=0
while i<years:
    savings*=interest_rate
    i+=1
print(f'Efter {years} års sparande har du {round(savings,2)} kr på kontot.')
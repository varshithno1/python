a = input("Enter Time (Format = \"[Hour]:[Minutes]\"): ")
b = a.split(":")
hour = int(b[0])
mins = int(b[1])

if 0 <= hour <= 24 and 0 <= mins <= 60:
    hour = hour % 12
    if mins == 60:
        hour += 1
        mins = 0
    hour = hour + mins / 60
    diffunits = abs(hour - mins / (60/12))
    ang = diffunits * (360/12)
    minorang = min( ang , 360 - ang)
    print(f"The angle between the hour hand and minute hand is : {minorang:.2f}°")
else:
    print("Enter a valid Time.")
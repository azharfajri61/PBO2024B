print("### REQUEST TACTICAL DOLL ###")
fajri  = input("Masukkan nama Tactical Doll :")
fajri1 = input("Masukkan nama Firepower :")
fajri2 = input("Masukkan Rate of Fire :")
fajri3 = input("Masukkan Accuracy :")
fajri4 = input("Masukkan Evasion ")
demage_per_second = round (float(fajri1) * float(fajri2)/60,2)
combat_effectiveness = int(30 * float(fajri) + (40 * (float(fajri2) ** 2)/120) + (15 * (float(fajri3) + float(fajri4))))

print("### SUCCESS ###")
print("Tactical Doll:" + str(fajri))
print("Firepower:" + str(fajri1))
print ("Rate of Fire : " +str(fajri2))
print("Accurancy:" + str(fajri3)) 
print("Evasion: " + str(fajri4))
print("Damage per second: " +str(demage_per_second))
print("combat Effectiveness: " + str(combat_effectiveness))
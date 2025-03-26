spaceship_name = "yag"
fuel_level =75
crew_size =3
planet = "Earth"


time_to_launch = "T-minus " + "10" + " seconds"
print("🚀 Welcome aboard the", spaceship_name, "with", crew_size, "dinosaurs!")


fuel_level = int(input(" enter fuel: "))


if fuel_level >= 80:
    print("🦖✅ Plenty of fuel! Launching in 3...2...1...🚀")
elif 10 < fuel_level < 80:
    print("🛑⚠️ Fuel is a bit low. Consider refueling before launch.")
else:
    print("❌ Not enough fuel! Mission aborted!")


print("🌟 Counting stars:")
for i in range (10):
    print("star")


    fuel = 50


while 10 < fuel_level <100:
    print("🛸 Floating through space... Fuel left:", fuel_level, "%")
    fuel_level -= 10


else:
    print("🚨 Out of fuel! Time to refuel!")


    dino_crew = [crew_size]


print("👨‍🚀 Meet the Jurassic Space Crew!")
print("🦕 Captain")
print("🦖 First Officer")
print("🦓 Engineer")
print("🦖 Scientist")
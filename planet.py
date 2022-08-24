# write a programe to find distance between 2 planets
planet1=input("Select planet 1 ")
planet2=input("Select planet 2 ")
mercury=35000000
venus=67000000
earth=93000000
mars=142000000
jupiter=484000000
saturn=889000000
uranus=1790000000
planet1='mercury'
if(planet1=='mercury'):
    if(planet2=='venus'):
        distance=mercury-venus
    elif planet2=='earth':
        distance=mercury-earth
    elif planet2=='mars':
        distance=mercury-mars
    elif planet2=='jupiter':
        distance=mercury-jupiter
    elif planet2=='saturn':
        distance=mercury-saturn
    elif planet2=='uranus':
        distance=mercury-uranus
    elif planet2=='neptune':
        distance=mercury-neptune
if(distance<0):
    distance=distance*(-1)
print(f"distance is {distance}")
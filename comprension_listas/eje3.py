personas = [('pedro',33),('ana',3),('juan',13),('carla',45)]
personas_mayores = [per for per in personas if per[1]>=18]
print(personas_mayores)
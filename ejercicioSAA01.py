import matplotlib.pyplot as plt

x = [1, 1, 1.5, 2, 2, 2, 3, 3, 3, 3.5, 3.75, 4, 5.1, 5.6, 6.1, 7]
y = [12, 7, 9, 11, 9, 5, 10, 6, 2, 8, 3, 2, 3, 4, 1, 2]
classes = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1]


from sklearn.neighbors import KNeighborsClassifier
data = list(zip(x, y))
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(data, classes)

new_x = 2.5
new_y = 7
new_x2 = 5.5
new_y2 = 4.5
new_point = [(new_x, new_y)]
new_point2 = [(new_x2, new_y2)]

prediction = knn.predict(new_point)
prediction2 = knn.predict(new_point2)

re = 'null'
plt.scatter(x + [new_x] + [new_x2], y + [new_y] + [new_y2], c=classes + [prediction[0]] + [prediction2[0]])
plt.plot
punto1 = [prediction[0]].pop(0)
punto2 = [prediction2[0]].pop(0)
    
if punto1 == 0:
    re = "Verde"
else:
    re = "Rojo"
plt.text(x=new_x-1.7, y=new_y-0.7, s="new point, class: "+re)

if punto2 == 0:
    re = "Verde"
else:
    re = "Rojo"
plt.text(x=new_x2-1.7, y=new_y2-0.7, s="new point, class: "+re)

plt.show()



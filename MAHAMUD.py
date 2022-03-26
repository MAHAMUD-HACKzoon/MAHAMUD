import matplotlib.pyplot as plt
import random
no_of_colors=5
color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]
print(color)
for j in range(no_of_colors):
    plt.scatter(random.randint(0,10),random.randint(0,10),c=color[j],s=200)
plt.show()

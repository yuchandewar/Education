import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Set up the animation
def animate():
    global width_range, height_range, bars

    # Create the figure and axis objects
    fig = plt.figure(figsize=(8, 4))
    ax = fig.add_subplot(111)

    # Get the range values from the parameters
    width_range, height_range = (0.8, 0.3), (0.5, 1)
    bars = []
    def __init__(self):
        self.widthes = [(width_range[0] - i * 0.2,
                       height_range[1] + i * 0.1) for i in range(5)]
        self.bars = []
    def __init__(self):
        self.widthes = [(width_range[0] - i * 0.2,
                         height_range[1] + i * 0.1) for i in range(5)]
        self.bars = []

    def init(self):
        # Clear the canvas
        ax.clear()
        return []

    def update(frame):
        ax.clear()
        if frame < len(bars):
            x, y = bars[frame]
            ax.bar(x, y, width=width_range[0] - frame * 0.2,
                   height=height_range[1] + frame * 0.1, color='black', alpha=0.5)

        # Remove the last bar from the plot
        if len(bars) > 0:
            bars.pop()

        return []

def animate(frame):
    global bars
    if not bars:
        # Reset the plot
        bars = [(i, height_range[1] + i * 0.1) for i in range(5)]

    update(frame)
    return []

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)

ani = FuncAnimation(fig, animate, frames=range(10), init_func=lambda: [])
plt.show()


# -- Online SQL Editor to Run SQL Online.
# -- Use the editor to create new tables, insert data and all other SQL operations.
  
# --SELECT first_name, age
# --FROM Customers;

# --INSERT INTO Customers (customer_id,first_name,last_name,age,country)
# --VALUES(6,"Yashpal","Chandewar",20,"IND");

# --UPDATE Customers SET country="IND" WHERE age=22;

# --DELETE FROM Orders WHERE order_id=5

# --SELECT Customers.customer_id,Orders.order_id,Customers.first_name
# --FROM Customers LEFT JOIN Orders
# --ON Customers.customer_id = Orders.order_id 


# SELECT Customers.customer_id,Orders.order_id,Customers.first_name,Customers.last_name
# FROM Customers INNER JOIN Orders
# ON Customers.customer_id = Orders.order_id
# WHERE 300 < Orders.amount 

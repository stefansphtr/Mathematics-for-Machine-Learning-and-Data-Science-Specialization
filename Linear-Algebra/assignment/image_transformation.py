#!/usr/bin/env python

# Import the library
import numpy as np
import matplotlib.pyplot as plt

heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray")
  plt.title(name_identifier)
  plt.show()
  plt.clf()

# Show heart image
show_image(heart_img, "Heart Image")

# Invert color
inverted_heart_img  = 255 - heart_img  
show_image(inverted_heart_img, "Inverted heart")

# Rotate heart
rotated_heart_img  = heart_img.T
show_image(rotated_heart_img, "Rotated heart")

# Random Image
random_img = np.random.randint(0,255, (7,7))
show_image(random_img, "Random Image")

# Solve for heart image

# Solve equation
# random_img . x = heart_img

# Create the x var
x = np.linalg.solve(random_img, heart_img)
# Create solved_heart_img var
solved_heart_img = random_img@x

# Plot the x
show_image(x, "x")
# Show the plot
show_image(solved_heart_img, "Solved Heart Image")
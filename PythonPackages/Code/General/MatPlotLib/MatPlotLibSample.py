# Matplotlib Code Example

import matplotlib.pyplot as plt
import numpy as np

# Example 1

#
# Here is a simple example of how to use Matplotlib to create 
# an array and perform basic operations on it
#


plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# Example 2:

#
# Here`s a more complex example of how to plot 
# multiple lines on the same plot:
#
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Matplotlib - Version Check:
# You can check the version of Matplotlib by using the following command:
#
print(matplotlib.__version__)

# Example - Files:

# Matplotlib can also save plots to various file formats, 
# such as PNG, PDF, SVG, and more. Here`s
# an example of how to save a plot as a PNG file:
# 
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig('output.png')

import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the stationarity triangle
# Vertex 1: (0, 1) -> phi1 + phi2 = 1 and phi2 - phi1 = 1 intersect
# Vertex 2: (2, -1) -> phi1 + phi2 = 1 and phi2 = -1 intersect
# Vertex 3: (-2, -1) -> phi2 - phi1 = 1 and phi2 = -1 intersect
vertices = np.array([[0, 1], [2, -1], [-2, -1], [0, 1]])

plt.figure(figsize=(8, 7))

# Plot the triangle
plt.plot(vertices[:, 0], vertices[:, 1], 'b-', linewidth=2, label='Stationarity Boundary')
plt.fill(vertices[:, 0], vertices[:, 1], 'skyblue', alpha=0.3, label='Stationary Region')

# Add the constraint equations as text labels
plt.text(1.1, 0.2, r'$\phi_1 + \phi_2 = 1$', rotation=-45, fontsize=12)
plt.text(-1.8, 0.2, r'$\phi_2 - \phi_1 = 1$', rotation=45, fontsize=12)
plt.text(0, -1.15, r'$|\phi_2| = 1$', ha='center', fontsize=12)

# Axis formatting
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-2.5, 2.5)
plt.ylim(-1.5, 1.5)
plt.xlabel(r'$\phi_1$', fontsize=14)
plt.ylabel(r'$\phi_2$', fontsize=14)
plt.title('AR(2) Process: The Stationarity Triangle', fontsize=15)
plt.legend(loc='upper right')

# Use this for MkDocs/Web compatibility
plt.savefig('ar2_triangle.svg', format='svg') 
plt.show()
import pandas as pd
import matplotlib.pyplot as plt


filtered_data = pd.read_csv('filtered_star_data.csv')


star_names = filtered_data['Star Name'].tolist()
mass_values = filtered_data['Mass'].tolist()
radius_values = filtered_data['Radius'].tolist()
distance_values = filtered_data['Distance'].tolist()
gravity_values = filtered_data['Gravity'].tolist()

plt.figure(figsize=(10, 6))


plt.subplot(221)
plt.bar(star_names, mass_values, color='blue')
plt.xlabel('Star Name')
plt.ylabel('Mass (kg)')
plt.title('Star Name vs Mass')
plt.xticks(rotation=45)


plt.subplot(222)
plt.bar(star_names, radius_values, color='green')
plt.xlabel('Star Name')
plt.ylabel('Radius (m)')
plt.title('Star Name vs Radius')
plt.xticks(rotation=45)


plt.subplot(223)
plt.bar(star_names, distance_values, color='red')
plt.xlabel('Star Name')
plt.ylabel('Distance (light years)')
plt.title('Star Name vs Distance')
plt.xticks(rotation=45)


plt.subplot(224)
plt.bar(star_names, gravity_values, color='purple')
plt.xlabel('Star Name')
plt.ylabel('Gravity (m/s^2)')
plt.title('Star Name vs Gravity')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

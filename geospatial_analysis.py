import pandas as pd
import folium

# Load dataset
df = pd.read_csv("sales_data.csv")

print(df.head())

# Create Map
m = folium.Map(
    location=[16.8,79.5],
    zoom_start=6
)

# Add Markers
for i,row in df.iterrows():

    color="green"

    if row["Demand"]=="High":
        color="red"
    elif row["Demand"]=="Medium":
        color="orange"

    folium.Marker(
        location=[row["Latitude"],row["Longitude"]],
        popup=f"""
City: {row['City']}
Sales: {row['Sales']}
Demand: {row['Demand']}
Stores: {row['Stores']}
""",
        icon=folium.Icon(color=color)
    ).add_to(m)

# Save Map
m.save("business_map.html")

print("Map Created Successfully")

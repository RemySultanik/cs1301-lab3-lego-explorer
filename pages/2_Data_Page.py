# Lab 3: API data page
# TODO: Rename this file to fit your page. Keep the number at the front, since it sets the
#       page's order in the sidebar (for example, 2_Pokedex.py).
#
# This page shows data from your API, processed with your own Python code. No AI on this page.
# It should have:
#   - at least 2 meaningful user inputs (for example st.selectbox, st.text_input, st.slider)
#   - at least 2 dynamic visuals that change based on the user's input: charts, displays of
#     images, or other visualizations (see the example website for examples!)

import requests
import streamlit as st
import time

key = st.secrets["rebrickableKey"]

baseUrl = f"https://rebrickable.com/api/v3/lego/sets/?key={key}&page_size=1000"

legoData = []

while baseUrl:
    response = requests.get(baseUrl)
    pageData = response.json()
    for item in pageData["results"]:
        legoData.append(item)
    baseUrl = pageData["next"]
    time.sleep(1)
    

st.header("Average number of pieces in Lego sets per year")

if "minSelection" not in st.session_state:
    st.session_state["minSelection"] = 1949
if "maxSelection" not in st.session_state:
    st.session_state["maxSelection"] = 2026

minSelection = st.selectbox("Select a minimum year", range(1949, st.session_state["maxSelection"] + 1), key = "minSelection")
st.session_state["minYear"] = minSelection
maxSelection = st.selectbox("Select a maximum year", range(minSelection, 2027), key = "maxSelection")
st.session_state["maxYear"] = maxSelection

yearParts = {}
yearCount = {}
setsInYear = {}

for i in legoData:
    year = i["year"]
    parts = i["num_parts"]
    if year not in yearParts:
        yearParts[year] = 0
        yearCount[year] = 0
    if year not in setsInYear:
        setsInYear[year] = []
    setsInYear[year].append(i)
    yearParts[year] += parts
    yearCount[year] += 1

avgDict = {"Year": [], "Average Parts": []}
for y in range(minSelection, maxSelection + 1):
    if y in yearParts:
        avg = yearParts[y] / yearCount[y]
        avgDict["Year"].append(str(y))
        avgDict["Average Parts"].append(avg)


st.line_chart(data=avgDict, x="Year", y="Average Parts", color=["#FF0000"])

st.header("Top 10 Lego sets by largest number of pieces released in a particular year")
yearSelection = st.selectbox("Select a year", range(1949, 2027), key = "yearSelection")
st.session_state["year"] = yearSelection

top10 = []
top10Sorted = []
top10Dict = {"Name": [], "Parts": []}

yearSets = setsInYear[yearSelection]

for item in yearSets:
    count = 0
    for otherItem in yearSets:
        if otherItem["num_parts"] > item["num_parts"]:
            count += 1
    if count < 10:
        top10.append(item)

while len(top10) > 0:
    maxSet = top10[0]
    for item in top10:
        if item["num_parts"] > maxSet["num_parts"]:
            maxSet = item
    top10Sorted.append(maxSet)
    top10.remove(maxSet)

for i in top10Sorted:
    top10Dict["Name"].append(i["name"])
    top10Dict["Parts"].append(i["num_parts"])

st.bar_chart(top10Dict, x="Name", y="Parts", sort = False)
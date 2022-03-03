import requests
from bs4 import BeautifulSoup
import json

#importing necessary libraries
#BeautifulSoup - Python module for web scraping
#website- "https://getlatka.com/"

results_final=[]
for i in range (1,1244):
    link='https://getlatka.com/?page='+str(i)
    r=requests.get(link)
    
    #creating a beautifulsoup object 
   
    soup=BeautifulSoup(r.text,'lxml')
    
    # table class="data-table_table__2P6Tl"- from inspecting the source code of the web site 
    
    table=soup.find('table',"data-table_table__2P6Tl")
    
    # extracting column names  and data seperately
    
    headers=[heading.text for heading in table.find_all('th')]
    table_rows=[rows for rows in table.find_all('tr')]
    
    #mapping the columan names with the data extracted 
    
    results=[{headers[index]:cell.text for index,cell in enumerate(row.find_all('td'))} for row in table_rows]
    
    # appending all the extracted data to results_final list
    results_final.append(results)

# converting the data scrapped as a list to a JSON file  using .dumps() function in json module 

jsonStr = json.dumps(results_final)
with open("intern assignment final.json", "w") as outfile:
    outfile.write(jsonStr)

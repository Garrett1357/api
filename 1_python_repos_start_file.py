import requests 

import json 

 

# Make an API call and store the response. 

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 

headers = {'Accept': 'application/vnd.github.v3+json'} 

r = requests.get(url, headers=headers) 

print(f"Status code: {r.status_code}") 

 

outfile = open('output.json', 'w') 

 

response_dict = r.json() 

 

json.dump (response_dict,outfile,indent=4) 

 

#print how many repos are in the file 

list_of_repos = response_dict['items'] 

 

print(type(list_of_repos)) 

 

print(len(list_of_repos)) 

 

first_repo = list_of_repos[0] 

 

#number of keys 

print(f'Number of keys (data points): {len(first_repo)}') 

 

#print each key 

for key in first_repo: 

    print(key) 

 

#print full name, the url, the licence name and topics for first repo 

full_name = first_repo["full_name"] 

url = first_repo["owner"]["url"] 

license_name = first_repo["license"]["name"] 

for topic in first_repo["topics"]: 

    print(f'Topic: {topic}') 

print(f'Full name: {full_name}') 

print(f'Url: {url}') 

print(f'license nmae {license_name}') 

 

repo_names, stars = [], [] 

 
 

for repo in list_of_repos[:10]: 
    repo_names.append(repo["full_name"]) 
    stars.append(repo["stargazers_count"]) 

 

from plotly.graph_objs import bar 

from plotly import offline 

 

data = [ 

        { 

            "type": "bar", 

                "x": repo_names, 

                "y": stars, 

        "marker": { 

            "color": "rgb(60,100,150)", 

            "line": { 

                "width": 1.5, 

                "color": "rgb(25,25,25)", 

            }, 

        }, 

        "opacity": .6 

    } 

] 

 

my_layout = { 
"title": "Most Starred Python Projects on Github", 
"xaxis": {"title":"Repository"}, 
"yaxis": {"title":"Stars"}, 
} 

 

fig = {"data": data, "layout":my_layout} 

 

offline.plot(fig, filename="python_repos.html") 

 
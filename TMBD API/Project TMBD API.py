#!/usr/bin/env python
# coding: utf-8

# Project Details
# 
# For this project, we are using the TMDb (The Movie Database) API.
# TMDb API enables you to find out the latest information about TV Shows, Movies and the biggest names in entertainment sector for a marvelous and fun TV/Movie watching experience.
# TMDb documentation link
# After joining TMDb, you can easily generate a new developer API key using this link
# Our Motivation for using TMDb API
# By collecting the data using TMDb API one can recommend TV Shows, Movies and all sorts of entertainment on the basis of user’s affinity to specific genres, actors, likes and dislikes.
# We can find details about upcoming TV Shows and Movies.
# We can find what is the most popular and/ or exclusive/new content at a given time.

# TMDb 1.1
# Find the 'id' of the movie "Andhadhun" using TMDb API.
# 
# Output Format:
# Print the id of the movie.

# In[6]:


# API key = 41ac02b200f1a5dd894c9036cdd9e7f9
import requests

# header ={'user_key':'41ac02b200f1a5dd894c9036cdd9e7f9'} 
# data = {'query' : 'Andhadhun', 'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'}

# a = requests.get('https://api.themoviedb.org/3/search/movie', params = data)

# data = a.json()
# for i in data['results']:
#         if i['title'] == 'Andhandhun':
#             print(i['id'])
data = {'query' : 'Andhadhun', 'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'}
req = requests.get('https://api.themoviedb.org/3/search/movie', params = data)

py = req.json()

for i in py['results']:
    if i['title'] == 'Andhadhun':
        print('Id of Andhadhun movie: ')
        print(i['id'])


# TMDb 1.2
# 
# Fetch the company id company 'Marvel Studios' using TMDb. Print the id.

# In[8]:


import requests
data = {'query':'Marvel Studios', 'api_key' :'41ac02b200f1a5dd894c9036cdd9e7f9'}
response = requests.get('https://api.themoviedb.org/3//search/company', params = data)
data = response.json()
results = data.get('results')
for result in results:
    if result.get('name') == 'Marvel Studios':
        print('Company id of marvel Studios: ')
        print(result.get('id'))


# TMDb 1.3
# 
# Find the vote count and vote average of the movie "3 Idiots" using the TMDb API
# Output format: Vote Count , Vote Average

# In[14]:


import requests
import json

data = {'api_key': 'e226f4a5f5bace766952aa0d17182959', 'query': '3 Idiots'}
response = requests.get('https://api.themoviedb.org/3/search/movie', params=data)
movie_data = response.json()['results'][0]

vote_count = movie_data['vote_count']
vote_average = movie_data['vote_average']

print("Vote Count:", vote_count)
print("Vote Average:", vote_average)


# TMDb 1.4
# 
# Fetch the names of top 5 similar movies to 'Inception' from the TMDb API.
# Note
# While fetching the movie id, use the "original_title" field not the "title". Because the "title" field may contain duplicate values.
# 
# Output Format:
# Print the name of the movies in a new line.
# movie_name_1
# movie_name_2
# and so on

# In[15]:


import requests
api_key = '41ac02b200f1a5dd894c9036cdd9e7f9' 
api_link = "https://api.themoviedb.org/3" 
params = {'query':"Inception", 'api_key':api_key}
response = requests.get(api_link + "/search/movie", params=params)
data = response.json()
results = data.get('results')
for result in results:
    if result.get('title') == 'Inception':
        id = result.get('id')
# print(id)
params2 = {'api_key':api_key}
response2 = requests.get(api_link + "/movie/" + str(27205) + "/similar", params=params2)
data2 = response2.json()
results2 = data2.get('results')
for result in results2[:5]:
    print(result.get("title"))


# TMDb 1.5
# 
# Fetch the top rated english movies in the US region using the TMDb API. From the result, print the first 10 movies which have original language as english. Also print their genres.
# Note: Do not use the search/movies API for finding genres.
# 
# Output Format:
# movie_name_1 - genre_1, genre_2 ....
# and so on..

# In[16]:


import requests
url = 'https://api.themoviedb.org/3/movie/top_rated'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9', 'page' : 1, 'region': 'US'})
data = response.json()
data = [row for row in data['results'] if row['original_language']=='en']

url = 'https://api.themoviedb.org/3/genre/movie/list'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'})
data1 = response.json()
gn = {}
for row in data1['genres']:
    gn[row['id']] = row['name']


for row in data[:10]:
    print(row['original_title'],'-' , ', '.join([ gn[g] for g in row['genre_ids']])+',')
    


# TMDb 2.1
# 
# Find the name and birthplace of the present most popular person according to TMDb API.
# Output Format:
# id
# name - birthplace

# In[17]:


import requests
api_key = "e226f4a5f5bace766952aa0d17182959"
api_link = "https://api.themoviedb.org/3"
params = {'api_key':api_key}
header = {'Accept': 'application/json'}
response = requests.get(api_link + "/person/popular", headers = header, params=params)
data = response.json()
id_of_most_popular = data.get('results')[0].get('id')
print(id_of_most_popular)
name_of_most_popular = data.get('results')[0].get('name')
response2 = requests.get(api_link + "/person/" + str(id_of_most_popular), headers = header, params=params)
data2 = response2.json()
print(name_of_most_popular,"-", data2.get("place_of_birth"))


# TMDb 2.2
# 
# Fetch the Instagram and Twitter handle of Indian Actress "Alia Bhatt" from the TMDb API.
# Output Format
# Print the Instagram and Twitter IDs space separated.
# instagram_id twitter_id

# In[22]:


import requests
url = 'https://api.themoviedb.org/3/search/person'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9', 'query' : 'Alia Bhatt'})
data = response.json()
id = data['results'][0]['id']

url = 'https://api.themoviedb.org/3/person/' + str(id) + '/external_ids'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'})
data = response.json()
Instagram   = data['instagram_id']
Twitter  = data['twitter_id']
print("Instagram:", Instagram)
print("Twitter:", Twitter)


# TMDb 2.3
# 
# Fetch the names of the character played by Tom Cruise in the movies:
# Top Gun
# Mission: Impossible - Fallout
# Minority Report
# Edge of Tomorrow
# Output Format:
# Print the names of the characters played by Tom Cruise line separated, in the respective order given in question.

# In[23]:


import requests
movies = ['Top Gun', 'Mission: Impossible - Fallout', 'Minority Report', 'Edge of Tomorrow']
url = 'https://api.themoviedb.org/3/search/movie'
ids = {}
for movie in movies:
    response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9', 'query' : movie})
    data = response.json()
    id = data['results'][0]['id']
    ids[movie] = id

for movie, id in ids.items():
    url1 = 'https://api.themoviedb.org/3/movie/'+ str(id) + '/credits'
    response = requests.get(url1, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'})
    data = response.json()
    #print(data)
    for row in data['cast']:
        if row['name'] == 'Tom Cruise':
            print(row['character'])
            break


# TMDb 2.4
# 
# Did James McAvoy play a role in the movie Deadpool 2. Print Yes or No.

# In[26]:


import requests

# Search for the movie "Deadpool 2"
search_url = 'https://api.themoviedb.org/3/search/movie'
search_response = requests.get(search_url, params={'api_key': '41ac02b200f1a5dd894c9036cdd9e7f9', 'query': 'Deadpool 2'})
search_data = search_response.json()
movie_id = search_data['results'][0]['id']

# Get the movie credits
credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
credits_response = requests.get(credits_url, params={'api_key': '6149f1c70750c8d49b3274ff886a308f'})
credits_data = credits_response.json()

# Check if James McAvoy is credited
flag = False
for row in credits_data.get('cast', []):
    if row.get('name') == 'James McAvoy':
        credit_id = row['credit_id']
        flag = True
        break

if flag:
    print('Yes')
else:
    print('No')


# TMDb 2.5
# 
# Using the result obtained in previous question, find out if James McAvoy was credited for his role in movie Deadpool 2. Print Yes or No.

# In[27]:



import requests
## Write your code here
apiKey = '41ac02b200f1a5dd894c9036cdd9e7f9'

res = requests.get('https://api.themoviedb.org/3/search/person',params={'api_key':apiKey,'query':'McAvoy'}) 
data=res.json()
ID  = data['results'][0]['id']

res = requests.get(f'https://api.themoviedb.org/3/person/{ID}/movie_credits',params={'api_key':apiKey}) 
data=res.json()

for result in data['cast']:
if result['title']=='Deadpool 2':
    a=result['character']
    print('No')


# TMDb 3.1
# 
# Fetch the overview of the TV Show "FRIENDS" using TMDb API.
# Output Format:
# Print the Overview.

# In[28]:


import requests
## Write your code here
api_key = "e226f4a5f5bace766952aa0d17182959"
api_link = "https://api.themoviedb.org/3"
params = {'api_key':api_key,'query':'FRIENDS'}
header = {'Accept': 'application/json'}
response = requests.get(api_link + "/search/tv", headers = header, params=params,verify=False)
data = response.json()
results = data.get('results')
for result in results:
    if result.get('name') == 'Friends':
        print(result.get('overview'))


# TMDb 3.2
# 
# Fetch the name and air date of S06E05 of the TV Show 'The Big Bang Theory' from TMDb API.
# Output Format:
# episode_name - air_date

# In[29]:


import requests
url = 'https://api.themoviedb.org/3/search/tv'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9', 'query' : 'The Big Bang Theory'})
data = response.json()
id = data['results'][0]['id']

url = 'https://api.themoviedb.org/3/tv/' + str(id)+'/season/6/episode/5'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'})
data = response.json()
print(data['name'],'-',data['air_date'])


# TMDb 3.3
# 
# Fetch the trending TV Shows for the week from the TMDb API and print the taglines of the top 5 shows. If there is no tagline, print 'Empty' instead
# Output Format:
# Print the taglines in new line.

# In[30]:


import requests
url = 'https://api.themoviedb.org/3/search/tv'
response = requests.get(url, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9', 'query' : 'Money Heist', 'first_air_date_year':2017})
data = response.json()
id = data['results'][0]['id']

url1 = 'https://api.themoviedb.org/3/tv/'+ str(id) + '/credits'
response = requests.get(url1, params = {'api_key' : '41ac02b200f1a5dd894c9036cdd9e7f9'})
data = response.json()
#print(data)
f = 0
m = 0
for actor in data['cast']:
    if actor['gender'] == 1:
        f += 1
    elif actor['gender'] == 2:
        m += 1
print(m,f)


# TMDb 3.4
# 
# Print the names of all the TV shows to be aired today whose original language is english.
# Output Format:
# Print the name of each TV show in a new line.

# In[31]:


import requests 
api_key = "e226f4a5f5bace766952aa0d17182959" 
api_link = "https://api.themoviedb.org/3" 
params = {'language':"en" , 'api_key':api_key} 
header = {'Accept': 'application/json'} 
response = requests.get(api_link + "/tv/airing_today/", headers = header, params = params) 
data= response.json() 
page_number = data.get('total_pages') 
for i in range(1, page_number + 1): 
    params = {'language':"en" , 'api_key':api_key, 'page':i} 
    response = requests.get(api_link + "/tv/airing_today/", headers = header, params = params) 
    data= response.json() 
    results = data.get('results') 
    for result in results: 
        if result.get('original_language') == 'en': 
            print(result.get('name'))


# TMDb 3.5
# 
# Count the number of males and females in the cast of "Money Heist" using the TMDb API.
# Output Format:
# Print the count of male and female space separated.
# male_count female_count

# In[34]:


import requests

# Search for the TV show "Money Heist" with a specific first_air_date_year
url = 'https://api.themoviedb.org/3/search/tv'
response = requests.get(url, params={'api_key': '6149f1c70750c8d49b3274ff886a308f', 'query': 'Money Heist', 'first_air_date_year': 2017})
data = response.json()

# Check if there are any search results
if 'results' in data and data['results']:
    id = data['results'][0]['id']

    # Get the TV show credits
    url1 = f'https://api.themoviedb.org/3/tv/{id}/credits'
    response = requests.get(url1, params={'api_key': '6149f1c70750c8d49b3274ff886a308f'})  # Use the same API key
    data = response.json()

    # Initialize counters for male and female actors
    male_count = 0
    female_count = 0

    # Loop through the cast and count male and female actors
    for actor in data.get('cast', []):
        gender = actor.get('gender')
        if gender == 1:  # Female
            female_count += 1
        elif gender == 2:  # Male
            male_count += 1

    print("Male Actors:", male_count)
    print("Female Actors:", female_count)
else:
    print("No results found for 'Money Heist' in 2017.")


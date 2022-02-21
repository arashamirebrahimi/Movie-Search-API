import requests,json
apiKey='http://www.omdbapi.com/?apikey=e07f4a84&'
movieName=str(input("Please Enter a movie you wanna search:"))
apiKey +='t=' + movieName
response = requests.get(apiKey)
print("Title: ",response.json()['Title'])
print("Year: ",response.json()['Year'])
print("Director: ",response.json()['Director'])
print("Language: ",response.json()['Language'])


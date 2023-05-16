from requests_oauthlib import OAuth1Session
import json
import csv
# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = "4tJkjceO2O3ObFafRvaiPavzW"
consumer_secret ="7Xxp5hv40keKozVUKCKxr7d0QE5AaNWXNUyZiFZu6mGzQbGAYO"
access_token = "1344983454304198656-iqxg2VihiFjQuV7N0k3AJlMDd3zmiS"
access_token_secret = "iF5g1GR6PDZ9U0dhN9xWkMcB1alkd8gRtrmS53JTXxKmN"
bearer_token = "AAAAAAAAAAAAAAAAAAAAADMXngEAAAAAVuJ7RgU53wvZ0KQJP82ZJzLVHF0%3DPFqxgAsVOffGTQsN1xuc0Z5L30tVeUiUsC1yxFBpvlBE8wCRQy"


# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld

#Please write a piece of code to scrape and summarize the 
# userID, userName, pinned Tweet ID, and creation date of your own account with Twitter Official API
 

fields = "id,name,pinned_tweet_id,created_at"
params = {"user.fields": fields}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)


# # Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]



# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.get("https://api.twitter.com/2/users/me", params=params)

if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()


print(json.dumps(json_response, indent=4))


# Extract relevant information
name = json_response['data']['name']
username = json_response['data']['username']
created_at = json_response['data']['created_at']
id = json_response['data']['id']

# Create a list to store the data
csv_data = [
    ["Name", "Username", "Created At", "ID"],
    [name, username, created_at, id]
]

# Define the CSV file path
csv_file = "data.csv"

# Write the data to the CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)


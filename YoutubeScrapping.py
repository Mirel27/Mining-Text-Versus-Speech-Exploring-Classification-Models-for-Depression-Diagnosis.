# Databricks notebook source
!pip install google-api-python-client
import requests
import csv
from io import StringIO
from googleapiclient.discovery import build
api_key ="AIzaSyDzbb5mwXSsdR2czvKaNdi5Ufq5G3PV_uk"
youtube = build('youtube', 'v3', developerKey=api_key)

# COMMAND ----------

#---------Working--------

#To do filter out only the ones in english

# Set your API key
#api_key = "YOUR_API_KEY"

api_key = "YOUR_API_KEY"
# Create YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Define your keywords
keywords = [
    "depressionvlogs",
    "Depressionvlogs",
    "DEPRESSIONVLOGS",
    "depressionVlogs",
    "DepressionVLogs",
    "DEPRESSIONvlogs",
    "DepressionVlogs",
    "DEPRESSIONVlogs",
    "DEPRESSIONVLOGS"   
]

# Set the desired number of video links
desired_links = 2000

# Set the maximum results per request (maximum: 50)
max_results_per_request = 50

# Calculate the number of requests needed
num_requests = int(desired_links / max_results_per_request) + 1

# Search for videos and retrieve links
video_links = []
video_ids = []

for keyword in keywords:
    for i in range(num_requests):
        search_response = youtube.search().list(
            q=keyword,
            part='id',
            order='date',
            type='video',
            videoCaption='closedCaption',
            relevanceLanguage= 'en',
            maxResults=max_results_per_request,
            pageToken=None if i == 0 else nextPageToken
        ).execute()

        # Extract video links from the search results
        for item in search_response['items']:
            if item['id']['kind'] == 'youtube#video':
                video_id = item['id']['videoId']
                video_link = f"https://www.youtube.com/watch?v={video_id}"
                video_links.append(video_link)
                video_ids.append(video_id)
            

        # Check if the desired number of links is reached
        if len(video_links) >= desired_links:
            break

        # Check if there are more pages of results
        nextPageToken = search_response.get('nextPageToken')
        if not nextPageToken:
            break

    # Check if the desired number of links is reached
    if len(video_links) >= desired_links:
        break

# Print the video links
for id in video_ids[:desired_links]:
    print(id)


# COMMAND ----------

#---------Working--------

#To do filter out only the ones in english

# Set your API key
#api_key = "YOUR_API_KEY"

api_key ="YOUR_API_KEY"
# Create YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Define your keywords
keywords = [
    "Happy",
    "Positive",
    "Smile"   
]

# Set the desired number of video links
desired_links = 2000

# Set the maximum results per request (maximum: 50)
max_results_per_request = 50

# Calculate the number of requests needed
num_requests = int(desired_links / max_results_per_request) + 1

# Search for videos and retrieve links
video_links = []
video_ids = []

for keyword in keywords:
    for i in range(num_requests):
        search_response = youtube.search().list(
            q=keyword,
            part='id',
            order='date',
            type='video',
            videoCaption='closedCaption',
            relevanceLanguage= 'en',
            maxResults=max_results_per_request,
            pageToken=None if i == 0 else nextPageToken
        ).execute()

        # Extract video links from the search results
        for item in search_response['items']:
            if item['id']['kind'] == 'youtube#video':
                video_id = item['id']['videoId']
                video_link = f"https://www.youtube.com/watch?v={video_id}"
                video_links.append(video_link)
                video_ids.append(video_id)
            

        # Check if the desired number of links is reached
        if len(video_links) >= desired_links:
            break

        # Check if there are more pages of results
        nextPageToken = search_response.get('nextPageToken')
        if not nextPageToken:
            break

    # Check if the desired number of links is reached
    if len(video_links) >= desired_links:
        break

# Print the video links
for id in video_ids[:desired_links]:
    print(id)


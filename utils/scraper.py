import pandas as pd
import streamlit as st
from apify_client import ApifyClient

# Constants
TWEETS_COLUMNS_LIST = [
    "url",
    "createdAt",
    "id",
    "isReply",
    "inReplyToId",
    "isRetweet",
    "isQuote",
    "viewCount",
    "retweetCount",
    "likeCount",
    "replyCount",
    "lang",
    "author__createdAt",
    "author__location",
    "author__name",
    "author__id",
    "author__description",
    "author__followers",
    "author__verified",
    "text"
]

REMOVE_COLUMNS_COMMENTS = [
    "author__name",
    "author__id",
    "author__description",
]

APIFY_ACTOR_ID = '61RPP7dywgiy0JPD0'
APIFY_TOKEN = st.secrets['APIFY_TOKEN']

# Start client
client = ApifyClient(APIFY_TOKEN)


def flatten_response(response):
    """ Returns a flat dictionary with unnested values """

    return {
        "url": response.get("url"),
        "createdAt": pd.to_datetime(response.get("createdAt")),
        "id": response.get("id"),
        "isReply": response.get("isReply"),
        "inReplyToId": response.get("inReplyToId", None), # Uses None if inReply is false
        "isRetweet": response.get("isRetweet"),
        "isQuote": response.get("isQuote"),
        "viewCount": response.get("viewCount"),
        "retweetCount": response.get("retweetCount"),
        "likeCount": response.get("likeCount"),
        "replyCount": response.get("replyCount"),
        "lang": response.get("lang"),
        "author__createdAt": pd.to_datetime(response["author"].get("createdAt")),
        "author__location": response["author"].get("location"),
        "author__name": response["author"].get("name"),
        "author__id": response["author"].get("id"),
        "author__description": response["author"].get("description"),
        "author__followers": response["author"].get("followers"),
        "author__verified": response["author"].get("isVerified"),
        "text": response.get("text")
    }


def main_tweet_dataframe(url):
    """ Given a tweet URL, returns a dataframe for it """

    # Input validation
    if 'x.com' not in url and 'twitter.com' not in url:
        return {'error': 'Input is not a tweet URL'}

    run_input = {
        "startUrls": [url],
    }

    run = client.actor(APIFY_ACTOR_ID).call(run_input=run_input)

    response = [dictionary for dictionary in client.dataset(run["defaultDatasetId"]).iterate_items()][0]

    flattened_data = flatten_response(response)

    # Convert the flattened dictionary to a DataFrame and return
    return pd.DataFrame([flattened_data], columns=TWEETS_COLUMNS_LIST)


def comments_dataframe(url):
    """ Given a tweet URL, returns a dataframe for the comments related to that tweet """

    # Input validation
    if 'x.com' not in url and 'twitter.com' not in url:
        return {'error': 'Input is not a tweet URL'}

    one_tweet_id = str(url.split('/')[-1])

    run_input_comment = {
        "conversationIds": [one_tweet_id],
        "tweetLanguage": "es",
        "maxItems": 50
    }

    run_comment = client.actor(APIFY_ACTOR_ID).call(run_input=run_input_comment)

    response_comment = [dictionary for dictionary in client.dataset(run_comment["defaultDatasetId"]).iterate_items()]

    flattened_responses = [flatten_response(response) for response in response_comment]

    include_columns = [column for column in TWEETS_COLUMNS_LIST if column not in REMOVE_COLUMNS_COMMENTS]

    # Convert the flattened dictionary to a DataFrame and return
    return pd.DataFrame(flattened_responses, columns=include_columns)


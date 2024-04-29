from celery import shared_task
import requests
import os
import logging

logger = logging.getLogger(__name__)
logger.debug("Test log message from tasks")

def send_facebook_message():
    page_access_token = 'YOUR_PAGE_ACCESS_TOKEN'
    recipient_id = '429716328007568'
    message_text = 'Hello'

    url = f"https://graph.facebook.com/v12.0/me/messages?access_token={page_access_token}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        # Handle error
        print(f"Error: {response.text}")
    else:
        print(f"not error: {response.text}")

"""
@shared_task(bind=True, max_retries=3, retry_backoff=True)
def send_facebook_message(self, page_access_token, recipient_id, message_text):
    logger.debug("Starting send_facebook_message task")

    url = "https://graph.facebook.com/v13.0/me/messages"
    headers = {"Content-Type": "application/json"}
    data = {
        "messaging_type": "RESPONSE",
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    }
    params = {
        "access_token": page_access_token
    }

    try:
        logger.debug(f"Sending request to Facebook API: {url}")
        response = requests.post(url, headers=headers, json=data, params=params)
        response.raise_for_status()
        logger.info(f"Successfully sent message: {response.json()}")
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        logger.error(f"Response: {response.text}")
    except Exception as err:
        logger.error(f"Error sending message: {err}")

    logger.debug("Finished send_facebook_message task")
    
"""
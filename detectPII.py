import json
import boto3
import base64
import io

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('comprehend')
    file_content = event['file']
    decoded_content = base64.b64decode(file_content)
    decodedStr = str(decoded_content, "utf-8")
    response = client.contains_pii_entities(
    Text=decodedStr,
    LanguageCode='en'
    )
    #response = client.detect_labels(
    #Image={
    #    'Bytes': decoded_content
    #},
    #MaxLabels=10,
    #MinConfidence=77
    #)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

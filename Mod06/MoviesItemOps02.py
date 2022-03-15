from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="https://dynamodb.ap-northeast-1.amazonaws.com")

    table = dynamodb.Table('Movies')

    try:
        #結果整合性
        response = table.get_item(Key={'year': year, 'title': title})
        #強い整合性
        # response = table.get_item(Key={'year': year, 'title': title}、ConsistentRead＝True)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)

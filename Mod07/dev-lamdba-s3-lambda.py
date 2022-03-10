import boto3
import os

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    "Process upload event"
    for record in event['Records']:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        size = record["s3"]["object"]["size"]
        print("Received event. Bucket: [%s], Key: [%s], Size: [%s]" % (bucket, key, size))

        tmpkey = key.replace("/", "")
        download_file_path = "/tmp/" + tmpkey
        target_bucket_name = "{}-target".format(bucket)
        backup_file_name = "{}.backup".format(key)

        s3_client.download_file(bucket, key, download_file_path)
        s3_client.upload_file(download_file_path, target_bucket_name, backup_file_name)
        
        if os.path.exists(download_file_path):
            os.remove(download_file_path)

# This is used for debugging, it will only execute when run locally
if __name__ == "__main__":
    # local debugging, send a simulated event
    fake_s3_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "dev-lambda-kubota"
                    },
                    "object": {
                        "key": "hi.gif"
                    }
                }
            }
        ]
    }

    fake_context = []
    lambda_handler(fake_s3_event, fake_context)

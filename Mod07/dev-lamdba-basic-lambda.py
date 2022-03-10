import json

def lambda_handler(event, context):
    myName = event["name"]
    print(myName)
    return "Hello World! " + myName

# This is used for debugging, it will only execute when run locally
if __name__ == "__main__":
    # local debugging, send a simulated event
    fake_s3_event = {
        "name": "Kubota"
    }

    fake_context = []
    lambda_handler(fake_s3_event, fake_context)
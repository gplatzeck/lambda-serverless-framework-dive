import time

def hello(event, context):
    print("second update!")
    time.sleep(4)
    return "hello-world"

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

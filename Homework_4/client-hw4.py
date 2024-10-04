import http.client
import sys

def get_resource(resource):
    # Establish connection to the server
    conn = http.client.HTTPConnection("localhost", 8070)

    # Send HTTP GET request for the resource
    conn.request("GET", f"/{resource}")

    # Get the server's response
    response = conn.getresponse()

    # Extract status code, content type, and content
    status_code = response.status
    content_type = response.getheader("Content-Type")
    content = response.read().decode()

    print(f"Response Status Code: {status_code}")
    print(f"Content Type: {content_type}")
    print("Response Content:")
    print(content)

    conn.close()


get_resource(sys.argv[1])

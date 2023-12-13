import requests

def main():
    # Prompt for url ex.fenty.com
    url = input("Enter the URL (e.g., fenty.com): ")

    # Show menu for HTTP method and print 
    print("Please select the HTTP method:")
    print("[1] GET")
    print("[2] POST")
    print("[3] PUT")
    print("[4] DELETE")
    print("[5] HEAD")
    print("[6] PATCH")
    print("[7] OPTIONS")

    # conevert input to number 
    method_choice = int(input("Enter your choice: "))

    #  input for HTTP methods
    http_methods = {
        1: "GET",
        2: "POST",
        3: "PUT",
        4: "DELETE",
        5: "HEAD",
        6: "PATCH",
        7: "OPTIONS",
    }

    # Get chosen method
    chosen_method = http_methods.get(method_choice)

    # Print summaries
    print(f"\nSummary:")
    print(f"URL: {url}")
    print(f"Method: {chosen_method}")

    # Confirm with user
    confirm = input("Do you want to proceed? (y/n): ")
    if confirm.lower() not in ["y", "yes"]:
        print("Exiting...")
        return

    # Send request
    response = requests.request(chosen_method, url)

    # Print response status and translated message
    status_code = response.status_code
    status_message = {
        200: "OK",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Site not found",
        405: "Method Not Allowed",
        500: "Internal Server Error",
    }.get(status_code, f"Unknown error: {status_code}")
    print(f"\nStatus: {status_code} ({status_message})")

    # Print response headers
    print("\nHeaders:")
    for key, value in response.headers.items():
        print(f"- {key}: {value}")

    # Handle potential response content
    if response.content:
        print("\nContent:")
        try:
            print(response.text)
        except UnicodeDecodeError:
            print("[Binary content]")

if __name__ == "__main__":
    main()

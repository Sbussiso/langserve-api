import requests

while True:
    # Replace with the actual URL of your deployed API
    api_url = "http://localhost:8000/gpt-one-shot/invoke/"

    prompt = input("Enter prompt: ")
    # Define the input topic (e.g., "cats")
    input_data = {"input": {"prompt": prompt}}

    # Make a POST request to the API
    response = requests.post(api_url, json=input_data)
    print(f"RESPONSE: {response}")

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        print(f"REQUEST RECEIVED: {result}")
        # Adjusted to fetch the joke from the correct location in the response JSON
        final_output = result.get("output", {}).get("content", "")
        print()
        print(f"AI Response: {final_output}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

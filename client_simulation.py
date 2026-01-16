import requests
import time

# -----------------------------------------------------
# URL of the Google Cloud Function:
# -----------------------------------------------------
url = "https://receive-data-55062664928.asia-southeast1.run.app" 


# Data to send (Simulating a car)
payload = {
    "plate": "PKD 1234",
    "status": "Entered"
}

print(f"🚗 Attempting to connect to: {url}")

try:
    # Send the data to Google Cloud
    response = requests.post(url, json=payload)
    
    # Check if it worked
    if response.status_code == 200:
        print("✅ SUCCESS! Server replied:", response.text)
    else:
        print(f"❌ FAILED. Status: {response.status_code}")
        print("Reason:", response.text)

except Exception as e:
    print(f"❌ Error: {e}")
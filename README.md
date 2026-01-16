# Smart Parking IoT System (GCP Proof of Concept)

## 📌 Project Overview
This repository contains the source code for the **Smart Parking IoT Solution**, a serverless Proof of Concept (PoC) designed for **CPC357: IoT Architecture & Smart Applications**.

The system demonstrates a decoupled architecture where an edge device (simulated client) sends license plate data to a **Google Cloud Run Function**, which processes the data and persists it in a real-time **Cloud Firestore** database.

##  System Architecture
The solution leverages Google Cloud Platform (GCP) components:
1.  **Edge Layer:** Python Client (Simulating ESP32-CAM) captures vehicle data.
2.  **Gateway Layer:** Google Cloud Run Function (Python 3.10) acts as a secure HTTP endpoint.
3.  **Storage Layer:** Cloud Firestore (NoSQL) stores vehicle logs and provides real-time listeners.

##  Repository Contents
* `main.py` - The backend logic deployed on Google Cloud Run Functions. It handles HTTP requests and writes to Firestore.
* `requirements.txt` - Dependency list for the Cloud environment (Functions Framework, Google Cloud Firestore).
* `client_simulation.py` - A local Python script that simulates an IoT camera detecting a car and sending a POST request to the cloud.

##  Setup & Installation

### 1. Cloud Function Deployment
The `main.py` script is designed to be deployed on **Google Cloud Run Functions** (2nd Gen).
* **Runtime:** Python 3.10+
* **Trigger:** HTTPS (Allow unauthenticated invocations for testing)
* **Region:** asia-southeast1

### 2. Local Client Simulation
To test the system locally, update the `url` variable in `client_simulation.py` with your deployed Cloud Function URL:

```python
url = "[https://YOUR-REGION-PROJECT.run.app](https://YOUR-REGION-PROJECT.run.app)"

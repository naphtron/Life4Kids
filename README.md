# 🌟 Life4Kids USSD Donation App 🌟

## Overview

Welcome to the Life4Kids USSD Donation App repository. Life4Kids is a conceptual charity organization created to address the need for a USSD (Unstructured Supplementary Service Data) application that facilitates donation payments in Kenya. The goal is to support the basic needs of Kenya's most vulnerable children through an efficient and accessible platform.

![Life4Kids Logo](logo.jpg)

The Life4Kids USSD Donation App utilizes M-Pesa, Kenya's leading mobile money platform, as the payment portal. By integrating with M-Pesa, donors can securely and conveniently make contributions, ensuring that funds are directed towards supporting children in need.

However, it's important to note that the USSD app has not been launched live. This delay is due to the high cost associated with purchasing a USSD code, which is currently prohibitive for this project.

While Life4Kids is not an actual charity organization, it serves as a fictional entity created solely for the purpose of developing and testing the USSD Donation App. The ultimate goal is to deploy this application to aid real charity organizations in efficiently collecting donations to support needy children in Kenya.

## Key Features:

- **M-Pesa Integration:** Seamlessly connects with M-Pesa for secure donation transactions.
- **Accessibility:** Allows donors to contribute without requiring internet access, making it accessible to a wider audience across Kenya.

## Installation

To set up the Life4Kids USSD Donation App for development, follow these steps:

1. Install Flask and other dependencies:
   
    ```bash
    pip install flask africastalking
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/naphtron/Life4Kids.git
    cd Life4Kids
    ```

3. Set Up:

    - Create a developer account with Safaricom to access the payment gateway. Visit the [Safaricom Developer Portal](https://developer.safaricom.co.ke/) for more information. 
    - Create a developer account with Africa's Talking to use their USSD service. Visit the [Africa's Talking website](https://africastalking.com/) for registration details.
    -  Register a callback URL with Africa's Talking to handle USSD session notifications and set up a shared service code to use for testing the USSD app.For this and additional information, please visit. [Africastalking USSD Tutorial](https://developers.africastalking.com/tutorials/building-an-offline-account-management-application-using-ussd)

 ### Port Forwarding with Ngrok

To enable your local development environment to be accessible externally, which is necessary for services like Africa's Talking and Mpesa Express callbacks, we recommend using Ngrok for port forwarding.

1. **Install Ngrok**: If you haven't installed Ngrok, download it from [Ngrok's official website](https://ngrok.com/download). Follow the installation instructions provided on their site.

2. **Start Ngrok**: Once Ngrok is installed, you can expose your local server to the internet by running the following command in your terminal: `ngrok http 5000`


This command assumes your local development server is running on port 5000. Adjust the port number according to your server's configuration.

3. **Access Port Forwarding Information**: For detailed guidance on setting up and using Ngrok for port forwarding, visit [Ngrok's documentation](https://ngrok.com/docs).
4. 
Using Ngrok, you'll receive a public URL that forwards to your local development server, allowing external services to interact with your app as if it were publicly hosted.


## Usage

Once you've set up your developer accounts, you can run the USSD app using Africa's Talking Simulator:

- Launch the [simulator](https://developers.africastalking.com/simulator) on the Africa's Talking website to test the USSD app.
- Make sure to configure port forwarding to enable your app to be accessed, and for the callbacks to work.

## Configuration

### Environment Variables

To securely manage your credentials, it's recommended to use a `.env` file. This file will store sensitive information such as your API keys and secrets, which should not be hardcoded into your application code. Here's how to set it up:

1. Create a `.env` file in the root directory of your project.
2. Populate the `.env` file with the necessary environment variables for your project. This typically includes API keys, secret tokens, and any other sensitive data that your application requires to run. Ensure that you replace placeholder values with your actual credentials.

### Configure M-Pesa Express API Credentials

1. Obtain your consumer key and consumer secret from the M-Pesa API portal. These are necessary for accessing the auth token.
2. Add these credentials to your `.env` file with the appropriate variable names.

### Set Up Africa's Talking SDK

1. Get your API key from your Africa's Talking dashboard.
2. Add this key to your `.env` file with the designated variable name for the Africa's Talking SDK.

This SDK will be configured using the API key to interact with Africa's Talking services, including USSD.

### Local Server Port Configuration

1. Decide on a local port number where your Flask app will run. This is useful for local development and testing, especially when using tools like Ngrok for port forwarding.
2. Specify this port number in your `.env` file with the corresponding variable name.

## Conclusion
If you have any suggestions, encounter any issues, or would like to contribute to the project, please don't hesitate to [reach out](mailto:ronymu2gi@gmail.com).

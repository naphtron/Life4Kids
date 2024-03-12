# 🌟 Life4Kids USSD Donation App 🌟

## Overview

Welcome to the Life4Kids USSD Donation App repository. Life4Kids is a conceptual charity organization created to address the need for a USSD (Unstructured Supplementary Service Data) application that facilitates donation payments in Kenya. The goal is to support the basic needs of Kenya's most vulnerable children through an efficient and accessible platform.

![Life4Kids Logo](logo.png)

The Life4Kids USSD Donation App utilizes M-Pesa, Kenya's leading mobile money platform, as the payment portal. By integrating with M-Pesa, donors can securely and conveniently make contributions, ensuring that funds are directed towards supporting children in need.

However, it's important to note that the USSD app is still in the development stage and has not been launched live. This delay is due to the high cost associated with purchasing a USSD code, which is currently prohibitive for this project.

While Life4Kids is not an actual charity organization, it serves as a fictional entity created solely for the purpose of developing and testing the USSD Donation App. The ultimate goal is to deploy this application to aid real charity organizations in efficiently collecting donations to support needy children in Kenya.

## Key Features:

- **M-Pesa Integration:** Seamlessly connects with M-Pesa for secure donation transactions.
- **Accessibility:** Allows donors to contribute without requiring internet access, making it accessible to a wider audience across Kenya.


Your interest and support in the Life4Kids USSD Donation App are greatly appreciated. Together, we can harness the power of technology to make a meaningful impact on the lives of Kenya's needy children.

## Installation

To set up the Life4Kids USSD Donation App for development, follow these steps:

1. Install Flask and other dependencies:
   
    ```bash
    pip install flask africastalking
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/life4kids/life4kids-ussd-app.git
    cd life4kids-ussd-app
    ```

3. Set up your developer accounts:

    - Create a developer account with M-Pesa Express API to access the payment gateway. Visit the [M-Pesa Developer Portal](https://developer.safaricom.co.ke/) for more information.
    - Create a developer account with Africa's Talking to use their USSD service. Visit the [Africa's Talking website](https://africastalking.com/) for registration details.

## Usage

Once you've set up your developer accounts, you can run the USSD app using Africa's Talking Simulator:

- Launch the simulator on the Africa's Talking website to test the USSD app as if it were running on a real phone.
- Make sure to configure port forwarding to enable your app to be accessed, and for the callbacks to work.

## Configuration

Before running the app, you'll need to set up the following configurations:

- Add your M-Pesa Express API credentials to the Flask app.
- Configure the Africa's Talking SDK with your API key and other necessary settings.

## Troubleshooting

If you encounter any issues during setup or usage, refer to the following troubleshooting tips:

- **Issue:** Unable to access the app remotely.
  **Solution:** Check your port forwarding settings and ensure they are correctly configured.

## License

This project is licensed under the MIT License.


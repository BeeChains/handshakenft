# handshakenft
handshakenft/ 
 
# My Handshake NFT Project Developing 

all for http://block1.handshakenft.hns.to/

# Objectives:

To create a decentralized trading platform for HandshakeNFT tokens.
To allow users to buy, sell, transfer, sign and add/update DNS records for their HandshakeNFT tokens.
To provide users with a secure and transparent platform for trading HandshakeNFT tokens.

# Requirements:

The platform should be accessible via a web interface or mobile app.
Users should be able to securely store and manage their HandshakeNFT tokens within the platform.
The platform should provide a simple and intuitive interface for buying, selling, transferring, signing and adding/updating DNS records for HandshakeNFT tokens.
The platform should incorporate secure and transparent smart contract functionality to handle token transactions and ownership transfers.
The platform should have robust security measures in place to protect user data and funds.
The platform should provide users with easy access to customer support in the event of any issues or concerns.

# Installation

1. Clone the HandshakeNFT Trading App repository from GitHub using the following command:
```git clone https://github.com/BeeChains/handshakenft.git```
2. Navigate to the cloned directory using the following command:
```cd handshakenft```
3. Create a virtual environment using the following command:
```python -m venv env```
4. Activate the virtual environment using the following command:
```source env/bin/activate```
5. Install the required Python packages using the following command:
```pip install -r requirements.txt```
6. Set the following environment variables:
```export FLASK_APP=app.py```
```export FLASK_ENV=development```
7. Start the Flask development server using the following command:
```flask run```

This will start the server at http://localhost:5000.

You should now be able to access the HandshakeNFT Trading App in your web browser


## too install Handshake

To interact with the Handshake blockchain and create NFTs, you need to have a Handshake node running on your machine or use the Handshake JSON-RPC API. The nft-maker-cli tool used in the script interacts with the Handshake node to create and manage NFTs.

To install and run a Handshake node, you can follow the instructions in the official Handshake documentation: <a href="https://hsd-dev.org/hsd">HSD</a> or go to <a href="https://handshake.org/">Handshake.org</a> or latest releases https://github.com/handshake-org/hsd/releases

# Example of how you can create a simple web page using Flask and Python to register Handshake NFT subdomains:

## Installation

1. Install Python 3.9 or above: https://www.python.org/downloads/
2. Install Flask using the command ```pip install Flask```
3. Clone the repository: ```git clone https://github.com/BeeChains/handshakenft```

## Deployment

1. Create a HandshakeNFT subdomain on Namebase: https://www.namebase.io/domains
2. Create a TXT record for the subdomain with the metadata URL. If you're using Namebase, go to the DNS section for your subdomain and add a TXT record with the    following value: "txt=handshakenft/"
3. Replace the TODO placeholders in the app.py file with your own code.
4 Start the server by running the command python app.py
5.Access the application by opening a web browser and navigating to http://localhost:5000.

## Frontend Code
Using Flask for a frontend that allows users to buy and sell NFTs:

## Backend
python

You can create a new route for each API endpoint (e.g., /buy, /sell, /transfer, /sign, /add_dns_record) and call the appropriate function for each endpoint.



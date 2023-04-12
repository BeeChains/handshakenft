from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

METADATA_URL = "https://handshakenft/"

def get_nft_metadata(nft_id):
    metadata_url = METADATA_URL + nft_id
    response = requests.get(metadata_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def buy_nft(nft_id, price, buyer):
    # Get the seller information from the NFT metadata
    nft_metadata = get_nft_metadata(nft_id)
    if nft_metadata is None:
        return jsonify({'error': 'NFT not found'}), 404
    seller = nft_metadata.get('owner')
    if seller is None:
        return jsonify({'error': 'Invalid NFT metadata'}), 400
    
    # Verify that the buyer has sufficient funds
    if buyer['balance'] < price:
        return jsonify({'error': 'Insufficient funds'}), 400
    
    # Transfer funds from buyer to seller using smart contract
    transfer_funds(nft_id, price, buyer, seller)
    
    # Update ownership information in NFT metadata
    nft_metadata['owner'] = buyer
    update_nft_metadata(nft_id, nft_metadata)
    
    # Return success response
    return jsonify({'success': True}), 200

def sell_nft(nft_id, price, seller):
    # Get the NFT metadata
    nft_metadata = get_nft_metadata(nft_id)
    if nft_metadata is None:
        return jsonify({'error': 'NFT not found'}), 404
    
    # Verify that the seller is the current owner of the NFT
    if nft_metadata.get('owner') != seller:
        return jsonify({'error': 'You are not the owner of this NFT'}), 401
    
    # Update the NFT metadata with the asking price
    nft_metadata['price'] = price
    update_nft_metadata(nft_id, nft_metadata)
    
    # Return success response
    return jsonify({'success': True}), 200

def transfer_nft(nft_id, new_owner):
    # Get the NFT metadata
    nft_metadata = get_nft_metadata(nft_id)
    if nft_metadata is None:
        return jsonify({'error': 'NFT not found'}), 404
    
    # Verify that the current user is the owner of the NFT
    if nft_metadata.get('owner') != new_owner:
        return jsonify({'error': 'You are not the owner of this NFT'}), 401
    
    # Update the NFT metadata with the new owner
    nft_metadata['owner'] = new_owner
    update_nft_metadata(nft_id, nft_metadata)
    
    # Return success response
    return jsonify({'success': True}), 200

def sign_nft(nft_id, signature):
    # Get the NFT metadata
    nft_metadata = get_nft_metadata(nft_id)
    if nft_metadata is None:
        return jsonify({'error': 'NFT not found'}), 404
    
    # Update the NFT metadata with the signature
    nft_metadata['signature'] = signature
    update_nft_metadata(nft_id, nft_metadata)
    
    # Return success response
    return jsonify({'success': True}), 200

def add_dns_record(nft_id, record):
    dns_url = METADATA_URL + nft_id + "/dns"
    payload = {"dns": record}
    response = requests.post(dns_url, json=payload)
    if response.status_code == 200:
        return True
    else:
        return False

@app.route('/buy', methods=['POST'])
def handle_buy_request():
    request_data = request.get_json()
    nft_id = request_data.get('nft_id')
    price = request_data.get('price')
    buyer = request_data.get('buyer')
    response, status_code = buy_nft(nft_id, price, buyer)
    return jsonify(response), status_code

@app.route('/sell', methods=['POST'])
def handle_sell_request():
    request_data = request.get_json()
    nft_id = request_data.get('nft_id')
    price = request_data.get('price')
    seller = request_data.get('seller')
    response, status_code = sell_nft(nft_id, price, seller)
    return jsonify(response), status_code

@app.route('/transfer', methods=['POST'])
def handle_transfer_request():
    request_data = request.get_json()
    nft_id = request_data.get('nft_id')
    new_owner = request_data.get('new_owner')
    response, status_code = transfer_nft(nft_id, new_owner)
    return jsonify(response), status_code

@app.route('/sign', methods=['POST'])
def handle_sign_request():
    request_data = request.get_json()
    nft_id = request_data.get('nft_id')
    signature = request_data.get('signature')
    response, status_code = sign_nft(nft_id, signature)
    return jsonify(response), status_code

@app.route('/dns', methods=['POST'])
def handle_dns_request():
    request_data = request.get_json()
    nft_id = request_data.get('nft_id')
    record = request_data.get('record')
    success = add_dns_record(nft_id, record)
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Failed to add DNS record'}), 400
   

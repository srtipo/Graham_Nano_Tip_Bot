from io import BytesIO
from flask import current_app as app

import json
import requests
import settings

class RPC():
    wallet_id = settings.wallet

    def __init__(self, node_url=settings.node_ip, node_port=settings.node_port):
        self.node_url = node_url
        self.node_port = node_port

    def communicate_wallet(self, wallet_command):
        formattedUrl = "http://{0}:{1}".format(self.node_url, self.node_port)
        try:
            r = requests.post(formattedUrl, json=wallet_command, timeout=300)
            return r.json()
        except requests.exceptions.RequestException:
            return None

    def account_create(self, wallet=wallet_id):
        action = {
            "action":"account_create",
            "wallet":wallet
        }
        response = self.communicate_wallet(action)
        if response is not None and 'account' in response:
            return response['account']
        else:
            return None

    def receive_block(self, account, hash, wallet=wallet_id):
        action = {
            "action":"receive",
            "wallet":wallet,
            "account":account,
            "block":hash
        }
        return self.communicate_wallet(action)

    def retrieve_block(self, hash):
        action = {
            "action":"block",
            "hash":hash
        }
        resp = self.communicate_wallet(action)
        if 'contents' in resp:
            return json.loads(resp['contents'])
        else:
            return None

    def account_info(self, account, wallet=wallet_id):
        action = {
            "action":"account_info",
            "wallet":wallet,
            "account":account,
            "representative":"true"
        }
        return self.communicate_wallet(action)

    def validate_account(self, account):
        """Returns True if the validate_account_number RPC
        action says account is valid"""
        action = {
            "action":"validate_account_number",
            "account":account
        }
        resp = self.communicate_wallet(action)
        return resp['valid'] == '1'

    def process_block(self, block):
        """Broadcast a block to the network"""
        action = {
            "action":"process",
            "block":block
        }
        return self.communicate_wallet(action)

    def account_balances(self, accounts):
        """Get balance for all accounts"""
        action = {
            "action":"accounts_balances",
            "accounts":accounts
        }
        return self.communicate_wallet(action)

    def balance(self, account):
        """Get balance for specific account"""
        action = {
            "action":"account_balance",
            "account":account
        }
        return self.communicate_wallet(action)

    def pending(self, account, count=5, threshold=100000000000000000000000000000):
        """Return pending blocks for a specific account"""
        action = {
            "action":"pending",
            "account":account,
            "count":count,
            "threshold":threshold
        }
        return self.communicate_wallet(action)
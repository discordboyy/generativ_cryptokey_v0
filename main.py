from solders.keypair import Keypair
import base58
import json
import os

WALLET_FILE = "wallet.json"


def create_wallet():
    keypair = Keypair()

    public_key = str(keypair.pubkey())
    private_key = base58.b58encode(bytes(keypair)).decode("utf-8")

    wallet_data = {
        "public_key": public_key,
        "private_key": private_key
    }

    return wallet_data


def save_wallet(wallet_data):
    with open(WALLET_FILE, "w") as f:
        json.dump(wallet_data, f, indent=4)


def load_wallet():
    if not os.path.exists(WALLET_FILE):
        return None

    with open(WALLET_FILE, "r") as f:
        return json.load(f)


if __name__ == "__main__":

    wallet = load_wallet()

    if wallet:
        print("🔁 Loaded existing wallet")
    else:
        print("🆕 Creating new wallet")
        wallet = create_wallet()
        save_wallet(wallet)

    print("=" * 60)
    print("SOLANA WALLET")
    print("=" * 60)
    print(f"Public Address:\n{wallet['public_key']}\n")
    print(f"Private Key (Base58):\n{wallet['private_key']}")
    print("=" * 60)
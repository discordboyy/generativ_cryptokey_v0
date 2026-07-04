import os
import requests
from dotenv import load_dotenv

load_dotenv()

PUBLIC_KEY = os.getenv("PUBLIC_KEY")

RPC_URL = "https://api.mainnet-beta.solana.com"


def get_balance(pubkey: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [pubkey]
    }

    response = requests.post(RPC_URL, json=payload)
    data = response.json()

    if "result" not in data:
        raise Exception(f"RPC error: {data}")

    lamports = data["result"]["value"]

    sol = lamports / 1_000_000_000  # 1 SOL = 1e9 lamports

    return sol


if __name__ == "__main__":
    if not PUBLIC_KEY:
        print("❌ PUBLIC_KEY not found in .env")
        exit()

    balance = get_balance(PUBLIC_KEY)

    print("=" * 50)
    print("SOLANA WALLET BALANCE")
    print("=" * 50)
    print(f"Address: {PUBLIC_KEY}")
    print(f"Balance: {balance} SOL")
    print("=" * 50)
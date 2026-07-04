import os
import requests
import base58
import base64
from dotenv import load_dotenv
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.system_program import transfer, TransferParams
from solders.transaction import Transaction
from solders.hash import Hash

load_dotenv()

RPC_URL = "https://api.mainnet-beta.solana.com"

PUBLIC_KEY = os.getenv("PUBLIC_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

def load_keypair():
    secret = base58.b58decode(PRIVATE_KEY)
    return Keypair.from_bytes(secret)


# ---------------- RPC CORE ---------------- #

def rpc(method, params):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }
    return requests.post(RPC_URL, json=payload).json()


def get_balance(pubkey):
    res = rpc("getBalance", [pubkey])
    lamports = res["result"]["value"]
    return lamports / 1_000_000_000


def get_transactions(pubkey, limit=5):
    return rpc("getSignaturesForAddress", [pubkey, {"limit": limit}])


# ---------------- FEATURES ---------------- #

def show_balance():
    bal = get_balance(PUBLIC_KEY)
    print(f"\n💰 Balance: {bal} SOL\n")


def show_history():
    res = get_transactions(PUBLIC_KEY)

    print("\n📜 Recent Transactions:")
    for tx in res["result"]:
        print(f"- {tx['signature']} | slot {tx['slot']}")
    print()


# ---------------- SIMULATED TRANSFER ---------------- #

def send_sol(to_address: str, amount_sol: float):
    sender = load_keypair()
    receiver = Pubkey.from_string(to_address)

    lamports = int(amount_sol * 1_000_000_000)

    ix = transfer(
        TransferParams(
            from_pubkey=sender.pubkey(),
            to_pubkey=receiver,
            lamports=lamports
        )
    )

    blockhash_resp = rpc("getLatestBlockhash", [])
    blockhash_str = blockhash_resp["result"]["value"]["blockhash"]
    blockhash = Hash.from_string(blockhash_str)

    tx = Transaction.new_with_payer([ix], sender.pubkey())
    tx.sign([sender], blockhash)

    raw = bytes(tx)  
    encoded_tx = base64.b64encode(raw).decode("utf-8")

    res = rpc("sendTransaction", [
        encoded_tx,
        {
            "encoding": "base64",
            "skipPreflight": False,
            "preflightCommitment": "confirmed"
        }
    ])

    return res

def safe_send(to, amount):
    balance = get_balance(PUBLIC_KEY)

    if amount + 0.001 > balance:
        print("❌ Not enough SOL (including fee)")
        return

    return send_sol(to, amount)

# ---------------- MENU ---------------- #

def menu():
    while True:
        print("\n====================")
        print(" SOLANA WALLET CLI")
        print("====================")
        print("1. Show balance")
        print("2. Send SOL (demo)")
        print("3. Transaction history")
        print("4. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            show_balance()

        elif choice == "2":
            to = input("Send to (public key): ")
            amount = float(input("Amount SOL: "))

            result = safe_send(to, amount)

            print("\n📤 TX RESULT:")
            print(result)

        elif choice == "3":
            show_history()

        elif choice == "4":
            break

        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    menu()
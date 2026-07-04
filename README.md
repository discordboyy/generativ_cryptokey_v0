# generativ_cryptokey_v0

A simple tool for creating a Solana wallet and working with it right from your browser, without installing anything on your computer — everything runs in **GitHub Codespaces**.

With this project you can:
- generate a new Solana wallet (public + private key);
- check the wallet balance;
- send SOL to another address;
- view transaction history.

---

## ⚠️ Security Notice

- The private key (`PRIVATE_KEY`) gives full access to the wallet and the funds in it. **Never share it with anyone or publish it anywhere.**
- The `.env` file with your keys must not be committed to git or published publicly.
- All operations are performed on the real Solana **mainnet** — this is not a test network, transactions are irreversible.

---

## What you'll need

- A GitHub account (Codespaces runs right in the browser, nothing needs to be downloaded).

---

## Step 1. Create a Codespace

1. Open this repository on GitHub.
<img width="1239" height="769" alt="image" src="https://github.com/user-attachments/assets/3a418d37-3dfa-40e1-8284-898cb3b8c3af" />

2. Click the green **Code** button.
<img width="1235" height="767" alt="image" src="https://github.com/user-attachments/assets/eb266081-9be5-49d3-96d5-66818b8340c8" />

3. Go to the **Codespaces** tab.
<img width="988" height="470" alt="image" src="https://github.com/user-attachments/assets/40a5171d-ad26-45db-8022-e9049cec9c45" />

4. Click **Create codespace on main**.
<img width="972" height="536" alt="image" src="https://github.com/user-attachments/assets/01636ece-ba80-4cb8-9108-d7d9a78e0477" />

5. Wait 1–2 minutes while the Codespace sets up — a full development environment will open in your browser.

---

## Step 2. Install dependencies
<img width="1125" height="677" alt="image" src="https://github.com/user-attachments/assets/8b4afb00-8377-430b-88e0-20298ffc9e30" />

Open the `command.txt` file — it contains all the commands you need. Run them one by one in the terminal (the terminal is already open at the bottom of the Codespace window):
<img width="892" height="387" alt="image" src="https://github.com/user-attachments/assets/cdd996af-da92-44f6-9dfc-15294f8f0c86" />

```bash
source .venv/bin/activate
pip install --upgrade --force-reinstall -r requirements.txt
```

Wait until the installation of dependencies finishes.
<img width="1354" height="860" alt="image" src="https://github.com/user-attachments/assets/d5a86c2d-7fb5-4bb1-afb8-789a583ff3b7" />

---

## Step 3. Create a wallet

### If you don't have a wallet yet

Run the following in the terminal:
<img width="631" height="107" alt="image" src="https://github.com/user-attachments/assets/ceb80714-6ca0-4034-b75c-7c486c66d49b" />

```bash
python main.py
```

The script will generate a new Solana wallet and print:

- **Public Address** — the wallet's public address;
- **Private Key** — the private key.

Copy both values — you'll need them in the next step.

### If you already have a wallet

Just skip this step — use your existing keys in step 4.

---

## Step 4. Fill in the .env file
<img width="706" height="347" alt="image" src="https://github.com/user-attachments/assets/05d8e8fb-95d1-48dc-8e9f-5cabea3e68b2" />

1. Create a `.env` file in the project root (if it doesn't already exist).
2. Paste your keys into it in the following format:

```dotenv
PUBLIC_KEY=your_public_address
PRIVATE_KEY=your_private_key
```

<img width="300" height="142" alt="image" src="https://github.com/user-attachments/assets/135b9158-2c9a-4365-a808-af8acbce8ad7" />

3. Save the file. Ctrl + S

---

## Step 5. Run the wallet

Run the following in the terminal:
<img width="1042" height="552" alt="image" src="https://github.com/user-attachments/assets/0fd0417a-0eed-4865-b0a9-bdfe844eae86" />

```bash
python wallet_cli.py
```

If you get an error — copy the error text and ask the built-in AI agent in Codespace for help, it will help you figure it out.

---

## Step 6. Use the menu

After launching, a menu will appear:
<img width="677" height="230" alt="image" src="https://github.com/user-attachments/assets/a5ef36e6-729a-4691-9215-1a3410a8bd4d" />

```
====================
 SOLANA WALLET CLI
====================
1. Show balance
2. Send SOL (demo)
3. Transaction history
4. Exit
```

Choose the option you need by entering its number:

| Option | What it does |
|---|---|
| **1** | Show the wallet balance in SOL |
| **2** | Send SOL to another address (you'll be asked to enter the recipient's address and the amount) |
| **3** | Show recent transaction history |
| **4** | Exit the program |

---

## Project structure

| File | Description |
|---|---|
| `main.py` | Creates a new wallet or loads an existing one from `wallet.json` |
| `wallet_cli.py` | Main menu: balance, sending SOL, transaction history |
| `balance.py` | Standalone script for quickly checking the balance |
| `requirements.txt` | List of Python dependencies |
| `command.txt` | List of commands for installation and launch |
| `check-key.txt` | Link to [Solscan](https://solscan.io) for manually checking an address/transactions |

---

## Verifying the wallet

You can also check the balance, address, and transactions manually on [Solscan](https://solscan.io) — just paste your public address into the search bar.

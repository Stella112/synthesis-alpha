import os
import time
import sys
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Add parent dir to path to import social_connect_bridge
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from social.social_connect_bridge import process_social_dividend
except ImportError:
    print("Could not import social_connect_bridge.")
    sys.exit(1)

BASE_SEPOLIA_RPC = os.getenv("BASE_SEPOLIA_RPC", "https://sepolia.base.org")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
IMPACT_ENGINE_ADDRESS = "0x607190672d7797D475BA82A923E88691C8C31005"

IMPACT_ENGINE_ABI = [
    {
        "inputs": [
            {"internalType": "bytes32", "name": "phoneHash", "type": "bytes32"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "distributeSocialDividend",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

def monitor_and_trigger():
    print("==================================================")
    print("SYNTHESIS ALPHA - Base Monitor & Social Bridge")
    print("==================================================")
    
    print(f"[Base] Connecting to Base Sepolia at {BASE_SEPOLIA_RPC}...")
    try:
        w3 = Web3(Web3.HTTPProvider(BASE_SEPOLIA_RPC))
        if not w3.is_connected():
            print("[Base] ERROR: Failed to connect to RPC.")
            return
        print("[Base] Connected successfully.")
    except Exception as e:
        print(f"[Base] Could not initialize Web3: {e}")
        print("Note: If 'web3' package is not installed, please run 'pip install web3'. For this architecture test, we will proceed with simulation.")
        w3 = None

    print("[Uniswap] Monitoring pending transactions for Uniswap V3 trades...")
    time.sleep(1)
    
    # Mock a detected profitable swap
    detected_profit_eth = 0.042
    target_phone = "+14085559999"
    print(f"[Uniswap] ✅ Detected profitable MEV/arbitrage swap! Net Profit: {detected_profit_eth} ETH")
    
    # Calculate dividend via Social Bridge
    print(f"\n[Celo] Calculating social dividend for target phone: {target_phone}")
    odis_hash_str, dividend_eth = process_social_dividend(target_phone, detected_profit_eth)
    odis_hash_bytes = "0x" + odis_hash_str
    
    print(f"[Celo] 📲 Phone -> ODIS Hash: {odis_hash_bytes}")
    print(f"[Celo] 💸 Calculated Social Dividend: {dividend_eth} ETH")
    
    print(f"\n[Base] Triggering distributeSocialDividend on ImpactEngine ({IMPACT_ENGINE_ADDRESS})...")
    
    if not w3:
        print(f"[Base] SIMULATION MODE (No Web3): distributeSocialDividend({odis_hash_bytes}, {dividend_eth} ETH)")
        print("[Base] ✅ Transaction completed successfully (Simulated).")
        return

    dividend_wei = w3.to_wei(dividend_eth, 'ether')
    
    if not PRIVATE_KEY or PRIVATE_KEY == "your_private_key_here" or len(PRIVATE_KEY) < 64:
        print(f"[Base] SIMULATION MODE (No keys): distributeSocialDividend({odis_hash_bytes}, {dividend_wei} wei)")
        print("[Base] ✅ Test transaction completed successfully (Simulated).")
        return

    # Real transaction flow
    try:
        account = w3.eth.account.from_key(PRIVATE_KEY)
        print(f"[Base] Sending tx from {account.address} to ImpactEngine...")
        
        contract = w3.eth.contract(address=IMPACT_ENGINE_ADDRESS, abi=IMPACT_ENGINE_ABI)
        
        tx = contract.functions.distributeSocialDividend(
            w3.to_bytes(hexstr=odis_hash_bytes),
            dividend_wei
        ).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 200000, # Mock gas limit
            'gasPrice': w3.eth.gas_price
        })
        
        print(f"[Base] Signing transaction...")
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
        
        print(f"[Base] Broadcasting to Base Sepolia...")
        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"[Base] ✅ Transaction broadcasted! tx_hash: {tx_hash.hex()}")
        
        print(f"[Base] Waiting for receipt...")
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        if receipt.status == 1:
            print(f"[Base] ✅ Transaction mined successfully in block {receipt.blockNumber}!")
        else:
            print(f"[Base] ❌ Transaction failed in block {receipt.blockNumber}!")
            
    except Exception as e:
        print(f"[Base] Error executing transaction: {e}")

if __name__ == "__main__":
    print("Starting Base Monitor Service in background mode...")
    while True:
        try:
            monitor_and_trigger()
        except Exception as e:
            print(f"Critical error in monitor loop: {e}")
            
        print("Sleeping for 10 seconds heartbeat...\n")
        time.sleep(10)

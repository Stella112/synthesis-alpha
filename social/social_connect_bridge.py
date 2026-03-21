import hashlib

def get_odis_hash(phone_number: str, pepper: str = "synthesis_alpha_pepper_v1") -> str:
    """
    Mock Celo ODIS logic to map phone numbers to a deterministic hash.
    In real usage, this would query the ODIS service to securely map the number.
    """
    data = phone_number + pepper
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def calculate_social_dividend(profit_eth: float, percentage: float = 0.10) -> float:
    """
    Calculates the Social Dividend to be sent based on swap profit.
    Default dividend is 10% of profit.
    """
    return profit_eth * percentage

def process_social_dividend(phone_number: str, profit_eth: float):
    """
    Helper function to get both ODIS hash and calculate dividend amount.
    Returns (odis_hash, dividend_eth)
    """
    odis_hash = get_odis_hash(phone_number)
    dividend_eth = calculate_social_dividend(profit_eth)
    return odis_hash, dividend_eth

if __name__ == "__main__":
    import math
    print("Testing SocialConnect Bridge...")
    phone = "+14085551234"
    profit = 0.8
    h_str, div = process_social_dividend(phone, profit)
    print(f"[Celo Logic] Phone: {phone} => ODIS Hash: 0x{h_str}")
    print(f"[Celo Logic] Swap Profit: {profit} ETH => Dividend: {div} ETH")

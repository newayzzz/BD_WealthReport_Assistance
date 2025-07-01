
import re
from typing import List, Dict

def extract_assets_from_text(text: str) -> List[Dict[str, str]]:
    asset_types = ["LIC", "PF", "FD", "Gold", "Land", "Loan", "Bank", "SIP", "Stock"]
    results = []

    for asset in asset_types:
        if asset.lower() in text.lower():
            results.append({
                "type": asset,
                "description": f"Found mention of {asset} in input text."
            })

    return results

# Example usage
if __name__ == "__main__":
    input_text = "My father has LIC and some land in Barisal. Also an FD at Sonali Bank."
    extracted = extract_assets_from_text(input_text)
    for item in extracted:
        print(item)

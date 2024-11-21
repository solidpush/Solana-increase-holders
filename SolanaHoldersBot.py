import random
import time

# Dummy IPFS links for resources
IPFS_RESOURCES = {
    "holders_guide": "ipfs://QmExampleHoldersGuideHash",
    "transaction_schema": "ipfs://QmExampleTransactionSchemaHash",
    "auto_sell_config": "ipfs://QmExampleAutoSellConfigHash",
}

class SolanaHoldersBot:
    def __init__(self, token_name):
        self.token_name = token_name
        self.wallets = {}
        print(f"Solana Holders Bot initialized for token '{self.token_name}'.")

    def create_holders(self, num_holders, rate=5):
        print(f"Creating {num_holders} holders at a rate of {rate} holders per second...")
        for _ in range(num_holders):
            wallet_id = f"wallet_{random.randint(100000, 999999)}"
            self.wallets[wallet_id] = 0.0001  # Small buy amount
            print(f"New holder created: {wallet_id} with 0.0001 {self.token_name}.")
            time.sleep(1 / rate)
        print(f"Completed creating {num_holders} holders. Guide: {IPFS_RESOURCES['holders_guide']}")

    def random_auto_sell(self, probability=0.3):
        print("Random auto-selling initiated...")
        for wallet in list(self.wallets.keys()):
            if random.random() < probability:
                sold_amount = self.wallets[wallet]
                self.wallets.pop(wallet, None)
                print(f"Wallet {wallet} auto-sold {sold_amount} {self.token_name}.")
        print("Auto-sell process completed. Configuration:", IPFS_RESOURCES["auto_sell_config"])

    def display_wallets(self):
        print("Current wallets and balances:")
        for wallet, balance in self.wallets.items():
            print(f"{wallet}: {balance} {self.token_name}")
        print("Wallets displayed. Transaction schema available at:", IPFS_RESOURCES["transaction_schema"])

if __name__ == "__main__":
    print("Welcome to Solana Holders Bot!")
    print("Effortlessly generate holders and simulate buy/sell activity for your token.")
    print("For more information, refer to the following resources:")
    print("- Holders Guide:", IPFS_RESOURCES["holders_guide"])
    print("- Transaction Schema:", IPFS_RESOURCES["transaction_schema"])
    print("- Auto-Sell Configuration:", IPFS_RESOURCES["auto_sell_config"])
    print("For support or inquiries, contact: t.me/mxdotsol")
    
    # Example usage
    bot = SolanaHoldersBot("YourTokenName")
    bot.create_holders(num_holders=15, rate=5)
    bot.display_wallets()
    bot.random_auto_sell(probability=0.5)
    bot.display_wallets()

import random

FISH_CONFIG = {
    "Useless": {
        "pool": ["🩴 Old Boot", "Nothing"],
        "weight": 100,
        "price_range": (0, 0)
    },
    "Common": {
        "pool": ["🐟 Minnow", "🐠 Goldfish"],
        "weight": 70,
        "price_range": (5, 10)
    },
    "Rare": {
        "pool": ["🐟 Salmon", "🐟 Bass"],
        "weight": 10,
        "price_range": (25, 30)
    },
    "Epic": {
        "pool": ["🦈 Shark", "🐙 Octopus"],
        "weight": 8,
        "price_range": (50, 120)
    },
    "Legendary": {
        "pool": ["🐉 Sea Dragon", "👑 Golden Carp"],
        "weight": 2,
        "price_range": (200, 500)
    }
}

def main():
    money = 10
    inventory = []
    worms = 5

    while True:
        print("\n--- FISHING GAME ---")
        print("What would you like to do?")
        print(f"Money: ${money}")
        print(f"Worms: {worms}")
        print("(Type 'fish', 'sell', 'inv', 'buy', or 'quit')\n")
        action = input(">>> ").lower()

        if action == "quit":
            print(f"Game saved. Walked away with ${money}.")
            break

        elif action == "fish":
            if worms <= 0:
                print("You're out of worms! You need to buy some bait first.")
                continue 
            
            worms -= 1
            print(f"🪱 Cast your line... \n(Worms left: {worms})\n(Money left: {money})")

        
            tier_list = list(FISH_CONFIG.keys())
            weight_list = [FISH_CONFIG[t]["weight"] for t in tier_list]

            chosen_tier = random.choices(tier_list, weights=weight_list, k=1)[0]
            
            fish_pool = FISH_CONFIG[chosen_tier]["pool"]
            caught_fish = random.choice(fish_pool)
            
            inventory.append({"name": caught_fish, "tier": chosen_tier})
            print(f"✨ CATCH: [{chosen_tier.upper()}] You reeled in a {caught_fish}!")

        elif action == "sell":
            if not inventory:
                print("You have no fish to sell.")
                continue

            total_earnings = 0

            for fish_item in inventory:
                # Use 'fish_tier' instead of 'tier' to avoid variable collision
                fish_tier = fish_item["tier"]
                min_p, max_p = FISH_CONFIG[fish_tier]["price_range"]
                
                rolled_price = random.randint(min_p, max_p)
                total_earnings += rolled_price
                print(f"  Sold {fish_item['name']} for ${rolled_price}")

            money += total_earnings
            inventory.clear()
            print(f"💰 Total earnings: ${total_earnings}. Current balance: ${money}")

            if money >= 1000:
                print("🏆 Congratulations! You've reached $1000 and won the game!")
                break

        elif action == "inv":
            if not inventory:
                print("🎒 Backpack is empty.")
            else:
                print("\n--- CURRENT CATCHES ---")
                for index, item in enumerate(inventory, start=1):
                    print(f"{index}. {item['name']} ({item['tier']})")

        elif action == "buy":
            print("\n--- TACKLE & VIBES SHOP ---")
            print("1. 🪱 1 Worm ($3)")
            print("2. 🪱📦 5 Worms ($12)")
            print("3. 🪱🚛 15 Worms ($35)")
            print("4. 🧃 Juice ($5)")
            
            shop_choice = input("Choose an option (1-4):\n>>> ").lower()
            
            if shop_choice == "1" or shop_choice == "worm":
                if money >= 3:
                    money -= 3
                    worms += 1
                    print("✅ Bought 1 worm.")
                else:
                    print("❌ You're too broke for even one worm!")
                    
            elif shop_choice == "2" or shop_choice == "5 worms":
                if money >= 12:
                    money -= 12
                    worms += 5
                    print("✅ Bought 5 worms.")
                else:
                    print("❌ Not enough cash for a 5-pack!")
                    
            elif shop_choice == "3" or shop_choice == "15 worms":
                if money >= 35:
                    money -= 35
                    worms += 15
                    print("✅ Bought a massive batch of 15 worms!")
                else:
                    print("❌ You can't afford 15 worms yet.")
                    
            elif shop_choice == "4" or shop_choice == "juice":
                if money >= 5:
                    money -= 5
                    print("🧃 You chugged the juice. Absolutely zero gameplay benefits, but you look cool.")
                else:
                    print("❌ Bro can't even afford juice.")
            else:
                print("Huh? Pick a real option, man.")

        else:
            print("Invalid action. Please choose 'fish', 'sell', 'inv', 'buy', or 'quit'.")

if __name__ == "__main__":
    main()

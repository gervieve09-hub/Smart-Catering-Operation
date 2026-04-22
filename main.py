import time

# ==========================================
# 🤖 DEFINITION OF AGENTS
# ==========================================

class CustomerInteractionAgent:
    def capture_details(self):
        print("\n👨‍💼 CUSTOMER AGENT: Gathering event details...")
        # Simulating user input
        details = {
            "event_type": "Wedding Reception",
            "guest_count": 150,
            "dietary_needs": "Vegetarian options needed",
            "budget": 50000  # in PHP
        }
        print(f"   -> Event: {details['event_type']}")
        print(f"   -> Guests: {details['guest_count']}")
        print(f"   -> Budget: PHP {details['budget']:,}")
        return details

class MenuPlanningAgent:
    def generate_menu(self, requirements):
        print("\n📋 MENU AGENT: Designing menu based on requirements...")
        # Simple logic: If budget is high, add more items
        if requirements["budget"] > 40000:
            menu = [
                "Appetizer: Garden Salad",
                "Main Course: Vegetable Lasagna & Grilled Chicken",
                "Soup: Creamy Mushroom Soup",
                "Dessert: Chocolate Mousse"
            ]
        else:
            menu = ["Rice", "Adobo", "Soup", "Fruit Salad"]
            
        print("   -> Menu Generated:")
        for item in menu:
            print(f"      * {item}")
        return menu

class InventoryAgent:
    def check_stock(self, menu):
        print("\n📦 INVENTORY AGENT: Calculating ingredients needed...")
        ingredients = ["Rice", "Chicken", "Vegetables", "Spices", "Oil"]
        print(f"   -> Ingredients required: {', '.join(ingredients)}")
        print("   ✅ Stock status: All items available.")
        return ingredients

class LogisticsPlanningAgent:
    def schedule(self):
        print("\n🚚 LOGISTICS AGENT: Planning timeline and resources...")
        schedule = {
            "prep_time": "2 days before event",
            "cooking_start": "4:00 AM",
            "delivery_time": "10:00 AM",
            "staff_needed": 5
        }
        print(f"   -> Preparation starts: {schedule['prep_time']}")
        print(f"   -> Delivery scheduled: {schedule['delivery_time']}")
        return schedule

class PricingAgent:
    def compute_cost(self, guests, budget):
        print("\n💰 PRICING AGENT: Calculating total cost and profit...")
        cost_per_head = budget / guests
        total_cost = guests * cost_per_head
        print(f"   -> Cost per person: PHP {cost_per_head:.2f}")
        print(f"   -> Total Projected Cost: PHP {total_cost:,}")
        return total_cost

class MonitoringAgent:
    def track_progress(self):
        print("\n🔍 MONITORING AGENT: Checking overall status...")
        print("   ✅ All processes running smoothly. No delays detected.")
        print("   📋 Status: READY FOR EXECUTION")

# ==========================================
# ⚙️ MAIN EXECUTION (WORKFLOW)
# ==========================================

def main():
    print("="*50)
    print("🤖 AI-POWERED MULTI-AGENT CATERING SYSTEM")
    print("="*50)
    
    # Step 1: Get Customer Details
    agent1 = CustomerInteractionAgent()
    customer_data = agent1.capture_details()
    time.sleep(1)

    # Step 2: Generate Menu
    agent2 = MenuPlanningAgent()
    final_menu = agent2.generate_menu(customer_data)
    time.sleep(1)

    # Step 3: Check Inventory
    agent3 = InventoryAgent()
    items_needed = agent3.check_stock(final_menu)
    time.sleep(1)

    # Step 4: Plan Logistics
    agent4 = LogisticsPlanningAgent()
    timeline = agent4.schedule()
    time.sleep(1)

    # Step 5: Calculate Price
    agent5 = PricingAgent()
    total_price = agent5.compute_cost(customer_data["guest_count"], customer_data["budget"])
    time.sleep(1)

    # Step 6: Monitor
    agent6 = MonitoringAgent()
    agent6.track_progress()

    print("\n" + "="*50)
    print("✅ TASK COMPLETED! CATERING PLAN GENERATED SUCCESSFULLY.")
    print("="*50)

if __name__ == "__main__":
    main()

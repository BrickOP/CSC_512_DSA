import datetime

class Company:
    def __init__(self, name, address, ceo_name, year_founded, assets):
        self.name = name
        self.address = address
        self.ceo_name = ceo_name
        self.year_founded = year_founded
        self.assets = assets
        self.policies = []
        self.claims = []

    def add_policy(self, policy):
        self.policies.append(policy)

    def add_claim(self, claim):
        if not self.find_policy(claim.policy_id):  # Check if the policy exists
            print(f"Error: Policy ID {claim.policy_id} does not exist. Claim not added.")
            return
        self.claims.append(claim)

    def find_policy(self, id_number):
        for policy in self.policies:
            if policy.id_number == id_number:
                return policy
        return None

    def find_claim(self, id_number):
        for claim in self.claims:
            if claim.id_number == id_number:
                return claim
        return None

class Policy:
    def __init__(self, id_number, customer_name, pet_name, species, start_date, end_date, cost_per_month, coverage_percentage):
        self.id_number = id_number
        self.customer_name = customer_name
        self.pet_name = pet_name
        self.species = species
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        self.cost_per_month = cost_per_month
        self.coverage_percentage = coverage_percentage
        self.last_payment = None
        self.overdue = False

    def payPremium(self):
        today = datetime.date.today()

        
        if self.last_payment is not None and self.last_payment == today:
            return False

        if self.last_payment is None or today > self.last_payment + datetime.timedelta(days=30):
            self.overdue = True
        else:
            self.overdue = False

        self.last_payment = today
        return True

class Claim:
    next_id = 1
    
    def __init__(self, id_number, policy_id, service_date, vet_name, amount_submitted, service_type):
        self.id_number = Claim.next_id
        Claim.next_id += 1
        self.policy_id = policy_id
        self.service_date = datetime.datetime.strptime(service_date, '%Y-%m-%d').date()
        self.vet_name = vet_name
        self.amount_submitted = amount_submitted
        self.service_type = service_type
        self.status = 'open'  
        self.amount_reimbursed = 0

    def changeStatus(self, status):
        if status in ["open", "closed"]:
            self.status = status
        else:
            print("Invalid status. Must be 'open' or 'closed'.")

    def payout(self, reimbursement_amount):
        if reimbursement_amount > self.amount_submitted:
            raise ValueError("Reimbursement amount exceeds the amount submitted.")
        
        self.amount_reimbursed = reimbursement_amount
        self.status = "closed"


# Example usage
if __name__ == "__main__":
    # Create a company
    company = Company("PetCare Insurance", "1234 Elm St, Suite 100, Springfield, IL, 62701", "Alice Smith", 2005, 5000000)

    # Create policies
    policy1 = Policy(1, "John Doe", "Fluffy", "Cat", "2024-01-01", "2024-12-31", 30, 80)
    policy2 = Policy(2, "Jane Roe", "Rex", "Dog", "2024-02-01", "2024-11-30", 50, 90)

    # Add policies to the company
    company.add_policy(policy1)
    company.add_policy(policy2)

    # Create claims
    claim1 = Claim(1, 1, "2024-03-15", "Dr. John", 200, "Checkup")
    claim2 = Claim(2, 2, "2024-04-20", "Dr. Vet", 300, "Surgery")
    claim3 = Claim(3, 1, "2024-05-01", "Dr. Samar", 150, "Vaccination")
    claim4 = Claim(3, 1, "2024-05-01", "Dr. Abbas", 150, "Something else")

    # Add claims to the company
    company.add_claim(claim1)
    company.add_claim(claim2)
    company.add_claim(claim3)
    company.add_claim(claim4)

    # Test finding policies
    policy_found = company.find_policy(1)
    if policy_found:
        print(f"Found Policy: {policy_found.customer_name}'s {policy_found.pet_name} policy")

    # Test finding claims and processing payouts
    claim_found = company.find_claim(1)
    if claim_found:
        try:
            claim_found.payout(160)  # Valid reimbursement
            print(f"Claim amount reimbursed: ${claim_found.amount_reimbursed}")
        except ValueError as e:
            print(e)

    # Test invalid payout
    claim_found = company.find_claim(2)
    if claim_found:
        try:
            claim_found.payout(400)  # Exceeds submitted amount
        except ValueError as e:
            print(e)  # Should raise an error

# 3: The problem is that 3 and 4 claims has same ID number.

# 4: Adjusted the class variable so that it generates the claim id by itself

# 5: Adjusted the add claim function to account for non-existent policy. Checked by changing the policy number to 3, since there are only 2 policies prensent in the example. It pops the error that policy is not found. 

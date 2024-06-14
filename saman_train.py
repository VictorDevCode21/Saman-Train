from personal import Personal
from typing import List


class SamanTrain:
    def __init__(self):
        self.persons: List[Personal] = [
            Personal("Victor", 30496974, "Super Sonic", 9)
        ]
    
    def add_personal(self, persons: Personal):
        self.persons.append(persons)
        
    def generate_report(self):
        total_personal = len(self.persons)
        super_sonic_personal: int = 0
        carbon_personal: int = 0 
        personal_with_benefits = 0
        total_carbon_pay: float = 0.0
        total_super_sonic_pay: float = 0.0
        
        for person in self.persons: 
            if person.train_type == "Super Sonic":
                super_sonic_personal += 1
                total_super_sonic_pay += person.calculate_pay()
                
            if person.train_type == "Carbon":
                carbon_personal += 1
                total_carbon_pay += person.calculate_pay()
            
            if person.hours > 8:
                personal_with_benefits += 1
                
            info = person.get_data()
            
        
        average_super_sonic_pay = total_super_sonic_pay / super_sonic_personal if super_sonic_personal > 0 else 0
        average_carbon_pay = total_carbon_pay / carbon_personal if carbon_personal > 0 else 0
        
        report = {
            "total_persons": total_personal,
            "information": info,
            "super_sonic_persons_quantity": super_sonic_personal,
            "carbon_persons_quantity": carbon_personal,
            "average carbon pay": average_carbon_pay,
            "average super sonic pay": average_super_sonic_pay,
            "personal with benefits": personal_with_benefits
            }
        
        return report
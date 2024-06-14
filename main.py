from personal import Personal 
from saman_train import SamanTrain 

def main():
    saman_train = SamanTrain()
    
    while True:
        name = input("Enter your name: ")
        id = input("Enter your id: ")
        train_type = input("Enter your train_type (Super Sonic/Carbon): ")
        hours = float(input("Enter the hours that you worked: "))
        
        try:
            personal = Personal(name= name, id= id, train_type=train_type, hours=hours)
            saman_train.add_personal(personal)
        
        except ValueError as e:
            print(e)
            continue
        
        report = saman_train.generate_report()
        
        print("\nReporte de Samán Train:")
        print(f"Total personal: {report['total_persons']}")
        print(f"Information about the personal: {report['information']}")
        print(f"Total super sonic personal: {report['super_sonic_persons_quantity']}")
        print(f"Total Carbon trains personal: {report['carbon_persons_quantity']}")
        print(f"Total personal with benefits: {report['personal with benefits']}")
        print(f"Average of payments for super sonic trains personal: {report['average super sonic pay']:.2f}")
        print(f"Average of payments for carbon trains personal: {report['average carbon pay']:.2f}")
        
        follow = input("Do u want to add more personal? (y/n): ")
        if follow.lower() != 'y':
            break
        #else:
        #    main()
        
        
        
if __name__ == "__main__":
    main()

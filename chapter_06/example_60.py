#6.8
pet_details ={
    'leo':{
        'owner_name':'alif',
        'pet_name':'cat',
    },
    'tomy':{
        'owner_name':'rahman',
        'pet_name':'dog'
    }
}
pets = ['leo','tomy']
for pet,pet_info in pet_details.items():
    for i in pets:
        if i in pet:
            print(f"\nPet Name: {pet}")
            if pet in pet_details.keys():
                print(f"\tOwner Name:{pet_info['owner_name']}\n\tPet Group: {pet_info['pet_name']} ")

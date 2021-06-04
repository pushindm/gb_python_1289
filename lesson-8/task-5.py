class StorageCapacityError(Exception):
    pass

class StorageDeliveryError(Exception):
    pass

class Storage():
    
    max_capacity = 10 # max amount of items
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity # current capacity
        self.storage_items_dict = {} # {Device_type: {key_1=val_1,...}}
    
    def __str__(self):
        """Return info about all unit types. Format of output: 'Unit_type: key_1=val_1, ... key_n=val_n'"""
        
        output_list = []
        for obj_class, vals in self.storage_items_dict.items():
            sample_arr = []
            for attr,val in vals.items():
                sample_arr.append('='.join([attr,str(val)])) # format: key=val
            output_list.append(': '.join([obj_class,', '.join(sample_arr)]))
        return "\nCurrent storage state\n"+'\n'.join(output_list) + "\n"
    
    def recieve_equipment(self, obj, attr_name='amount'):
        """
        recieve equipment on a storage balance. The storage overflow is checked. 
        New item is added as dict: {Device_type: {key_1=val1,...}}, where
        'Device type' is a class name (e.g. Printer).
        """
        
        print("Receiving starts")
        temp_dict = dict(zip([attr for attr in obj.__dict__.keys()],[val for val in obj.__dict__.values()]))
        try:
            if self.capacity == Storage.max_capacity:
                raise StorageCapacityError
        except StorageCapacityError:
            print("The storage is full")
        else:
            if self.capacity + obj.amount < Storage.max_capacity:
                self.storage_items_dict[obj.__class__.__name__] = temp_dict
                self.capacity += obj.amount
                print(f"{obj.amount} {obj.name} (type {obj.__class__.__name__}) were added succesfully")
            else:
                temp_dict[attr_name] = Storage.max_capacity - self.capacity
                self.storage_items_dict[obj.__class__.__name__] = temp_dict
                print(f"Warning: only {Storage.max_capacity - self.capacity} {obj.name} (type {obj.__class__.__name__}) was added due to capacity limit.")
                self.capacity = Storage.max_capacity
    
    def give_equipment(self, model_name, dep_name, amount, attr_name='amount'):
        """Give 'amount' of 'model_name' devices to department 'dep_name'"""
        print("Delivery starts")
        try:
            for device_type,device_dict in self.storage_items_dict.items():
                if model_name not in device_dict.values():
                    raise StorageDeliveryError
                
                if device_dict[attr_name] < amount:
                    print(f"Warning: not enough items in the storage. Only {device_dict[attr_name]} {model_name} (type: {device_type}) were delivered to {dep_name}")
                    self.capacity -= device_dict[attr_name]
                    device_dict[attr_name] = 0
                    break
                else:
                    print(f"The {amount} {model_name} (type: {device_type}) were delivered to {dep_name}")
                    self.capacity -= amount
                    device_dict[attr_name] -= amount
                    break
        except StorageDeliveryError: 
            print(f"There is no {model_name} in the storage")
                    
class OfficeEquipment:
    
    def __init__(self, name, price, amount=1):
        self.name = name
        self.price = price
        self.amount = amount
    
    def __str__(self):
        return 'Type: {0.__class__.__name__}, model: {0.name}, price: {0.price}, amount: {0.amount}'.format(self)
    
class Printer(OfficeEquipment):
    def __init__(self, name, price, amount, printer_type):
        OfficeEquipment.__init__(self, name, price, amount)
        self.printer_type = printer_type
            
    def __str__(self):
        return '{0}, printer_type: {1.printer_type}'.format(super().__str__(), self)

class Scaner(OfficeEquipment):
    def __init__(self, name, price, amount, dim):
        OfficeEquipment.__init__(self, name, price, amount)
        self.dim = dim 
    
    def __str__(self):
        return '{0}, dim of scanning: {1.dim}'.format(super().__str__(), self)

class Xerox(OfficeEquipment):
    def __init__(self, name, price, amount, is_portable):
        OfficeEquipment.__init__(self, name, price, amount)
        self.is_portable = is_portable
    
    def __str__(self):
        return '{0}, portability: {1}'.format(super().__str__(), bool(self.is_portable))

# create objects
printer = Printer('hp_1020', 3000, 3, 'color')
scaner = Scaner('canon_240', 2000, 5, '1D')
xerox = Xerox('dell_3050', 10000, 10, 0)
storage = Storage('storage', 0)

# recieve devices to storage
for obj in [printer, scaner, xerox]:
    storage.recieve_equipment(obj)
print(storage)

# send devices to department
storage.give_equipment('hp_1020', 'IT department', 4)
print(storage)

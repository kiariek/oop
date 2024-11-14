class Car:      #have created another file that can be imported to the other files for use.
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def drive(self):  #methods.
        print(f'you can drive the {self.model}!')

    def stop(self):
        print(f'you stop {self.model}')
    
    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
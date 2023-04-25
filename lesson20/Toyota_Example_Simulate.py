class Toyota:
    Catagory1= "cars"
    Catagory2= "electrified"
    Catagory3= "Crossovers"
    Catagory4= "SUV"
    Catagory5= "Trucks"
    Catagory6= "Minivan"
    
    #how do we use it. 
    #example of instance
    def __init__(self, finished_price, basic_price, model, year, picture):
        self.finished_price = finished_price 
        self.basic_price = basic_price
        self.model = model
        self.year = year
        self.picture = picture
        
        #use  __str__ f
    def __str__(self):
        return f" For the car model: {self.model} and year: {self.year}, base price{self.basic_price}"
    
    #represent our objects
car1 = Toyota("34,550", "28,770", "Prius_Prime", "2022", "https://www.toyota.com/priusprime")
car2 = Toyota("52,350", "39,950", "Toyota_Crown", "2023", "https://www.toyota.com/toyotacrown") 
car3 = Toyota("23,315", "21,550", "Corolla", "2023", "https://www.toyota.com/corolla")
car4 = [car1, car2, car3]
for _ in car4:
    print (_)
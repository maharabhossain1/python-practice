
# practice 1 
# two list make a  list of dictionaries 
fruits = ["apple", "banana", "orange", "lemon"]
extra_fruits = ["Blueberry","Cantaloupe","Cranberry","Fig"]
vegetables =["Beetroot","Carrot","Radish","Daikon","Celeriac","Sugar beet"]

fruits.extend(extra_fruits)
new_fruits=fruits[:6]


def make_list_of_dict(list_1 ,list_2):
    new_dict=[]
    for i in range(len(list_1)):
        test_dict = {}
        test_dict['fruit'] = list_1[i]
        for j in range(len(list_2)):
            if i == j:
              test_dict['vegetable'] = list_2[j]
              break
        new_dict.append(test_dict)
    return new_dict

# print(range(len(vegetables)))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]
# print(new_list)
# data =make_list_of_dict(new_fruits, vegetables)
# print(data)


# problem -02 
list_of_id = [1,2,3,4,7,9]
give_list_of_dict = [
    {
        "id": 1,
        "name":'opi'
    },
    {
        "id": 2,
        "name":'maharab'
    },
    {
        "id": 3,
        "name":'hossain'
    },
    {
        "id": 4,
        "name":'rony'
    },
    {
        "id": 5,
        "name":'jamil'
    },
    {
        "id": 6,
        "name":'nirob'
    },
    {
        "id": 7,
        "name":'tanjim'
    },
    {
        "id": 8,
        "name":'shaon'
    },
    {
        "id": 9,
        "name":'tawhid'
    },
    {
        "id": 10,
        "name":'rakib'
    }
] 

class FilterList:
    def __init__(self,dependent_list :list, dict_list :list ):
        self.dependent_list = dependent_list
        self.dict_list = dict_list
        self.new_list = []

    def filter_list (self):
        for i in range(len(self.dict_list)):
            item = self.dict_list[i]
            for j in range(len(self.dependent_list)):
                single_id = self.dependent_list[j]
                if single_id == item["id"]:
                    self.new_list.append(item)
                    break

    def isInclude (self,value):
        for item in self.dependent_list:
            if value == item:
              return True
            else:
                return False

    def print_list(self):
        print( self.new_list)



my_new_filter = FilterList(list_of_id, give_list_of_dict)

# my_new_filter.filter_list()
print(my_new_filter.isInclude(100))


# problem -03 
products = [
    
  {
    "productId": 234435,
    "colorId": 1,
    "size": "11-M",
  },
  {
    "productId": 443434,
    "colorId": 2,
    "size": "11-M",
  },
  {
    "productId": 343434,
    "colorId": 1,
    "size": "11-L",
  },
  {
    "productId": 322333,
    "colorId": 2,
    "size": "12-M",
  },
]
student= {
    "name":"sadie",
    "age":23,
     "subjects":["maths","english","science"],
     "tuple":(4,5,6,7,8),
    "sgpa":9.7,
    "is_student":True       
}
print(student)
# key= string,number,tuple,value,float,list,boolean

print(student["name"])
print(student["subjects"])
student["name"]="millie"
print(student)
null_dict={}
print(null_dict)
null_dict["name"]="shriya"
print(null_dict)
# nested dictionary
student1={
    "name":"sadie" ,
    "subjects":{  
        "chemistry":90,
         "maths":80,
          "english":70
    }
    
}
print(len(student1))
print(list(student1.keys()))
print(list(student1.values()))
print(student1.items()) 
# items=in the form of tuples
pairs=list(student1.items())
print(pairs[0])
new_dict={"name":"delhi"}
student1.update(new_dict)
collection={1,2,2,2,"hello","world",5}
print(collection)
print(type(collection))
# sets have no order
print(len(collection))
# sets does not allow duplicate values
# sets=mutable
# sets k elements=immuatable
collection=set()
collection.add(1)
collection.add(5)
collection.add(6)
collection.add(3)
collection.add((1,2,3,4))
collection.remove(6)
print(len(collection))
collection1=("python","java","c++","javascript")
print(collection1)
set1={1,2,3,4}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
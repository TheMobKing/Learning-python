class person:
    def __init__(self,name,age):
        self.name =name
        self.age =age

    def __str__(self):
        return f"{self.name}"
p1 = person("desire",3)
print(p1)

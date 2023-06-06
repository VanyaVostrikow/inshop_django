import json



def Create(name):
    with open('json/' + name +'.json', 'w') as f:
        print("The json file is created")

def Read(name):
    try: 
        with open('json/' + name + '.json') as f:
            data = json.load(f)
            return data
    except:
        print("NO DATA IN .JSON")
        data = {0:0}
        return data
    
def Write(name, data):
     with open('json/' + name + '.json', 'w') as f:
        json.dump(data, f, indent=2)
        print("New json file is created from data.json file")

def Check(name):
    with open('json/' + name + '.json') as f:
            data = json.load(f)
            print(data)
            return data

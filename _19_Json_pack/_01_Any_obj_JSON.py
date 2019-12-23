import json

json_data = '''{"widget": {
                        "debug": "on",
                        "window": {
                        "title": "Sample Konfabulator Widget",
                        "name": "main_window",
                        "width": 500,
                        "height": 500
                                     },
                "image": { 
                        "src": "Images/Sun.png",
                        "name": "sun1",
                        "hOffset": 250,
                        "vOffset": 250,
                        "alignment": "center"
                                         },
                "text": {
                        "data": "Click Here",
                        "size": 36,
                        "style": "bold",
                        "name": "text1",
                        "hOffset": 250,
                        "vOffset": 100,
                        "alignment": "center",
                        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
                                                      }
                         } 
                 }   '''

py_data = json.loads(json_data)
print(type(py_data))
print(py_data.keys())
print(py_data.values())
for item in py_data["widget"]["image"]:
    print(item)
print('-----------------------------------------------')    
for item in py_data["widget"]["text"]:
    print(item)
print('-----------------------------------------------')  
for item in py_data["widget"]:
    print(item)
print('-----------------------------------------------')
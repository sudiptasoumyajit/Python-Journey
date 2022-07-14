from tkinter import *
import requests
import json
root=Tk()
root.overrideredirect(True)
root.title("SSweather")
root.geometry("350x300")

root.configure(background="lightblue")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Work Sans", 18,'bold'),bg="lightblue")
city_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="lightblue", font=("Work Sans", 10, "bold"))
weather_info_label.place(relx=0.23,rely=0.6,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="lightblue", font=("Work Sans",10, "bold")) 
humidity_info_label.place(relx=0.22,rely=0.7,anchor=CENTER) 
    
def city_name():
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&appid="+ "21cab08deb7b27f4c2b55f3e2df28ea4")
    api_output_json=json.loads(api_request.content)
    weather_info=api_output_json['weather']['0']['main']
    print(weather_info)
    humidity=api_output_json['main']['humidity']
    print(humidity+"%")

    weather_info_label["text"]="Weather: "+weather_info
    humidity_info_label['text']="Humidity: "+humidity+"%"

    city_name_label['text']=city_entry.get()
    city_entry.destroy()
    search_btn.destroy()

search_btn = Button(root,text="Search",command=city_name, bg="lightblue", font=("Work Sans",10, "bold"),relief=FLAT) 
search_btn.place(relx=0.5,rely=0.48,anchor=CENTER) 

root.mainloop()

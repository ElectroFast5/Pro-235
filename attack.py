import requests

for i in range(1,100):
    URL=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
    r=requests.get(URL)
    if r.status_code==200:
        print(URL+" works 👍")
    else:
        print(URL+" doesn't work 👎👎👎")
resolutions = [
(1920 , 1080) ,
(1280 , 720) ,
(2560 , 1440)
]
factor = 0.5
for w,h in resolutions:
    x=int(w*factor)
    y=int(h*factor)
    print("x=",x)
    print("Y=",y)
    
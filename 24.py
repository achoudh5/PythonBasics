ip=["a","b","c","k","l","g","r"]
#nimble interview
y=[]
for i in ip:
    for j in ip:
        if i!=j:
            x=i+j
            y.append(x)
print y
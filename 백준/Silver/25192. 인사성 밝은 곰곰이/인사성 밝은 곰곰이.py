N=int(input())

gumgum={}

cnt=0

for _ in range(N):
    Input=input()

    if Input=="ENTER":
        for key,value in gumgum.items():
            if value==1:
                cnt+=1
        gumgum={}
    else:
        if Input not in gumgum:
            gumgum[Input]=1

for key,value in gumgum.items():
    if value==1:
        cnt+=1

print(cnt)
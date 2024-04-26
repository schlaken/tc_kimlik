tc_no=input("lütfen tc kimlik numaranızı giriniz")
tc_split=list(tc_no)
tc_1=int(tc_split[0])
tc_2=int(tc_split[1])
tc_3=int(tc_split[2])
tc_4=int(tc_split[3])
tc_5=int(tc_split[4])
tc_6=int(tc_split[5])
tc_7=int(tc_split[6])
tc_8=int(tc_split[7])
tc_9=int(tc_split[8])
tc_10=int(tc_split[9])
tc_11=int(tc_split[10])

tekler_top=(tc_1+tc_3+tc_5+tc_7+tc_9)
ciftler_top=(tc_2+tc_4+tc_6+tc_8)
tctoplam=tekler_top+ciftler_top+tc_10
tc_11a=tctoplam%10
yedi=tekler_top*7
tc_10a=(yedi-ciftler_top)%10
if(tc_10a!=tc_10):
    print("girilen tc dogru degildir")
elif(tc_11!=tc_11a):
    print("girilen tc dogru degildir")
else:
    print("girilen tc dogrudur")
    


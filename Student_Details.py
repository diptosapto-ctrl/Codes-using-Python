
# def std_details(name,uid,*marks):
#    percentage=sum(marks)/len(marks)
#    print("The name of the student is:",name,"with user id:",uid,"he got",percentage,"% marks")
   
# std_details("dipto",97707,90,90,90,88,89) 


def std_details(uid,name,**marks):
    percentage=sum(marks.values())/len(marks)
    if len(marks)==0:
        print(name,"din't attend the exam")
    else:
        print(name,"got",percentage,"% marks")

std_details(54659,"Dipto",sub1=99,sub2=98,sub3=100)
std_details(62623,"Sapto",sub1=88,sub2=89,sub3=90)   
std_details(58455,"Riya",sub1= ,sub2= ,sub3= )       
  
       
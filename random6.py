import random
main_list= [{"what is your birth place":"bhavnagar"},{"what is your favourite car":"supra"},{"enter your favourite book":"atomic habit"},{"enter your favourite color":"red"},{"enter your favourite sport":"hockey"},{"enter your nick name":"param"},{"enter your mother maiden name":"truptiben"},{"enter your pet name":"gingur"},{"enter your first vehicle number":"0000"}]
quest=random.choices(main_list,k=3)
total_correct=0
for i in quest:
    questions=i.keys()
    answer=i.values()
    for k in answer:
        org_answer=k
    print(questions)
    user_answer=str(input("Enter your answer "))
    if user_answer==org_answer:
        total_correct+=1        
print("your score is ",total_correct);
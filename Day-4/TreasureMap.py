
list1=["⬜","⬜","⬜"]
list2=["⬜","⬜","⬜"]
list3=["⬜","⬜","⬜"]
map=[list1,list2,list3]
print(f"{list1}\n{list2}\n{list3}")
position=input("Enter the position of the TILE you would like to CHANGE?")
ver=int(position[1])
hor=int(position[0])
change_position=map[ver-1]
change_position[hor-1]="X"
print(f"{list1}\n{list2}\n{list3}")



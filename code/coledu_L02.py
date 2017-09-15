##########################
#Dusty Cole
#coledu
#A14
#referce
#Jan
#Use the stack class she gave to us.
##########################
import sys
from Stack import Stack
import copy





#this stack is use to keep track of all the intersection we have been to and use that when we back track to determine how far back we need to go
inter_stack = Stack()
#This is a list of all the start pos of all the path we already took so we do not try a path multipl time
do_not_enter=[]
#This is the stack to keep track of all the move.
movement_stack=Stack()
#this keep all the path to the treasure or loot
loot_path=[]

def check_loot(map,curr_pos):
    ''' Take the map and curr pos and check for tresure all around the curr pos north,south,east,and west.
    Return the map with the loot taken out of the map and add the path to the loot to the loot_path list.'''
    row=curr_pos[0]
    col=curr_pos[1]
    # north
    if map[row - 1][col] == 'T':
        map[row - 1][col]='.'
        addlist = []
#make a deep copy of the stack so we can unpack it to get the path to the loot without unpacking the stack that we need for backtracking
        movement_copy = copy.deepcopy(movement_stack)
        addlist.append([row-1,col])
        addlist.append(curr_pos)
        while movement_copy.size() != (0):
            addlist.append(movement_copy.pop())

        loot_path.append(addlist)

    # east
    if map[row][col + 1] == 'T':
        map[row][col+1] = '.'
        addlist = []

        movement_copy = copy.deepcopy(movement_stack)
        addlist.append([row,col+1])

        addlist.append(curr_pos)
        while movement_copy.size() != (0):
            addlist.append(movement_copy.pop())

        loot_path.append(addlist)

    # south
    if map[row + 1][col] == 'T':
        map[row + 1][col] = '.'
        addlist = []

        movement_copy = copy.deepcopy(movement_stack)
        addlist.append([row+1,col])

        addlist.append(curr_pos)
        while movement_copy.size() != (0):
            addlist.append(movement_copy.pop())

        loot_path.append(addlist)

    # west
    if map[row][col - 1] == 'T':
        map[row ][col-1] = '.'
        addlist=[]

        movement_copy=copy.deepcopy(movement_stack)
        addlist.append([row,col-1])

        addlist.append(curr_pos)
        while movement_copy.size()!=(0):
            addlist.append(movement_copy.pop())

        loot_path.append(addlist)

    return map

def backtracking(curr_pos,map):
    '''When the curr_pos is at a dead end this will take the movement_stack and pop it until it reach the pos of the top of the inter_stack
    or to the last intersection return the map with the user is at the last intersection and b in the pos that we have already been'''
    goto_pos=inter_stack.pop()
    while True:
        try_pos=movement_stack.pop()
        las_pos=curr_pos
        if try_pos==goto_pos:
            map[curr_pos[0]][curr_pos[1]]='b'
            map[goto_pos[0]][goto_pos[1]]='M'
            do_not_enter.append(las_pos)

            break
        map[curr_pos[0]][curr_pos[1]] = 'b'
        curr_pos = try_pos
    return map

def find_curr_pos(map):
    '''Interate though the list map to find M or the curr pos and return it.'''

    for list in map:
        for x in list:
            if x=='M':
                col=list.index('M')#Rember to strat counting from 0
                list_pos=list
                break
    row=map.index(list_pos)

    return[row,col]

def checker(map,pos):
    '''This check all the possible route that we can take in the map from our curr pos. and return that number. 0 is a dead end so we need to backtrack
    ,1 we just need to move forward if it is more than 2 we need to move forward and add that pos to the inter_stack(this is done in the main() but this is base on the number we return)'''
    row=pos[0]
    col=pos[1]
    las_pos=movement_stack.top()

    num_path=0
    #north
    if map[row-1][col]=='.':
        if las_pos==[row-1,col]:
            pass
        else:
            num_path+=1
    #east
    if map[row][col+1]=='.':
        if las_pos==[row,col+1]:
            pass
        else:
            if [row, col + 1] in do_not_enter:
                pass
            else:
                num_path+=1
    #south
    if map[row+1][col]=='.':
        if las_pos==[row+1,col]:
            pass
        else:
            if [row+1, col ] in do_not_enter:
                pass
            else:
                if [row+1, col] in do_not_enter:
                    pass
                else:
                    num_path+=1
    #west
    if map[row][col-1]=='.':
        if las_pos==[row,col-1]:
            pass
        else:
            if [row, col - 1] in do_not_enter:
                pass
            else:
                num_path+=1
    return num_path

def moving(map,pos,las_pos):
    '''Take the curr pos and move it to the next empty location in the map. Return the new map with the new curr pos and replace the previous pos with a E'''

    row = pos[0]
    col = pos[1]
#There are alot of if statement to check to choose which path to go we do not want to go backward or into a wall or take a path we already took
    #I woould say the lap_pos and the movement stack top is the same check which is reduncecy
    #north
    while True:
        if map[row-1][col]=='.':
            if las_pos==[row - 1,col]:
                pass
            else:
                if [row-1,col] in do_not_enter:
                    pass
                else:
                    if [row - 1, col]==movement_stack.top():
                        pass
                    else:
                        map[row - 1][col] ='M'
                        map[row][col] ='e'
                        break
        #east
        if map[row][col+1]=='.':
            if las_pos==[row,col+1]:
                pass
            else:
                if [row,col+1] in do_not_enter:
                    pass
                else:
                    if [row, col+1] == movement_stack.top():
                        pass
                    else:
                        map[row][col+1] = 'M'
                        map[row][col] = 'e'
                        break
                    # west
        if map[row][col - 1] == '.':
            if las_pos == [row, col - 1]:
                pass
            else:
                if [row, col - 1] in do_not_enter:
                    pass
                else:
                    if [row, col - 1] == movement_stack.top():
                        pass
                    else:
                        map[row][col - 1] = 'M'
                        map[row][col] = 'e'
                        break
        #south
        if map[row+1][col]=='.':
            if las_pos==[row + 1,col]:
                pass
            else:
                if [row+1,col] in do_not_enter:
                    pass
                else:
                    if [row+1, col] == movement_stack.top():
                        pass
                    else:
                        map[row + 1][col] = 'M'
                        map[row][col] = 'e'
                        break
    return map

def main():



    map_1=raw_input('What is the file name that contain the map?')
    mapfile=open(map_1)
    mapfile=mapfile.read()
    total_row=int(mapfile[0]+mapfile[1])
    total_col = int(mapfile[3] + mapfile[4])

    map_pos=6
    map_list=[]
    #This two for loop make list inside of a list to represent the map.
    for x in range(total_row):
        row_list=[]
        for x in range(total_col):
            row_list.append(mapfile[map_pos])
            map_pos+=2

        map_list.append(row_list)

    curr_pos=find_curr_pos(map_list)
    #start pos is the base case which is use when their is no way else to explore and we are back in the start pos end the program
    start_pos=curr_pos
    #This was to fix a bug in where the inter_stack would be empty once you return to it the first time but you will need to try the other path around it
    #and then return it to it a second time
    inter_stack.push(start_pos)

    movement_stack.push(curr_pos)
    #print the map to the console
    for list in map_list:
        print list
    print 'end of map'

    #The las pos is now redunent since the movement_stack.top is the same thing
    las_pos=[0,0]
    #There is reduncecy is this code and something might be checked twice

    #This while loop move though the cave while checking for treasure, intersetion and dead end it also backtrack until it explore all the area
    while True:
        #check for treasure
        map_list=check_loot(map_list,curr_pos)
        #dead end back track to last intersection
        if checker(map_list,curr_pos)==0:
            #Check to see if we are back at the begin which is the base case and that we explore all possible area end the program
            if curr_pos==start_pos:
                for list in loot_path:
                    print 'Path to the loot.'
                    print list
                break
            backtracking(curr_pos,map_list)
            curr_pos=find_curr_pos(map_list)
#move though the cave
        elif checker(map_list, curr_pos) == 1:
            map_list = moving(map_list, curr_pos, las_pos)
            las_pos = curr_pos
            curr_pos = find_curr_pos(map_list)

            movement_stack.push(las_pos)
            #We are at a intersection add curr pos to inter_stack and choose a path to move though
        elif checker(map_list, curr_pos) >=2:
            inter_stack.push(curr_pos)
            map_list = moving(map_list, curr_pos, las_pos)
            las_pos = curr_pos
            curr_pos = find_curr_pos(map_list)

            movement_stack.push(las_pos)
#print new map to the sccreen after every move
        for list in map_list:
            print list
        print 'end of map'

    for list in loot_path:
        time = 0
        for item in list:
            if time==0:
                map_list[item[0]][item[1]]='T'
                time+=1
            else:
                map_list[item[0]][item[1]]='X'
                time+=1

    for list in map_list:
        print list
    print 'end of treasure map follow the x to the treasure mark as T'

main()

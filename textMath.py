def textMath(mathList):
    
    #seach through and do the operations in parentheses
    index=0
    while index < len(mathList):

        #if a right parentheses is found before a left parentheses
        if mathList[index]==")":
            print("Open Parentheses found. Try again")
            return None
        
        elif mathList[index]=="(":
            subIndex=index+1
            openParentheses=1

            #loop until the set of parentheses is closed
            while(openParentheses != 0):

                #if there are still open parentheses at the end of the list
                if(subIndex >= len(mathList)):
                   print("Open Parentheses found")
                   return None

                #A right parentheses opens a set of parentheses
                if mathList[subIndex]=="(":
                    openParentheses+=1
                #A left parentheses closes a set of parentheses
                elif mathList[subIndex]==")":
                    openParentheses-=1

                subIndex+=1

            #take the substring contained with in the parentheses and perform the operations in it
            mathList[index]=textMath(mathList[index+1 : subIndex-1])

            #delete the parentheses and everything inside since it has been replaced with a numeric value
            del mathList[index + 1 : subIndex ]
            
        index+=1


    try:
        #search through and apply the multiplication operator
        index=0
        while index < len(mathList):

            if mathList[index]=="*":
                mathList[index]=float( mathList[index-1] ) * float( mathList[index+1] )
                del mathList[index-1]
                del mathList[index]
            else:
                index+=1

        #search through and apply the division operator
        index=0
        while index < len(mathList):
        
            if mathList[index]=="/":
                mathList[index]=float( mathList[index-1] ) / float( mathList[index+1] )
                del mathList[index-1]
                del mathList[index]
            else:
                index+=1

        #search through and apply the addition operator
        index=0
        while index < len(mathList):
        
            if mathList[index]=="+":
                mathList[index]=float( mathList[index-1] ) + float( mathList[index+1] )
                del mathList[index-1]
                del mathList[index]
            else:
                index+=1

        #search through and apply the subtraction operator
        #**********This must be done before the regular subtraction operator
        #**********since the first '-' would be incorrectly picked up in the search
        index=0
        while index < len(mathList):
        
            if mathList[index]=="--":
                mathList[index]=float( mathList[index+1] ) - float( mathList[index-1] )
                del mathList[index-1]
                del mathList[index]
            else:
                index+=1

        #search through and apply the subtraction operator
        index=0
        while index < len(mathList):
        
            if mathList[index]=="-":
                mathList[index]=float( mathList[index-1] ) - float( mathList[index+1] )
                del mathList[index-1]
                del mathList[index]
            else:
                index+=1

    #this exception will be raised if a non numeric character is found such as 'w' or '?'
    except ValueError:
        print("Your math problem could not be understood")
        return None

    #make sure the value being returned is a float
    if(type(mathList[0]) != float):
        print("Your math problem could not be understood")
        return None

    return mathList[0]

def parseSpeech(speechString):
    
	#ensure that the string has proper spacing around the operators.
	#This will help ensure that situations like this "3/2" will be converted to this "3 / 2".
    index=0
    while index < len(speechString):
        if (speechString[index]=="*") or (speechString[index]=="/") or (speechString[index]=="+") or (speechString[index]=="-"):
            speechString=speechString[ : index] + " " + speechString[index] + " " + speechString[index+1 : ]
            index+=2
        else:
            index+=1

    speechString=speechString.strip()

    #Special case that covers A subtracted from B
    #This used double equals to that it will be handled differently as
    #B-A instead of A-B
    speechString=speechString.replace("subtracted from", "--")

    #special cases for addition
    speechString=speechString.replace("added to", "+")
    speechString=speechString.replace("plus", "+")
    speechString=speechString.replace("summed with", "+")

    #convert parentheses
    speechString=speechString.replace("close parentheses", ")")
    speechString=speechString.replace("parentheses", "(")

    #special cases for division
    speechString=speechString.replace("divided by", "/")
    speechString=speechString.replace("over", "/")

    #special cases for multiplication
    speechString=speechString.replace("times", "*")
    speechString=speechString.replace("x", "*")

    #special case for pi
    speechString=speechString.replace("pi", "3.14159265")
    speechString=speechString.replace("Pi", "3.14159265")

    return speechString

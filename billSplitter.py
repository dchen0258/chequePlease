# Write your code here :-)
import pprint

def intro() :
    print('How many people are you splitting between?')
    global numPeople, people, names
    numPeople = int(input())
    people = {}
    names = []

def getNames() :

    global numPeople, people, names
    for i in range(1 , numPeople + 1) :
        print('Enter the person ' + str(i) + '\'s name')
        name = input()
        people.setdefault(name,{'Total' : 0})
        names.append(name)

def soleExpenses() :

    global people
    for name , receipt in people.items() :
        print ('Enter ' + name + '\'s sole expenses. Type \"q" once you are done. \nItem Name/q:')
        itemName = input()

        while itemName != 'q' :
            receipt.setdefault(itemName, 0)
            print ('Price of ' + itemName + ': ')
            itemPrice = float(input())
            receipt[itemName] += itemPrice
            # receipt['Total'] += itemPrice
            print ('Item Name/q:')
            itemName = input()


def splitExpenses () :

    global numPeople, people, names
    for i in range(numPeople) :
        for j in range (i + 1, numPeople) :
            print ('Enter ' + names [i] + ' and ' + names[j] + '\'s shared expenses. Type \"q" once you are done. \nItem Name/q:')
            itemName = input()
            while itemName != 'q' :
                people[names[i]].setdefault(itemName, 0)
                people[names[j]].setdefault(itemName, 0)
                print ('Price of ' + itemName + ': ')
                itemPrice = float(input())
                people[names[i]][itemName] += itemPrice/2
                people[names[j]][itemName] += itemPrice/2
                print ('Item Name/q:')
                itemName = input()

def sharedExpenses () :
    global numPeople, people, names
    print ('Enter all shared expenses. Type \"q" once you are done. \nItem Name/q:')
    itemName = input()
    while itemName != 'q' :
        for i in range(numPeople) :
            people[names[i]].setdefault(itemName, 0)

        print ('Price of ' + itemName + ': ')
        itemPrice = float(input())

        for i in range(numPeople) :
            people[names[i]][itemName] += itemPrice/float(numPeople)
        print ('Item Name/q:')
        itemName = input()

def addPercentDiscounts():
    global people
    print ('How many different percent discounts do you have?')
    numTaxes = int(input())
    for i in range(numTaxes) :
        print ('What is the discount rate ' + str(i + 1)+ '? Please only write the number.')
        discountRate = float(input())
        if numTaxes == 1:
            print ('Does this discount apply to all items? Write \'y\' for yes and \'n\' for no.')
            if (input() == 'y') :
                for name, receipt in people.items() :
                    for item, price in receipt.items() :
                        if item != ('Total' or 'Tip'):
                            receipt[item] = receipt[item] - (discountRate/100)*receipt[item]

                break
        print('What items apply to this tax rate? Please separate the commas and do not add spaces.')
        items = input().split(',')
        for name, receipt in people.items() :
            for item in items :
                if item in receipt.keys() :
                    receipt[item] = receipt[item] - (discountRate/100)*receipt[item]

# def addDollarDiscounts():
#     global people
#     print ('What dollar discount do you have? Enter 0 if none.')
#     discount = int (input())
#     total = 0
#     for name, receipt in people.items() :
#         total += receipt['Total']



# def addTip () :
#     global people
#     print ('Do you want to add tip? Write \'y\' for yes and \'n\' for no.')
#     if (input() == 'y'):
#         print ('What is the tip amount?')
#         tip = float(input())
#             for name, receipt in people.items() :
#                 receipt.setdefault('Tip', tip)



def addTaxes () :
    global people
    print ('How many different tax rates do you have?')
    numTaxes = int(input())
    for i in range(numTaxes) :
        print ('What is the tax rate ' + str(i + 1)+ '? Please only write the number.')
        taxRate = float(input())
        if numTaxes == 1:
            for name, receipt in people.items() :
                for item, price in receipt.items() :
                    if item != ('Total' or 'Tip') :
                        receipt[item] *= 1 + (taxRate / 100)
        else :
            print('What items apply to this tax rate? Please separate the commas and do not add spaces.')
            items = input().split(',')
            for name, receipt in people.items() :
                for item in items :
                    if item in receipt.keys() :
                        receipt[item] *= 1 + (taxRate / 100)


def calculateIndividualTotals() :
    global people
    for name , receipt in people.items() :
        for item, price in receipt.items() :
            if item != 'Total' :
                receipt['Total'] += price


def printTotal() :
    global people
    pprint.pprint(people)
    total = 0
    for name, receipt in people.items() :
        total += receipt['Total']
    print('The total is: ' + str(total))

def resetTotals() :
    global people
    for name , receipt in people.items() :
        for item, price in receipt.items() :
            if item != 'Total' :
                receipt['Total'] = 0



def billSplitter() :
    intro()
    getNames()
    soleExpenses()
    splitExpenses()
    sharedExpenses()
    calculateIndividualTotals()
    printTotal()
    print('This is the current receipt without tips, taxes, or discounts.')
    addPercentDiscounts()
    resetTotals()
    calculateIndividualTotals()
    printTotal()
    print('This is the current receipt without tips or taxes.')
    addTaxes()
    resetTotals()
    calculateIndividualTotals()
    printTotal()

billSplitter()









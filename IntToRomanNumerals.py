def intToRomanNumerals(num):
    romanNumeralMap = { # a dictionary consisting of key-value pairs of numbers and their Roman numeral equivalents, respectively
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    if (not(type(num) == int)): # executes if num is not an integer
        raise ValueError("The value you entered is not an integer.")
    elif (num >= 4000): # executes if num is greater than or equal to 4000
        raise ValueError("The number you entered is too large to convert to Roman numerals. Please enter a number between 1 and 3999.")
    elif (num < 0): # executes if num equals a negative number
        raise ValueError("The number you entered is a negative number. Please enter a number between 1 and 3999.")
    else:
        if (num == 0): # returns an empty string if num equals 0
            return ""
        
        for value, numeral in romanNumeralMap.items(): # iterates through romanNumeralMap's items with "value" as the key and 
            # "numeral" as the value
            if (num >= value): # executes if num is greater than or equal to the current key of romanNumeralMap
                return numeral + intToRomanNumerals(num - value)
                # returns the current value of romanNumeralMap concatenated with the output of the recursively-called
                # intToRomanNumerals method with the current key of romanNumeralMap subtracted from num
            
# currentYear = 2024
# currentYearInRomanNumeral = intToRomanNumerals(currentYear)
# print(currentYear, "in Roman numerals is", currentYearInRomanNumeral)

# superBowlNumber = 58
# superBowlInRomanNumeral = intToRomanNumerals(superBowlNumber)
# print(superBowlNumber, "in Roman numerals is", superBowlInRomanNumeral)

# olympiadNumber = 33
# olympiadInRomanNumeral = intToRomanNumerals(olympiadNumber)
# print(olympiadNumber, "in Roman numerals is", olympiadInRomanNumeral)
def intToRomanNumerals(num):
    romanNumeralMap = {
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

    if (not(type(num) == int)):
        raise ValueError("The value you entered is not an integer.")
    elif (num >= 4000):
        raise ValueError("The number you entered is too large to convert to Roman numerals. Please enter a number between 1 and 3999.")
    elif (num < 0):
        raise ValueError("The number you entered is a negative number. Please enter a number between 1 and 3999.")
    else:
        if (num == 0):
            return ""
        
        for value, numeral in romanNumeralMap.items():
            if (num >= value):
                return numeral + intToRomanNumerals(num - value)
            
# currentYear = 2024
# currentYearInRomanNumeral = intToRomanNumerals(number)

# print(currentYear, "in Roman numerals is", currentYearInRomanNumeral)
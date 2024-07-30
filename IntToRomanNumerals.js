function intToRomanNumerals(num) {
    const romanNumeralMap = { // an object consisting of key-value pairs of numbers and their Roman numeral equivalents, respectively
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
    };
    const numbers = Object.keys(romanNumeralMap).reverse(); // an array with the keys of romanNumeralMap in the order shown above

    if (!(Number.isInteger(num))) { // executes if num is not an integer
        throw new TypeError("The value you entered is not an integer.");
    }
    else if (num >= 4000) { // executes if num is greater than or equal to 4000
        throw new Error("The number you entered is too large to convert to Roman numerals. Please enter a number between 1 and 3999.");
    }
    else if (num < 0) { // executes if num is a negative number
        throw new Error("The number you entered is a negative number. Please enter a number between 1 and 3999.");
    }
    else {
        if (num == 0) { // returns an empty string if num equals 0
            return "";
        }

        while (num > 0) { // executes while num is greater than 0
            for (let value = 0; value < numbers.length; value++) { // iterates through the numbers array, with "value" as the current index
                if (num >= numbers[value]) { // executes if num is greater than or equal to the current index of the numbers array
                    let numeral = romanNumeralMap[numbers[value]]; // a variable that stores the romanNumeralMap value associated with
                    // the current value from the numbers array
                    return numeral + intToRomanNumerals(num - numbers[value]);
                    // returns the current value of romanNumeralMap concatenated with the output of the recursively-called
                    // intToRomanNumerals method with the current value of the numbers array subtracted from num
                }
            }
        }
    }
}

// let currentYear = 2024;
// let currentYearInRomanNumeral = intToRomanNumerals(currentYear);
// console.log(currentYear + " in Roman numerals is " + currentYearInRomanNumeral);

// let superBowlNumber = 58;
// let superBowlInRomanNumeral = intToRomanNumerals(superBowlNumber);
// console.log(superBowlNumber + " in Roman numerals is " + superBowlInRomanNumeral);

// let olympiadNumber = 33;
// let olympiadInRomanNumeral = intToRomanNumerals(olympiadNumber);
// console.log(olympiadNumber + " in Roman numerals is " + olympiadInRomanNumeral);

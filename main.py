# Tower of Hanoi (homework)
"""
   The puzzle was invented by the French mathematician Édouard Lucas in 1883.
   Numerous myths regarding the ancient and mystical nature of the puzzle
   popped up almost immediately.
   There is a story about an Indian temple in Kashi Vishwanath which contains
   a large room with three time-worn posts in it, surrounded by 64 golden disks.
   Brahmin priests, acting out the command of an ancient prophecy, have been moving
   these disks in accordance with the immutable rules of Brahma since that time.
   The puzzle is therefore also known as the Tower of Brahma puzzle.
   According to the legend, when the last move of the puzzle is completed, the world will end.
   
   If the legend were true, and if the priests were able to move disks at a rate of one per second,
   using the smallest number of moves it would take them (2**64 − 1) seconds ( 2 in power of 64 minus 1)
   
   *****************************************************************************************************
   Your program should give the output how many years and days it is.
   Is the end of the world near?????
   
"""

# help:
# math operations: ** (power), *(multiplication), // (whole division), % (remainder)
# website for conversion from a number to words: https://www.calculatorsoup.com/calculators/conversions/numberstowords.php

#******************************************************************************************************
# Hanoi Towers Program

total_moves_needed = 2 ** 64 - 1
total_seconds = total_moves_needed
seconds_in_words='''
                    eighteen quintillion
                    four hundred forty-six
                    quadrillion seven hundred
                    forty-four trillion
                    seventy-three billion
                    seven hundred nine million
                    five hundred fifty-one thousand
                    six hundred fifteen'''

print(f"To complete  Hanoi Tower: would take {total_seconds} ({seconds_in_words}) seconds,\n")


# in minutes and seconds 
whole_minutes = total_seconds // 60
seconds_remaining = total_seconds % 60
minutes_in_words='''three hundred seven quadrillion
                    four hundred forty-five trillion
                    seven hundred thirty-four billion
                    five hundred sixty-one million
                    eight hundred twenty-five thousand
                    eight hundred sixty '''

print(f"or it would take {whole_minutes} ({minutes_in_words}) minutes and  {seconds_remaining} seconds,\n")


# in hours and minutes
whole_hours=whole_minutes//60
minutes_remaining=whole_hours%60
hours_in_words='''
                    five quadrillion one hundred twenty-four trillion
                    ninety-five billion five hundred seventy-six million
                    thirty thousand four hundred thirty-one'''

print(f"or it would take {whole_hours} ({hours_in_words})hours and {minutes_remaining} minutes,\n")


#in days and hours
whole_days=whole_hours//24
hours_remaining=whole_hours % 24
days_in_words='''
                    two hundred thirteen trillion
                    five hundred three billion
                    nine hundred eighty-two million
                    three hundred thirty-four thousand
                    six hundred one'''

print(f"or it would take {whole_days} ({days_in_words}) days and {hours_remaining} hours,\n")

# in years and days aproximately 
whole_years=whole_days//365
days_remaining=whole_days%365
years_in_words='''
                    five hundred eighty-four billion
                    nine hundred forty-two million
                    four hundred seventeen thousand
                    three hundred fifty-five'''

print(f"or it would take {whole_years}  ({years_in_words}) years and {days_remaining} days,\n")


# in centuries and years
whole_centuries= whole_years//100
years_remaining=whole_years%100
centuries_in_words='''
                    five billion eight hundred forty-nine million
                    four hundred twenty-four thousand
                    one hundred seventy-three '''

print(f"or it would take {whole_centuries} ({centuries_in_words}) centuries and {years_remaining} years.")


# Calculates the average test score after they are all added together
def calc_average(grades):
    return sum(grades)/ len(grades)

# Turns the average score into a letter grade

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif 80<= average < 90:
        return 'B'
    elif 70 <= average <80:
        return 'C'
    elif 60<= average <70:
        return 'D'
    else:
        return 'F'
    
#main function
    
def main():

    total_students = 12
    
# Loop that repeats 12 times because of 12 students

    for i in range(total_students):

        name = input("Enter student name:")
        grades = []

        for x in range(8):
            test_score = float(input(f"Enter test score for {name}:"))
            grades.append(test_score)
            
# calculate the averages

        average = calc_average(grades)
        
#Determines letter grade of the student
        
        grade = determine_grade(average)

#Display results
        
        print(f"\nStudent: {name}")
        print(f"Average Test Score: {average}")
        print(f"Overall Grade: {grade}\n")       

main()
            

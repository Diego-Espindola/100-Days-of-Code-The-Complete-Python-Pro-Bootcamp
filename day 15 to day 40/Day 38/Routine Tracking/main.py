from nutritionix import Nutritionix
from sheety import Sheety

try:
    natural_language_exercise = input("Tell me which exercises you did:\n")

    result = Nutritionix.request_exercise(natural_language_exercise)
    exercises = result.get('exercises')
    if not exercises:
        raise ValueError("No exercise data found in response")

    for exercise in exercises:
        name = exercise.get('name')
        duration = exercise.get('duration_min')
        calories = exercise.get('nf_calories')
        if name and duration and calories:
            Sheety.add_new_row(exercise=name, duration=duration, calories=calories)
            print("Data inserted successfully")
        else:
            raise ValueError("Incomplete exercise data")

except Exception as e:
    print(f"An error occurred: {e}")

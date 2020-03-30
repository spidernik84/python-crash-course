from survey import AnonymousSurvey

question = "What language did you first learn to speak?"

my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to end.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)

# show results

print("\nThank you for participating")
my_survey.show_results()
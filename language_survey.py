from survey import AnonymousSurvey

question = "what's your favorite language?"
language_survey = AnonymousSurvey(question)
language_survey.show_question()
while True:
    new_response = input('language: ')
    if new_response == 'q':
        break
    language_survey.store_response(new_response)
print('----------------------------------')
language_survey.show_result()

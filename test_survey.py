import unittest
from survey import AnonymousSurvey


class TsetAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'what language ?'
        self.language_survey = AnonymousSurvey(question)
        self.responses = ['chinese', 'english', 'japanese']

    def test_store_single_response(self):
        self.language_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.language_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.language_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.language_survey.responses)


if __name__ == '__main__':
    unittest.main()

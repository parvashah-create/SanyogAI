import openai
from decouple import config



class Prompts:
    def __init__(self, openAI_key):
        self._openAI_key = openAI_key
        openai.api_key = openAI_key

    def gpt3_completion(self, prompt):
        """
        Makes an API call to OpenAI's GPT-3.5 and returns the completion.

        Args:
            prompt (str): The prompt to be passed to GPT-3.5.

        Returns:
            str: The completion generated by GPT-3.5.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            messages=[
                {"role": "system", "content": "You are a experienced recruiter"},
                {"role": "user", "content": f"{prompt}"}
            ]
        )

        return response.choices[0].message["content"]

    @property
    def resume_screening(self):
        """
        Generates the security audit prompt.

        Returns:
            str: The security audit prompt.
        """
        prompt = (
            "Analyze the resume above and infer the following information about the candidate:"
            """
            {
            "work_experience":"",
            "education":"",
            "projects":"",
            "hard_skills":"",
            "inferred_soft_skills":""
            }
            """
        )
        return prompt
    
    @property
    def jd_search(self):
        """
        Generates the security audit prompt.

        Returns:
            str: The security audit prompt.
        """
        prompt = (
            "Examine the provided job description and create a comprehensive profile of an ideal candidate suited for this position in short paragraph"
            
        )
        return prompt

# prom = Prompts(config('OPENAI_KEY'))
# prompt = prom.resume_screening
# print(prom.gpt3_completion("Parva Shah" + prompt))
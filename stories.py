"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["place","name","adjective","noun","verb","noun_2"],
    """In a small village named {place}, there once lived a man named, {name}. Now {name}, was a {adjective} kind-of guy who always feared the day he would see a {noun} with his own two eyes. 
    One day, {name} decided to walk through the local valley when he spotted a {noun}. He shrieked and {verb} so fast that he passed out! To this day, {name} is remembered as the {adjective}-{noun_2} of {place}."""
)

stories = [story, story2];

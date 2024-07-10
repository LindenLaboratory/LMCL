from lmcl import init,func,script
init("openai_api_key")
@func
def randomStoryDescription():
    return """
instruction {
Generate a paragraph description of a random made-up story as well as a title for it and its genre
}
logic {
import os
var1 = int(input('Enter Book Number: '))
os.system('clear')
}
format {
BOOK NUMBER: [var1]
TITLE: [title]
GENRE: [genre]
DESCRIPTION: [description]
}
rules {
EXCLUDE: =['Fantasy','Magic']
}
llm {
LLM: ['gpt-3.5-turbo']
TEMPERATURE: [0.2]
}
    """
print(randomStoryDescription().result)

import openai
from io_proj import get_input_from_file

openai.api_key = ""
openai.Engine.list()
prompt = get_input_from_file("../input_files/testfile.py")
p = ""
for line in prompt[1]:
    p += line
print(openai.Completion.create(engine="davinci-codex", prompt="# give comments for \n" + p))

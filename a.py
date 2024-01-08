from bardapi import Bard

import os

os.environ["_BARD_API_KEY"] = "ewgifj5X2CmZV9YBKimqnGrmHXKxBAbV-z_zGwKj602U13P488aaXgOqgzl-beAVDfkWlg."

prompt=input("Enter your prompt:")

print(Bard().get_answer(prompt))
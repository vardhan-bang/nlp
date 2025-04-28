import pandas as pd

data = {
    "Base Word":["play","happy","run","write","book","un","care","boy"],
    "Added Morpheme":["-ed","-ness","-ing","-er","-s","-happy","-less","-ish"],
    "New Word":["played","happiness","running","writer","books","unhappy","careless","boyish"],
}

df = pd.DataFrame(data)
df['Deleted Morpheme'] = df['Added Morpheme']
df['New word after deletion'] = df['Base Word']
df

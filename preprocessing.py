import re

def clean(text):
  # to lower case
  text = text.lower()
  # remove html tags
  text = re.sub(r"<.+?>", " ", text)
  # keep only alphanumeric and spaces
  text = re.sub(r"[^A-Za-z ]", " ", text)
  # remove multiple spaces
  text = re.sub(" +", " ", text)

  # strip spaces at the beginning and end
  return text.strip()

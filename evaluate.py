class Solution:

  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    # Build the dictionary efficiently
    dictionary = {k: v for k, v in knowledge}

    res = []
    curr_key = ""
    in_bracket = False

    for char in s:
      if char == "(":
        in_bracket = True
        curr_key = ""
      elif char == ")":
        in_bracket = False
        # If key exists, append its value; otherwise, append '?'
        res.append(dictionary.get(curr_key, "?"))
        curr_key = ""
      elif in_bracket:
        curr_key += char
      else:
        # Regular character outside of brackets
        res.append(char)

    return "".join(res)

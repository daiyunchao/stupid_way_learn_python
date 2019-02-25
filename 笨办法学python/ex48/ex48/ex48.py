class Lexicon(object):
  def __init__(self):
    self.directions=['north','south','east','west','down','up','left','right','back']
    self.verbs=['go','stop','kill','eat']
    self.stops=['the', 'in', 'of', 'from', 'at', 'it']
    self.nouns=['door','bear','princess','cabinet']
  def scan(self,user_inputs_str):
    input_words=user_inputs_str.split(' ')
    ret_vals=[]
    for word in input_words:
      if word in self.directions:
        ret_vals.append(('direction',word))
      elif word in self.verbs:
        ret_vals.append(('verb',word))
      elif word in self.stops:
        ret_vals.append(('stop',word))
      elif word in self.nouns:
        ret_vals.append(('noun',word))
      else:
        try:
          ret_vals.append(('number',int(word)))
        except ValueError:
          ret_vals.append(('error',word))
    
    return ret_vals


lexicon=Lexicon()

# 判断元素是否在数组中 in
#
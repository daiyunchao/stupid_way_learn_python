#coding=utf-8
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

class ParserError(Exception):
  pass

class Sentence(object):
  def __init__(self,subject,verb,object):
    self.subject=subject[1]
    self.verb=verb[1]
    self.object=object[1]
  
def peek(word_list):
  if word_list:
    word=word_list[0]
    return word
  else:
    return None

def match(word_list,expecting):
  if word_list:
    word=word_list.pop(0)

    if word[0]==expecting:
      return word
    else:
      return None

def skip(word_list,word_type):
  while peek(word_list)==word_type:
    match(word_list,word_type)

def parse_verb(word_list):
  skip(word_list,'verb')

  if peek(word_list)=='verb':
    return match(word_list,'verb')
  else:
    raise ParserError("Expcted a verb next.")

def parse_object(word_list):
  skip(word_list,'stop')
  next=peek(word_list)

  if next=='noun':
    return match(word_list,'noun')
  if next=='direction':
    return match(word_list,'direction')
  else:
    raise ParserError('Excepted a noun or direction next.')

def parse_subject(word_list,subj):
  verb=parse_verb(word_list)
  obj=parse_object(word_list)
  return Sentence(subj,verb,obj)

def parse_sentence(word_list):
  skip(word_list,'stop')
  start=peek(word_list)

  if start=='noun':
    subj=match(word_list,'noun')
    return parse_subject(word_list,subj)
  elif start=='verb':
    return parse_subject(word_list,('noun','player'))
  else:
    raise ParserError('Must start with subject,object,or verb not :%s' %start)  
lexicon=Lexicon()


# 判断元素是否在数组中 in
#
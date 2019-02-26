from nose.tools import *
from ex48.ex48 import lexicon,peek,match,skip,parse_verb,parse_object,parse_subject,parse_sentence,ParserError

def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'), ('direction', 'south'), ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'), ('verb', 'kill'), ('verb', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'), ('stop', 'in'), ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'), ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3), ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'), ('error', 'IAS'), ('noun', 'princess')])

def test_peek():
  result=peek([('verb','kill'),('noun','door')])
  assert_equal(result,('verb','kill'))

def test_match():
  word_listA=[('verb','kill'),('direction','north')]
  result=match(word_listA,'verb')
  assert_equal(result,('verb','kill'))

def test_skip():
     result=skip([('verb','kill'),('direction','north')],'verb')
     assert_equal(result,('verb','kill'))
     
def test_parse_verb():
    result=parse_verb([('verb','kill'),('direction','north')])
    assert_equal(result,('verb','kill'))
    assert_raises(ParserError,parse_verb,[('stop','the'),('direction','north')])
    

def test_parse_object():
    result=parse_object([('stop','the'),('noun','door')])
    assert_equal(result,('noun','door'))
    result1=parse_object([('stop','the'),('direction','north')])
    assert_equal(result1,('direction','north'))    
    assert_raises(ParserError,parse_object,[('stop','the'),('verb','go')])

def test_parse_subject():
    result=parse_subject([('verb','go'),('stop','the'),('noun','door')],('m','k'))
    assert_equal(result.subject,'k')
    assert_equal(result.verb,'go')
    assert_equal(result.object,'door')
    
def test_parse_sentence():
    result=parse_sentence([('verb','go'),('stop','the'),('noun','door')])
    assert_equal(result.subject,'player')
    assert_equal(result.verb,'go')
    assert_equal(result.object,'door')
    
    result1=parse_sentence([('stop','in'),('noun','door'),('verb','go'),('direction','north')])
    assert_equal(result1.subject,'door')
    assert_equal(result1.verb,'go')
    assert_equal(result1.object,'north')
    
    assert_raises(ParserError,parse_sentence,[('stop','in'),('stop','the')])
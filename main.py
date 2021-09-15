import os
import json
import config
from playsound import playsound
from requests import Session

os.system('')
print(config.welcome)
sess = Session()
sess.trust_env = False

while True:
    query = input(f'({config.language_code}) > ')
    if query == '-lang':
        print('| code\t | language\t |\n'
              '-----------------------------')
        [print(f'| {code}\t | {language}\t |') for code, language in config.language_list.items()]
        config.language_code = input('New language code: ')
        continue
    response = sess.get(f"https://api.dictionaryapi.dev/api/v2/entries/{config.language_code}/{query}", verify=True)
    if response.status_code != 200:
        print('Network error: status =', response.status_code)
        print('* The 404 error will occur if the word does not exist.')
        continue
    meaning = json.loads(response.text)[0]
    if 'word' not in meaning.keys():
        print("Cannot parse response data from Free Dictionary API.")
        continue
    print('\33[35m' + meaning['word'] + '\33[0m')
    print('\33[31mPhonetics:\33[0m')
    if 'phonetics' in meaning.keys():
        for phonetic in meaning['phonetics']:
            if 'text' in phonetic.keys():
                print('\t' + phonetic['text'])
            if 'audio' in phonetic.keys() and config.play_sound:
                try:
                    playsound('https:' + phonetic['audio'])
                except:
                    config.play_sound = False
    print('\33[31mMeaning:\33[0m')
    if 'meanings' in meaning.keys():
        for meaning_ in meaning['meanings']:
            if 'partOfSpeech' in meaning_.keys():
                print('\t\33[33m' + meaning_['partOfSpeech'] + '\33[0m')
            if 'definitions' in meaning_.keys():
                for def_ in meaning_['definitions']:
                    print(def_['definition'])
                    if 'example' in def_.keys() and def_['example']:
                        print('\t\33[32me.g. ' + def_['example'] + '\33[0m')
                    if 'synonyms' in def_.keys() and def_['synonyms']:
                        print('\t\33[34msynonyms: ' + ', '.join(def_['synonyms']) + '\33[0m')

MALE = 'male' 
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both' 

MALE_WORDS = set([
        'guy','spokesman','chairman',"men's",'men','him',"he's",'his',
        'boy','boyfriend','boyfriends','boys','brother','brothers','dad',
        'dads','dude','father','fathers','fiance','gentleman','gentlemen',
        'god','grandfather','grandpa','grandson','groom','he','himself',
        'husband','husbands','king','male','man','mr','nephew','nephews',
        'priest','prince','son','sons','uncle','uncles','waiter','widower',
        'widowers'
])

FEMALE_WORDS = set([
        'heroine','spokeswoman','chairwoman',"women's",'actress','women',
        "she's",'her','aunt','aunts','bride','daughter','daughters','female',
        'fiancee','girl','girlfriend','girlfriends','girls','goddess',
        'granddaughter','grandma','grandmother','herself','ladies','lady',
        'lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
        'priestess','princess','queens','she','sister','sisters','waitress',
        'widow','widows','wife','wives','woman'
])

# Now if we randomly take a senetence and try to GENDERISE it. Then we go through the words in the sentence. And if 
# all the count of words which fell in the MALE_WORDS category is non_zero and the number of words falling in the 
# female category is zero. Then the sentence is MALE sentence. Otherwise for the opposite thing it will be a female sentence. 
# If there is a non-zero count of both the words then it will be a unknown and both stuff. 

def genderize(words): 
        one = len(MALE_WORDS.intersection(words))
        two = len(FEMALE_WORDS.intersection(words))

        if one == 0 and two == 0: 
                return UNKNOWN
        elif one > 0 and two > 0: 
                return BOTH 
        elif one > 0 and two == 0: 
                return MALE
        else: 
                return FEMALE

from collections import Counter

def count_gender(sentences): 
        sents = Counter()
        words = Counter()

        for sentence in sentences: 
                gender = genderize(sentence) 
                sents[gender] += 1
                words[gender] += len(sentence)

        return sents, words 

# Finally, in order to engage our gender counters, we require some mechanism for
# parsing the raw text of the articles into component sentences and words, and for this
# we will use the NLTK library

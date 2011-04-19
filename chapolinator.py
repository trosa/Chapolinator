import random

class Chapolinator():

    def _triples(self, words):
        if len(words) < 3:
            return
        for i in range(len(words) - 2):
            yield (words[i], words[i+1], words[i+2])

    def _get_words(self):
        corpus = open('corpus.txt', 'r')
        corpus_data = corpus.read()
        corpus.close()
        phrases = corpus_data.split('\r\n')
        words = corpus_data.split()
        return words, phrases

    def _get_wordcache(self, words):
        wordcache = {}
        for w1, w2, w3 in self._triples(words):
            key = (w1, w2)
            if key in wordcache:
                if not w3 in wordcache[key]:
                    wordcache[key].append(w3)
            else:
                wordcache[key] = [w3]
        return wordcache

    def __init__(self):
        self.words, self.phrases = self._get_words()
        self.wordcache = self._get_wordcache(self.words)
    
    def talk(self):
        '''
        Puts together some messed up proverb, Chapolin Colorado-style
        '''
        #the below line requires that the corpus is made of well-formed phrases
        ini_indexes = [self.words.index(word) for word in self.words if word[0].isupper()]
        mid_indexes = [self.words.index(word) for word in self.words if word[0].islower() and not word.endswith('.')]
        chapo_talk = []

        while not ' '.join(chapo_talk).endswith('.') or ' '.join(chapo_talk) in self.phrases:
            chapo_talk = []
            seed = random.choice(ini_indexes)
            w1, w2 = self.words[seed], self.words[seed+1]
            while not len(chapo_talk) > 4 and len(' '.join(chapo_talk)) <= 123 or not ' '.join(chapo_talk).endswith('.'):
                if ' '.join(chapo_talk + [w1]) in self.phrases:
                    seed = random.choice(mid_indexes[:-3])
                    w1, w2 = self.words[seed], self.words[seed+1]
                    chapo_talk.append(w1)
                elif w1.endswith('.') and len(chapo_talk) <= 4:
                    chapo_talk.append(w1.strip('.').lower())
                elif w1[0].isupper() and len(chapo_talk) > 0:
                    chapo_talk.append(w1.lower())
                else:
                    chapo_talk.append(w1)
                nextcache = self.wordcache[(w1, w2)]
                if (w1.lower(), w2) in self.wordcache:
                    nextcache += self.wordcache[(w1.lower(), w2)]
                w1, w2 = w2, random.choice(nextcache)

        if chapo_talk:
            #print ' '.join(chapo_talk).decode('latin-1').encode('utf-8'), ' | ', len(chapo_talk), ' | ', len(' '.join(chapo_talk))
            return ' '.join(chapo_talk)


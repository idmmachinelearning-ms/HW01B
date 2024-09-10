# p5.js sketch link = https://editor.p5js.org/thiagohersan/sketches/KJO5CEwKM

# edits: did not include sans serif font, used default instead

class FadingWord(object):
    def __init__(self, word, wordDelay):
        self.word = word
        self.alpha = 255
        self.startTime = millis()
        self.letterDelay = wordDelay / len(self.word)
        
        self.red = 0
        self.size = minTextSize
        self.yOffset = 0
        self.fadeVel = -0.3
        
        if ((self.word.lower() == "glitch") or (random(0, 1) > 0.95)):
            self.word = self.word.upper()
            self.red = 200
            self.size = maxTextSize
            self.yOffset = -self.size / 6
            self.fadeVel = -0.01
            
        textSize(self.size)
        self.width = textWidth(self.word)
            
        if cx + textWidth(self.word) > width - MARGIN:
            cx = MARGIN
            cy += lineHeight
            if cy > height - MARGIN:
                cy = MARGIN
                
        self.x = cx
        self.y = cy
        
        cx += self.width + spaceWidth
    
    def update(self):
        self.alpha += self.fadeVel
        
    def display(self):
        elapsed = millis() - self.startTime
        lastLetter = min(floor(elapsed / self.letterDelay), len(self.word))
        letters = self.word[0:len(self.word)]
        
        fill(self.red, 0, 0, self.alpha)
        textSize(self.size)
        text(letters, self.x, self.y + self.yOffset)
        
      
phrase = "Glitch is something that extends beyond the most literal technological mechanics: it helps us to celebrate failure as a generative force, a new way to take on the world."

MARGIN = 40

def setup():
    global phrase, MARGIN, words, drawnWords, nextWord, wordCount, nextUpdateMillis, minTextSize, maxTextSize, cx, cy, spaceWidth, lineHeight
    size(displayWidth, displayHeight)
    
    words = phrase.split(" ")
    drawnWords = []
    
    cx = MARGIN
    cy = MARGIN
    
    wordCount = 0
    nextUpdateMillis = 0
    
    minTextSize = 20
    maxTextSize = 30
    
    textAlign(LEFT, TOP)
    textSize(minTextSize)
    
    spaceWidth = textWidth(" ")
    lineHeight = 1.5 * minTextSize
    
    # referred to Objects example 
    
    
def isVisible(fw):
    return fw.alpha > 0


def draw():
    background(220)
    
    drawnWords = drawnWords.filter(isVisible)
    


    
    if millis() > nextUpdateMillis:
        nextWordIndex = wordCount % len(words)
        nextWord = words[nextWordIndex]
        
        wordDelay = random(450,600)
        
        drawnWords.append(FadingWord(nextWord, wordDelay))

        
        wordCount += 1
        
        nextUpdateMillis = millis() + 1.2 * wordDelay
        
    for nextWord in drawnWords:
        nextWord.display()
        nextWord.update()
    
    

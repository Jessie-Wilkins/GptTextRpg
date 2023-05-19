
class TextInterface:
    
    def RenderText(self,*text: str):
        new_text = ""
        new_line = False
        for single_text in text:
            if new_line:
                new_text = new_text + "\n"
            else:
                new_line = True
            new_text = new_text + single_text
        return new_text
    
    def UserInput(self):
        return input()
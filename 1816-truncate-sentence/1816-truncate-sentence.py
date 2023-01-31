class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        a=s.split(" ")                  # create "a" a list of elements
        return " ".join(a[0:k])         # we traverse list and join() gives a str so we return that                                           string now
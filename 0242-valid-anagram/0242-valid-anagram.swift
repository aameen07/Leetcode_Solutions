class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var d=[Character: Int]()
        for i in s {
            if let count = d[i] {
                d[i]=count+1
            } else {
                d[i]=1
            }
        }
        for j in t {
            if let count = d[j] {
                d[j]=count-1
            } else {
                return false
            }
        }
        for (_,v) in d {
            if v != 0 {
                return false
            }
        }
        return true
    }
}
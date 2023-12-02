class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var dic = [Int:Int]()
        for i in nums {
            if dic[i] == nil {
                dic[i] = 1
            } else {
                return true
            }
        }
        return false
    }
}

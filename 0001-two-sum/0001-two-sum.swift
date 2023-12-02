class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var d = [Int:Int]()
        
        for i in 0..<nums.count {
            if let targeted = d[target-nums[i]] {
                return [targeted,i]
            }
            d[nums[i]]=i
        }
        return []
    }
}
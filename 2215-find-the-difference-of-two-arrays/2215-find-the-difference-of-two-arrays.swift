class Solution {
    func findDifference(_ nums1: [Int], _ nums2: [Int]) -> [[Int]] {
        
        [Array(Set(nums1).subtracting(nums2)), Array(Set(nums2).subtracting(nums1))]
    }
}
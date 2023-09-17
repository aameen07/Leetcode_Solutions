class Solution {
    func rotateString(_ s: String, _ goal: String) -> Bool {
        return s==goal || s.count==goal.count && (s+s).contains(goal)
    }
}
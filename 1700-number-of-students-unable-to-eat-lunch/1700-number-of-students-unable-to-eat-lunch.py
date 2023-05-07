class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students=collections.Counter(students)
        for sand in sandwiches:
            if not students[sand]:
                break
            students[sand]-=1
        
        return sum(students.values())
        
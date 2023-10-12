import Foundation

func solution(_ n: Int, _ a: Int, _ b: Int) -> Int {
    var answer = 0
    var x: Float = Float(a)
    var y: Float = Float(b)
        
    while x != y {
        x = ceil(x / 2)
        y = ceil(y / 2)
        answer += 1
    }
    
    return answer
}
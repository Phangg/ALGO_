import Foundation

func solution(_ n: Int) -> [Int] {
    var answer = [Int]()
    var tri = Array(repeating: Array(repeating: 0, count: n), count: n)
    
    var (x, y) = (-1, 0)
    var num = 1
    
    for i in 0..<n {
        for _ in i..<n {            
            switch i % 3 {
                case 0:
                    x += 1
                case 1:
                    y += 1
                default: // case 2
                    x -= 1
                    y -= 1
            }
            tri[x][y] = num
            num += 1
        }
    }
    
    for i in 0..<n {
        for j in 0...i {
            answer.append(tri[i][j])
        }
    }
    
    return answer
}
import Foundation

func solution(_ n: Int, _ computers: [[Int]]) -> Int {
    var visited = Array(repeating: false, count: n)
    var answer: Int = 0
    
    func dfs(_ c: Int) {
        visited[c] = true
        for i in 0..<n {
            if computers[c][i] == 1 && visited[i] == false {
                dfs(i)
            }
        }
    }
    
    for i in 0..<n {
        if !visited[i] {
            answer += 1
            dfs(i)
        }
    }
    
    return answer
}
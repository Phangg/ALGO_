import Foundation

func solution(_ keymap: [String], _ targets: [String]) -> [Int] {
    var keyDictionary = [String: Int]()
    var keymap = keymap.map { $0.map { String($0) } }
    var answer = [Int]()
    
    for key in keymap {
        for k in key {
            if keyDictionary[k] == nil {
                keyDictionary[k] = key.firstIndex(of: k)! + 1
            } else {
                keyDictionary[k] = min(keyDictionary[k]!, key.firstIndex(of: k)! + 1)
            }
        }
    }

    for target in targets {
        var res = 0
        for t in target.map { String($0) } {
            if keyDictionary[t] == nil {
                res = -1
                break
            } else {
                res += keyDictionary[t]!
            }
        }
        answer.append(res)
    }
    
    return answer
}
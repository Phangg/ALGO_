import Foundation

func solution(_ s: String) -> Int {
    var answer = ""
    let numberDictionary = [
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    ]
    var tmp_s = ""
    for c in s {
        if let num = numberDictionary[tmp_s] {
            answer.append(num)
            tmp_s = ""
        }
        
        if let _ = Int(String(c)) {
            answer.append(c)
        } else {
            tmp_s.append(c)
        }
    }
    
    if !tmp_s.isEmpty {
        answer.append(numberDictionary[tmp_s] ?? "")
    }
        
    return Int(answer)!
}
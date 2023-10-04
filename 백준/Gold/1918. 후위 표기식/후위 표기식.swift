let inputValue = readLine()!

var answer = [String]()
var specialCharacter = [String]()
let priorityOrder: [String: Int] = ["*": 1, "/": 1, "+": 2, "-": 2]

for char in inputValue {
    let c = String(char)

    switch c {
        case "A"..."Z":
        answer.append(c)
        case "+", "-", "*", "/":
        while let lastValue = specialCharacter.last, lastValue != "(",
        priorityOrder[c]! >= priorityOrder[lastValue]! {
            answer.append(specialCharacter.popLast()!)
        }
        specialCharacter.append(c)
        case "(":
        specialCharacter.append(c)
        case ")":
        while let lastValue = specialCharacter.last, lastValue != "(" {
            answer.append(specialCharacter.popLast()!)
        }
        _ = specialCharacter.popLast()!
        default: break
    }
}
answer += specialCharacter.reversed()

print(answer.joined(separator: ""))

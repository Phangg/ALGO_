import Foundation

func getCombinations(_ order: String, _ targetNum: Int, _ dict: inout [String: Int]) {
    func combination(_ index: Int, _ comb: String) {
        if comb.count == targetNum {
            let str = String(Array(comb.sorted()))
            dict[str, default: 0] += 1
            return
        }
        for i in index..<order.count {
            let nextCharIndex = order.index(order.startIndex, offsetBy: i)
            combination(i + 1, comb + String(order[nextCharIndex]))
        }
    }
    combination(0, "")
}

func solution(_ orders: [String], _ course: [Int]) -> [String] {
    var result = [String]()

    for c in course {
        
        var dict = [String: Int]()
        for order in orders {
            if c <= order.count {
                getCombinations(order, c, &dict)
            }
        }
        
        let maxValue = dict.values.max()
        result += dict.filter { $0.value > 1 && $0.value == maxValue }.map { $0.key }
    }
    
    return result.sorted()
}
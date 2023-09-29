import Foundation

func solution(_ today: String, _ terms: [String], _ privacies: [String]) -> [Int] {
    var answer = [Int]()
    
    let now = today.components(separatedBy: ".").map{ Int($0)! }
    
    let termsComponents = terms.map{ $0.components(separatedBy: " ") }
    var termsDictionary = [String:Int]()
    termsComponents.map{ termsDictionary[$0[0]] = Int($0[1]) }
    
    let privaciesComponents = privacies.map{ $0.components(separatedBy: " ") }
    
    for (idx, p) in privaciesComponents.enumerated() {
        let end = p[0].components(separatedBy: ".").map{ Int($0)! }
        let type = p[1]
        
        var (y, m, d) = (end[0], end[1], end[2])
                
        m += termsDictionary[type]!
        if m > 12 {
            let (q, r) = m.quotientAndRemainder(dividingBy: 12)
            if r == 0 {
                m = 12
                y += (q - 1)
            } else {
                m = r
                y += q
            }
        }
        
        d -= 1
        if d == 0 {
            d = 28
            m -= 1
            if m == 0 {
                m = 12
                y -= 1
            }
        }
        
        if now[0] > y {
            answer.append(idx + 1)
        } else if now[0] == y, now[1] > m {
            answer.append(idx + 1)
        } else if now[0] == y, now[1] == m, now[2] > d {
            answer.append(idx + 1)
        }

    }
        
    return answer
}
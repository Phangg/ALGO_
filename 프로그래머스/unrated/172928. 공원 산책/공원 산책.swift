import Foundation

func getParseData(_ data: String) -> (String, Int) {
    let components = data.components(separatedBy: " ")
    return (components[0], Int(components[1])!)
}

func getStartPoint(_ park: [String]) -> (Int, Int)? {
    if let rowIndex = park.firstIndex(where: { $0.contains("S") }) {
        if let colIndex = park[rowIndex].firstIndex(of: "S") {
            let row = park.distance(from: park.startIndex, to: rowIndex)
            let col = park[rowIndex].distance(from: park[rowIndex].startIndex, to: colIndex)
            return (row, col)
        }
    }
    return nil
}

func solution(_ park: [String], _ routes: [String]) -> [Int] {
    let wayDictionary: [String:(Int, Int)] = ["E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)]
    let (row, col) = (park.count, park[0].count)
    guard var (x, y) = getStartPoint(park) else {
        return []
    }
    // print(x, y)
    
    for r in routes {
        let (way, cnt) = getParseData(r)
        let (i, j) = wayDictionary[way]!
        
        var flag = true
        for k in 1...cnt {
            let nx = x + (i * k)
            let ny = y + (j * k)
            if 0 > nx || nx >= row || 0 > ny || ny >= col {
                flag = false
                break
            }
            let charIndex = park[nx].index(park[nx].startIndex, offsetBy: ny)
            if park[nx][charIndex] == "X" {
                flag = false
                break
            }
        }
        
        if flag {
            x += (i * cnt)
            y += (j * cnt)
        }
        
        // print(way, cnt)
    }
    
    
    return [x, y]
}
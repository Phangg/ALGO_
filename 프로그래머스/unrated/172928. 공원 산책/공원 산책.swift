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
    
    for r in routes {
        let (way, cnt) = getParseData(r)
        let (i, j) = wayDictionary[way]!

        let isValidMove = (1...cnt).allSatisfy { k in
            let nx = x + (i * k)
            let ny = y + (j * k)

            guard (0..<row).contains(nx), (0..<col).contains(ny) else {
                return false
            }

            let charIndex = park[nx].index(park[nx].startIndex, offsetBy: ny)
            return park[nx][charIndex] != "X"
        }

        if isValidMove {
            x += (i * cnt)
            y += (j * cnt)
        }
    }
    return [x, y]
}
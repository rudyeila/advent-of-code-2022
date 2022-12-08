import java.io.File

/*
* 1 ROCK
* 2 PAPER
* 3 SCISSORS
*
* ROCK:
*   1 1 = D
*   2 1 = L
*   3 1 = W
*
* PAPER:
*   1 2 = W
*   2 2 = D
*   3 2 = L
*
* SCISSORS:
*   1 3 = L
*   2 3 = W
*   3 3 = D
* */

val winAgainst = mapOf('C' to 'X', 'A' to 'Y', 'B' to 'Z')
val loseAgainst = mapOf('A' to 'Z', 'B' to 'X', 'C' to 'Y')
val drawAgainst = mapOf('A' to 'X', 'B' to 'Y', 'C' to 'Z')

val strategyMap = mapOf('Z' to winAgainst, 'Y' to drawAgainst, 'X' to loseAgainst)

fun getScore(opMove: Char, ownMove: Char) : Int {

    var opMoveInt: Int = opMove.code - 64
    var ownMoveInt: Int = ownMove.code - 87

    var result = 0
    if (opMoveInt == ownMoveInt) {
        result = 3
    } else if (winAgainst[opMove] == ownMove) {
        result = 6
    }

    return ownMoveInt + result;
}

fun playRoundPart1(round: String) : Int {
    var score = 0
    var moves = round.split(" ")
    var opMove = moves[0].first()
    var ownMove = moves[1].first()

    return getScore(opMove, ownMove)
}


fun playRoundPart2(round: String) : Int {
    var score = 0
    var moves = round.split(" ")
    var opMove = moves[0].first()
    var expectedResult = moves[1].first()
    var ownMove = strategyMap[expectedResult]?.get(opMove) ?: 'Y'
    return getScore(opMove, ownMove)
}


fun main(args: Array<String>) {
    var inputFile = "src/main/kotlin/input.txt"
    var rounds = File(inputFile).useLines { it.toList() }
    var totalScore = 0
    for (round in rounds) {
        totalScore += playRoundPart1(round)
    }
    print(totalScore)
    print("\n")
    totalScore = 0
    for (round in rounds) {
        totalScore += playRoundPart2(round)
    }
    print(totalScore)
}
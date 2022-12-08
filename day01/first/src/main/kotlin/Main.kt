import java.io.File

fun parseInput(fileName: String) : List<String> {
    return File(fileName).bufferedReader().readLines()
}

fun getAllCalories(foods: List<String>) : List<Int> {
    var maxCalories = 0
    var elfCalories = 0
    var elfTotals: ArrayList<Int> = arrayListOf()

    for (food in foods) {
        if (food == "") {
            elfTotals.add(elfCalories)
            elfCalories = 0
        } else {
            elfCalories += food.toInt()
        }

        if (elfCalories > maxCalories) {
            maxCalories = elfCalories
        }
    }
    elfTotals.add(elfCalories)
    elfTotals.sort()
    elfTotals.reverse()
    return elfTotals
}



fun main(args: Array<String>) {
    var inputFile = "src/main/kotlin/input.txt"
    var foods = parseInput(inputFile)
    var calories = getAllCalories(foods)

    var maxCalories = calories.get(0)
    print(maxCalories)
    print("\n")

    var maxThree = calories.take(3).sum()
    print(maxThree)
}

import UIKit

// variables are mutable
// let constants are immutable
var greeting: String = "Hello, playground"
print(greeting)

greeting = "likes Hummus"
print(greeting)

var name  = "Jethro"
print(name + " " + greeting)

let listOfPeople = ["Jethro","Ming","Lin"]
let likeHummus = "likes Hummus"

print("------------------")
for name in listOfPeople{
    // greeting = name + " " + "likes Hummus"
    greeting = "\(name) \(likeHummus) a lot"
    print(greeting)
}

let names: [String] = [
    "A","B","C","D","E"
]
for name in names{
    print("\(name) likes to skateboard.")
}

struct PersonWithHobby{
    let name: String
    let hobby: String
}

func printDash(){
    print("-------------------------")
}

let people: [PersonWithHobby] = [
    PersonWithHobby(
        name: "ron",
        hobby: "skateboard"),
    PersonWithHobby(
        name: "elmo",
        hobby: "program"),
    PersonWithHobby(
        name: "cookie",
        hobby: "bake"),
    PersonWithHobby(
        name: "big bird",
        hobby: "fly"),
    PersonWithHobby(
        name: "grover",
        hobby: "nothing"),
    PersonWithHobby(
        name: "oscar",
        hobby: "nothing"),

]

printDash()
for p in people {
    print("\(p.name.capitalized) likes \(p.hobby).")
}



// introduce optionals
// [1,2,10,-3,10]

var x: Int = 7  // cann't be assigned to type int
var y: Int? = 10

x = 123
y = 1245
y = nil

struct PersonWithOptHobby{
    let name: String
    let hobby: String
}

let opt_people: [PersonWithOptHobby] = [
    PersonWithOptHobby(
        name: "ron",
        hobby: "skateboard"),
    PersonWithOptHobby(
        name: "elmo",
        hobby: "program"),
    PersonWithOptHobby(
        name: "cookie",
        hobby: "bake"),
    PersonWithOptHobby(
        name: "big bird",
        hobby: "fly"),
    PersonWithOptHobby(
        name: "grover",
        hobby: "?"),
    PersonWithOptHobby(
        name: "oscar",
        hobby: "?"),

]

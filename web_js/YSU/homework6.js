//Task1
const myObject = {
    name: "Janik",
    age: 75,
    city: "Leninakan"
};

for (const key of Object.keys(myObject)) {
    console.log(`${key}`);
}
//Task 2
function* idGenerator() {
    let id = 1;
    while (true) {
        yield id++;
    }
}

const generator = idGenerator();

console.log(generator.next().value); 
console.log(generator.next().value); 
console.log(generator.next().value); 

//Task 3
const getLargestThree = (array) => array.sort((a, b) => b - a).slice(0, 3);

const myArray = [1, 2, 3, 4, 5];
console.log(getLargestThree(myArray)); 
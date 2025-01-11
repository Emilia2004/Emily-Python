// Task 1
const person1 = {
    name: 'Anna',
    age: 22,
};

const person2 = {
    name: 'David',
    age: 35,
};

function display() {
    console.log(this);
}

const displayPerson1 = display.bind(person1);
displayPerson1();

// Task 2
const theme1 = {
    color: 'green',
    fontSize: '14px',
    margin: '15px'
};

const theme2 = {
    backgroundColor: 'yellow'
};

function applyStyles(source) {
    this.color = source.color;
    this.fontSize = source.fontSize;
    this.margin = source.margin;
}

applyStyles.call(theme2, theme1);

console.log(theme2);

// Task 3
const rectangle = {
    length: 6,
    width: 8,
    height: 10,
    volume: function() {
        return this.length * this.width * this.height;
    }
};

const rectangle2 = Object.create(rectangle);
rectangle2.surfaceArea = function() {
    return 2 * (this.length * this.width + this.width * this.height + this.height * this.length);
};

console.log(rectangle2.volume());
console.log(rectangle2.surfaceArea());
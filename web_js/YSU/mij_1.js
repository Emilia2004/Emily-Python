const students = [
    { name: "Anna", surname: "Sahakyan", scholarship: 1500 },
    { name: "Armen", surname: "Karapetyan", scholarship: 500 },
    { name: "Sona", surname: "Manukyan", scholarship: 2000 }
];

students.forEach(student => {
    if (student.scholarship > 1000) {
        console.log(`${student.name} ${student.surname}`);
    }
});

//Task 1
function addPunctuals(employees) {
    let table = document.createElement('table');
    let headerRow = table.insertRow();
    let nameHeader = headerRow.insertCell(0);
    let surnameHeader = headerRow.insertCell(1);
    nameHeader.innerHTML = 'Name';
    surnameHeader.innerHTML = 'Surname';

    employees.forEach(employee => {
        if (employee.lateTime === 0) {
            let row = table.insertRow();
            let nameCell = row.insertCell(0);
            let surnameCell = row.insertCell(1);
            nameCell.innerHTML = employee.name;
            surnameCell.innerHTML = employee.surname;
        }
    });

    document.body.appendChild(table);
}

let employees = [
    { name: 'ynker', surname: 'Saroyan', lateTime: 0 },
    { name: 'Aram', surname: 'Tumanyan', lateTime: 3 },
    { name: 'Karen', surname: 'Qochar', lateTime: 2}
];

addPunctuals(employees);

//Task 2
function addAbsents(students) {
    let table = document.createElement('table');
    let headerRow = table.insertRow();
    let nameHeader = headerRow.insertCell(0);
    let surnameHeader = headerRow.insertCell(1);
    let ageHeader = headerRow.insertCell(2);
    nameHeader.innerHTML = 'Name';
    surnameHeader.innerHTML = 'Surname';
    ageHeader.innerHTML = 'Age';

    let maxAbsences = Math.max(...students.map(student => student.absences));
    students.forEach(student => {
        if(student.absences === maxAbsences) 
            {
            let row = table.insertRow();
            let nameCell = row.insertCell(0);
            let surnameCell = row.insertCell(1);
            let ageCell = row.insertCell(2);
            nameCell.innerHTML = student.name;
            surnameCell.innerHTML = student.surname;
            ageCell.innerHTML = student.age;
        }
    });

    document.body.appendChild(table);
};

let students = [
    { name: 'Viliam', surname: 'Saroyan', absences: 0,  age: 80 },
    { name: 'Hovhannes', surname: 'Tumanian', absences: 5, age: 25 },
    { name: 'Eznik', surname: 'Koxbaci', absences: 0 , age: 45 }
];
addAbsents(students);
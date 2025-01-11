// kartaci Armine, 25, developer
class A{
    name : &quot;Armen&quot;
    age = 22;
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
    }
class B extends A{
    constructor(ob){
        super(ob.name,ob.age);
        this.work = work;
    }
}
let obj = new B({
    name : &quot;Armine&quot;
    age : 25;
    work : &quot;developer&quot;
})
console.log('${obj.name} ${obj.age} ${obj.work}')
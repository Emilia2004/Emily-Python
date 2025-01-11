class Base {
    static kataryal(array) {
        const isPerfect = (num) => {
            if (num < 2) return false;
            let divisorsSum = 0;
            for (let i = 1; i <= Math.floor(num / 2); i++) {
                if (num % i === 0) {
                    divisorsSum += i;
                }
            }
            return divisorsSum === num;
        };

        let sum = 0;
        for (const num of array) {
            if (isPerfect(num)) {
                sum += num;
            }
        }
        return sum;
    }
}


class Derived extends Base {
    static simetrik(array) {
        const isSymmetric = (num) => num.toString() === num.toString().split('').reverse().join('');

        let sum = 0;
        for (const num of array) {
            if (isSymmetric(num)) {
                sum += num;
            }
        }
        return sum;
    }
}


const array = [6, 28, 7, 28, 6, 88];

const perfectSum = Base.kataryal(array);
console.log(`Kataryal tveri gumar ${perfectSum}`);

const symmetricSum = Derived.simetrik(array);
console.log(`Simetrik tveri gumar ${symmetricSum}`);

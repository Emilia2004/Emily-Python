const promise1 = new Promise(resolve => {
    setTimeout(() => resolve({ color: 'karmir', ekran1: '16px' }), 1000);
});

const promise2 = new Promise(resolve => {
    setTimeout(() => resolve({ color: 'blue', ekran2: '20px' }), 500);
});

const promise3 = new Promise(resolve => {
    setTimeout(() => resolve({ sharavix: '5px', nkar: '10px' }), 1500);
});

const promises = [promise1, promise2, promise3];

async function outputCSSProperties(promises) {
    const results = await Promise.all(promises);
    const allProperties = Object.assign({}, ...results); 
    console.log(allProperties);
}

outputCSSProperties(promises);

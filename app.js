const arr = [];

const addBike = (motorcycle) => {
    if (!arr.includes(motorcycle)) arr.push(motorcycle);
    else alert('This bike is taken');
}

addBike('Husqvarna tc 85');
addBike('Honda cr 85');
addBike('Ktm sx 125');
addBike('Husqvarna tc 85');
console.log(arr);

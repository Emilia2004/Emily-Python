// const obj = {
//     a: 1,
//     b: "hello",
//     c: true,
//     d: null,
//     e: undefined,
//     info : {
//       work : 
//     }
//   };
  
//   const values = Object.values(obj); 
//   const count = values.filter(value => value !== undefined).length; 
  
//   console.log("Number of values:", count);
  

























  function countValues(obj) {
    let count = 0;
  
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        if (typeof obj[key] === "object" && obj[key] !== null) {
          count += countValues(obj[key]); // Recursively count nested objects
        } else {
          count += 1; // Count primitive values
        }
      }
    }
  
    return count;
  }
  
  const obj = {
    a: 1,
    b: { c: 2, d: { e: 3,
      k :11,
      i: 22,
      w : {
        ss :22,
        nn :33,
      }
     },
   },
    f: null,
    g: undefined
  };
  
  console.log("Total values:", countValues(obj));
  

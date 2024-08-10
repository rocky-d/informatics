/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
function checkIfInstanceOf(obj, classFunction) {
    return obj === null || obj === undefined || !(classFunction instanceof Function) ? false : Object(obj) instanceof classFunction;
}

let egObj = new Date();
let egClassFunction = Date;
console.log(checkIfInstanceOf(egObj, egClassFunction));

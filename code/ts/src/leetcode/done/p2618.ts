function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    return obj === null || obj === undefined || !(classFunction instanceof Function) ? false : Object(obj) instanceof classFunction;
}

let egObj = new Date();
let egClassFunction = Date;
console.log(checkIfInstanceOf(egObj, egClassFunction));

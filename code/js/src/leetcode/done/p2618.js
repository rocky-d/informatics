/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
    return obj === null || obj === undefined || !(classFunction instanceof Function) ? false : Object(obj) instanceof classFunction;
};

egObj = new Date()
egClassFunction = Date
console.log(checkIfInstanceOf(egObj, egClassFunction));

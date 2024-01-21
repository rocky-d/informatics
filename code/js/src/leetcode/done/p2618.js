/**
 * @param {*} obj
 * @param {*} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
    return obj === null || obj === undefined || !(classFunction instanceof Function) ? false : Object(obj) instanceof classFunction;
};

eg_obj = new Date()
eg_classFunction = Date
console.log(checkIfInstanceOf(eg_obj, eg_classFunction));

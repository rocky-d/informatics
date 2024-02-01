local function main()
    x = io.read('n')

    local property1, property2, a, b, c, d
    property1 = 0 == x % 2
    property2 = 4 < x and x <= 12
    if property1 and property2 then
        a = 1
    else
        a = 0
    end
    if property1 or property2 then
        b = 1
    else
        b = 0
    end
    if 0 == a and 1 == b then
        c = 1
    else
        c = 0
    end
    if 0 == b then
        d = 1
    else
        d = 0
    end
    print(string.format('%u %u %u %u', a, b, c, d))
end

main()

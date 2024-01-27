local function main()
    local n, char
    n, _, char = io.read('n', 1, 1)

    local shape, spaces
    spaces = 0
    while 1 + spaces * (4 + 2 * spaces) <= n do
        spaces = spaces + 1
    end
    spaces = spaces - 1
    shape = {}
    for i = 1, spaces, 1 do
        table.insert(shape, '')
        for _ = 1, i - 1 do
            shape[#shape] = shape[#shape] .. ' '
        end
        for _ = 1, 1 + 2 * (spaces + 1) - 2 * i do
            shape[#shape] = shape[#shape] .. char
        end
    end
    table.insert(shape, '')
    for _ = 1, spaces do
        shape[#shape] = shape[#shape] .. ' '
    end
    shape[#shape] = shape[#shape] .. char
    for i = spaces, 1, -1 do
        table.insert(shape, '')
        for _ = 1, i - 1 do
            shape[#shape] = shape[#shape] .. ' '
        end
        for _ = 1, 1 + 2 * (spaces + 1) - 2 * i do
            shape[#shape] = shape[#shape] .. char
        end
    end
    print(table.concat(shape, '\n'))
    print(n - (1 + spaces * (4 + 2 * spaces)))
end

main()

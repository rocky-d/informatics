local function main()
    local n, c
    n, _, c = io.read('n', 1, 1)

    print(string.rep(string.rep(c, n), math.ceil(n / 2), '\n'))
end

main()

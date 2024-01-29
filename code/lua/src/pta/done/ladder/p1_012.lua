local function main()
    local n
    n = io.read('n')

    print(string.format('2^%u = %u', n, 2 ^ n))
end

main()

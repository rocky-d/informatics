local function main()
    local f
    f = io.read('n')

    print(string.format('Celsius = %d', math.modf(5 * (f - 32) / 9)))
end

main()

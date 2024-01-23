function is_prime_1(n)
    local res
    if n < 2 then
        res = false
    else
        res = true
        for i = 2, n - 1 do
            if 0 == n % i then
                res = false
                break
            end
        end
    end
    return res
end

local function main()
    print(is_prime_1(13))

    for key in pairs(_G) do
        if 'main' == key then
            print('Found:', key)
            print(_G[key])
        end
    end

end

main()

local function is_prime_1(n)
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

local function is_prime_2(n)
    local res
    if n < 2 then
        res = false
    else
        res = true
        for i = 2, math.floor(math.sqrt(n)) do
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
    print(is_prime_2(13))
end

main()

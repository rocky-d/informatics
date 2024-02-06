local function is_prime_1(num)
    local res
    if num < 2 then
        res = false
    else
        res = true
        for i = 2, num - 1 do
            if 0 == num % i then
                res = false
                break
            end
        end
    end
    return res
end

local function is_prime_2(num)
    local res
    if num < 2 then
        res = false
    else
        res = true
        for i = 2, math.floor(math.sqrt(num)) do
            if 0 == num % i then
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

function is_prime_1(n)
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


print(is_prime_1(13))
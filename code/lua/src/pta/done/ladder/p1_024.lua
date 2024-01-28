local function main()
    local d
    d = io.read('n')

    local ans
    if d <= 5 then
        ans = d + 2
    else
        ans = d - 5
    end
    print(ans)
end

main()

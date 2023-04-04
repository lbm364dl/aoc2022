inp = File.read!("input.txt") |> String.split("\n", trim: true)
      |> Enum.map(fn(<<p1, _, p2>>) -> {p1-?A, p2-?X} end)

rem_pos = &(rem(&1 + &2, &2))

star1 = inp
        |> Enum.map(fn({p1, p2}) -> 3*rem_pos.(p2-p1+1, 3) + p2+1 end)
        |> Enum.sum

star2 = inp
        |> Enum.map(fn({p1, res}) -> 3*res + rem_pos.(p1+res-1, 3)+1 end)
        |> Enum.sum

IO.inspect(star1)
IO.inspect(star2)

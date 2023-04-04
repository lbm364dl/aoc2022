half = &(div(length(&1), 2))

inp = File.read!("input.txt") 
      |> String.split("\n", trim: true)
      |> Enum.map(&to_charlist/1)

score = fn(inp) ->
        inp
        |> Enum.map(fn(s) -> 
          s
          |> Enum.map(&MapSet.new/1)
          |> Enum.reduce(&MapSet.intersection/2)
          |> Enum.random
          |> (&(rem(&1-?a+1 + 58, 58))).()
        end)
        |> Enum.sum
end

star1 = inp
        |> Enum.map(&(Enum.chunk_every(&1, half.(&1))))
        |> score.()

star2 = inp
        |> Enum.chunk_every(3)
        |> score.()

IO.inspect(star1)
IO.inspect(star2)

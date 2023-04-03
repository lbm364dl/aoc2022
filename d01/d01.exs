inp = File.read!("input.txt") 
      |> String.split("\n\n") 
      |> Enum.map(fn(row) -> 
            row
            |> String.split("\n", trim: true)
            |> Enum.map(&String.to_integer/1)
            |> Enum.sum
      end)

star1 = inp |> Enum.max
star2 = inp |> Enum.sort |> Enum.take(-3) |> Enum.sum

IO.inspect(star1)
IO.inspect(star2)

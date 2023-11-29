contained? = fn [x1, x2, y1, y2] ->
  x1 >= y1 && x2 <= y2 ||
  y1 >= x1 && y2 <= x2
end

overlap? = fn [x1, x2, y1, y2] ->
  max(x1, y1) <= min(x2, y2)
end

solve = fn count_function ->
  File.stream!("input.txt")
  |> Stream.map(fn ln -> 
    Regex.split(~r{[-,\n]}, ln, trim: true) 
    |> Enum.map(&String.to_integer/1) 
  end)
  |> Enum.count(& count_function.(&1))
end

IO.inspect(solve.(& contained?.(&1)), label: "Star 1")
IO.inspect(solve.(& overlap?.(&1)), label: "Star 2")

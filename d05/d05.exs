parse_table = fn table ->
  table
  |> String.split("\n") 
  |> Enum.drop(-1)
  |> Enum.map(& 
    &1
    |> to_charlist()
    |> Enum.drop(1)
    |> Enum.take_every(4)
  )
  |> Enum.zip()
  |> Enum.map(fn pile ->
    pile
    |> Tuple.to_list()
    |> Enum.drop_while(& &1 == ?\s)
  end)
  |> then(& ['' | &1])
end

parse_commands = fn commands ->
  commands
  |> String.split("\n")
  |> Enum.drop(-1)
  |> Enum.map(fn command ->
    Regex.run(~r{move (\d+) from (\d+) to (\d+)}, command) 
    |> tl() 
    |> Enum.map(&String.to_integer/1)
  end)
end

solve = fn [reverse?: reverse?] ->
  {table, commands} = File.read!("input.txt")
    |> String.split("\n\n")
    |> then(fn [table, commands] -> {parse_table.(table), parse_commands.(commands)} end)
  
  Enum.reduce(commands, table, fn [cnt, from, to], acc ->
    {move, rest} = acc
      |> Enum.at(from)
      |> Enum.split(cnt)
  
    acc
      |> List.update_at(to, & 
        case reverse? do
          true -> Enum.reverse(move)
          false -> move
        end
        ++ &1
      )
      |> List.replace_at(from, rest)
  end)
  |> tl()
  |> Enum.map(&hd/1)
  |> to_string()
end

IO.inspect(solve.(reverse?: true), label: "Star 1")
IO.inspect(solve.(reverse?: false), label: "Star 2")

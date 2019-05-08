defmodule Console do
  def read_integer() do
    IO.gets("")
    |> Integer.parse()
    |> elem(0)
  end
end

defmodule Exercise do
  def iterate(times) do
    Console.read_integer()
    |> PrimeNumber.is_primal()
    if times > 1 do
      iterate(times - 1)
    end
  end
end

defmodule PrimeNumber do
  def is_primal(number) do
    case {number} do
      _ when number <= 3 ->
        case number do
          _ when number > 1 ->
            IO.puts("TAK")
          _ when number <= 1 ->
            IO.puts("NIE")
        end
      _ when rem(number, 2) == 0 or rem(number, 3) == 0 ->
        IO.puts("NIE")
      _ ->
        check_more(number, 5)
    end
  end
  def check_more(n, i) when i * i > n do
    IO.puts("TAK")
  end
  def check_more(n, i) when i * i <= n do
    case {n, i} do
      _ when rem(n, i) == 0 or rem(n, i + 2) == 0 ->
        IO.puts("NIE")
      _ ->
        check_more(n, i + 6)
    end
  end
end

Console.read_integer()
|> Exercise.iterate()

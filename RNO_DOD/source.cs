using System;

namespace App
{
    class Helper
    {
        public static int GetNumberFromStdin()
        {
            int number = Convert.ToInt32(Console.ReadLine());

            if (number < 0)
            {
                number = 0;
            }

            return number;
        }

        public static int[] GetNumbersArrayFromStdin()
        {
            string line = Console.ReadLine();

            string[] numbers = line.Split(' ');

            return Array.ConvertAll<string, int>(numbers, int.Parse);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            int iterationCount = Helper.GetNumberFromStdin();

            while (iterationCount-- > 0)
            {
                int numberCount = Helper.GetNumberFromStdin();

                int[] numbers = Helper.GetNumbersArrayFromStdin();

                int sum = 0;

                for (int i = 0; i < numberCount; i++)
                {
                    sum += numbers[i];
                }

                Console.WriteLine(sum);
            }
        }
    }
}

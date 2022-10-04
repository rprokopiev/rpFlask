Console.WriteLine("Enter number ");
string value1 = Console.ReadLine();
int A = int.Parse(value1);
if (A % 7 ==0 & A % 23 ==0)
{
    Console.WriteLine("ДА");
}
else
{
     Console.WriteLine("НЕТ");
}
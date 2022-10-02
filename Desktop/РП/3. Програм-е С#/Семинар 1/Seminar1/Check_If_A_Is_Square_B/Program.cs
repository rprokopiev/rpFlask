Console.WriteLine("Enter number A");
string value1 = Console.ReadLine();
int A = int.Parse(value1);
Console.WriteLine("Enter number B");
string value2 = Console.ReadLine();
int B = int.Parse(value2);
if(A == B*B)
{
    Console.WriteLine("true");
}
else
{
    Console.WriteLine("false");
}


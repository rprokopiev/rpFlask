Console.WriteLine("Enter number");
string value = Console.ReadLine();
int x = int.Parse(value);
int y = -x;
int count = y;
while (count <= x)
{
    Console.Write(count);
    count = count + 1;
    if (count <= x)
    Console.Write(", ");
}
int randomvalue1 = new Random ().Next(1, 50);
int randomvalue2 = new Random ().Next(1, 50);
Console.WriteLine(randomvalue1);
Console.WriteLine(randomvalue2);
if(randomvalue2 % randomvalue1 == 0)
{
    Console.WriteLine("Кратно");
}
else
{
    Console.WriteLine("Не кратно, остаток" + randomvalue2 % randomvalue1);
}

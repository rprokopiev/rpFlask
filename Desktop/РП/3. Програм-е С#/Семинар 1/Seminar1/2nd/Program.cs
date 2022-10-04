int randomvalue = new Random ().Next(100, 1000);
Console.WriteLine(randomvalue);
int a = randomvalue / 100;
int b = randomvalue % 10;
Console.WriteLine(a*10+b);

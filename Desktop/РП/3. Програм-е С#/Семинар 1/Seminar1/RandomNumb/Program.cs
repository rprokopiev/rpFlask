int randomvalue = new Random ().Next(10, 100);
int decadeDigit = randomvalue / 10;
int unitDigit = randomvalue %10;
int maxValue = decadeDigit;
if(maxValue < unitDigit)
{
    maxValue = unitDigit;
}
Console.WriteLine("randomvalue =" + randomvalue);
Console.WriteLine("maxValue =" + maxValue);

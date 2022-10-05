int Max(int arg1, int arg2, int arg3) // Создали свою функцию
{
    int result = arg1;
    if (arg2>result) result=arg2;
    if (arg3>result) result=arg3;
    return result;
}

int a1 = new Random().Next(1,100);
Console.Write(a1);
Console.Write(" ");
int a2 = new Random().Next(1,100);
Console.Write(a2);
Console.Write(" ");
int a3 = new Random().Next(1,100);
Console.Write(a3);
Console.Write(" ");

int b1 = new Random().Next(1,100);
Console.Write(b1);
Console.Write(" ");
int b2 = new Random().Next(1,100);
Console.Write(b2);
Console.Write(" ");
int b3 = new Random().Next(1,100);
Console.Write(b3);
Console.Write(" ");

int c1 = new Random().Next(1,100);
Console.Write(c1);
Console.Write(" ");
int c2 = new Random().Next(1,100);
Console.Write(c2);
Console.Write(" ");
int c3 = new Random().Next(1,100);
Console.WriteLine(c3);
// Console.WriteLine(" ");

// используем функцию поочереди
int max1 = Max(a1,a2,a3); 
int max2 = Max(b1,b2,b3);
int max3 = Max(c1,c2,c3);

Console.WriteLine(max1);
Console.WriteLine(max2);
Console.WriteLine(max3);

int maxOf9 = Max(max1,max2,max3);
Console.WriteLine(maxOf9);

// INSTEAD of lines 40-49
int max = Max(Max(a1,a2,a3),Max(b1,b2,b3),Max(b1,b2,b3));
Console.WriteLine(maxOf9);
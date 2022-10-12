// Поиск индекса нужного числа в массиве
// break - используется для остановки цикла после того, как найдено искомое значение в первый раз
int [] array = {31,28,73,64,55,64,73,81};

int n = array.Length;
int find = 64;

int index = 0;

while (index < n)
{
    if(array[index] == find)
    {
        Console.WriteLine(index);
        break;
    }
    index++;
}
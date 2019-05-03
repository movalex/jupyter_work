[![](https://img.youtube.com/vi/XKu_SEDAykw/0.jpg)](https://www.youtube.com/watch?v=XKu_SEDAykw)

Год назад, когда я в первый раз посмотрел это интервью, то восхитился логикой мышления интервьюируемого и в целом объяснение мне было понятно. Однако код, который он писал, тогда был для меня скорее похож на китайскую грамоту. 
Сейчас я посмотрел интервью еще раз, и уже попытался интерпретировать его решение для Python. Оказалось, при желании все возможно. И код выглядит не так устрашающе, как на C++. И кажется, что не так уж это и сложно.  Однако насколько здорово уметь не замыкаться в себе при встрече с заковыристым вопросом, а продолжать размышлять вслух и в результате найти ответ. Думаю. не каждый способен на такое в состоянии стресса.

## первый подход

```python
test1 = [1,2,3,4,4,6,9]

def has_sum(data, target):
    low = 0
    high = len(data)-1
    for _i in range(high):
        s = data[low] + data[high]
        if s == target:
            return True
        low += 1
    return False

has_sum(test1, 9)
```

## второй подход

```python
test2 = [1,2,1,1,1,3,1,3,9]

def has_sum_unordered(data, target):
    cache = set()
    for value in data:
        if value in cache:
            print(f'found {value}')
            return True
        cache.add(target - value)
    return False
        
has_sum_unordered(test2,10)
```
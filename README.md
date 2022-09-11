# sentence-generator
Утилита, которая на основе заданных текстов генерирует свои.

## Идея
Я реализовал следующий простой и эффективный метод: [n-граммная языковая модель](https://ru.wikipedia.org/wiki/N-грамма).  
Если конкретнее, то я использовал триграммы.

## Интерфейс
Я разбил основной код на две части: *обучение* и *генерация*.  

### Обучение
- Считал входные данные из файла или стандартного ввода.
- Очистил текст (например, выкинул неалфавитные символы).
- Сделал токенизацию.
- Сохранил модель в формате `.pkl`, который позволяет восстановить ее в утилите генерации.

### Параметры `train.py`
- `--input-dir` - путь к файлу, в котором лежат данные. Если данные аргумент не задан, считать, что тексты вводятся из `stdin`.
- `--model` - путь к файлу, в который сохраняют модель.

### Генерация
- Загрузил модель.
- Сгенерировал последовательность нужной длины и с нужным префиксом.
- Вывел ее на экран.

### Параметры `generate.py`
- `--model` - путь к файлу из которого загружается модель.
- `--prefix` - необязательный аргумент. Начало предложения (одно или несколько слов). Если не указано, выбираем начальное слово случайно из всех слов.
- `--length` - необязательный аргумент. Длина генерируемой последовательности. Если не указано, длина последовательности будет равна `5`.

### Детали реализации
- Реализовал консольный интерфейс через `argparse`.
- Для токенизации использовал библиотеку регулярных выражений `re`.
- Обернул модель в класс, у которого есть методы `fit` и `generate`.
- Создал `train.py`, `generate.py`, модуль `sentence_generator.py`, папку `data` с файлом в котором лежат обучающие данные и обученную на них модель, как `finalized_model.pkl`.
- Обучил модель на обработанном (почищенном) корпусе `gem`.

### Примеры работы
```console
(TinkoffTextGeneration) olegoratovskiy@MBP-Oleg TinkoffTextGeneration % python3 generate.py --model=/Users/olegoratovskiy/PycharmProjects/TinkoffTextGeneration/finalized_model.pkl --prefix=Nikola --length=5
Nikola warm up in clouds.

(TinkoffTextGeneration) olegoratovskiy@MBP-Oleg TinkoffTextGeneration % python3 generate.py --model=/Users/olegoratovskiy/PycharmProjects/TinkoffTextGeneration/finalized_model.pkl
Smiling doctor with an arrow.

(TinkoffTextGeneration) olegoratovskiy@MBP-Oleg TinkoffTextGeneration % python3 generate.py --model=/Users/olegoratovskiy/PycharmProjects/TinkoffTextGeneration/finalized_model.pkl --prefix="He was not a boy" --length=10
He was not a boy in the snow. Christmas gifts.

```

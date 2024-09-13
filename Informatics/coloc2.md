### 1. Основы многопоточного программирования

### a. Параллелизм и конкурентность

**Параллелизм** означает возможность системы одновременно выполнять несколько операций. **Конкурентность** — это свойство системы, при котором несколько процессов или потоков могут выполняться в перекрывающихся периодах времени (не обязательно одновременно).

**Процесс** — это экземпляр программы в выполнении, имеющий свое адресное пространство. **Поток** — это легковесный процесс, который делит адресное пространство своего процесса-родителя, что облегчает обмен данными и коммуникацию между потоками.

**Организация параллелизма:**
- **С использованием процессов:** Изоляция процессов упрощает отладку и повышает устойчивость системы (сбой одного процесса не влияет на другие). Недостаток — более высокие затраты на обмен данными и переключение контекста.
- **С использованием потоков:** Эффективное использование ресурсов и меньшие затраты на создание потока. Основной недостаток — сложности с синхронизацией и возможность возникновения ошибок, связанных с конкурентным доступом.

### b. Потоки. Класс std::thread

**Поток** — это базовая единица исполнения кода. В C++, потоки можно создавать с использованием класса `std::thread`.

**Создание нового потока:**
```cpp
#include <thread>
void function() {
    // Код потока
}
int main() {
    std::thread t(function);
    t.join(); // ожидает завершения потока
    return 0;
}
```

**Методы join и detach:**
- `join()` ожидает завершения потока.
- `detach()` отсоединяет поток, позволяя ему выполняться асинхронно.

**Исключения в потоках:**
Если в потоке происходит исключение, и оно не перехвачено внутри, то приложение завершится аварийно. Важно обеспечить обработку исключений внутри потоков.

**Передача аргументов и возврат данных:**
Используйте `std::ref` для передачи по ссылке и `std::future` для получения результатов из потока.

### c. Состояние гонки

**Разделяемые данные** — это данные, доступ к которым осуществляют несколько потоков. **Состояние гонки** возникает, когда несколько потоков одновременно изменяют разделяемые данные и конечный результат зависит от порядка исполнения потоков.

**Гонка данных** — это особый случай состояния гонки, при котором происходит одновременный доступ к памяти без должной синхронизации, что может привести к непредсказуемым результатам.

### d. Стандартный мьютекс

**`std::mutex`** используется для защиты разделяемых данных. Методы:
- `lock()` блокирует мьютекс.
- `unlock()` освобождает мьютекс.
- `try_lock()` пытается заблокировать мьютекс без блокировки.

### e. Классы lock_guard и unique_lock

**`std::lock_guard`** обеспечивает автоматическую блокировку и разблокировку

 мьютекса, что снижает риск ошибок.

**`std::unique_lock`** предоставляет больше гибкости, позволяя отложенную блокировку, повторное владение и передачу владения, что может быть полезно в более сложных сценариях синхронизации.

### f. Взаимоблокировка

**Взаимоблокировка** происходит, когда два или более потоков взаимно ожидают освобождения ресурсов, занятых друг другом. `std::lock` помогает избежать взаимоблокировок, блокируя несколько мьютексов одновременно.

### g. Потокобезопасные структуры данных

**Потокобезопасные структуры данных** обеспечивают корректное функционирование при конкурентном доступе. Примеры включают специальные контейнеры, которые используют блокировки для защиты данных. Стандартные контейнеры STL не являются потокобезопасными.

### h. Недостатки std::stack

**`std::stack`** не потокобезопасен, что требует дополнительной синхронизации при использовании в многопоточной среде.

### i. Потокобезопасный стек с блокировками

**Реализация потокобезопасного стека** основана на стандартном `std::stack`, с добавлением мьютексов для операций `push` и `pop`. Необходимо также учитывать исключения, чтобы не нарушить захват мьютекса.### 2. Механизмы синхронизации

### 2. Механизмы синхронизации

#### a. Условные переменные
Условные переменные используются для блокировки потока до тех пор, пока не произойдёт какое-либо событие. В C++, это реализовано через класс `std::condition_variable`.

**Использование `std::condition_variable`:**
1. **wait**: Поток вызывающий `wait` блокируется до тех пор, пока другой поток не вызовет `notify_one` или `notify_all` на той же условной переменной. Этот метод обычно используется в цикле для проверки условия, чтобы избежать ложных пробуждений.
   
2. **notify_one**: Пробуждает один из потоков, которые ожидают на условной переменной, если таковые имеются.
   
3. **notify_all**: Пробуждает все потоки, ожидающие на условной переменной.

**Ложные пробуждения (spurious wake-ups)** — это ситуации, когда поток пробуждается без получения уведомления. Это может произойти из-за особенностей реализации на некоторых платформах. Для предотвращения ошибок из-за ложных пробуждений условие проверяется в цикле после пробуждения.

Пример использования `std::condition_variable`:

```cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
bool ready = false;

void print_id(int id) {
    std::unique_lock<std::mutex> lck(mtx);
    while (!ready) cv.wait(lck);
    std::cout << "Thread " << id << '\n';
}

void go() {
    std::unique_lock<std::mutex> lck(mtx);
    ready = true;
    cv.notify_all();
}

int main() {
    std::thread threads[10];
    for (int i = 0; i < 10; ++i)
        threads[i] = std::thread(print_id, i);

    std::cout << "10 threads ready to race...\n";
    go();

    for (auto& th : threads) th.join();

    return 0;
}
```

#### b. Запуск асинхронной задачи
Функция `std::async` в C++ используется для асинхронного выполнения задачи. Она возвращает объект `std::future`, который можно использовать для получения результата выполнения задачи.

**Пример использования `std::async` и `std::future`:**
```cpp
#include <future>
#include <iostream>

int find_the_answer_to_ltuae() {
    return 42;
}

int main() {
    std::future<int> the_answer = std::async(find_the_answer_to_ltuae);
    std::cout << "The answer to life, the universe and everything is " << the_answer.get() << std::endl;
    return 0;
}
```

#### c. Класс packaged_task
`std::packaged_task` оборачивает любую вызываемую цель (функцию, лямбда-выражение, связывание и т.д.), так что её выполнение можно осуществлять асинхронно, а результат получить через `std::future`.

**Методы `std::packaged_task`:**
- **get_future()**: Возвращает объект `std::future`, который будет хранить результат выполнения задачи.
- **operator()()**: Выполняет задачу.

**Пример использования `std::packaged_task`:**
```cpp
#include <iostream>
#include <future>
#include <thread>

void task_function(std::packaged_task<int()> &task) {
    task();
}

int main() {
    std::packaged_task<int()> task([](){ return 7; });
    std::future<int> result = task.get_future();
    std::thread th(task_function, std::ref(task));
    th.join();
    std::cout << "Result from packaged_task: " << result.get() << std::endl;
    return 0;
}
```

#### d. Класс promise
`std

::promise` позволяет устанавливать значение из одного контекста и получать его в другом через `std::future`.

**Методы `std::promise`:**
- **get_future()**: Возвращает `std::future`, связанный с данным `promise`.
- **set_value()**: Устанавливает значение, которое можно получить через `future`.
- **set_exception()**: Передаёт информацию об исключении, которое можно получить через `future`.

**Пример использования `std::promise`:**
```cpp
#include <iostream>
#include <future>
#include <thread>

void function(std::promise<int> prom) {
    prom.set_value(10);
}

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();
    std::thread t(function, std::move(prom));
    std::cout << "The value set in promise is " << fut.get() << std::endl;
    t.join();
    return 0;
}
```

Эти инструменты предоставляют мощные возможности для управления многопоточными программами и асинхронными задачами в C++, позволяя разрабатывать эффективные и безопасные приложения.

### 3. Модели памяти

#### a. Барьеры памяти

**Барьеры памяти** используются для управления порядком, в котором инструкции выполняются на процессорах с различными моделями памяти. Это предотвращает ряд проблем, связанных с многопоточностью, таких как неопределённое поведение из-за гонок данных и проблемы с когерентностью кэша.

1. **Причины неопределённого поведения при гонке данных:**
   - Когда два или более потока одновременно читают и пишут в одну и ту же переменную без должной синхронизации, возникает неопределённое поведение.
   - Процессоры могут переупорядочивать выполнение инструкций для повышения производительности, что может привести к несоответствию между порядком выполнения инструкций и порядком, предполагаемым программистом.

2. **Когерентность кэша:**
   - Современные процессоры используют кэши для ускорения доступа к данным. Когерентность кэша гарантирует, что данные в кэше всех процессоров синхронизированы, т.е., любые изменения в одном кэше видны в других.

3. **Барьеры памяти:**
   - **LoadLoad**: Гарантирует, что загрузки до барьера будут выполнены перед загрузками после барьера.
   - **LoadStore**: Загрузки до барьера должны быть выполнены перед сохранениями после барьера.
   - **StoreLoad**: Сохранения до барьера должны быть выполнены перед загрузками после барьера.
   - **StoreStore**: Сохранения до барьера должны быть выполнены перед сохранениями после барьера.
   - **Acquire и Release**: Обеспечивают, что операции до Release барьера видимы другим потокам, которые выполняют Acquire для того же объекта.

#### b. Модели памяти в языке C++

C++ определяет несколько стратегий упорядочения памяти:
- **memory_order_seq_cst**: Строгий порядок упорядочения, подразумевает полную последовательную согласованность.
- **memory_order_acquire**: Гарантирует, что операции, расположенные после этой, не могут быть перенесены до неё.
- **memory_order_release**: Гарантирует, что операции, расположенные до этой, не могут быть перенесены после неё.
- **memory_order_relaxed**: Отсутствие гарантий порядка, позволяет максимальные оптимизации.

**Функция `std::atomic_thread_fence`** используется для вставки барьера памяти в нужном месте вашей программы для обеспечения необходимого упорядочения памяти.

#### c. Атомарные типы и операции над ними

**Атомарные переменные** — это типы, операции с которыми выполняются атомарно, т.е., неделимо относительно других потоков.

- **atomic_flag**:
  - `clear()`: Очищает флаг.
  - `test_and_set()`: Устанавливает флаг и возвращает его предыдущее значение.

- **atomic<T>**:
  - `load()`: Возвращает значение.
  - `store()`: Устанавливает значение.
  - `compare_exchange()`: Сравни

вает и заменяет значение, если оно соответствует ожидаемому.

**Реализация спинлока на основе атомарной переменной**:
```cpp
#include <atomic>
#include <thread>

std::atomic_flag lock = ATOMIC_FLAG_INIT;

void lock_spin() {
    while (lock.test_and_set(std::memory_order_acquire));
}

void unlock_spin() {
    lock.clear(std::memory_order_release);
}
```

#### d. Основные определения

- **Неблокирующие структуры данных**: Работают без блокировок, используя атомарные операции.
- **Структуры данных, свободные от блокировок**: Гарантируют завершение операций даже если некоторые потоки приостановлены.
- **Структуры данных, свободные от ожидания**: Каждый поток завершает операции за конечное число шагов.

#### e. Реализация потокобезопасного стека без блокировок

Реализация потокобезопасного стека без блокировок основывается на атомарных операциях и compare-and-swap (CAS) для управления вершиной стека:

```cpp
#include <atomic>
#include <memory>

template<typename T>
class LockFreeStack {
private:
    struct Node {
        std::shared_ptr<T> data;
        Node* next;

        Node(T const& data_) : data(std::make_shared<T>(data_)) {}
    };

    std::atomic<Node*> head;

public:
    void push(T const& data) {
        Node* const new_node = new Node(data);
        new_node->next = head.load();
        while (!head.compare_exchange_weak(new_node->next, new_node));
    }

    std::shared_ptr<T> pop() {
        Node* old_head = head.load();
        while (old_head && !head.compare_exchange_weak(old_head, old_head->next));
        return old_head ? old_head->data : std::shared_ptr<T>();
    }
};
```

Этот код использует CAS для безопасного изменения вершины стека, минимизируя блокировки и конкурентные конфликты.

### 4. CMake I

#### a. Основы CMake
**CMake** — это кросс-платформенная система автоматизации сборки программного обеспечения, которая использует файлы конфигурации для генерации нативных файлов проектов для конкретных сред разработки. Это позволяет разработчикам создавать программы независимо от используемой среды.

**Основы работы с CMake:**
- **Структура CMake-проекта**: Проект обычно содержит один или несколько файлов `CMakeLists.txt`, которые определяют, как проект должен быть построен, какие файлы включены в проект, и какие зависимости существуют.
- **Файл `CMakeLists.txt`**: Основной файл, который содержит инструкции и команды для CMake.
- **Генерация файлов проекта**: CMake генерирует файлы проекта для среды (например, Makefiles или Visual Studio projects) на основе инструкций в `CMakeLists.txt`.
- **Компиляция проекта**: После генерации файлов проекта, используйте соответствующую систему сборки (например, make) для компиляции и сборки проекта.

**Команды CMake:**
- `cmake_minimum_required(VERSION <min_version>)`: Определяет минимальную требуемую версию CMake.
- `project(<name>)`: Задаёт имя проекта и возможные языки, используемые в проекте.
- `message(<message>)`: Выводит сообщение во время выполнения CMake.
- `add_executable(<name> <source1> <source2> ...)`: Создаёт исполняемый файл с именем `<name>` из указанных исходных файлов.

**Переменные CMake:**
- **Типы переменных**: В CMake переменные могут быть строками, булевыми значениями или списками.
- **Создание и использование переменных**: Используйте команду `set(<variable> <value>)` для создания переменной и `message(${<variable>})` для вывода её значения.

#### b. Таргеты
**Таргет (target)** в CMake — это исполняемый файл, библиотека или любой другой продукт сборки, указанный в файле `CMakeLists.txt`.

**Команды CMake для таргетов:**
- `add_library(<name> STATIC|SHARED <source1> <source2> ...)`: Создаёт библиотеку (статическую или динамическую).
- `target_include_directories(<target> <INTERFACE|PUBLIC|PRIVATE> <dir1> <dir2> ...)`: Указывает директории, которые будут включены в поиск заголовочных файлов для таргета.
- `target_compile_features(<target> <INTERFACE|PUBLIC|PRIVATE> <feature1> <feature2> ...)`: Задаёт компиляторные фичи, требуемые таргетом.
- `target_compile_definitions(<target> <INTERFACE|PUBLIC|PRIVATE> <definition1> <definition2> ...)`: Добавляет определения компилятора для таргета.
- `target_compile_options(<target> <INTERFACE|PUBLIC|PRIVATE> <option1> <option2> ...)`: Задаёт дополнительные опции компилятора для таргета.
- `target_link_libraries(<target> <INTERFACE|PUBLIC|PRIVATE> <lib1> <lib2> ...)`: Связывает таргет с библиотеками. Опции `PUBLIC`, `PRIVATE`, и `INTERFACE` определяют, как свойства распространяются на зависимые таргеты.

#### c. Списки
**Список в CMake** —

 это структура данных, которая хранит значения (обычно строки), разделённые точкой с запятой.

**Работа со списком с использованием команды `list`:**
- `list(APPEND <list> <value1> <value2> ...)`: Добавляет значения в конец списка.
- `list(LENGTH <list> <output_variable>)`: Сохраняет длину списка в переменной.
- `list(GET <list> <index> <output_variable>)`: Получает элемент по индексу.
- `list(FIND <list> <value> <output_variable>)`: Находит индекс первого вхождения значения в списке.
- `list(SORT <list>)`: Сортирует список.

#### d. Условия и циклы
**Условные операторы и циклы в CMake:**
- `if(<condition>) ... elseif(<condition>) ... else() ... endif()`: Выполняет блоки кода в зависимости от условия.
- `while(<condition>) ... endwhile()`: Повторяет блок кода, пока условие истинно.
- `foreach(<item> IN ITEMS <item1> <item2> ...) ... endforeach()`: Итерирует по элементам списка.

#### e. Функции
**Функции в CMake** позволяют группировать код для повторного использования. Создаются с помощью `function(<name> <arg1> <arg2> ...) ... endfunction()`. Передача аргументов осуществляется через `ARGC`, `ARGV`, `ARGN`. Использование `PARENT_SCOPE` позволяет изменять переменные в родительской области видимости.

#### f. Переменные CMake
**Переменные CMake** включают переменные среды и кешированные переменные (`CACHE`). Кешированные переменные сохраняют своё состояние между запусками CMake. Изменить их можно через CMake GUI или командной строке (`-D<var>:<type>=<value>`).

#### g. Поддиректории
**Использование `add_subdirectory`** позволяет включать другие проекты или части проекта. С помощью `PARENT_SCOPE` изменения переменных в поддиректории могут быть "подняты" в родительскую директорию.

### e. Функции в CMake

**Функции в CMake** позволяют группировать логически связанный код для повторного использования и упорядочения скрипта.

**Создание функций:**
Для создания функции в CMake используется команда `function`, после которой указывается имя функции и список аргументов:

```cmake
function(my_function arg1 arg2)
    message("Argument 1: ${arg1}")
    message("Argument 2: ${arg2}")
endfunction()
```

**Передача аргументов в функцию:**
Аргументы передаются в функцию посредством вызова функции с конкретными значениями:

```cmake
my_function("Hello" "World")
```

**Специальные переменные функций:**
- `ARGC`: Число аргументов, переданных в функцию.
- `ARGV`: Список всех аргументов. `ARGV0`, `ARGV1`, ..., `ARGVn` обращаются к конкретным аргументам.
- `ARGN`: Список аргументов, которые не имеют имен в объявлении функции.

**Возвращение значений из функции:**
Прямого возвращения значения в CMake нет, но изменения переменных в родительской области видимости возможны через опцию `PARENT_SCOPE` в команде `set`:

```cmake
function(set_global_var)
    set(my_var "Value" PARENT_SCOPE)
endfunction()
```

**Команда `return`:**
Используется для немедленного завершения функции:

```cmake
function(example_func)
    if(NOT CONDITION)
        return()
    endif()
    # Дополнительный код, если CONDITION истинно
endfunction()
```

**Области видимости:**
Переменные в функциях CMake по умолчанию локальны. Использование `PARENT_SCOPE` позволяет изменять переменные в родительской области видимости.

### f. Переменные CMake

**Создание переменных:**
Переменные в CMake создаются с помощью команды `set`:

```cmake
set(MY_VARIABLE "SomeValue")
```

**Типы переменных в CMake:**
- **Обычные переменные**: Локальные или глобальные переменные, заданные в скрипте.
- **Переменные среды**: Отображают значения из окружения операционной системы.
- **Кешированные переменные**: Сохраняют свои значения между запусками CMake и определяются с помощью `CACHE` опции в `set`.

**Кешированные переменные** отличаются от обычных переменных тем, что сохраняются в файле `CMakeCache.txt` и доступны между сеансами сборки. Создать кешированную переменную можно так:

```cmake
set(MY_CACHE_VAR "CacheValue" CACHE STRING "Description of the cached variable")
```

Типы данных кешированных переменных:
- `BOOL` - логическое значение
- `STRING` - строка
- `PATH` - путь к файлу или папке
- `FILEPATH` - путь к файлу

**Стандартные переменные CMake:**
- `CMAKE_SOURCE_DIR` - корневой каталог исходного кода
- `CMAKE_BUILD_DIR` - каталог, в котором выполняется сборка
- `CMAKE_CURRENT_SOURCE_DIR` - каталог, где находится текущий обрабатываемый CMakeLists.txt
- `CMAKE_CURRENT_BUILD_DIR` - каталог сборки для текущего CMakeLists.txt
- `CMAKE_HOST_SYSTEM` - система, на которой выполняется CMake
- `WIN32`, `LINUX`, `APPLE` - платформы
- `MSVC`, `MINGW` - компиляторы
- `CMAKE_CXX_COMPILER

` - путь к C++ компилятору
- `CMAKE_CXX_FLAGS` - флаги компиляции для C++
- `CMAKE_CXX_STANDARD` - стандарт C++, используемый в проекте

### g. Поддиректории

**Команда `add_subdirectory`** позволяет включать другие CMake проекты или части проекта, размещённые в поддиректориях:

```cmake
add_subdirectory(src)
```

**Области видимости в поддиректориях:**
Изменения переменных в поддиректориях не видны в родительской директории, если не использовать `PARENT_SCOPE`. Это позволяет локализовать переменные и изменения в конкретной части проекта.

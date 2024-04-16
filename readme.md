# Package Comparison Tool

Этот инструмент позволяет сравнивать списки бинарных пакетов между разными ветками Alt Linux. Он использует публичное REST API для получения данных о пакетах из веток `sisyphus` и `p10` и выводит результаты сравнения в формате JSON.

## Установка

1. Клонируйте репозиторий на свой компьютер:

git clone https://github.com/yourusername/package-comparison-tool.git

markdown
Copy code

2. Перейдите в каталог с проектом:

cd package-comparison-tool

markdown
Copy code

3. Установите зависимости:

pip install -r requirements.txt

markdown
Copy code

## Использование

Запустите утилиту `package_comparison_tool.py` с указанием ветки, которую вы хотите сравнить:

python3 package_comparison_tool.py sisyphus

Copy code

или

python3 package_comparison_tool.py p10

javascript
Copy code

Это выведет результаты сравнения в формате JSON.

## Структура JSON-результата

Результаты сравнения содержат три категории:

1. `packages_in_p10_not_in_sisyphus`: Список пакетов, которые есть в ветке `p10`, но отсутствуют в ветке `sisyphus`.
2. `packages_in_sisyphus_not_in_p10`: Список пакетов, которые есть в ветке `sisyphus`, но отсутствуют в ветке `p10`.
3. `packages_with_newer_version_in_sisyphus`: Список пакетов, версия-релиз которых выше в ветке `sisyphus`, чем в ветке `p10`.

Пример JSON-результата:

```json
{
    "packages_in_p10_not_in_sisyphus": [],
    "packages_in_sisyphus_not_in_p10": [],
    "packages_with_newer_version_in_sisyphus": []
}
Примечания
Убедитесь, что у вас есть доступ к интернету, так как утилита использует публичное REST API для получения данных о пакетах.
Утилита предполагает, что ветки sisyphus и p10 содержат пакеты, которые можно сравнивать. Если пакетов нет, результаты сравнения будут пустыми.
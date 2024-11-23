# Шаблон пакета

С использованием данного шаблона возможно создание сервисов (демонов), web-служб и библиотек.

Предусматриваются следующие параметры шаблона, которые должны быть соответствующим образом скорректированы при создании реального проекта:
- <project_name> - наименование проекта. Это строка, которая указывается в качестве названия подкаталога папки src, в именах ряда файлов, а также их содержимом;
- <наименование ИС> - как правило, именно наименование информационной системы указывается в названии каталогов, в которых размещаются исполнимые или лог-файлы;
- <вид продукта> - предполагаются следующие значения: "services" - сервисы (демоны), "web_services" - web-службы, packages - библиотеки;
- <author> - псевдоним автора проекта, как правило, указывемый в имени электронной почты и учетной записи в github;
- <author@domain.name> - адрес электронной почты автора проекта;
- <full_path_to_pypi_win> - локальный каталог размещения whl-файлов в Windows;
- <full_path_to_pypi_lnx> - локальный каталог размещения whl-файлов в Linux;

# Быстрый старт

Для работы с использованием данного шаблона необходимо.
На начальном этапе
1. Создать каталог для нового пакета его имя - будет значение параметра <project_name>
2. Если под него уже имеется репозиторий, то скачать его командой, находясь уже внутри каталога
   git clone <имя репозитория> .

*) о вариантах связывания с удаленным репозиторием можно ознакомиться по ссылке
https://it4each.com/blog/kak-sviazat-lokalnyi-repozitorii-s-udalennym-na-github/
о смене привязки - по ссылке
https://jeka.by/ask/137/git-change-origin/

3. Скачать данный шаблон в созданный каталог.
4. Переименовать подкаталог *project_name* в каталоге *src* на требуемое имя пакета.
5. Если требуется наличие main-файла, вызывающего фукнциональность пакета (например, при создании сервиса (демона) или web-службы, то переименовать с использованием имени проекта файл *main_PROJECT_NAME.py*. Если такой файл не требуется, то удалить его.
6. Если предполагается создание сервиса (демона), то переименовать с использованием имени проекта файл *PROJECT_NAME.service*. В противном случае удалить данный файл.
7. Определиться с местом размещения whl-файлов и отразить это в файлах *build+.bat*, *install.bat* и *install.sh*.
8. Уточнить значение параметра <наменование ИС> и отразить это в файлах *.env*, *main_<project_name>.py* и *<project_name>.service* для окончательного определения указываемых в них сведений.
9. Скорректировать файл *pyproject.toml*, указав требуемые значения параметров.

В дальнейшем осуществить функциональное наполнение пакета, добавляя файлы с текстами программ в подкаталог с именем проекта, расположенный в каталоге *src*, а также изменяя файлы *main_<project_name>.py*, *.env* и другие (по необходимости). Используемые другие пакеты перед сборкой данного пакета, необходимо описать в разделе **dependencies** файла *pyproject.toml*.

Отладка функциональности пакета, именно как пакета, осуществляется его сборокой и установкой в свое виртульное окружение. После этого в этом виртульном окружении запускается файл *main_<project_name>.py* и выполняется отладка по коду установленного пакета. Изменения, вносимые в тексты установленного пакета должны впоследствие быть перенесены в исходные тексты, а затем осуществлена повторная сбока и установка пакета.
Для упрощения пересоздания виртуального окружения и последующей установки пакета предназначены командные файлы: *build+.bat* и *install.bat*. Первый файл собирает из исходных текстов whl-файл, копирует его в заданный каталог, пересоздает виртуальное окружение и активизирует его. Второй файл выполняет установку пакета. После исполнения второго файла рекомендуется выйти из активизированного виртуального окружения командой _**deactivate**_.

Перед выдачей пакета в установку на целевую среду необходимо уточнить версию разрабатываемого проекта и указать ее в файлах: *pyproject.toml*, *install.bat*, *install.sh* и, возможно, *README.md*.

Для установки разработанного пакета в целевую среду, как минимум, необходимо предоставить следующие файлы:
- файл README.md с описание назначения пакета, особенностями его установки и функционирования;
- .whl-файл пакета;
- .env-файл (при наличии);
- файл install.sh (в случае установки в собственное виртуальное окружение. Актуально для сервисов (демонов) и web-служб);
- файл main_<project_name>.py (при наличии);
- файл *<project_name>.service* в случае реализации сервиса (демона).

# Описание содержания пакета

Состав проекта

Каталоги:
- docs - предназначен для размещения файлов с документацией;
- src - каталог с исходными текстами, размещаемые в подкаталоге, соответствующим имени проекта;
- test - предназначен для размещения файлов с тестами.

Файлы
В корневом каталоге проекта размещаются:
- .env - файл с параметрами, используемыми в проекте;
- build+.bat - командный файл (для Windows), выполняющий формирование whl-файла, а также пересоздание виртуального окружения;
- install.bat - командный файл (для Windows) установки whl-файла, соответствующего данному пакету;
- install.sh - командный файл (для Linux) пересоздания виртуального окружения и установки whl-файла, соответствующего данному пакету;
- LICENSE.md - текст MIT-лицензии, требующий уточнения года и автора;
- main_PROJECT_NAME.py - файл запуска основной функциональности пакета. "PROJECT_NAME" необходимо изменить на имя создаваемого пакета. В файле в комментарии представлены варианты для сервиса (демона) и web-службы;
- PROJECT_NAME.service - файл описания службы (демона). "PROJECT_NAME" необходимо изменить на имя создаваемого пакета;
- pyproject.toml - файл описания проекта, как пакета;
- README.me - описание пакета.

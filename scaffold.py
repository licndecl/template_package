#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parent

"""
Инициализация скелета проекта.

Назначение: единообразно и безопасно привести шаблон к реальному проекту, не забыв ни одну замену.

Процесс и шаги:
1) Замена параметров в текстовых файлах
    Производится поиск по совпадению подстроки с учетом угловых скобок.
    По ключевым значениям выполняется два отдельных поиска: в нижнем и верхнем регистрах.
    При совпадении в нижнем регистре значение указывается, как задано, а для верхнего регистра приводится к ЗАГЛАВНЫМ БУКВАМ
"""

MAPPING_VARIANTS = {
    # Имя модуля (проекта)
    "project_name": "new_project",
    # Описание модуля (проекта)
    "description": "Модуль предназначен для...",
    # Версия
    "version": "0.0.1",
    # Наименование информационной системы (используется для именования корневого каталога установки, а также для указания владельца сервиса)
    "owner_name": "moslicense",
    # Вид продукта (один из вариантов: api, web_services, services)
    "product_type": "web_services",
    # Автор (псевдоним автора проекта)
    "author": "nickname",
    # Почта автора
    "author_email": "nickname@domain.name",
    # Локальные каталоги PyPI (Linux/Windows)
    "full_path_to_pypi_lnx": "/opt/moslicense/PyPackets",
    "full_path_to_pypi_win": "D:\\Projects\\Moslic_deployment\\PyPi"
}

"""
    Из рассмотрения исключаются заданные файлы и каталоги
    А также ограничивается множество изменяемых файлов - заданным перечнем расширений имен файлов
"""

EXCLUDED_DIRS = {".gitignore", ".git", "venv", "dist", "build", "__pycache__", ".mypy_cache", ".pytest_cache", "scaffold.py"}
TEXT_FILE_EXTENSIONS = {"", ".py", ".toml", ".md", ".service", ".sh", ".bat", ".env"}

"""
2) переименование каталогов и файлов
    Производится поиск подкаталогов и файлов, содержащих в названиях подстроки в квадратных скобках
    Замена производится всегда на значение в нижнем регистре
    
3) Режимы
   - --do-it - производит требуемые модификации
   - без этого ключа только выводит предполагаемые модификации
    
"""

def collect_files(only_files: bool = True) -> List[Path]:
    """Собрать список файлов для обработки, исключая технические каталоги."""
    files: List[Path] = []
    for p in ROOT.rglob("*"):
        # Пропустим файлы и каталоги в исключаемых путях
        if any(part in EXCLUDED_DIRS for part in p.parts):
            continue
        if only_files and p.is_dir():
            continue
        if p.name.startswith(".DS_Store"):
            continue
        if not only_files or is_text_file(p):
            files.append(p)
    return files

def is_text_file(path: Path) -> bool:
    """Проверка, является ли файл текстовым для наших замен.

    Критерий упрощён: по расширению. Двоичные и каталоги исключаются.
    """
    if path.is_dir():
        return False
    return path.suffix in TEXT_FILE_EXTENSIONS

def replace_in_text(content: str, mapping: Dict[str, str]) -> str:
    """Подстановка значений по всем известным вариантам замен.
    """
    # Прямые подстановки по заменам
    for key, value in mapping.items():
        content = content.replace(key, value)
    return content

def apply_replacements(files: List[Path], do_it: bool) -> None:
    """Применить подстановки к собранным файлам с учётом dry-run и спец‑правил."""
    for path in files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        updated = text

        mapping = { f"<{key}>": value for key, value in MAPPING_VARIANTS.items() }
        updated = replace_in_text(updated, mapping)
        
        mapping = { f"<{key.upper()}>": value.upper() for key, value in MAPPING_VARIANTS.items() }
        updated = replace_in_text(updated, mapping)

        if updated != text:
            if do_it:
                path.write_text(updated, encoding="utf-8")
            else:
                print(f"[dry-run] patch: {rel}")
                
def rename_filename(filename: str, mapping: Dict[str, str]) -> str:
    """Подстановка значений по всем известным вариантам замен.
    """
    # Прямые подстановки по заменам
    for key, value in mapping.items():
        filename = filename.replace(key, value)
    return filename
                
def rename_paths(files: List[Path], do_it: bool) -> None:
    """Сформировать и выполнить (или вывести) переименования путей."""

    mapping = { f"[{key}]": value for key, value in MAPPING_VARIANTS.items() }
    
    for path in files:
        
        fullpath = str(path)
        dir = path.parent
        filename = path.name

        updated_name = rename_filename(filename, mapping)

        if updated_name != filename:
            if do_it:
                path.rename(Path(dir / updated_name))
            else:
                print(f"[dry-run] rename: {fullpath} to {str(Path(dir / updated_name))}")
    
def main() -> None:
    ap = argparse.ArgumentParser(description="Заполнение шаблона проекта")
    ap.add_argument("--do-it", action="store_true", help="Применять изменения")

    print("Произведен запуск утилиты заполнения шаблона проекта")

    args = ap.parse_args()

    if args.do_it:
        print("в режиме реального заполнения")
    else:
        print("в режиме тестового заполнения (только информирование о предполагаемых заменах)")
        
    # Сбор списка файлов
    files = collect_files()

    # для каждого файла выполним поиск требуемых для замены элементов
    apply_replacements(files, args.do_it)

    # Сбор списка файлов
    files = collect_files(False)

    # для каждого файла выполним проверку на необходимость переименования
    rename_paths(files, args.do_it)

    print("Успешное завершение работы")

if __name__ == "__main__":
    main()

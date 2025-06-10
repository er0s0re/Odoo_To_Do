# -*- coding: utf-8 -*-
{
    'name': 'To-Do List Sederhana Ku',
    'version': '1.0',
    'summary': 'Modul sederhana untuk mencatat tugas harian.',
    'description': """
        Ini adalah aplikasi To-Do List sederhana yang dibuat dengan Odoo.
        Fitur:
        - Membuat tugas baru
        - Melihat daftar tugas
        - Mengubah status tugas
    """,
    'author': 'Eros Alfedo Hermanto', # Ganti dengan nama lu!
    'website': 'https://er0s0re.github.io/Portofolio1', # Opsional, bisa diganti atau dihapus
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # File akses model
        'views/todo_task_views.xml',  # Ganti dengan nama file XML yang sesuai
    ],
    'installable': True,
    'application': True, # Ini penting biar modul kita dianggap sebagai aplikasi
    'auto_install': False,
    'license': 'LGPL-3',
}
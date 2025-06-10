# -*- coding: utf-8 -*-

from odoo import models, fields

# Kita membuat class baru bernama TodoTask
# Nama class biasanya pake format CamelCase (tiap awal kata huruf besar)
class TodoTask(models.Model):
    # _name adalah ID unik model kita di Odoo.
    # Formatnya pake huruf kecil semua dan titik sebagai pemisah.
    # Ini nanti akan jadi nama tabel di database (dengan underscore -> todo_task)
    _name = 'todo.task'
    
    # _description adalah deskripsi singkat buat model kita.
    _description = 'To-Do Task Model'

    # ---- Di bawah ini adalah daftar "field" atau kolom data kita ----

    # Field buat nyimpen nama/judul tugas. Tipe Char itu buat teks singkat.
    # 'string' adalah label yang akan muncul di tampilan.
    # 'required=True' artinya field ini wajib diisi.
    name = fields.Char(string='Tugas', required=True)

    # Field buat deskripsi. Tipe Text itu buat teks yang panjang.
    description = fields.Text(string='Deskripsi')

    # Field buat nandain tugas udah selesai atau belum. Tipe Boolean itu cuma bisa True/False.
    # 'default=False' artinya setiap tugas baru dibuat, statusnya otomatis "belum selesai".
    is_done = fields.Boolean(string='Selesai?', default=False)
    
    # Field buat nyimpen tanggal deadline.
    due_date = fields.Date(string='Batas Waktu')
    
    # Field buat prioritas. Tipe Selection ini ngasih pilihan dropdown.
    # Isinya adalah daftar pasangan ('nilai_teknis', 'label_yang_terlihat').
    priority = fields.Selection([
        ('0', 'Rendah'),
        ('1', 'Sedang'),
        ('2', 'Tinggi')
    ], string='Prioritas', default='1') # Defaultnya kita set 'Sedang'

    def action_mark_as_done(self):
        """Method untuk menandai tugas sebagai selesai."""
        for task in self:
            task.is_done = True
            task.priority = '0'
        return True
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "49621fae-e74b-44b6-8e97-28949c149a76",
   "metadata": {},
   "outputs": [],
   "source": [
    "def nama_fungsi():\n",
    "    print (\"Hello ini Fungsi\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7656c509-71ad-4d69-a869-45e6127ade43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Selamat Pagi\n"
     ]
    }
   ],
   "source": [
    "# Membuat Fungsi\n",
    "def salam():\n",
    "    print (\"Hello, Selamat Pagi\")\n",
    "\n",
    "## Pemanggilan Fungsi\n",
    "salam()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "87967e23-eaee-4574-a136-c3a4dbb80923",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Selamat Pagi\n",
      "Hello, Selamat Pagi\n",
      "Hello, Selamat Pagi\n"
     ]
    }
   ],
   "source": [
    "# Membuat Fungsi\n",
    "def salam():\n",
    "    print (\"Hello, Selamat Pagi\")\n",
    "\n",
    "## Pemanggilan Fungsi\n",
    "salam()\n",
    "salam()\n",
    "salam()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "00a5209c-3c3c-434a-a26c-f15b550a648e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def salam(ucapan):\n",
    "    print(ucapan)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2d36d2b1-4b97-42e0-bb1a-18e750e92092",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fungsi(parameter):\n",
    "    print(parameter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c27ab334-02fc-4764-bbab-99ec978ef659",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Luas segitiga: 12.000000\n"
     ]
    }
   ],
   "source": [
    "# Membuat fungsi dengan parameter\n",
    "def luas_segitiga(alas, tinggi):\n",
    "    luas = (alas * tinggi) / 2\n",
    "    print(\"Luas segitiga: %f\" % luas)\n",
    "\n",
    "# Pemanggilan fungsi\n",
    "luas_segitiga(4, 6)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f0ac5563-4f6a-4632-aa5c-9e76e0ffbb07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Luas persegi: 36\n"
     ]
    }
   ],
   "source": [
    "def luas_persegi(sisi):\n",
    "    luas = sisi * sisi\n",
    "    return luas\n",
    "\n",
    "# pemanggilan fungsi\n",
    "print (\"Luas persegi: %d\" % luas_persegi(6))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4a1efc27-235f-4ee8-a759-ada8cbea4c46",
   "metadata": {},
   "outputs": [],
   "source": [
    "# rumus: sisi x sisi\n",
    "def luas_persegi(sisi):\n",
    "    luas = sisi * sisi\n",
    "    return luas\n",
    "\n",
    "\n",
    "# rumus: sisi x sisi x sisi\n",
    "def volume_persegi(sisi):\n",
    "    volume = luas_persegi(sisi) * sisi\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7618909f-9178-4b47-a606-299ea69f0e09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nama: Muhammad Bintang Muharram\n",
      "Versi: 1.0.0\n",
      "Nama: Programku\n",
      "Versi: 1.0.2\n"
     ]
    }
   ],
   "source": [
    "# membuat variabel global\n",
    "nama = \"Muhammad Bintang Muharram\"\n",
    "versi = \"1.0.0\"\n",
    "\n",
    "def help():\n",
    "    # ini variabel lokal\n",
    "    nama = \"Programku\"\n",
    "    versi = \"1.0.2\"\n",
    "    # mengakses variabel lokal\n",
    "    print(\"Nama: %s\" % nama)\n",
    "    print(\"Versi: %s\" % versi)\n",
    "\n",
    "# mengakses variabel global\n",
    "print(\"Nama: %s\" % nama)\n",
    "print(\"Versi: %s\" % versi)\n",
    "\n",
    "# memanggil fungsi help()\n",
    "help()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "7cc8725e-830b-42b4-92a7-09ad82b3012a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variabel global untuk menyimpan data Buku\n",
    "buku = []\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e1ed4b62-f9e4-4a32-a364-0b75f6060494",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menampilkan semua data\n",
    "def show_data():\n",
    "    if len(buku) <= 0:\n",
    "        print(\"BELUM ADA DATA\")\n",
    "    else:\n",
    "        for indeks in range(len(buku)):\n",
    "            print(\"[%d] %s\" % (indeks, buku[indeks]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "795c1acf-c383-4b64-b43a-0dd670d87ac3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menambah data\n",
    "def insert_data():\n",
    "    buku_baru = raw_input(\"Judul Buku: \")\n",
    "    buku.append(buku_baru)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "09b7e2cd-d789-44e2-ad84-11483491227d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk edit data\n",
    "def edit_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            judul_baru = input(\"Judul baru: \")  # gunakan input() di Python 3\n",
    "            buku[indeks] = judul_baru\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a54f6f75-9768-4c69-a424-1bec29410ebe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fungsi untuk menghapus data\n",
    "def delete_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            buku.remove(buku[indeks])\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "954b8439-1525-4811-afad-578e174696bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "----------- MENU ----------\n",
      "[1] Show Data\n",
      "[2] Insert Data\n",
      "[3] Edit Data\n",
      "[4] Delete Data\n",
      "[5] Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "PILIH MENU>  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "BELUM ADA DATA\n",
      "\n",
      "\n",
      "----------- MENU ----------\n",
      "[1] Show Data\n",
      "[2] Insert Data\n",
      "[3] Edit Data\n",
      "[4] Delete Data\n",
      "[5] Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "PILIH MENU>  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Variabel global untuk menyimpan data Buku\n",
    "buku = []\n",
    "\n",
    "# fungsi untuk menampilkan semua data\n",
    "def show_data():\n",
    "    if len(buku) <= 0:\n",
    "        print(\"BELUM ADA DATA\")\n",
    "    else:\n",
    "        for indeks in range(len(buku)):\n",
    "            print(\"[%d] %s\" % (indeks, buku[indeks]))\n",
    "\n",
    "# fungsi untuk menambah data\n",
    "def insert_data():\n",
    "    buku_baru = input(\"Judul Buku: \")  # ganti raw_input() dengan input()\n",
    "    buku.append(buku_baru)\n",
    "\n",
    "# fungsi untuk edit data\n",
    "def edit_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            judul_baru = input(\"Judul baru: \")  # ganti raw_input() dengan input()\n",
    "            buku[indeks] = judul_baru\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "# fungsi untuk menghapus data\n",
    "def delete_data():\n",
    "    show_data()\n",
    "    try:\n",
    "        indeks = int(input(\"Inputkan ID buku: \"))  # konversi ke integer\n",
    "        if indeks >= len(buku):\n",
    "            print(\"ID salah\")\n",
    "        else:\n",
    "            buku.remove(buku[indeks])\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "# fungsi untuk menampilkan menu\n",
    "def show_menu():\n",
    "    print(\"\\n\")\n",
    "    print(\"----------- MENU ----------\")\n",
    "    print(\"[1] Show Data\")\n",
    "    print(\"[2] Insert Data\")\n",
    "    print(\"[3] Edit Data\")\n",
    "    print(\"[4] Delete Data\")\n",
    "    print(\"[5] Exit\")\n",
    "    \n",
    "    try:\n",
    "        menu = int(input(\"PILIH MENU> \"))  # konversi ke integer\n",
    "        print(\"\\n\")\n",
    "\n",
    "        if menu == 1:\n",
    "            show_data()\n",
    "        elif menu == 2:\n",
    "            insert_data()\n",
    "        elif menu == 3:\n",
    "            edit_data()\n",
    "        elif menu == 4:\n",
    "            delete_data()\n",
    "        elif menu == 5:\n",
    "            exit()\n",
    "        else:\n",
    "            print(\"Salah pilih!\")\n",
    "    except ValueError:\n",
    "        print(\"Input harus berupa angka!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    while(True):\n",
    "        show_menu()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

import os
from flask import Flask,request,session,url_for,render_template,redirect
import pymysql
import datetime
conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='',db='perpus')
now = datetime.datetime.now()
cur  = conn.cursor()
app = Flask(__name__)
app.secret_key = '@*($*@&#&#&$*JAHSU$*#**'


class helper:
	def form(self,name):
		return request.form[name]


helper = helper()


@app.route('/')
def index():
	return "tess"


@app.route('/dashboard')
def dashboard():
	if 'admin' not in session:
		return redirect(url_for('login'))

	cur.execute("SELECT * FROM data_buku")
	data1 = cur.fetchall()
	cur.execute("SELECT * FROM data_anggota")
	data2 = cur.fetchall()
	cur.execute("SELECT * FROM admin")
	data3 = cur.fetchall()
	cur.execute("SELECT * FROM pengunjung")
	data4 = cur.fetchall()
	return render_template('dasboard.html',data1=data1,data2=data2,data3=data3,data4=data4)

@app.route('/login',methods=['GET','POST'])
def login():
	error = None


	if request.method == 'POST':
		username = helper.form('username')
		password = request.form['password']
		cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s",(username,password))
		if cur.fetchone() == None:
			error = "Password Dan Username Salah"
		else:
			session['admin'] = username
			return redirect(url_for('dashboard'))

	if 'admin' in session:
		return redirect(url_for('dashboard'))


	return render_template('login.html',error=error)


@app.route('/logout')
def logout():
	session.pop('admin',None)
	return redirect(url_for('login'))



@app.route('/data_buku',methods=['GET','POST'])
def databuku():

	if 'admin' not in session:
		return redirect(url_for('login'))

	if request.method == 'POST':
		judul = request.form['judul']
		pengarang = request.form['pengarang']
		tahun = request.form['tahun']
		penerbit = request.form['penerbit']
		jumlah = request.form['jumlah']
		lokasi = request.form['lokasi']
		cur.execute("INSERT INTO data_buku (judul,pengarang,tahun,penerbit,jumlah,lokasi) VALUES(%s,%s,%s,%s,%s,%s)",(
			judul,pengarang,tahun,penerbit,jumlah,lokasi))
		conn.commit()
		return redirect(url_for('databuku'))


	cur.execute("SELECT * FROM data_buku")
	data = cur.fetchall()
	return render_template('data_buku.html',data=data)

@app.route('/edit_buku',methods=['GET','POST'])
def edit_buku():
	if request.method == "POST":
		id_buku = request.form['id_buku']
		judul 	= request.form['judul']
		pengarang = request.form['pengarang']
		tahun = request.form['tahun']
		penerbit = request.form['penerbit']
		jumlah = request.form['jumlah']
		lokasi = request.form['lokasi']
		cur.execute("UPDATE data_buku SET judul=%s,pengarang=%s,tahun=%s,penerbit=%s,jumlah=%s,lokasi=%s WHERE id_buku=%s",
			(judul,pengarang,tahun,penerbit,jumlah,lokasi,id_buku))
		conn.commit()
		return redirect(url_for('databuku'))



@app.route('/data_anggota',methods=['GET','POST'])
def dataanggota():
	if 'admin' not in session:
		return redirect(url_for('login'))

	if request.method == 'POST':
		nik = request.form['nik']
		nama = request.form['nama']
		jeniskelamin = request.form['jeniskelamin']
		kelas = request.form['kelas']
		tempat = request.form['tempat']
		tanggal = request.form['tanggal']
		alamat = request.form['alamat']
		cur.execute("INSERT INTO data_anggota(nik,nama,jenis_kelamin,kelas,tempat_lahir,tanggal,alamat) VALUES (%s,%s,%s,%s,%s,%s,%s)",
			(nik,nama,jeniskelamin,kelas,tempat,tanggal,alamat))
		conn.commit()
		return redirect(url_for('dataanggota'))


	cur.execute("SELECT * FROM data_anggota")
	data = cur.fetchall()
	return render_template('data_anggota.html',data=data)



@app.route('/edit_anggota',methods=['GET','POST'])
def edit_anggota():
	if request.method == "POST":
		nik = request.form['nik']
		nama = request.form['nama']
		jeniskelamin = request.form['jeniskelamin']
		kelas = request.form['kelas']
		tempat = request.form['tempat']
		tanggal = request.form['tanggal']
		alamat = request.form['alamat']
		cur.execute("UPDATE data_anggota SET nama=%s,jenis_kelamin=%s,kelas=%s,tempat_lahir=%s,tanggal=%s,alamat=%s WHERE nik=%s",
			(nama,jeniskelamin,kelas,tempat,tanggal,alamat,nik))
		conn.commit()
		return redirect(url_for('dataanggota'))


@app.route('/anggota')
def anggota():
	if 'admin' not in session:
		return redirect(url_for('login'))

	ids = request.args.get('id')
	cur.execute("SELECT * FROM data_anggota WHERE nik=%s",(ids))
	data = cur.fetchone()
	return render_template('anggota.html',data=data)


@app.route('/admin')
def admin():
	if 'admin' not in session:
		return redirect(url_for('login'))

	username = request.args.get('username')
	cur.execute("SELECT * FROM admin WHERE username=%s",(username))
	data = cur.fetchone()
	return render_template('admin.html',data=data)

@app.route('/data_admin',methods=['GET','POST'])
def data_admin():

	if 'admin' not in session:
		return redirect(url_for('login'))

	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		nama	 = request.form['nama']
		cur.execute("SELECT * FROM admin WHERE username=%s",(username))
		if cur.fetchone() == None:
			cur.execute("INSERT INTO admin (username,password,nama) VALUES (%s,%s,%s)",(username
			,password,nama))
			conn.commit()
			return redirect(url_for('data_admin'))
		else:
			return "USERNAME SUDAH ADA"

	cur.execute("SELECT * FROM admin")
	data = cur.fetchall()
	return render_template('data_admin.html',data=data)


@app.route('/edit_admin',methods=['GET','POST'])
def edit_admin():
	if request.method == "POST":
		id_admin = request.form['id_admin']
		username = request.form['username']
		password = request.form['password']
		nama	 = request.form['nama']
		cur.execute("UPDATE admin SET username=%s,password=%s,nama=%s WHERE id_admin=%s",
			(username,password,nama,id_admin))
		conn.commit()
		return redirect(url_for('data_admin'))

	return "Belum Mengoper parameter"

@app.route('/delete')
def delete():
	vid   = request.args.get('vid')
	table = request.args.get('table')
	if table == "admin":
		cur.execute("DELETE FROM admin WHERE id_admin=%s",(vid))
		conn.commit()
		return redirect(url_for('data_admin'))
	elif table == "anggota":
		cur.execute("DELETE FROM data_anggota WHERE nik=%s",(vid))
		conn.commit()
		return redirect(url_for('dataanggota'))
	elif table == "buku":
		cur.execute("DELETE FROM data_buku WHERE id_buku=%s",(vid))
		conn.commit()
		return redirect(url_for('databuku'))
	elif table == "pengunjung":
		cur.execute("DELETE FROM pinjam WHERE id_pinjam=%s",(vid))
		conn.commit()
		return redirect(url_for('pinjam'))


	return "Anda Belum Mengoper variable"


@app.route('/pengunjung',methods=['GET','POST'])
def pengunjung():
	if request.method == "POST":
		nama = request.form['nama']
		keperluan = request.form['keperluan']
		kelas = request.form['kelas']
		cari = request.form['cari']
		saran = request.form['saran']
		tanggal = now.strftime("%Y-%m-%d")
		jam     = now.strftime("%H:%M")
		cur.execute("INSERT INTO pengunjung(nama,keperluan,kelas,cari,saran,tanggal,jam) VALUE(%s,%s,%s,%s,%s,%s,%s)",
			(nama,keperluan,kelas,cari,saran,tanggal,jam))
		conn.commit()
		return redirect(url_for('pengunjung'))

	tanggal = now.strftime("%Y-%m-%d")
	cur.execute("SELECT * FROM pengunjung WHERE tanggal=%s",(tanggal))
	data = cur.fetchall()
	return render_template('pengunjung.html',data=data)


@app.route('/pinjam',methods=['GET','POST'])
def pinjam():
	if 'admin' not in session:
		return redirect(url_for('login'))

	if request.method == "POST":
		nip = request.form['nip']
		id_buku = request.form['id_buku']
		nama = request.form['nama']
		judul = request.form['judul']
		status = request.form['status']
		tanggal = now.strftime("%Y-%m-%d")
		cur.execute("INSERT INTO pinjam(nip,id_buku,nama,judul,status,tanggal) VALUES(%s,%s,%s,%s,%s,%s)",
			(nip,id_buku,nama,judul,status,tanggal))
		conn.commit()
		return redirect(url_for('pinjam'))


	cur.execute("SELECT * FROM pinjam")
	data = cur.fetchall()
	return render_template('pinjam.html',data=data)

@app.route('/edit_pinjam',methods=['GET','POST'])
def edit_pinjam():
		id_pinjam = request.form['id_pinjam']
		nip = request.form['nip']
		id_buku = request.form['id_buku']
		nama = request.form['nama']
		judul = request.form['judul']
		status = request.form['status']
		tanggal = request.form['tanggal']
		cur.execute("UPDATE pinjam SET nip=%s,id_buku=%s,nama=%s,judul=%s,status=%s,tanggal=%s WHERE id_pinjam=%s",
			(nip,id_buku,nama,judul,status,tanggal,id_pinjam))
		conn.commit()
		return redirect(url_for('pinjam'))


@app.route('/tentang',methods=['GET','POST'])
def tentang():
	if 'admin' not in session:
		return redirect(url_for('login'))

	if request.method == "POST":
		ids = "1"
		tentang = request.form['tentang']
		author  = request.form['author']
		github  = request.form['github']
		cur.execute("UPDATE tentang SET tentang=%s,author=%s,github=%s WHERE id=%s",
			(tentang,author,github,ids))
		conn.commit();
		return redirect(url_for('tentang'));


	cur.execute("SELECT * FROM tentang");
	data = cur.fetchone()
	return render_template('tentang.html',data=data)

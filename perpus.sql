-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2018 at 06:22 PM
-- Server version: 10.1.9-MariaDB
-- PHP Version: 5.5.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpus`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `username`, `password`, `nama`) VALUES
(2, 'koko', 'koko', 'kokojempol');

-- --------------------------------------------------------

--
-- Table structure for table `data_anggota`
--

CREATE TABLE `data_anggota` (
  `nik` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jenis_kelamin` varchar(20) NOT NULL,
  `kelas` varchar(10) NOT NULL,
  `tempat_lahir` varchar(40) NOT NULL,
  `tanggal` date NOT NULL,
  `alamat` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_anggota`
--

INSERT INTO `data_anggota` (`nik`, `nama`, `jenis_kelamin`, `kelas`, `tempat_lahir`, `tanggal`, `alamat`) VALUES
('123141', 'Jonas', 'Perempuan', '10-2', 'Long Island, New York, USA', '2016-05-04', 'jalan kengan'),
('12315', 'Umino', 'Perempuan', '9-3', 'Denver, Colorado, USA', '1981-06-04', 'jalan marunda'),
('124125', 'Unag', 'Laki-Laki', '10-9', 'Jakarta', '2008-09-28', 'jalan marunda');

-- --------------------------------------------------------

--
-- Table structure for table `data_buku`
--

CREATE TABLE `data_buku` (
  `id_buku` int(11) NOT NULL,
  `judul` varchar(60) NOT NULL,
  `pengarang` varchar(70) NOT NULL,
  `tahun` varchar(4) NOT NULL,
  `penerbit` varchar(20) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `lokasi` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `data_buku`
--

INSERT INTO `data_buku` (`id_buku`, `judul`, `pengarang`, `tahun`, `penerbit`, `jumlah`, `lokasi`) VALUES
(3, 'pemograman java 2', 'berti', '2009', 'Erlangga', 100, 'L-56'),
(4, 'Membuat Web 1 Bulan', 'Erlangga', '2008', 'Jaya Baya', 40, 'C-09');

-- --------------------------------------------------------

--
-- Table structure for table `pengunjung`
--

CREATE TABLE `pengunjung` (
  `id_pengunjung` int(11) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `keperluan` varchar(30) NOT NULL,
  `kelas` varchar(10) NOT NULL,
  `cari` varchar(20) NOT NULL,
  `saran` text NOT NULL,
  `tanggal` date NOT NULL,
  `jam` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pengunjung`
--

INSERT INTO `pengunjung` (`id_pengunjung`, `nama`, `keperluan`, `kelas`, `cari`, `saran`, `tanggal`, `jam`) VALUES
(1, 'udin', 'baca', 'ips2', 'komik', 'sudah cukup baik pelayanan nya', '2018-09-09', '18:08'),
(2, 'koko lomel', 'Baca', '12Ips1', 'Buku', 'sudah bagus', '2018-09-29', '23:39'),
(3, 'dugong', 'Meminjam', 'x_12', 'Jayabaya', 'sudah bagus', '2018-10-08', '11:26'),
(4, 'Unut Emery', 'Meminjam', '10-ips', 'sangaskala', 'lumayan bagus', '2018-10-13', '00:06');

-- --------------------------------------------------------

--
-- Table structure for table `pinjam`
--

CREATE TABLE `pinjam` (
  `id_pinjam` int(11) NOT NULL,
  `nip` varchar(10) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `nama` varchar(40) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tentang`
--

CREATE TABLE `tentang` (
  `id` int(11) NOT NULL,
  `tentang` text NOT NULL,
  `author` varchar(40) NOT NULL,
  `github` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tentang`
--

INSERT INTO `tentang` (`id`, `tentang`, `author`, `github`) VALUES
(1, 'Perpus Ini Merupakan aplikasi perpustakaan berbasis website yang di gunakan mengunakan python (Flask Framework) dan Mysql dan bootstrap. Tujuan membuat aplikasi perpus untuk belajar bahasa python dan Framework Flask. Aplikasi ini juga dapat di pakai untuk refresni Tugas Akhir Ataupun Skripsi yang Sedang Anda Susun Pepus Ini Berbasis Open Source Siapa Saja Dapat Mengembangkan nya \r\nDan jangan Lupa Di tulis Sumber nya', 'Arjun Dwiyantoro', 'https://github.com/arjundwiyantoro');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `data_anggota`
--
ALTER TABLE `data_anggota`
  ADD PRIMARY KEY (`nik`);

--
-- Indexes for table `data_buku`
--
ALTER TABLE `data_buku`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `pengunjung`
--
ALTER TABLE `pengunjung`
  ADD PRIMARY KEY (`id_pengunjung`);

--
-- Indexes for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD PRIMARY KEY (`id_pinjam`);

--
-- Indexes for table `tentang`
--
ALTER TABLE `tentang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `data_buku`
--
ALTER TABLE `data_buku`
  MODIFY `id_buku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `pengunjung`
--
ALTER TABLE `pengunjung`
  MODIFY `id_pengunjung` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `pinjam`
--
ALTER TABLE `pinjam`
  MODIFY `id_pinjam` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `tentang`
--
ALTER TABLE `tentang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

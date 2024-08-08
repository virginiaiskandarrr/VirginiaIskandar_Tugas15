-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 08, 2024 at 03:37 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hematinaja`
--

-- --------------------------------------------------------

--
-- Table structure for table `hitunguang`
--

CREATE TABLE `hitunguang` (
  `id` int(11) NOT NULL,
  `tanggal` varchar(255) NOT NULL,
  `kategori` varchar(255) NOT NULL,
  `pemasukan` varchar(255) NOT NULL,
  `pengeluaran` varchar(255) NOT NULL,
  `saldo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hitunguang`
--

INSERT INTO `hitunguang` (`id`, `tanggal`, `kategori`, `pemasukan`, `pengeluaran`, `saldo`) VALUES
(2, '2024-08-01', 'Gaji', '5000000', '0', '5000000'),
(3, '2024-08-01', 'Listrik', '0', '200000', '4800000'),
(4, '2024-08-01', 'Makan', '0', '30000', '4770000'),
(5, '2024-08-02', 'Baju', '0', '500000', '4270000'),
(7, '2024-08-05', 'Bonus Gaji', '1000000', '0', '5270000'),
(8, '2024-08-10', 'Kosan', '0', '900000', '4370000'),
(9, '2024-08-12', 'Ojol', '0', '50000', '4320000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hitunguang`
--
ALTER TABLE `hitunguang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hitunguang`
--
ALTER TABLE `hitunguang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 28, 2023 at 01:43 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `turnaus`
--

-- --------------------------------------------------------

--
-- Table structure for table `joukkueet`
--

CREATE TABLE `joukkueet` (
  `joukkueID` int(5) NOT NULL,
  `joukkueennimi` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `paikkakunta` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `paastetyt` int(5) NOT NULL,
  `tehdyt` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `joukkueet`
--

INSERT INTO `joukkueet` (`joukkueID`, `joukkueennimi`, `paikkakunta`, `paastetyt`, `tehdyt`) VALUES
(1, 'South Park', 'Colorado', 13, 13),
(2, 'Lords of the Hockeyrings', 'Minas Tirith', 4, 6),
(3, 'Hockeybat Man', 'Gotham', 7, 12),
(4, 'The Sopranos', 'New Jersey', 5, 20);

-- --------------------------------------------------------

--
-- Table structure for table `pelaajat`
--

CREATE TABLE `pelaajat` (
  `pelaajaID` int(5) NOT NULL,
  `nimi` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `joukkueID` int(5) NOT NULL,
  `pelipaikkaID` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pelaajat`
--

INSERT INTO `pelaajat` (`pelaajaID`, `nimi`, `joukkueID`, `pelipaikkaID`) VALUES
(1, 'Bruce Wayne', 3, 1),
(2, 'Dick Grayson', 3, 2),
(3, 'Barbara Gordon', 3, 2),
(4, 'Ethan Bennett', 3, 3),
(5, 'James Gordon', 3, 3),
(6, 'Angel Rojas', 3, 3),
(7, 'Frodo Baggins', 2, 1),
(8, 'Peregrin Took', 2, 2),
(9, 'Samwise Gamgee', 2, 2),
(10, 'Meriadoc Brandybuck', 2, 3),
(11, 'Bilbo Baggins', 2, 3),
(13, 'Alfred Pennyworth', 3, 7),
(14, 'Gollum', 2, 4),
(15, 'Sauron', 2, 5),
(16, 'Aragorn II Elessar', 2, 3),
(17, 'Galadriel', 2, 6),
(18, 'Saruman', 2, 3),
(19, 'Witch-king of Angmar', 2, 7),
(20, 'Detective Ellen Yin', 3, 5),
(21, 'Bane', 3, 4),
(22, 'The Joker', 3, 6),
(23, 'Lex Luthor', 3, 3),
(24, 'Eric Cartman', 1, 5),
(25, 'Kenny McCormick', 1, 1),
(26, 'Mr. Garrison', 1, 2),
(27, 'Chef', 1, 2),
(28, 'Towelie', 1, 4),
(29, 'Tolkien Black', 1, 3),
(30, 'Stan Marsh', 1, 3),
(31, 'Randy Marsh', 1, 7),
(32, 'Linda Stotch', 1, 6),
(33, 'Kyle Broflovski', 1, 3),
(34, 'Bono', 1, 3),
(35, 'Tony Soprano', 4, 1),
(36, 'Paulie Gualtieri', 4, 7),
(37, 'Meadow Soprano', 4, 6),
(38, 'Adriana La Cerva', 4, 5),
(39, 'Christopher Moltisanti', 4, 4),
(40, 'Silvio Dante', 4, 2),
(41, 'Jennifer Melfi', 4, 2),
(42, 'Vito Spatafore', 4, 3),
(43, 'Furio Giunta', 4, 3),
(44, 'Carmela Soprano', 4, 3),
(46, 'Junior Soprano', 4, 3);

-- --------------------------------------------------------

--
-- Table structure for table `pelipaikka`
--

CREATE TABLE `pelipaikka` (
  `pelipaikkaID` int(5) NOT NULL,
  `rooli` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pelipaikka`
--

INSERT INTO `pelipaikka` (`pelipaikkaID`, `rooli`) VALUES
(1, 'maalivahti'),
(2, 'puolustaja'),
(3, 'hyokkaaja'),
(4, 'huoltaja'),
(5, 'paavalmentaja'),
(6, 'apuvalmentaja'),
(7, 'joukkueenjohtaja');

-- --------------------------------------------------------

--
-- Table structure for table `pelit`
--

CREATE TABLE `pelit` (
  `peliID` int(5) NOT NULL,
  `kotijoukkue` int(5) NOT NULL,
  `vierasjoukkue` int(5) NOT NULL,
  `aloitusaika` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pelit`
--

INSERT INTO `pelit` (`peliID`, `kotijoukkue`, `vierasjoukkue`, `aloitusaika`) VALUES
(2, 4, 1, '2023-03-24 17:00:00'),
(6, 1, 4, '2023-03-22 18:00:00'),
(7, 4, 2, '2023-03-21 15:15:00'),
(8, 4, 3, '2023-04-26 17:15:00'),
(9, 3, 2, '2023-09-13 21:00:00'),
(11, 3, 2, '2023-04-01 21:00:00'),
(12, 1, 3, '2023-09-12 21:15:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `joukkueet`
--
ALTER TABLE `joukkueet`
  ADD PRIMARY KEY (`joukkueID`);

--
-- Indexes for table `pelaajat`
--
ALTER TABLE `pelaajat`
  ADD PRIMARY KEY (`pelaajaID`),
  ADD KEY `joukkueID` (`joukkueID`),
  ADD KEY `pelipaikkaID` (`pelipaikkaID`);

--
-- Indexes for table `pelipaikka`
--
ALTER TABLE `pelipaikka`
  ADD PRIMARY KEY (`pelipaikkaID`);

--
-- Indexes for table `pelit`
--
ALTER TABLE `pelit`
  ADD PRIMARY KEY (`peliID`),
  ADD KEY `kotijoukkue` (`kotijoukkue`,`vierasjoukkue`),
  ADD KEY `vierasjoukkue` (`vierasjoukkue`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `joukkueet`
--
ALTER TABLE `joukkueet`
  MODIFY `joukkueID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `pelaajat`
--
ALTER TABLE `pelaajat`
  MODIFY `pelaajaID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `pelipaikka`
--
ALTER TABLE `pelipaikka`
  MODIFY `pelipaikkaID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `pelit`
--
ALTER TABLE `pelit`
  MODIFY `peliID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pelaajat`
--
ALTER TABLE `pelaajat`
  ADD CONSTRAINT `pelaajat_ibfk_1` FOREIGN KEY (`pelipaikkaID`) REFERENCES `pelipaikka` (`pelipaikkaID`),
  ADD CONSTRAINT `pelaajat_ibfk_2` FOREIGN KEY (`joukkueID`) REFERENCES `joukkueet` (`joukkueID`);

--
-- Constraints for table `pelit`
--
ALTER TABLE `pelit`
  ADD CONSTRAINT `pelit_ibfk_1` FOREIGN KEY (`kotijoukkue`) REFERENCES `joukkueet` (`joukkueID`),
  ADD CONSTRAINT `pelit_ibfk_2` FOREIGN KEY (`vierasjoukkue`) REFERENCES `joukkueet` (`joukkueID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

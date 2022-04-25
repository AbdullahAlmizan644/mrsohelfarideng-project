-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 24, 2022 at 12:44 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `storybook`
--

-- --------------------------------------------------------

--
-- Table structure for table `audiobooks`
--

CREATE TABLE `audiobooks` (
  `id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` varchar(10000) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'audiobook.png',
  `audio` varchar(200) NOT NULL,
  `writer` varchar(200) NOT NULL DEFAULT 'writer',
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `audiobooks`
--

INSERT INTO `audiobooks` (`id`, `name`, `description`, `image`, `audio`, `writer`, `date`) VALUES
(1, 'Pagla Dashu', 'pagla dashu written by sukumar roy', 'audiobook.png', 'pagla_dashu.mp3', 'writer', '2022-04-19 12:05:34.000000'),
(2, 'gabi bittanto', 'written by', 'audiobook.png', 'gabi.mp3', 'writer', '2022-04-19 12:05:34.000000');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'book.jpg',
  `description` varchar(10000) NOT NULL,
  `price` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `name`, `image`, `description`, `price`, `date`) VALUES
(1, 'book1', 'book.jpg', 'this is book1', '200', '2022-04-15 17:54:11.000000'),
(2, 'book2', 'book.jpg', 'this is book2', '100', '2022-04-15 17:54:11.000000'),
(3, 'book3', 'book.jpg', 'this is book3', '300', '2022-04-15 17:55:20.000000'),
(4, 'book4', 'book.jpg', 'this is book4', '400', '2022-04-15 17:55:20.000000');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `sno` int(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `image` varchar(200) NOT NULL DEFAULT 'user.png',
  `address` varchar(1000) NOT NULL DEFAULT 'Add your adress',
  `phone` varchar(200) NOT NULL DEFAULT 'Add your phone number',
  `password` varchar(200) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`sno`, `username`, `email`, `image`, `address`, `phone`, `password`, `date`) VALUES
(1, 'mizan', 'mizan@gmail.com', '89716241_2559523860959437_1994742812679077888_n.jpg', 'Add your adress', 'Add your phone number', '12345678', '2022-04-15 00:02:42.093777');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audiobooks`
--
ALTER TABLE `audiobooks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audiobooks`
--
ALTER TABLE `audiobooks`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `sno` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 25-01-2021 a las 05:41:57
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `denuncias_desaparecidos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `avistamiento`
--

CREATE TABLE `avistamiento` (
  `ID_avistamiento` int(10) NOT NULL,
  `ID_desaparecido` int(10) NOT NULL,
  `Pais` varchar(20) NOT NULL,
  `Provincia` varchar(20) DEFAULT NULL,
  `Descripción_lugar` varchar(100) NOT NULL,
  `Fecha_avistamiento` date NOT NULL,
  `Descripcion_avistamiento` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `Cedula` varchar(10) NOT NULL,
  `Nombres` varchar(100) NOT NULL,
  `Apellidos` varchar(100) NOT NULL,
  `Fecha_Nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona_denunciante`
--

CREATE TABLE `persona_denunciante` (
  `ID_denunciante` int(10) NOT NULL,
  `Cedula` varchar(10) NOT NULL,
  `Relacion` varchar(20) DEFAULT NULL COMMENT 'Cómo está relacionado con el desaparecido',
  `Telefono` varchar(9) NOT NULL,
  `Celular` varchar(10) DEFAULT NULL,
  `Correo` varchar(50) DEFAULT NULL,
  `Desaparicion` varchar(500) NOT NULL COMMENT 'Resumen de la desaparicion'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona_desaparecida`
--

CREATE TABLE `persona_desaparecida` (
  `ID_desaparecido` int(10) NOT NULL,
  `Cedula` varchar(10) NOT NULL,
  `Edad` int(5) NOT NULL,
  `Estatura` int(10) NOT NULL COMMENT 'Basada en cm',
  `Peso` decimal(5,2) NOT NULL COMMENT 'basada en kg',
  `Especificacion_piel` varchar(100) NOT NULL COMMENT 'Color, raza, tatuajes, lunares y cicatrices',
  `Especificacion_rostro` varchar(100) NOT NULL COMMENT 'Color de ojos, forma del rostro, tamanio de las orejas, nariz y boca, etc',
  `Especificacion_cabello` varchar(100) NOT NULL COMMENT 'color del cabello, si es hondulado, risado, etc, calvo ',
  `Especificacion_adicional` varchar(100) DEFAULT NULL COMMENT 'Especificacion adicional que ayude a facilitar la busqueda',
  `Fotografia` varchar(100) NOT NULL,
  `Fecha_desaparicion` date NOT NULL,
  `Vestimenta` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reportar`
--

CREATE TABLE `reportar` (
  `ID_Reportar` int(10) NOT NULL,
  `ID_denunciante` int(10) NOT NULL,
  `ID_desaparecido` int(10) NOT NULL,
  `Reporte` varchar(100) NOT NULL COMMENT 'link del archivo de tipo reporte'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reportar_aparicion`
--

CREATE TABLE `reportar_aparicion` (
  `ID_aparicion` int(10) NOT NULL,
  `ID_denunciante` int(10) NOT NULL,
  `ID_desaparecido` int(10) NOT NULL,
  `Reporte` varchar(100) NOT NULL COMMENT 'archivo de reporte de aparicion',
  `Foto` varchar(100) NOT NULL COMMENT 'archivo .png o jpg',
  `Condicion` varchar(100) NOT NULL COMMENT 'condicion de salud, psicologica, etc'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `avistamiento`
--
ALTER TABLE `avistamiento`
  ADD PRIMARY KEY (`ID_avistamiento`),
  ADD KEY `ID_desaparecido` (`ID_desaparecido`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`Cedula`);

--
-- Indices de la tabla `persona_denunciante`
--
ALTER TABLE `persona_denunciante`
  ADD PRIMARY KEY (`ID_denunciante`),
  ADD KEY `Cedula` (`Cedula`);

--
-- Indices de la tabla `persona_desaparecida`
--
ALTER TABLE `persona_desaparecida`
  ADD PRIMARY KEY (`ID_desaparecido`),
  ADD KEY `Cedula` (`Cedula`);

--
-- Indices de la tabla `reportar`
--
ALTER TABLE `reportar`
  ADD PRIMARY KEY (`ID_Reportar`),
  ADD KEY `ID_denunciante` (`ID_denunciante`),
  ADD KEY `ID_desaparecido` (`ID_desaparecido`);

--
-- Indices de la tabla `reportar_aparicion`
--
ALTER TABLE `reportar_aparicion`
  ADD PRIMARY KEY (`ID_aparicion`),
  ADD KEY `ID_denunciante` (`ID_denunciante`),
  ADD KEY `ID_desaparecido` (`ID_desaparecido`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `avistamiento`
--
ALTER TABLE `avistamiento`
  MODIFY `ID_avistamiento` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona_denunciante`
--
ALTER TABLE `persona_denunciante`
  MODIFY `ID_denunciante` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona_desaparecida`
--
ALTER TABLE `persona_desaparecida`
  MODIFY `ID_desaparecido` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reportar`
--
ALTER TABLE `reportar`
  MODIFY `ID_Reportar` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `reportar_aparicion`
--
ALTER TABLE `reportar_aparicion`
  MODIFY `ID_aparicion` int(10) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `avistamiento`
--
ALTER TABLE `avistamiento`
  ADD CONSTRAINT `avistamiento_ibfk_1` FOREIGN KEY (`ID_desaparecido`) REFERENCES `persona_desaparecida` (`ID_desaparecido`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `persona_denunciante`
--
ALTER TABLE `persona_denunciante`
  ADD CONSTRAINT `persona_denunciante_ibfk_1` FOREIGN KEY (`Cedula`) REFERENCES `persona` (`Cedula`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `persona_desaparecida`
--
ALTER TABLE `persona_desaparecida`
  ADD CONSTRAINT `persona_desaparecida_ibfk_1` FOREIGN KEY (`Cedula`) REFERENCES `persona` (`Cedula`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `reportar`
--
ALTER TABLE `reportar`
  ADD CONSTRAINT `reportar_ibfk_1` FOREIGN KEY (`ID_desaparecido`) REFERENCES `persona_desaparecida` (`ID_desaparecido`) ON UPDATE CASCADE,
  ADD CONSTRAINT `reportar_ibfk_2` FOREIGN KEY (`ID_denunciante`) REFERENCES `persona_denunciante` (`ID_denunciante`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `reportar_aparicion`
--
ALTER TABLE `reportar_aparicion`
  ADD CONSTRAINT `reportar_aparicion_ibfk_1` FOREIGN KEY (`ID_desaparecido`) REFERENCES `persona_desaparecida` (`ID_desaparecido`) ON UPDATE CASCADE,
  ADD CONSTRAINT `reportar_aparicion_ibfk_2` FOREIGN KEY (`ID_denunciante`) REFERENCES `persona_denunciante` (`ID_denunciante`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

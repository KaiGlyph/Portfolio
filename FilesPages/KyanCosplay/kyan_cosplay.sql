-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2025 a las 08:39:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `kyan_cosplay`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cabfac`
--

CREATE TABLE `cabfac` (
  `numfac` int(11) NOT NULL,
  `tipo_destinatario` enum('cliente','proveedor') NOT NULL,
  `idcliente` int(11) DEFAULT NULL,
  `idproveedor` int(11) DEFAULT NULL,
  `nombre_destinatario` varchar(100) NOT NULL,
  `email_destinatario` varchar(100) DEFAULT NULL,
  `telefono_destinatario` varchar(20) DEFAULT NULL,
  `doc_destinatario` varchar(20) DEFAULT NULL,
  `nombreempresa` int(50) NOT NULL,
  `fecha` date NOT NULL,
  `tipo` char(1) NOT NULL DEFAULT 'F',
  `numfac_rectificada` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cabfac`
--

INSERT INTO `cabfac` (`numfac`, `tipo_destinatario`, `idcliente`, `idproveedor`, `nombre_destinatario`, `email_destinatario`, `telefono_destinatario`, `doc_destinatario`, `nombreempresa`, `fecha`, `tipo`, `numfac_rectificada`) VALUES
(1, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-22', 'F', NULL),
(2, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-26', 'F', NULL),
(3, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-26', 'A', NULL),
(4, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-26', 'A', NULL),
(5, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-26', 'A', NULL),
(6, 'cliente', 1, NULL, 'Paula Aguayo Gomez', 'paula@gmail.com', '403050340', '43010203D', 2, '2025-05-26', 'A', NULL),
(7, 'cliente', 5, NULL, 'Ariadna Monton', 'ariadna@gmail.com', '2147483647', '4326436434T', 2, '2025-05-26', 'F', NULL),
(8, 'cliente', 5, NULL, 'Ariadna Monton', 'ariadna@gmail.com', '2147483647', '4326436434T', 2, '2025-05-26', 'A', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `Nombre` text NOT NULL,
  `Apellidos` text NOT NULL,
  `telefono` int(12) NOT NULL,
  `email` varchar(20) NOT NULL,
  `dni` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `Nombre`, `Apellidos`, `telefono`, `email`, `dni`) VALUES
(1, 'Paula', 'Aguayo Gomez', 403050340, 'paula@gmail.com', '43010203D'),
(5, 'Ariadna', 'Monton', 2147483647, 'ariadna@gmail.com', '4326436434T'),
(6, 'Albert', 'Enrique', 654693492, 'albert@gmail.com', '324235253D'),
(8, 'Jordi', 'Gallardo', 234356464, 'jordi@gmail.com', '123443242D');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id` char(36) NOT NULL DEFAULT uuid(),
  `numero_albaran` varchar(50) NOT NULL,
  `id_proveedor` char(36) NOT NULL,
  `fecha_compra` datetime NOT NULL,
  `fecha_recepcion` datetime DEFAULT NULL,
  `estado` varchar(20) NOT NULL,
  `metodo_pago` varchar(30) NOT NULL,
  `referencia_proveedor` varchar(50) DEFAULT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `iva` decimal(10,2) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`id`, `numero_albaran`, `id_proveedor`, `fecha_compra`, `fecha_recepcion`, `estado`, `metodo_pago`, `referencia_proveedor`, `subtotal`, `iva`, `total`, `observaciones`) VALUES
('d887357a-b4bd-4b95-9f0c-0bd7d8e87a75', '432534647', '1', '2025-05-22 00:00:00', NULL, 'Pendiente', 'Transferencia', NULL, 100.00, 10.00, 110.00, NULL),
('e112a155-8465-4ed7-a2e0-09e41e24ecfc', '1', '1', '2025-05-26 16:28:21', NULL, 'Pendiente', 'Transferencia', NULL, 80.00, 21.00, 100.00, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` int(12) NOT NULL,
  `email` varchar(40) NOT NULL,
  `cif` varchar(10) NOT NULL,
  `codigopostal` int(5) NOT NULL,
  `poblacion` varchar(30) NOT NULL,
  `cuentabancaria` varchar(30) NOT NULL,
  `formapago` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empresa`
--

INSERT INTO `empresa` (`id`, `nombre`, `direccion`, `telefono`, `email`, `cif`, `codigopostal`, `poblacion`, `cuentabancaria`, `formapago`) VALUES
(2, 'KyanCosplay', 'Pg. de St. Joan 37', 777, 'kyancosplay0901@gmail.com', 'B-832496', 8010, 'Barcelona', 'ES 43829420749', 'Transferencia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventos`
--

CREATE TABLE `eventos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `fecha` date NOT NULL,
  `horario` time NOT NULL DEFAULT curtime(),
  `precio` decimal(6,0) NOT NULL,
  `iva` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `eventos`
--

INSERT INTO `eventos` (`id`, `nombre`, `fecha`, `horario`, `precio`, `iva`) VALUES
(1, 'Manga Barcelona', '2025-12-05', '09:00:00', 500, 21),
(2, 'Japan Weekend', '2025-09-21', '00:00:00', 500, 21);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `linfac`
--

CREATE TABLE `linfac` (
  `id` int(10) UNSIGNED NOT NULL,
  `id_cabfac` int(11) NOT NULL,
  `numfac` int(11) NOT NULL,
  `id_producto` int(10) UNSIGNED DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `unidad` int(11) DEFAULT NULL,
  `iva` int(2) DEFAULT NULL,
  `descuento` int(3) DEFAULT NULL,
  `total_linea` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `linfac`
--

INSERT INTO `linfac` (`id`, `id_cabfac`, `numfac`, `id_producto`, `descripcion`, `precio`, `unidad`, `iva`, `descuento`, `total_linea`) VALUES
(1, 0, 1, 1, 'Espada Elucidator de Kirito (Sword Art Online)', 46.00, 1, 21, 0, 56),
(2, 0, 1, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', 60.00, 2, 21, 5, 138),
(3, 0, 1, 3, 'Peluca rubia estilo Naruto Uzumaki', 25.00, 3, 21, 0, 91),
(4, 0, 1, 5, 'Uniforme completo del Cuerpo de Exploración (Attack on Titan)', 75.00, 5, 21, 10, 408),
(5, 0, 1, 1, 'Espada Elucidator de Kirito (Sword Art Online)', 46.00, 1, 21, 0, 56),
(6, 0, 1, 12, 'Peluca azul mediana con flequillo ', 20.00, 1, 21, 0, 24),
(7, 0, 2, 1, 'Espada Elucidator de Kirito (Sword Art Online)', 46.00, 1, 21, 0, 56),
(8, 0, 2, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', 60.00, 1, 21, 5, 69),
(9, 0, 3, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(10, 0, 3, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', -60.00, 2, 21, 5, -138),
(11, 0, 3, 3, 'Peluca rubia estilo Naruto Uzumaki', -25.00, 3, 21, 0, -91),
(12, 0, 3, 5, 'Uniforme completo del Cuerpo de Exploración (Attack on Titan)', -75.00, 5, 21, 10, -408),
(13, 0, 3, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(14, 0, 3, 12, 'Peluca azul mediana con flequillo ', -20.00, 1, 21, 0, -24),
(15, 0, 4, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(16, 0, 4, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', -60.00, 1, 21, 5, -69),
(17, 0, 5, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(18, 0, 5, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', -60.00, 2, 21, 5, -138),
(19, 0, 5, 3, 'Peluca rubia estilo Naruto Uzumaki', -25.00, 3, 21, 0, -91),
(20, 0, 5, 5, 'Uniforme completo del Cuerpo de Exploración (Attack on Titan)', -75.00, 5, 21, 10, -408),
(21, 0, 5, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(22, 0, 5, 12, 'Peluca azul mediana con flequillo ', -20.00, 1, 21, 0, -24),
(23, 0, 6, 1, 'Espada Elucidator de Kirito (Sword Art Online)', -46.00, 1, 21, 0, -56),
(24, 0, 6, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', -60.00, 1, 21, 5, -69),
(25, 0, 7, 12, 'Peluca azul mediana con flequillo ', 20.00, 1, 21, 0, 24),
(26, 0, 7, 6, 'Diadema con orejas de gato negras', 10.00, 1, 21, 0, 12),
(27, 0, 7, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', 60.00, 1, 21, 5, 69),
(28, 0, 8, 12, 'Peluca azul mediana con flequillo ', -20.00, 1, 21, 0, -24),
(29, 0, 8, 6, 'Diadema con orejas de gato negras', -10.00, 1, 21, 0, -12),
(30, 0, 8, 2, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda', -60.00, 1, 21, 5, -69);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `tipodeproducto` varchar(15) NOT NULL,
  `codigoproducto` varchar(30) NOT NULL,
  `precio` decimal(4,0) NOT NULL,
  `iva` int(2) NOT NULL,
  `stock` int(5) NOT NULL,
  `descuento` int(3) NOT NULL,
  `descripcion` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `tipodeproducto`, `codigoproducto`, `precio`, `iva`, `stock`, `descuento`, `descripcion`) VALUES
(1, 'Arma', 'COS001', 46, 21, 8, 0, 'Espada Elucidator de Kirito (Sword Art Online)'),
(2, 'Traje', 'COS002', 60, 21, 13, 5, 'Traje completo de Tanjiro Kamado con kimono y pendientes hanafuda'),
(3, 'Peluca', 'COS003', 25, 21, 17, 0, 'Peluca rubia estilo Naruto Uzumaki'),
(5, 'Traje', 'COS005', 75, 21, 7, 10, 'Uniforme completo del Cuerpo de Exploración (Attack on Titan)'),
(6, 'Accesorio', 'COS006', 10, 21, 30, 0, 'Diadema con orejas de gato negras'),
(7, 'Traje', 'COS007', 55, 21, 10, 5, 'Vestido tradicional rosa de Nezuko Kamado'),
(8, 'Accesorio', 'COS008', 14, 21, 25, 0, 'Guantes verdes de Izuku Midoriya (My Hero Academia)'),
(9, 'Accesorio', 'COS009', 90, 21, 5, 0, 'Casco de The Mandalorian (Din Djarin)'),
(10, 'Traje', 'COS010', 50, 21, 18, 5, 'Gi naranja y azul de Goku (Dragon Ball)'),
(12, 'Peluca', '23123213', 20, 21, 99, 0, 'Peluca azul mediana con flequillo ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `id` int(11) NOT NULL,
  `nombreapellidos` varchar(40) NOT NULL,
  `razonsocial` varchar(40) NOT NULL,
  `direccion` varchar(40) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` int(15) NOT NULL,
  `cif` varchar(15) NOT NULL,
  `cuentabancaria` varchar(100) NOT NULL,
  `iva` int(2) NOT NULL,
  `mediodepago` varchar(20) NOT NULL,
  `moneda` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`id`, `nombreapellidos`, `razonsocial`, `direccion`, `email`, `telefono`, `cif`, `cuentabancaria`, `iva`, `mediodepago`, `moneda`) VALUES
(1, 'Ribes y Casals', 'Ribes y Casals', 'Plaza Urquinaona', 'ribesycasals@gmail.com', 543953463, '4325364', '538237284723', 21, 'Transferencia', 'euro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `talleres`
--

CREATE TABLE `talleres` (
  `id` int(11) NOT NULL,
  `nombretaller` varchar(20) NOT NULL,
  `dia` date NOT NULL,
  `hora` time(6) NOT NULL,
  `plazasreservadas` int(3) NOT NULL,
  `plazastotales` int(3) NOT NULL,
  `precio` decimal(5,0) NOT NULL,
  `iva` int(2) NOT NULL,
  `descuento` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `talleres`
--

INSERT INTO `talleres` (`id`, `nombretaller`, `dia`, `hora`, `plazasreservadas`, `plazastotales`, `precio`, `iva`, `descuento`) VALUES
(1, 'MakeUp', '0000-00-00', '12:00:00.000000', 0, 20, 7, 21, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` enum('admin','moderador','empleado','invitado') NOT NULL DEFAULT 'empleado'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `rol`) VALUES
(1, 'admin', 'admin123', 'admin'),
(4, 'Paula', 'Paula123', 'moderador'),
(5, 'Jordi', 'Jordi123', 'empleado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cabfac`
--
ALTER TABLE `cabfac`
  ADD PRIMARY KEY (`numfac`),
  ADD KEY `idproveedor` (`idproveedor`),
  ADD KEY `idcliente` (`idcliente`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_proveedor` (`id_proveedor`);

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `linfac`
--
ALTER TABLE `linfac`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_cabfac` (`id_cabfac`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `talleres`
--
ALTER TABLE `talleres`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `empresa`
--
ALTER TABLE `empresa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `eventos`
--
ALTER TABLE `eventos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `linfac`
--
ALTER TABLE `linfac`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `talleres`
--
ALTER TABLE `talleres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cabfac`
--
ALTER TABLE `cabfac`
  ADD CONSTRAINT `cabfac_ibfk_1` FOREIGN KEY (`idproveedor`) REFERENCES `proveedores` (`id`),
  ADD CONSTRAINT `cabfac_ibfk_2` FOREIGN KEY (`idcliente`) REFERENCES `clientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

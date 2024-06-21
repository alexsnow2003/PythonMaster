CREATE DATABASE IF NOT EXISTS QLKS;
USE QLKS;

-- Định nghĩa bảng user
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50)
);

-- Định nghĩa bảng PhongBan
CREATE TABLE PhongBan (
    MaPB NVARCHAR(10) PRIMARY KEY NOT NULL,
    TenPB NVARCHAR(50) NOT NULL,
    SDT NVARCHAR(20) NOT NULL,
    Email NVARCHAR(50) NOT NULL
);

-- Định nghĩa bảng NhanVien
CREATE TABLE NhanVien (
    MaNV NVARCHAR(10) PRIMARY KEY NOT NULL,
    TenNV NVARCHAR(50) NOT NULL,
    NgaySinh DATE,
    GioiTinh NVARCHAR(4) CHECK (GioiTinh IN ('Nam','Nu','Khac')),
    QuocTich NVARCHAR(50),
    CCCD NVARCHAR(20) NOT NULL,
    DiaChi NVARCHAR(225),
    SDT NVARCHAR(20) NOT NULL,
    ChucVu NVARCHAR(50),
    Luong FLOAT,
    MaPB NVARCHAR(10),
    FOREIGN KEY (MaPB) REFERENCES PhongBan(MaPB)
);

-- Bảng KhachHang với mã tự động
CREATE TABLE KhachHang (
    MaKH INT AUTO_INCREMENT PRIMARY KEY,
    TenKH NVARCHAR(50) NOT NULL,
    NgaySinh DATE,
    GioiTinh NVARCHAR(4) CHECK (GioiTinh IN ('Nam', 'Nu', 'Khac')),
    QuocTich NVARCHAR(50),
    CCCD NVARCHAR(20) NOT NULL,
    SDT NVARCHAR(20) NOT NULL,
    Email NVARCHAR(50)
);


-- Định nghĩa bảng LoaiPhong
CREATE TABLE LoaiPhong (
    MaLP NVARCHAR(10) PRIMARY KEY NOT NULL,
    TenLP NVARCHAR(20) NOT NULL,
    Gia FLOAT,
    SoNguoiLonToiDa NUMERIC(10,0),
    SoTreEmToiDa NUMERIC(10,0),
    SoGiuong NUMERIC(10,0)
);

-- Định nghĩa bảng Phong
CREATE TABLE Phong (
    MaPhong NVARCHAR(10) PRIMARY KEY NOT NULL,
    MaLP NVARCHAR(10),
    TinhTrangPhong NVARCHAR(20),
    FOREIGN KEY (MaLP) REFERENCES LoaiPhong(MaLP)
);

-- Định nghĩa bảng ThietBi
CREATE TABLE ThietBi (
    MaTB NVARCHAR(10) PRIMARY KEY NOT NULL,
    TenTB NVARCHAR(50) NOT NULL,
    Dvt NVARCHAR(20),
    DonGia FLOAT
);

-- Định nghĩa bảng ThietBi_Phong
CREATE TABLE ThietBi_Phong (
    MaTB NVARCHAR(10),
    MaPhong NVARCHAR(10),
    SoLuong INT,
    PRIMARY KEY (MaTB, MaPhong),
    FOREIGN KEY (MaTB) REFERENCES ThietBi(MaTB),
    FOREIGN KEY (MaPhong) REFERENCES Phong(MaPhong)
);

-- Định nghĩa bảng DichVu
CREATE TABLE DichVu (
    MaDV NVARCHAR(10) PRIMARY KEY NOT NULL,
    TenDV NVARCHAR(50) NOT NULL,
    DonGia FLOAT,
    Dvt NVARCHAR(20)
);

CREATE TABLE PhieuDangKy (
    MaPDK NVARCHAR(10) PRIMARY KEY NOT NULL,
    NgayLPDK DATE,
    NgayDK DATE,
    NgayHenTra DATE,
    NgayTra DATE,
    HinhThuc NVARCHAR(7),
    TienDatCoc FLOAT,
    MaPhong NVARCHAR(10),
    MaNV NVARCHAR(10),
    MaKH INT,  -- Assuming MaKH in KhachHang is INT AUTO_INCREMENT PRIMARY KEY
    FOREIGN KEY (MaPhong) REFERENCES Phong(MaPhong),
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV),
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);


-- Bảng HoaDon với MaPDK tham chiếu đến bảng PhieuDangKy
CREATE TABLE HoaDon (
    MaHD NVARCHAR(10) PRIMARY KEY NOT NULL,
    NgayLap DATE,
    TienPhong FLOAT,
    TienDV FLOAT,
    MaNV NVARCHAR(10),
    MaPDK NVARCHAR(10),  -- Trường MaPDK trong HoaDon tham chiếu đến MaPDK trong PhieuDangKy
    FOREIGN KEY (MaPDK) REFERENCES PhieuDangKy(MaPDK),
    FOREIGN KEY (MaNV) REFERENCES NhanVien(MaNV)
);

-- Định nghĩa bảng PhieuThu
CREATE TABLE PhieuThu (
    MaPT NVARCHAR(10) PRIMARY KEY NOT NULL,
    MaHD NVARCHAR(10),
    TongTien FLOAT,
    PhuongThucTT NVARCHAR(20),
    FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD)
);

-- Định nghĩa bảng TriAnKH
CREATE TABLE TriAnKH (
    MaTAKH NVARCHAR(10) PRIMARY KEY NOT NULL,
    MaKH INT,
    TenQua NVARCHAR(20),
    NgayTriAn DATE,
    GiaTri FLOAT,
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

-- Định nghĩa bảng PhieuTichDiem
CREATE TABLE PhieuTichDiem (
    MaPTD NVARCHAR(10) PRIMARY KEY NOT NULL,
    MaKH INT,
    NgayPhieu DATE,
    BienDongDiem FLOAT,
    NguyenNhanBienDongDiem NVARCHAR(225),
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);

-- Thêm dữ liệu mẫu vào các bảng (ví dụ)
INSERT INTO user (username, password, role) VALUES ('snow', '123', 'admin'), ('alex', '123', 'user');
INSERT INTO PhongBan (MaPB, TenPB, SDT, Email) VALUES ('PB001', 'Phòng ban A', '123456789', 'pb_a@example.com');
INSERT INTO NhanVien (MaNV, TenNV, NgaySinh, GioiTinh, QuocTich, CCCD, DiaChi, SDT, ChucVu, Luong, MaPB) 
VALUES ('NV001', 'Nguyễn Văn A', '1990-01-01', 'Nam', 'Việt Nam', '123456789', 'Hà Nội', '0987654321', 'Nhân viên', 10000000, 'PB001');
INSERT INTO KhachHang (TenKH, NgaySinh, GioiTinh, QuocTich, CCCD, SDT, Email) 
VALUES ('Nguyễn Thị B', '1995-05-05', 'Nữ', 'Việt Nam', '987654321', '0987123456', 'nguyenthib@example.com');
INSERT INTO LoaiPhong (MaLP, TenLP, Gia, SoNguoiLonToiDa, SoTreEmToiDa, SoGiuong) 
VALUES ('LP001', 'Phòng đơn', 100000, 1, 0, 1);
INSERT INTO Phong (MaPhong, MaLP, TinhTrangPhong) VALUES ('P001', 'LP001', 'Trống');
INSERT INTO ThietBi (MaTB, TenTB, Dvt, DonGia) VALUES ('TB001', 'Máy lạnh', 'Cái', 5000000);
INSERT INTO ThietBi_Phong (MaTB, MaPhong, SoLuong) VALUES ('TB001', 'P001', 2);
INSERT INTO DichVu (MaDV, TenDV, DonGia, Dvt) VALUES ('DV001', 'Dịch vụ giặt là', 50000, 'Lần');
INSERT INTO PhieuDangKy (MaPDK, NgayLPDK, NgayDK, NgayHenTra, NgayTra, HinhThuc, TienDatCoc, MaPhong, MaNV, MaKH)
VALUES ('PDK001', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', 'Trực tiếp', 1000000, 'P001', 'NV001', 1);
INSERT INTO HoaDon (MaHD, NgayLap, TienPhong, TienDV, MaNV, MaPDK) 
VALUES ('HD001', '2023-01-04', 200000, 50000, 'NV001', 'PDK001');
INSERT INTO PhieuThu (MaPT, MaHD, TongTien, PhuongThucTT) VALUES ('PT001', 'HD001', 250000, 'Tiền mặt');
INSERT INTO TriAnKH (MaTAKH, MaKH, TenQua, NgayTriAn, GiaTri) VALUES ('TAKH001', '1', 'Quà tri ân', '2023-01-05', 500000);
INSERT INTO PhieuTichDiem (MaPTD, MaKH, NgayPhieu, BienDongDiem, NguyenNhanBienDongDiem) 
VALUES ('PTD001', '1', '2023-01-05', 100, 'Đăng ký thành viên');


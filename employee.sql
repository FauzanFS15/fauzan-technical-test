-- Active: 1757966511733@@127.0.0.1@3306
-- Membuat Tabel employee

DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    Name VARCHAR(50),
    Position VARCHAR(50),
    JoinDate DATE,
    ReleaseDate DATE,
    Year_of_Experience DECIMAL(5, 2),
    Salary DECIMAL(10, 2)
);

-- Input Data untuk Tabel employee

INSERT INTO
    employee (
        Name,
        Position,
        JoinDate,
        ReleaseDate,
        Year_of_Experience,
        Salary
    )
VALUES (
        'Jacky',
        'Solution Architect',
        '2018-07-25',
        '2022-07-25',
        8.0,
        150
    ),
    (
        'John',
        'Assistant Manager',
        '2016-02-02',
        '2021-02-02',
        12.0,
        155
    ),
    (
        'Alano',
        'Manager',
        '2010-11-09',
        NULL,
        14.0,
        175
    ),
    (
        'Aaron',
        'Engineer',
        '2021-08-16',
        '2022-08-16',
        1.0,
        80
    ),
    (
        'Allen',
        'Engineer',
        '2024-06-06',
        NULL,
        4.0,
        75
    ),
    (
        'Peter',
        'Team Leader',
        '2020-01-09',
        NULL,
        3.0,
        85
    );

-- Menambahkan Employee Baru dengan nama Albert

INSERT INTO
    employee (
        Name,
        Position,
        JoinDate,
        Year_of_Experience,
        Salary
    )
VALUES (
        'Albert',
        'Engineer',
        '2024-01-24',
        2.5,
        50
    );

-- update salary engineer menjadi $85

UPDATE employee SET Salary = 85 WHERE Position = 'Engineer';

-- Menghitung jumlah gaji karyawan yang masih aktif pada tahun 2021

SELECT SUM(Salary) AS Total_Salary_2021
FROM employee
WHERE
    strftime('%Y', JoinDate) <= '2021'
    AND (
        strftime('%Y', ReleaseDate) >= '2021'
        OR ReleaseDate IS NULL
    );

-- Menampilkan nama dan tahun pengalaman dari karyawan dengan posisi Engineer yang memiliki pengalaman kurang dari atau sama dengan 3 tahun

SELECT Name, Year_of_Experience
FROM employee
WHERE
    Position = 'Engineer'
    AND Year_of_Experience <= 3;
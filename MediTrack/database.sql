create database if not exists meditrack;
use meditrack;
-- users table
create table if not exists users(id int auto_increment primary key, username varchar(50) unique not null, password varchar(100) not null);
-- Medicines table
create table if not exists medicines (
    id int auto_increment primary key,
    username varchar(50) not null,
    medicine_name varchar(100) not null,
    diseasevarchar(100),
    dosage varchar(50),
    time_slot varchar(30),
    food_instruction varchar(50),
    start_date date,
    end_date date,
    status varchar(20) default 'Pending'
);

-- BMI records table
create table if not exists bmi_records (
    id int auto_increment primary key,
    username varchar(50) not null,
    weight float,
    height float,
    bmi float,
    category varchar(30)
);
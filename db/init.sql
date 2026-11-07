CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL
);

INSERT INTO employees (full_name, department) VALUES
('Иванов И.И.', 'ИТ-департамент'),
('Петрова А.С.', 'Департамент рисков'),
('Сидоров П.П.', 'Операционный блок');
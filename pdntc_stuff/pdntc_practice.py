from base_model import Employee


Employee(
        name="Chris DeTuma",
        email="cdetuma@example.com",
        dateOfBirth="1998-04-02",
        compensation=123_000.00,
        department="IT",
        elected_benefits=False,
        )

new_employee_dict = {
        "name": "Chris DeTuma",
        "email": "cdetuma@example.com",
        "dateOfBirth": "1998-04-02",
        "compensation": 123_000.00,
        "department": "IT",
        "elected_benefits": False,
}

new_employee_json = """
        {"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
        "name":"Eric Slogrenta",
        "email":"eslogrenta@example.com",
        "dateOfBirth":"1990-01-02",
        "compensation":125000.0,
        "department":"HR",
        "elected_benefits":false}
        """

print(Employee.model_validate(new_employee_dict))
json_employee = Employee.model_validate_json(new_employee_json)
print(json_employee.model_dump_json())

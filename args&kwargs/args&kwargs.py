def momo(plate, *args, **kwargs):
    print(f"plate: {plate}")
    for item in args:
        print(f"- {item}")
    
    print("------------------------")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

  


momo("1", "buff", "veg", "chicken", delivery=True, price=100)

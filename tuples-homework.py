import helpers


def first_task():
    computer = ("Intel Core i7", "16GB", "512GB SSD", "Windows 10")
    processor, ram, storage, os = computer
    print(processor, ram, storage, os)


for f in {first_task}:
    helpers.run(f)

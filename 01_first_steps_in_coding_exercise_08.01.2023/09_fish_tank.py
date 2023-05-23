length = int(input())
width = int(input())
height = int(input())
percentage_taken = float(input())

volume_aquarium = length * width * height
volume_in_litre = volume_aquarium / 1000
volume_taken = volume_in_litre * (percentage_taken / 100)
volume_real = volume_in_litre - volume_taken

print(f"{volume_real} litres")
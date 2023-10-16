import image
import rNumber
import rPhoto

def main():
    goAgain = "10"
    goAgain = input("Press 1 to get a random image press anything else to exit: ")
    while goAgain == "1":
        with open("prng-service.txt", "w") as f:
            f.write("1")
        print("UI wrote to prng-service.txt")
        rNumber.generateNumber()
        rPhoto.photos()
        image.displayImage()
        goAgain = input("Press 1 to get a random image press anything else to exit: ")
main()
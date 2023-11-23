def vowels_and_consonants(text):
    vowels = 'aeiouAEIOU'
    consonants = "bcdfghjklmnpqrstvwxyzBCDFHJKLMNPQRSTVWXYZ"
    
    num_vowels = sum(1 for char in text if char in vowels)
    num_consonants = sum(1 for char in text if char in consonants)
    
    return num_vowels,num_consonants

def main():
    file_path ='file.txt'
    try:
        with open(file_path, 'r') as file:
          content = file.read()
          vowels,consonants = vowels_and_consonants(content)
          print(f"number of vowels: {vowels}")
          print(f"number of consonants: {consonants}")
    except FileNotFoundError:
        print(f"file not found:{file_path}") 

if __name__ == "__main__":
    main()

//string operation?
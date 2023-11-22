# Check if the number is prime

def is_prime(num):
    return True

# Get the desired number of primes
def get_primes(start_from, num_primes):
    print('Get', num_primes, 'primes after', start_from)
    primes = []
    return primes

if __name__ == '__main__':
    try:
        num_primes = int(input("Number of primes to be fetched: "))
        fetch_from = input("Smallest prime is 2; Fetch primes after this number: ")
        if fetch_from.strip():
            fetch_from_num = int(fetch_from)
        else:
            fetch_from_num = 2 
        print(get_primes(fetch_from_num, num_primes))
    except Exception as e:
        print("Give a valid input; got error", e)
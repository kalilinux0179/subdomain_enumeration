#!/usr/bin/python3
import dns.resolver
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Subdomain BruteForcer", usage="%(prog)s -d domain.com -f wordlist.txt",
                                     epilog="Example: python3 %(prog)s -d domain.com -f wordlist.txt")
    parser.add_argument("-d", "--domain", help="Domain Name", dest="domain")
    parser.add_argument(
        "-f", "--file", help="Subdomain Wordlists", dest="wordlist")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    domain = args.domain
    wordlist = args.wordlist

    if domain and wordlist:
        with open(wordlist, "r")as wordlists:
            word = wordlists.read().splitlines()
            for subs in word:
                try:
                    ip_value = dns.resolver.resolve(f"{subs}.{domain}", "A")
                    if ip_value:
                        print(f"{subs}.{domain}")
                except dns.resolver.NXDOMAIN:
                    pass
                except dns.resolver.NoAnswer:
                    pass
                except KeyboardInterrupt:
                    print("\nYour pressed CTRL + C")
                    sys.exit()


if __name__ == "__main__":
    main()

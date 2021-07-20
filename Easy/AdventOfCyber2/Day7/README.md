# Advent of Cyber 2 - Day 7

## Associated files
* `pcap1.pcap` - First wireshark file
* `pcap2.pcap` - Second wireshark file
* `pcap3.pcap` - Third wireshark file
* `christmas.zip` - Zip file from `pcap3`
* `elf_mcskidy_wishlist.txt` - Elf's wishlist

## Steps
We use `wireshark` for the entirety of this question. The IP that initiates a ping is `10.11.3.2`. The filter is `http.request.method == GET`. The name of the article is `reindeer-of-the-week`. The password that is leaked is `plaintext_password_fiasco`. SSH is the only encrypted protocol in the logs. For the wishlist we can download the zip file that we find and unzip it to see the elf's wishlist and see that `Rubber ducky` is what is going to replace McEager.